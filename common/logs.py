from all_path import Paths
import logging
import threading
import os


class Log:
    def __init__(self, log_level='DEBUG'):
        self.logger = logging.getLogger(__name__)
        if log_level.upper() == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        elif log_level.upper() == 'INFO':
            self.logger.setLevel(logging.INFO)
        elif log_level.upper() == 'WARNING':
            self.logger.setLevel(logging.WARNING)
        elif log_level.upper() == 'ERROR':
            self.logger.setLevel(logging.ERROR)
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


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def my_log(log_level='DEBUG'):
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log(log_level)
            MyLog.mutex.release()
        return MyLog.log


if __name__ == '__main__':
    my_log = MyLog.my_log().get_logger()
    my_log.error('error')
    my_log.info('info')
    my_log.debug('debug')
