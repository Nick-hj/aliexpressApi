# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: base
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/7 15:47
# Software: PyCharm

# import logging.config
import loguru
import os

# logging.config.fileConfig('utils/conf_logs.ini')
# logger_info = logging.getLogger('info')
# logger_debug = logging.getLogger('debug')
# logger_error = logging.getLogger('error')


def proxy():
    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = ""
    proxyPass = ""
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    return proxies


class SpiderLog(object):
    def __new__(cls, *args, **kwargs):
        logger = loguru.logger
        basic_path =  '/data/logs'
        logger.add(os.path.join(basic_path, 'ae_order_check_info_{time:YYYY-MM-DD}.log'),
                   format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file.path} | {module} | {function} | {line} | {message}",
                   level="INFO", rotation="00:00", retention='20 days', enqueue=True, encoding='utf-8')
        logger.add(os.path.join(basic_path, 'ae_order_check_error_{time:YYYY-MM-DD}.log'),
                   format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file.path} | {module} | {function} | {line} | {message}",
                   level="ERROR", rotation="00:00", retention='20 days', enqueue=True, encoding='utf-8')
        return logger

logger = SpiderLog()