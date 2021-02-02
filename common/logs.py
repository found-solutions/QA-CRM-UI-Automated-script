from all_path import Paths
import logging
import threading
import os


class Log:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        print(os.path.join(Paths.log_path, '{}.log'.format(Paths.now_date)))
        fh = logging.FileHandler(os.path.join(Paths.log_path, '{}.log'.format(Paths.now_date)), encoding="utf-8")
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        format_msg = logging.Formatter("[%(asctime)s][%(filename)s][line:%(lineno)d][%(levelname)s]：%(message)s")
        fh.setFormatter(format_msg)
        ch.setFormatter(format_msg)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger

    def case_start(self, case_no):
        self.logger.info("--------" + case_no + " START--------")

    def case_end(self, case_no):
        self.logger.info("--------" + case_no + " START--------")

    def test_end(self, case_name, code, msg):
        self.logger.info(case_name + " -code:" + code + " -msg:" + msg)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def my_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log


if __name__ == '__main__':
    my_log = MyLog.my_log().get_logger()
    my_log.error('error')
    my_log.info('info')
    my_log.debug('debug')
