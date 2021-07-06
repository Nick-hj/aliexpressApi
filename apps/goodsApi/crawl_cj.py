# -*- coding: utf-8 -*-
# ProjectName: ali_freight
# FileName: crawl_data
# User: haijun
# Email: haijun0422@gmail.com
# Time: 2020/5/7 15:47
# Software: PyCharm
import sys

# sys.path.append('C:/Users/haijun/Dropbox/kfbuy/web_project/topdser_spider')
import requests
import re
import json
from utils.base import proxy,logger

class CrawlCJSingle(object):
    def __init__(self,url):
        '''
        :param name: 用户名
        :param password: 密码
        :param goods_list_url: 商品列表url
        :param goods_detail_url: 商品详情url
        '''
        self.post_url = 'https://app1.cjdropshipping.com/cj/locProduct/huoQuShangPinXiangQing'
        self.url = url

    def headers(self,goods_id):
        return {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '56',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'app1.cjdropshipping.com',
            'Origin': 'https://app.cjdropshipping.com',
            'Referer': f'https://app.cjdropshipping.com/product-detail.html?id={goods_id}&push_id=&fromType=',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'token': '',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

    def crawl_detail(self):
        '''
        详情接口 https://app1.cjdropshipping.com/cj/locProduct/huoQuShangPinXiangQing
        params {"token":"a1a8d49c4b3e9adc18f83a49e40d68ee","id":"50D0FACA-1B26-4A33-9ACB-F852CBEFE5C0","productType":"0"}
        method: post
        :param id: 商品id
        :return:
        '''
        item = {}
        try:
            url = self.url.split('&')[0]
            if 'id' not in url:
                return {}
            goods_id = re.findall(r'id=(.*)',url)
            if goods_id:
                pid = goods_id[0]
                data = {"token": "", "id":pid, "productType": "0"}
                response = requests.post(url=self.post_url,headers=self.headers(pid),data=json.dumps(data),proxies=proxy())
                ret = json.loads(response.text)
                if ret['statusCode'] == '200':
                    data = ret['result']
                    price_list = self.price_info(data)
                    item['originalProductId'] = pid
                    item['originalProductMasterImage'] = data.get('BIGIMG', '')  # 主图
                    item['originalProductName'] = data.get('NAMEEN', '') # 产品英文名
                    item['originalProductURL'] = self.url
                    item['channel'] = 4
                    item['minPrice'] = min(price_list)
                    item['maxPrice'] = max(price_list)
            logger.info(item)
        except Exception as e:
            logger.error(f'爬虫返回异常：{self.post_url} =====>{e}')
        return item

    def price_info(self,data):
        '''
        sku信息
        :param data:
        :return:
        '''
        price_list = [] # 用于算最高价和最低价
        sku_list = data['stanProducts']
        for sku in sku_list:
            sku_property = {}
            price = sku.get('SELLPRICE', '')
            seller_price = float(price) if price is not None else 0
            sku_property['price'] = seller_price
            price_list.append(sku_property['price'])
        return sorted(price_list)


if __name__ == '__main__':
    CrawlCJSingle('https://app.cjdropshipping.com/product-detail.html?id=85022B17-D31B-4589-AFBF-16917F725D1F&push_id=&fromType=').crawl_detail()


