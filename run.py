import unittest
from all_path import Paths
from common.HTMLTestRunner import HTMLTestRunner
import os


def find_case():
    member_case_path = os.path.join(Paths.cases, 'member_portal', 'cases')
    admin_case_path = os.path.join(Paths.cases, 'admin_portal', 'cases')
    tests = unittest.TestSuite()
    member_cases = unittest.defaultTestLoader.discover(member_case_path, top_level_dir=member_case_path)
    # admin_cases = unittest.defaultTestLoader.discover(admin_case_path, top_level_dir=admin_case_path)
    # for t1 in admin_cases:
    #     tests.addTests(t1)
    for t2 in member_cases:
        tests.addTests(t2)
    return tests


def run_all():
    report = os.path.join(Paths.report_path, Paths.now_date + '-result.html')
    with open(report, "wb") as f:
        r = HTMLTestRunner(stream=f, title="UI Auto Test", description="test result")
        r.run(find_case())


if __name__ == "__main__":
    run_all()
