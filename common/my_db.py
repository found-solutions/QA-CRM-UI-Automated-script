# -*- coding: utf-8 -*-
# @Author ：Mingjie Huang
# @Time   ：2019/7/4 13:12
# @IDE    ：PyCharm

import pymysql
from read_config import ReadConfig
from sshtunnel import SSHTunnelForwarder
from common.logs import MyLog
import paramiko
import os
import time

logs = MyLog.my_log().get_logger()


def mysql_db(sql):
    # 直接连接MySQL数据库，无SSH隧道
    # 获取数据库信息
    host = ReadConfig().get_mysql('host')
    port = int(ReadConfig().get_mysql('port'))
    user = ReadConfig().get_mysql('username')
    passwd = ReadConfig().get_mysql('password')
    dbn = ReadConfig().get_mysql('database')
    charset = ReadConfig().get_mysql('mysql_charset')

    # 创建连接
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            port=port,
            db=dbn,
            charset=charset)
    except BaseException as e:
        res = "数据库链接失败：{}".format(e)
        logs.error(res)
    else:
        # cur = conn.cursor()  # 建立游标,结果是元组
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 结果是字典
        if sql.strip()[:6].upper() == 'SELECT':
            # res = cur.fetchall()
            cur.execute(sql)  # 执行sql
            res = cur.fetchall()  # 显示查询结果
            cur.close()
            conn.close()
        else:
            try:
                cur.execute(sql)  # 执行sql
            except BaseException as e:
                logs.error(e)
                conn.rollback()  # SQL异常，回滚
                res = e
            else:
                # 无异常时执行
                conn.commit()  # 提交
                res = 'SQL 执行 ok！'
                logs.info(res)
            finally:
                # 总是执行
                cur.close()
                conn.close()
    return res


def ssh_server():

    # 获取当前文件的路径
    file_path = os.path.dirname(__file__)
    # 获取配置文件config.ini的路径
    config_path = os.path.join(file_path, 'private_key')

    # 创建ssh连接
    ssh_host = ReadConfig().get_mysql('ssh_address')
    ssh_port = ReadConfig().get_mysql('ssh_port')
    ssh_user = ReadConfig().get_mysql('ssh_user')
    # 用密码访问
    # ssh_password = read_config('projectname', 'ssh_password')
    # 用密钥访问
    ssh_password = paramiko.RSAKey.from_private_key_file(config_path)
    host = ReadConfig().get_mysql('host')
    port = int(ReadConfig().get_mysql('port'))
    try:
        server = SSHTunnelForwarder(
            ssh_address_or_host=(ssh_host, int(ssh_port)),  # 端口转为int类型
            ssh_username=ssh_user,
            # ssh_password=ssh_password,
            ssh_pkey=ssh_password,
            remote_bind_address=(host, int(port))  # 端口转为int类型
        )
    except BaseException as e:
        logs.error("SSH链接失败：{}".format(e))
        return
    else:
        pass
    return server


def ssh_mysql_db(sql):
    # 通过ssh隧道连接MySQL

    ssh = ssh_server()
    ssh.start()
    # 添加ssh链接之后的等待时间
    time.sleep(2)

    host = "127.0.0.1"
    user = ReadConfig().get_mysql('username')
    passwd = ReadConfig().get_mysql('password')
    port = ssh.local_bind_port
    dbn = ReadConfig().get_mysql('database')
    charset = ReadConfig().get_mysql('mysql_charset')

    # 创建连接
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            port=port,
            db=dbn,
            charset=charset)
    except BaseException as e:
        res = "数据库链接失败：{}".format(e)
        logs.error(res)
        ssh.stop()

    else:
        # cur = conn.cursor()#元组形式
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        if sql.strip()[:6].upper() == 'SELECT':
            # res = cur.fetchall()
            cur.execute(sql)  # 执行sql
            res = cur.fetchall()  # 显示查询结果
            cur.close()
            conn.close()
            ssh.stop()
        else:
            try:
                cur.execute(sql)  # 执行sql
            except BaseException as e:
                logs.error(e)
                conn.rollback()  # SQL异常，回滚
                res = e
            else:
                # 无异常时执行
                conn.commit()  # 提交
                res = 'SQL 执行 ok！'
                logs.info(res)
            finally:
                # 总是执行
                cur.close()
                conn.close()
                ssh.stop()
    return res


def db(sql):
    if ReadConfig().get_mysql('is_ssh') == '1':
        res = ssh_mysql_db(sql)
    elif ReadConfig().get_mysql('is_ssh') == '0':
        res = mysql_db(sql)
    else:
        res = "无效的参数/参数未配置!"
        logs.error(res)
    return res


if __name__ == '__main__':
    sql1 = "SELECT external_id FROM trading_accounts"
    res1 = db(sql1)
    print(res1)
