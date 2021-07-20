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
redis_conn = redis.StrictRedis(host=settings.REDIS.HOST, port=settings.REDIS.PORT, db=settings.REDIS.DB,
                               password=settings.REDIS.PASSWD)


@router.post('/goodsUrl')
async def save_data(data: dict = Body(...)):
    '''
    校验用户下单时地址
    :param data:
    :return:
    '''
    try:
        url = data.get('url')
        product = ProductsSpider(url)
        data = product.goods_info()
        logger.info(f'采集AE数据成功========{data}')
        return data
    except Exception as e:
        return {
            'code': False,
            'msg': e
        }


@router.post('/batchImportAeUrl')
async def save_data(data: dict = Body(...)):
    '''
    校验用户下单时地址
    :param data:
    :return:
    '''
    try:
        url_list = data.get('urlList', None)
        for url in url_list:
            redis_conn.rpush(settings.ALIEXPRESS_URL, url)
        return {
            'code': True,
            'msg': '成功'
        }
    except Exception as e:
        return {
            'code': False,
            'msg': e
        }
