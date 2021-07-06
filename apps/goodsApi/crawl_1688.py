# -*- coding: utf-8 -*-
# ProjectName: topder_spider
# FileName: crawl_1688
# User: Navy
# Time: 2020/6/8 14:19
import sys
import demjson
sys.path.append('C:/Users/haijun/Dropbox/kfbuy/web_project/topdser_spider')
import random
import requests
from utils.base import logger,proxy
import http.client
import re
from lxml import etree
from apps.goodsApi.cookie import COOKIE_1688


http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch

class CrawlGoods(object):
    '''
    /**
     * 原始商品id
     */
    private String originalProductId;

    /**
     * 原始商品主图
     */
    private String originalProductMasterImage;

    /**
     * 原始商品名称
     */
    private String originalProductName;

    /**
     * 原始商品URL
     */
    private String originalProductURL;

    /**
     * 商品最低价格
     */
    private String minPrice;

    /**
     * 商品最高价格
     */
    private String maxPrice;
    渠道
    channel=5
    '''
    def __init__(self,url):
        self.url = url

    def headers(self,pid):
        header = {
            ':authority': 'detail.1688.com',
            ':method': 'GET',
            ':path': '/offer/'+pid+'.html',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'referer': 'https://show.1688.com/pinlei/industry/pllist.html?spm=a260k.dacugeneral.home2019category.5.6633436ckDIBbZ&sceneSetId=857&sceneId=17125',
            'cookie':random.choice(COOKIE_1688),
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        return header

    def crawl_goods(self):
        ret_data = {}
        try:

            pid = re.findall(r'/offer/(\d+)',self.url)[0]
            data = requests.get(url=self.url, headers=self.headers(pid),proxies=proxy())
            html = etree.HTML(str(data.text))
            image = html.xpath('//meta[@property="og:image"]/@content')
            ret_data['originalProductMasterImage'] = re.sub(r'(\d+x\d+\.)','',image[0]) if image else ''
            ret_data['originalProductName'] = html.xpath('//meta[@property="og:title"]/@content')[0]
            ret_data['originalProductId'] = re.search(r'/(\d+)',self.url).group(1)
            ret_data['originalProductURL'] = self.url
            ret_data['channel'] = 5
            price = self.sku_list(html)
            ret_data['minPrice'] = min(price) if price else 0
            ret_data['maxPrice'] = max(price) if price else 0
            logger.info(f'url:{self.url},data:{ret_data}')
        except Exception as e:
            logger.error(f'爬虫返回异常：{self.url} =====>{e}')
        return ret_data

    def sku_list(self,html):
        sku_str = html.xpath(
            '//script[contains(text(),"var iDetailData")]/text()')[0]
        sku = re.findall('var iDetailData = ([\s\S]*);[\s\S]*?iDetailData.allTagIds', sku_str)
        price_range = []
        if sku:
            sku_dict = demjson.decode(sku[0])
            # sku_dict = json.loads(sku[0])  # 因为有换行符等不规则字符，所有此方法会报错
            price_range = [i[1] for i in sku_dict['sku']['priceRange']]
        return price_range

if __name__ == '__main__':

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(CrawlGoods('https://detail.1688.com/offer/618063982189.html').crawl_goods())
    CrawlGoods('https://detail.1688.com/offer/618063982189.html').crawl_goods()



