# CiscopyATS

# 🔧 Cisco pyATS + Genie Test Suite

This repository contains two test cases built using **Cisco pyATS + Genie**, targeting IOS and IOS-XE routers. These tests validate **ping connectivity** and **static route consistency** across two routers.

---

## 📋 Test Environment

| Router Name   | Platform | IP Address      | OS     | Protocol |
|---------------|----------|------------------|--------|----------|
| iosv-0        | IOS      | 192.168.30.182    | ios    | SSH      |
| csr1000v-0    | IOS-XE   | 192.168.30.183    | iosxe  | SSH      |

Both routers must be reachable over SSH and allow CLI access for `ping` and `show ip route`.

✅ Overview

Devices:

iosv-0 – 192.168.30.182 (IOS)

csr1000v-0 – 192.168.30.183 (IOS-XE)


---

## ✅ Test Cases

### **Test Case 1: Ping Success Rate**

- **Command**: `ping 100.1.1.1`
- **Validation**: Verifies the ping result contains the string `"Success rate is 100 percent"`
- **Pass Criteria**: Both routers must return **exactly 100%** success rate
- **Fail Criteria**: Any router with less than 100% will fail the test

Testcases:

Ping 100.1.1.1 and verify "Success rate is 100 percent"

Compare static routes ("S") from show ip route

---

### **Test Case 2: Static Route Comparison**

- **Command**: `show ip route`
- **Validation**:
  - Extracts all routes starting with `"S"` (Static routes)
  - Compares the route prefixes from both routers
- **Pass Criteria**: Static routes must match exactly
- **Fail Criteria**: Any mismatch in static route prefixes causes the test to fail

---

## 🗂 Project Structure

<img width="500" height="124" alt="image" src="https://github.com/user-attachments/assets/3b04677c-b76e-4fb5-97c8-8fb7a0468f7b" />

🔒 Requirements

Python 3.8+

pyATS and Genie installed: pip install pyats[full]

SSH access to routers with valid credentials

Static routes configured on both routers (if test 2 is expected to pass)

📦 Future Enhancements

Add retry logic for ping

Support for dynamic route types (O, B, E, etc.)

Use Genie parsers instead of CLI regex for better accuracy


