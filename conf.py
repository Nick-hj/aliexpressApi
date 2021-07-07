# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: conf
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/6 18:40
# Software: PyCharm

import sys

# import os
# import logging
# import logging.handlers
# from logging.handlers import WatchedFileHandler
# import os
# import multiprocessing
# sys.path.append('/data/ROOT/order_spider')

bind = "0.0.0.0:8010"  # 绑定的ip与端口
backlog = 512  # 监听队列数量，64-2048
# chdir = '/data/ROOT/shopify'  #gunicorn要切换到的目的工作目录
# worker_class = 'gtheard' #使用gevent模式，还可以使用sync 模式，默认的是sync模式
worker_class = 'uvicorn.workers.UvicornWorker'  # 使用gevent模式，还可以使用sync 模式，默认的是sync模式
workers = 2  # multiprocessing.cpu_count()    #进程数
threads = 2  # multiprocessing.cpu_count()*4 #指定每个进程开启的线程数
loglevel = 'info'  # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
# access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# accesslog、errorlog日志文件可以写到文件
accesslog = "./logs/ae_api_access.log"  # 访问日志文件
errorlog = "./logs/ae_api_error.log"  # 错误日志文件
# accesslog = "-"  #访问日志文件，"-" 表示标准输出
# errorlog = "-"   #错误日志文件，"-" 表示标准输出

proc_name = 'ae_api'  # 进程名
daemon = True  # 守护进程
reload = True  # 自启动

# gunicorn -c conf.py main:app -D 配置文件启动
# gunicorn -w 4 -b 0.0.0.0:8010  main:app -D 命令行启动
# gunicorn -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:8010" --log-level debug main:app

