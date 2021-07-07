# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 15:33
# @Author  : Haijun

from aliexpress.conf.settings import load_or_create_settings
from aliexpress.core.goods_detail import ProductsSpider
from aliexpress.core.shop import ShopProducts

load_or_create_settings('')


def crawler(url):
    if '/item/' in url:
        p = ProductsSpider(url)
        p.goods_info()
    elif '/store/' in url:
        goods_url = ShopProducts()
        goods_url.goods_list(url)
