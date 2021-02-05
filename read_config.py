from configparser import ConfigParser
import os


class ReadConfig(object):
    cfg_p = os.path.join(os.path.realpath(__file__).rsplit("\\", 1)[0], "config.ini")

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(self.cfg_p, encoding='utf8')

    def get_url(self, key):
        value = self.cf.get("URL", key)
        return value

    def get_mysql(self, key):
        value = self.cf.get("DATABASE", key)
        return value

    def get_ssh(self, key):
        value = self.cf.get("SSH", key)
        return value

    def get_global(self, key):
        value = self.cf.get("GLOBAL", key)
        return value


if __name__ == '__main__':
    f = ReadConfig()
    u = f.get_url('url1')
    print(u)
