# -*- coding: utf-8 -*-
# User: Navy
# Time: 2020/6/8 14:43

import redis
import json

from dynaconf import settings
from fastapi import APIRouter, Body
from aliexpress import ProductsSpider
from utils.base import logger

router = APIRouter()


@router.post('/goodsUrl')
async def save_data(data: dict = Body(...)):
    '''
    校验用户下单时地址
    :param data:
    :return:
    '''
    logger.info(data)
    url = data.get('url')
    product = ProductsSpider(url)
    data = product.goods_info()
    return data


@router.post('/batchImportAeUrl')
async def save_data(data: dict = Body(...)):
    '''
    校验用户下单时地址
    :param data:
    :return:
    '''
    redis_conn = redis.StrictRedis(host=settings.REDIS.HOST, port=settings.REDIS.PORT, db=settings.REDIS.DB,
                                   password=settings.REDIS.PASSWD)
    url_list = data.get('urlList', None)
    for url in url_list:
        redis_conn.lpush(settings.ALIEXPRESS_URL, url)
    return {
        'code': True,
        'msg': '成功'
    }
