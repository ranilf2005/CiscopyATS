from pyats.easypy import run

def main(runtime):
    run(testscript='combined_test.py', testbed=runtime.testbed)
