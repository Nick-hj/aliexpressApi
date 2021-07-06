# -*- coding: utf-8 -*-
# ProjectName: topdser_spider
# FileName: views
# User: Navy
# Time: 2020/6/8 14:43

from fastapi import APIRouter
from apps.goodsApi.crawl_1688 import CrawlGoods
from apps.goodsApi.crawl_cj import CrawlCJSingle
from apps.goodsApi.crawl_aliexpress import CrawlAliexpressSingle



router = APIRouter()

@router.get('/goods')
async def send_data(url:str):
    data = {}
    if '1688.com' in url:
        data = CrawlGoods(url).crawl_goods()
    elif 'cjdropshipping.com' in url:
        data = CrawlCJSingle(url).crawl_detail()
    elif 'aliexpress.com' in url:
        data = CrawlAliexpressSingle(url).crawl_aliexpress_detail()
    return data
