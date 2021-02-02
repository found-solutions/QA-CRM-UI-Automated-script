import unittest
from all_path import Paths
from common.HTMLTestRunner import HTMLTestRunner
import os


def find_case(p="test*.py"):
    case_path = Paths.cases
    all_case = unittest.defaultTestLoader.discover(case_path, pattern=p)
    return all_case


def run_all():
    report = os.path.join(Paths.report_path, Paths.now_date + '-result.html')
    with open(report, "wb") as f:
        r = HTMLTestRunner(stream=f, title="UI Auto Test", description="test result")
        r.run(find_case())


if __name__ == "__main__":
    run_all()




