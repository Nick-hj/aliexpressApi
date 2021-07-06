# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: views
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/8 14:27
# Software: PyCharm

from .crwal_freight import CrawlFreight
from .check_addr import IlogisticsAddress
from fastapi import APIRouter, Body

router = APIRouter()


@router.get('/freight')
async def send_data(aeProductId: int, productNum: int, shipToCountry: str,
                    currency: str, sendCountry: str = '', minPrice: float = '1.00',
                    maxPrice: float = '2.00') -> list:
    '''
    ae运费接口
    :param aeProductId:
    :param productNum:
    :param shipToCountry:
    :param currency:
    :param sendCountry:
    :param minPrice:
    :param maxPrice:
    :return:
    '''
    data = CrawlFreight(aeProductId, productNum, shipToCountry, currency,
                        sendCountry, minPrice, maxPrice)
    return data.crawl_data()


@router.post('/ajaxSaveOrUpdateBuyerAddress')
async def save_data(data: dict = Body(...)):
    '''
    校验用户下单时地址
    :param data:
    :return:
    '''
    ret = IlogisticsAddress().submit_post(data)
    return ret

# http://172.18.115.161:8010/freight?aeProductId=
# 32788188511&productNum=1&currency=USD&shipToCountry=US
