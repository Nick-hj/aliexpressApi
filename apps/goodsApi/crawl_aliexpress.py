# -*- coding: utf-8 -*-
# ProjectName: topdser_spider
# FileName: crawl_aliexpress
# User: Navy
# Time: 2020/6/9 15:03

import requests

import http.client
import random
import re
import sys
import json

# sys.path.append('C:/Users/haijun/Dropbox/kfbuy/web_project/topdser_spider')

from apps.goodsApi.cookie import AE_cookie
from utils.base import proxy, logger

cookies = random.choice(AE_cookie)
http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch


class CrawlAliexpressSingle(object):
    def __init__(self, url):
        self.url = url

    def p_path(self, ali_id):
        path = '/item/' + str(
            ali_id) + '.html' + '?spm=a2g0o.productlist.0.0.7c7d131f8f5MAk&s=p&ad_pvid=202003100323484217588639233650002852041_2&algo_pvid=7405f564-28b9-4017-b7d9-08176565b6a9&algo_expid=7405f564-28b9-4017-b7d9-08176565b6a9-1&btsid=0bb47aa615838358283355049e68cc&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'
        return path

    def headers(self, ali_id):
        headers = {
            ':authority': 'www.aliexpress.com',
            ':path': self.p_path(ali_id),
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
            # 'user-agent': self.user_agent_r
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'cookie': cookies

        }
        return headers

    def crawl_aliexpress_detail(self):
        item = {}
        try:
            ali_id = re.findall(r'item/(\d+)', self.url)
            if ali_id:
                p_id = ali_id[0]
                response = requests.get(url=self.url, headers=self.headers(p_id), proxies=proxy())
                data_str = re.findall(r'data:(.*),.*csrfToken:', response.text, re.S)
                if data_str:
                    data = json.loads(data_str[0])
                    item['originalProductId'] = p_id
                    item['originalProductMasterImage'] = self.main_image(data)
                    item['originalProductName'] = data['titleModule']['subject']
                    item['originalProductURL'] = f'https://www.aliexpress.com/item/{p_id}.html'
                    item['maxPrice'] = self.highest_price(data)
                    item['minPrice'] = self.lowest_price(data)
                    item['channel'] = 1
            logger.info(item)
        except Exception as e:
            logger.error(f'爬虫返回异常：{self.url} =====>{e}')
        return item

    def main_image(self, data):
        image_url = data['imageModule']['imagePathList'][0]
        if '//' not in image_url:
            image_url = 'htpps://' + image_url
        elif 'http' not in image_url:
            image_url = 'https:' + image_url
        return image_url

    def highest_price(self, data):
        '''
        最高价格
        :param data:
        :return:
        '''
        try:
            hig_price = data['priceModule']['maxActivityAmount']['value']
        except Exception as e:
            hig_price = data['priceModule']['maxAmount']['value']
        return hig_price

    def lowest_price(self, data):
        '''
        最低价格
        :param data:
        :return:
        '''
        try:
            low_price = data['priceModule']['minActivityAmount']['value']
        except Exception as e:
            low_price = data['priceModule']['minAmount']['value']
        return low_price


if __name__ == '__main__':
    CrawlAliexpressSingle(
        'https://www.aliexpress.com/item/4000972971712.html?spm=a2g0o.productlist.0.0.79af3178lQkuM9&algo_pvid=9c9c87d0-487a-4c53-8872-3955f3f2d363&algo_expid=9c9c87d0-487a-4c53-8872-3955f3f2d363-0&btsid=0ab6fab215916867996495971ef0be&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_').crawl_aliexpress_detail()
