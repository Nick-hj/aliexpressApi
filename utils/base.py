# -*- coding: utf-8 -*-
# User: haijun
# Time: 2020/5/7 15:47

import loguru
import os


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
        basic_path =  './logs'
        logger.add(os.path.join(basic_path, 'ae_api_info_{time:YYYY-MM-DD}.log'),
                   format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file.path} | {module} | {function} | {line} | {message}",
                   level="INFO", rotation="00:00", retention='20 days', enqueue=True, encoding='utf-8')
        logger.add(os.path.join(basic_path, 'ae_api_error_{time:YYYY-MM-DD}.log'),
                   format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file.path} | {module} | {function} | {line} | {message}",
                   level="ERROR", rotation="00:00", retention='20 days', enqueue=True, encoding='utf-8')
        return logger

logger = SpiderLog()