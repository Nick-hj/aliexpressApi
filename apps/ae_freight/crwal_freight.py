# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: crwal_freight
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/6 16:06
# Software: PyCharm
from retrying import retry
import requests
import json
import http.client
import re
from utils.base import logger

http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
'''
https://www.aliexpress.com/aeglodetailweb/api/logistics/freight?productId=32863610510&count=10&minPrice=30.02&maxPrice=30.02&country=US&provinceCode=&cityCode=&tradeCurrency=USD&userScene=PC_DETAIL
'''

'''
    传参
    aeProductId: 商品ID
    productNum: 购买数量
    sendCountry: 发货国家码(可能为空)
    shipToCountry: 收货国家码
    currency: 货币单位
'''
'''
    返回数据
    {
        "freightList":[
            {
                "shipCost":8.42, //运费
                "shipChannel":"OTHER_US", // 运费简称
                "channelDisplayName":"Seller's Shipping Method - US", //运费全称
                "isTracked":true, // 是否可跟踪
                "estimatedDeliveryTime":"8-8" // 配送时长
            }
        ]
    }
'''


class CrawlFreight(object):
    def __init__(self, product_id, count, country, trade_currency, sendGoodsCountry, minPrice, maxPrice):
        '''
        初始化
        :param product_id: 商品id
        :param count:  商品数量
        :param country: 收件国家码
        :param trade_currency: 币种
        '''
        self.url = 'https://www.aliexpress.com/aeglodetailweb/api/logistics/freight'
        self.product_id = product_id
        self.count = count
        self.country = country
        self.trade_currency = trade_currency,
        self.sendGoodsCountry = sendGoodsCountry
        self.min_price = minPrice
        self.max_price = maxPrice

    def proxy(self):
        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "H0W6QL9KT8T905JD"
        proxyPass = "5450A9EF3224A0EF"
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

    def headers(self) -> dict:
        '''
        请求头
        :return:
        '''
        return {
            ':authority': 'www.aliexpress.com',
            # ':path': path,
            'accept-encoding': 'gzip,deflate,br',
            ':method': 'GET',
            'cache-control': 'max-age=0',
            ':scheme': 'https',
            'referer': 'https://www.aliexpress.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

    def params(self) -> dict:
        '''
        参数
        https://www.aliexpress.com/aeglodetailweb/api/logistics/freight?productId=32821068996&count=1&minPrice=4.66&maxPrice=4.66&country=US&provinceCode=&cityCode=&tradeCurrency=USD&sellerAdminSeq=225245298

        https://www.aliexpress.com/aeglodetailweb/api/logistics/freight?productId=4001015573016&count=1&minPrice=21.19&maxPrice=21.19&country=US&provinceCode=&cityCode=&tradeCurrency=USD&sellerAdminSeq=239301968&userScene=PC_DETAIL_SHIPPING_PANEL
        :return:
        '''

        return {
            'productId': self.product_id,
            'count': self.count,
            'country': self.country,
            'tradeCurrency': self.trade_currency,
            'sendGoodsCountry': self.sendGoodsCountry,
            "userScene": 'PC_DETAIL_SHIPPING_PANEL',
            'provinceCode': '',
            'minPrice': self.min_price,
            'maxPrice': self.max_price,
            'cityCode': '',
            'sellerAdminSeq': 239301968

        }

    @retry(stop_max_attempt_number=5)
    def crawl_data(self) -> list:
        '''
        获取数据
        :return:
        '''
        import time
        s = time.time()
        # ret = requests.get(url=self.url,headers=self.headers(),params=self.params(),proxies=self.proxy())
        ret = requests.get(url=self.url, headers=self.headers(), params=self.params())
        data = json.loads(ret.text)
        body = data.get('body', '')
        freightList = []
        if body:
            freight_result = body.get('freightResult', '')
            if freight_result:
                for result in freight_result:
                    cost_detail = {
                        'deliveryDate': result.get('deliveryDate', ''),  # 配送预计到达时间
                        'channelDisplayName': result.get('company', ''),  # 运输方式
                        'currency': result.get('currency', ''),  # 币种
                        'isTracked': result.get('tracking', ''),  # 是否可追踪
                        'shipChannel': result.get('serviceName', ''),  # 运输方式简称
                        'estimatedDeliveryTime': result.get('time', ''),  # 配送时长
                        'shipCost': result.get('freightAmount').get('value')
                    }
                    freightList.append(cost_detail)
            else:
                logger.error(f'运费返回为空，url:{self.url}')
        logger.info(f'运费爬取，url:{self.url},data:{freightList},时间{time.time() - s}')
        return freightList


if __name__ == '__main__':
    data = CrawlFreight(4001015573016, 1, 'US', 'USD', 'CN', 21.19, 21.19)

    print(json.dumps(data.crawl_data()))

'''
{"freightList": [{"deliveryDate": "2020-06-05", "channelDisplayName": "TNT", "currency": "USD", "isTracked": true, "shipChannel": "TNT", "estimatedDeliveryTime": "12-23", "shipCost": 154.28}, {"deliveryDate": "2020-05-22", "channelDisplayName": "DHL", "currency": "USD", "isTracked": true, "shipChannel": "DHL", "estimatedDeliveryTime": "6-13", "shipCost": 169.28}, {"deliveryDate": "2020-05-15", "channelDisplayName": "Fedex IP", "currency": "USD", "isTracked": true, "shipChannel": "FEDEX", "estimatedDeliveryTime": "5-8", "shipCost": 169.77}]}
{"freightList": [{"deliveryDate": "", "channelDisplayName": "USPS", "currency": "USD", "isTracked": true, "shipChannel": "USPS", "estimatedDeliveryTime": "4-13", "shipCost": 2.36}, {"deliveryDate": "2020-06-16", "channelDisplayName": "Seller's Shipping Method - US", "currency": "USD", "isTracked": true, "shipChannel": "OTHER_US", "estimatedDeliveryTime": "9-18", "shipCost": 2.98}]}
'''
