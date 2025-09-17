from pyats import aetest
import logging
import re

log = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self, testbed):
        self.parent.parameters['ios'] = testbed.devices['iosv-0']
        self.parent.parameters['iosxe'] = testbed.devices['csr1000v-0']

        for device in [self.parent.parameters['ios'], self.parent.parameters['iosxe']]:
            log.info(f"Connecting to {device.name}")
            device.connect()

# -----------------------------------------------------------------------------
# TESTCASE 1: Ping with Success Rate Check
# -----------------------------------------------------------------------------
class PingTest(aetest.Testcase):
    @aetest.test
    def ping_check(self, ios, iosxe):
        for device in [ios, iosxe]:
            log.info(f"Pinging 100.1.1.1 from {device.name}")
            output = device.execute("ping 100.1.1.1")
            log.info(f"{device.name} ping output:\n{output}")

            # Check for exact success rate match
            if re.search(r"Success rate is 100 percent", output):
                log.info(f"{device.name}: Ping successful (100%)")
            else:
                self.failed(f"{device.name}: Ping failed or success rate < 100%")

        self.passed("Ping success rate is 100% on both routers")

# -----------------------------------------------------------------------------
# TESTCASE 2: Static Route Comparison
# -----------------------------------------------------------------------------
class StaticRouteComparison(aetest.Testcase):
    @aetest.test
    def compare_static_routes(self, ios, iosxe):
        log.info("Getting static routes from iosv-0")
        output1 = ios.execute("show ip route")
        log.info("Getting static routes from csr1000v-0")
        output2 = iosxe.execute("show ip route")

        static_routes_ios = sorted(re.findall(r'^S\s+(\S+)', output1, re.MULTILINE))
        static_routes_iosxe = sorted(re.findall(r'^S\s+(\S+)', output2, re.MULTILINE))

        log.info(f"iosv-0 static routes: {static_routes_ios}")
        log.info(f"csr1000v-0 static routes: {static_routes_iosxe}")

        if static_routes_ios == static_routes_iosxe:
            self.passed("Static routes match on both routers")
        else:
            self.failed("Static routes do NOT match between iosv-0 and csr1000v-0")

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_devices(self, ios, iosxe):
        ios.disconnect()
        iosxe.disconnect()
