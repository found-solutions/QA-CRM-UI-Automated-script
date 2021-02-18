import time
import os


class Paths:
    now_date = time.strftime('%m%d')
    log_path = os.path.join(os.path.realpath(__file__).rsplit('\\', 1)[0], 'logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    report_path = os.path.join(os.path.realpath(__file__).rsplit('\\', 1)[0], 'report')
    error_img = os.path.join(os.path.realpath(__file__).rsplit('\\', 1)[0], 'error_img', now_date)
    if not os.path.exists(error_img):
        os.makedirs(error_img)
    cases = os.path.join(os.path.abspath(__file__).rsplit('\\', 1)[0], 'src')
    driver_path = os.path.join(os.path.realpath(__file__).rsplit('\\', 1)[0], 'common', 'chromedriver.exe')


if __name__ == '__main__':
    p = Paths.error_img
    print(p)
