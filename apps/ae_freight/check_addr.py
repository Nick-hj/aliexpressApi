# -*- coding: utf-8 -*-
# ProjectName: topdser_spider
# FileName: crawl_addr
# User: Navy
# Time: 2020/8/3 14:27

import requests
import json
import http.client
import re
import os
import execjs
from utils.base import logger
http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch


class IlogisticsAddress(object):
    def __init__(self):
        self.url = 'https://ilogisticsaddress.aliexpress.com/ajaxSaveOrUpdateBuyerAddress.htm'
        self.username = 'haijun0425@126.com'
        self.password = 'haijun19840422@'
        self.session = requests.session()

    def headers(self):
        header = {
            ':authority': 'ilogisticsaddress.aliexpress.com',
            ':method': 'POST',
            ':path': '/ajaxSaveOrUpdateBuyerAddress.htm',
            ':scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'content-length': '466',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ali_apache_id=11.134.216.25.1595408820122.207399.7; cna=te+eFzkPsyACAXeJNI7fzH/w; _ga=GA1.2.1903783294.1595408828; _fbp=fb.1.1595408828208.26533891; aep_common_f=A4WJE9HcbRg0BKi6TCgAoFuS5Bn53OHp40RSYuoZ8MQYPmoCqmwP5g==; acs_usuc_t=x_csrf=1ehwhknw3j7d4&acs_rt=2c89361850cf42d7badb31988d3e14c9; intl_locale=en_US; _gid=GA1.2.196898434.1596425768; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000074678274%094000165426444%094001145579866%0932813748506%094000828360942%0932852027460%094001148045357%094001148048333; _m_h5_tk=fbd3afb77c874c68e18ea3f746be8ae1_1596437876322; _m_h5_tk_enc=d1375b4a9413102de6cf135a59d6ec91; havana_tgc=eyJjcmVhdGVUaW1lIjoxNTk2NDM1OTMzMzI2LCJsYW5nIjoiZW5fVVMiLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDEyMTA0MDY5NzEsInRndElkIjoiMWtCZk5VSHExRjFIRDVJd0pNRHEzOEEifX19fQ; _hvn_login=13; xman_us_t=x_lid=cn258600111mbaae&sign=y&rmb_pp=haijun0425@126.com&x_user=1C6MdPhdWie82igD7yg4p8+1PJGvt4hsWoSuBo78D7U=&ctoken=p2bd7wjbhbec&need_popup=y&l_source=aliexpress; aep_usuc_t=ber_l=A1; xman_f=XUSoOP7FplaL2Z2PznGn2a780dg6q0xcjTR2FaorCRtpCxQkzZSealNcqkpjymKHc3sX/d5k+00o5vxQNz7WMNAcOdQbiqnYdEoej4GJA+cnHEc663b93uKjf1dv6d+9jmAkdxTm47moO2TlBuCFUskQfpTi2bDD7N9BIM69AMaejqX32PeqG8ZwhT+hZsusz6vNeb+1Qj0fb/LQJ/PkvyBz44QzkhqKAILfn3sY/eY6kpU45sf2LNbbbA76RsfmCNFkSNKUEOlpajJDDmgi+gV9OndGpnPXbR4xXTymb6cRdpopo9tEDENflrJLCKTfBHTuQGk7Lf/CjLZGXlT6O/67FAbrq/luePZB0SCie/r+ZTSokJjUZdiAlE8PbhdOq2ebviRrNEbp6Hdw8hKDXJq2U8elQcYg5vhWXM37+IFe1Kb9g1actg==; aep_usuc_f=site=glo&c_tp=USD&x_alimid=1859821111&isb=y&region=CN&b_locale=en_US; intl_common_forever=MYYsj7Fg2QMtIxjhcGmTNNNySBAKtChsrOU3mV9dmX4sHga6+Ac8Ew==; ali_apache_track=mt=1|ms=|mid=cn258600111mbaae; ali_apache_tracktmp=W_signed=Y; JSESSIONID=WCYJRXVV-9QMH5HMMX2MBO3XHNDQT3-D2UQ4EDK-R662; tmp0=aFZxLUU91r7XvGYrNDyr9%2BTPOavhSYlx7RoJzHldMjn1jD4wJgib80q8kOz7%2Fv39ATQZOXvqgwwezE8wx1MgBHBCRuHGEmNr3hg1lpIzQEkOrcPnntPklcRtaLUg%2FzzbNgU%2B%2FjIW92TlQHyYeWeslQ%3D%3D; xman_us_f=x_lid=cn258600111mbaae&x_l=0&x_locale=en_US&no_popup_today=n&x_user=CN|haijun|yu|ifm|1859821111&x_c_chg=0&zero_order=y&acs_rt=600507a434994f9faf302c7fa1cb3fa9&last_popup_time=1595494909569&x_as_i=%7B%22cookieCacheEffectTime%22%3A1596436236985%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D; xman_t=tSF4z4AUyzOrHpORdExSNIyAzeFJFqDiAWwWIvewiVZJpXsNWakBT1nytt/srzDQ/Y0TlEvLeKwiWQp0CPTyP0cgY/BQuA6/Wdr87IKj0PNeXUD2huBRkTdfbZXq7EdTKizE82oJmZkcI/vtoeMMinV7tv1YRy/iQhvcdvM7OJOupqTZI7DMJm0hKtUglw1WODJF2j3p5vcIEBiwkmzsln8nknlRwGq74XnBZcMpgjdz1p0h+5Fm7ZJPWUmLcOzq7T9eu8JqE9Zim7TRl86gsXSTf5vdn0HjOtfRgNmCKcyh9xJnW7HhMzSlNfuVtCREIg4LYgX8+SX6gOzAvs2o4SW8EHIfeSOCNM/tjw8GoN2rIaU0FAb1CrXvWARNwfnOpIX2Ve4B1vnYspvt+WriYZ+NoDhLdzGZl0k6NCDJ0dyahkoWMJx5wcwSiZWvkxRO80r8dr26toRaLV1KUxorUUh6LyzcM1Aee8uEB/CfvixojEj0cFK+gjHd3GUjfmuC4k7SWj9eWeBm2+2lam1Pdgm5mwFMkX7lIbN57ZdpaSIvHu8frbWU7uTqHmrOYT0d1JKQ0Tix0UwagX0MtIpfI9GLCGKCVZecB4IPCqGXyPwCUs98AmsUXHYRFxCcqAEZoSBSpUzDUK2xEN/ma6V48w==; l=eBxRzo2mONEkzEraBO5Zlurza7794QOfhsPzaNbMiInca69F6eZPQNQqq1MWJdtjgt50MFtPe0F7oRUH5ja38x18LCHEL0oyHApB7e1..; isg=BKenj9_ptJlrqDAqaPICWtGSNttxLHsOPLDN4nkXkDZAaMEqhf4LX4Iuimh2gFOG',
            'origin': 'https://ilogisticsaddress.aliexpress.com',
            'referer': 'https://ilogisticsaddress.aliexpress.com/addressList.htm?spm=a2g0s.9042311.0.0.3ada4c4dCNEOGT',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        return header

    def getpwd(self):
        with open('./rsa_password.js', 'r', encoding='utf8')as f:
            content = f.read()
        jsdata = execjs.compile(content)
        pw = jsdata.call('getPwd', self.password)
        return pw

    def get_cookie(self):
        url = 'https://passport.aliexpress.com/newlogin/login.do?appName=aebuyer&fromSite=13'

        data = {
            'loginId': self.username,
            # 'password2': '591633f408abb342c2573a14d68f95021b28a28d3eb92b3b67db0ff15f8734ba104def6a43216f413c7abd8fe3e960ed95c02ba818c930aaeac4605683ab03cb1f1b56d86dc2b47984762ac0618fbbd8f4d8e3824a298bf24d7d95b8df9c7280d3910e4a76d763a0518b9d6c3685b2da0af41ea1c88f5aff97c49909b9fefa20',
            'password2': self.getpwd(),
            'keepLogin': 'false',
            'umidGetStatusVal': '255',
            'screenPixel': '1536x864',
            'navlanguage': 'zh-CN',
            'navUserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'navPlatform': 'Win32',
            'appName': 'aebuyer',
            'appEntrance': 'aebuyer',
            'isMobile': 'false',
            'lang': 'en_US',
            'returnUrl': '',
            'fromSite': 13,
            'bizParams': '',
            'umidToken': 'T8803408A2B6DC73B235FD433960984BA46DD4198FF9B2B3BDAF86BD1D2'
        }

        cookie_jar = self.session.post(url=url, data=data, headers=self.headers())
        logger.info(cookie_jar.text)
        cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar.cookies)
        # cookie字典转化为字符串
        cookie_str = ';'.join([k + '=' + v for k, v in cookie_dict.items()])
        return cookie_str

    def write_cookie(self):
        base_dir = os.path.join(os.getcwd(), 'cookie')
        file_name = self.username + '.txt'
        file = os.path.join(base_dir, file_name)
        with open(file, 'w') as f:
            f.write(self.get_cookie())

    def read_cookie(self):
        base_dir = os.path.join(os.getcwd(), 'cookie')
        file_name = self.username + '.txt'
        file = os.path.join(base_dir, file_name)
        try:
            with open(file, 'r') as f:
                cookie = f.readline()
                # print(f'读取cookie{cookie}')
        except Exception:
            IlogisticsAddress().write_cookie()
            with open(file, 'r') as f:
                cookie = f.readline()
        return cookie

    def submit_post(self, data):
        logger.info(f'地址校验接收数据===={data}')
        header_addr = {
            ':authority': 'ilogisticsaddress.aliexpress.com',
            ':method': 'GET',
            ':path': '/addressList.htm',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'referer': 'https://coupon.aliexpress.com/buyer/coupon/listView.htm?spm=a2g0o.detail.1000001.35.509918d6pPFV5g',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            # 'cookie':self.read_cookie(),
            'cookie': 'ali_apache_id=11.134.216.25.1595408820122.207399.7; cna=te+eFzkPsyACAXeJNI7fzH/w; _ga=GA1.2.1903783294.1595408828; _fbp=fb.1.1595408828208.26533891; intl_locale=en_US; _gid=GA1.2.196898434.1596425768; ali_apache_tracktmp=W_signed=Y; JSESSIONID=WCYJRXVV-9QMH5HMMX2MBO3XHNDQT3-D2UQ4EDK-R662; tmp0=aFZxLUU91r7XvGYrNDyr9%2BTPOavhSYlx7RoJzHldMjn1jD4wJgib80q8kOz7%2Fv39ATQZOXvqgwwezE8wx1MgBHBCRuHGEmNr3hg1lpIzQEkOrcPnntPklcRtaLUg%2FzzbNgU%2B%2FjIW92TlQHyYeWeslQ%3D%3D; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094001145579866%0932813748506%094000828360942%0932852027460%094001148045357%094001148048333%094000077838042%094000077838042; _hvn_login=13; aep_usuc_t=ber_l=A1; _m_h5_tk=f8b9c308d3b8774b1886a57f8d9d2596_1596512154657; _m_h5_tk_enc=6f75b95a9a2386688dba6be4e239290e; acs_usuc_t=x_csrf=9xhlfc64q4hg&acs_rt=2c89361850cf42d7badb31988d3e14c9; havana_tgc=eyJjcmVhdGVUaW1lIjoxNTk2NTA5OTg5OTU1LCJsYW5nIjoiZW5fVVMiLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDEyMTA0MDY5NzEsInRndElkIjoiMWJ1VXpTejJvZDRFUkJzS2xGVzJnV3cifX19fQ; xman_us_t=x_lid=cn258600111mbaae&sign=y&rmb_pp=haijun0425@126.com&x_user=cwOcoaJyxUMwE/vTQnnMxH8I56M6mUL+mIyUeSfUZT0=&ctoken=lmbw4l3ju8j3&need_popup=y&l_source=aliexpress; aep_common_f=pgeElPt9DfKNXOfoBUvaBzLg6AO4njR831T/aXNcDLeyYpeDnIGOsw==; xman_f=48XzP2JOAvEYKRATqk1PHtMr3VQIvG3o0+aPYCy9aj0jd0AouPCRneNSsYBuFTBvkdndLhhUTyPwP0D63YBTY7nQH5loNw+as1r7GG4HI3eEWfRUCFnneiDsJ1qqlE0jNuOwz+cIrT7W41H8AsX9FDemaRlKUFRCmFCykwROp7zp18wJkPfm5yDsGnvHV9IbMddTRnRkp6f+IWRWlia4H9u4DBEHfUh7kKvfbZ4gSktZ5/0gyPH8WkjuuZmeGOAemA5JOmnXXyp9FIcjvipyM+irtmDY6WMmxHqHUvAuqQJFwZxU0LxlfGOGR1NoyrdsT0KiICJXt4iolzWtVwxfgh/Bs86TnaQ1kepPgG8Ftpc4eOUrRTHar0TZdysGt3c70hxU2sbltVTR9xgHvn0dMxjq4L3lo5aXXOQg7K9nTX29TjTzTeGxVw==; aep_usuc_f=site=glo&c_tp=USD&x_alimid=1859821111&isb=y&region=CN&b_locale=en_US; intl_common_forever=tl9Z6kTNP4AnpaKTWxHZ0iFNrqoSb5i70sryvNxxhWhfFHe0lGKeaw==; ali_apache_track=mt=1|ms=|mid=cn258600111mbaae; xman_us_f=x_lid=cn258600111mbaae&x_l=0&x_locale=en_US&no_popup_today=n&x_user=CN|haijun|yu|ifm|1859821111&x_c_chg=0&zero_order=y&acs_rt=600507a434994f9faf302c7fa1cb3fa9&last_popup_time=1595494909569&x_as_i=%7B%22cookieCacheEffectTime%22%3A1596510022477%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D; xman_t=hZ+6YP08NSWywkLRJJaUXFC1wwvgjjvQdy2My7TFgiOvGeqkXWuRL9I39ssUUywz9SXIyqiXXsX2kGN0+KuUSq+aezlKIWrC+obO68pAFmsHxih60Fsaf1kmx6VOMoERnKol7cjrxfGV2aSZDkVbT98/FIHVNeJEa/hBhdFK717KphlOPYCd7gvn6z/XG4t36o84e5fwiroRbDVRaU/F6MbRf/DD69AJBq/C+fC3c39lnabjrdU/4TopHBuYWldzlWSK/LtkxkFbuFaY/Iw0x9ogrGHAXC75CtMAk3zZUoPMCMgzBVp3GkXtJiT3WpzB1wYDKNhDWIvjS+QvPYwOBArNg5Xlkn96kHioue5EowWU9yKlYLFE1/yuYbP8ahqFw1JxxjSJglHcwpZD/QCgAAhrW4KcJ4j4bh8ur5lpaAeNd62eBia1ErsyHdY1Edkq9BavqNDl1o5tAsRDkg4rJrQERy5MAr2bqybQjDbyH84ru12r/tehoo9EloqTNOgFuYv8fJ+bjrfQJOzWdFnXyHwkdFqJjaKA7cC8pdJEWAsdWqOXUEfJQlCZxO6sJKtBGFVkmO/hEmt0tD8+wVpNrMiB3ZhloratgOF4Ib1liyDdVyjiGdNzkf+btnHbB6O8BaatqpM2RtLMGx+1LOfBiw==; tfstk=cBdFBQaR6XhUjoCSH61zOlv5Y4WdZ8Slc57VKKF9M83the6hioqRST3V7aSxs9f..; l=eBxRzo2mONEkziLNBO5aourza77TaIdb8sPzaNbMiInca6ilteOUCNQqX3xJSdtjgt5c4etPe0F7oRny8l4LRxtc051rL0oyHFJM8e1..; isg=BFZW_6VfFQnTwiGd8ZnDlZj5pwxY95oxBYv89cC-mznEg_cdKIYzQTE1Gx9vK5JJ',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

        data = {
            '_csrf_token_': 'gV66KDSla2qQIbgxJ7pAxA',
            'useLocalAddress': 'true',
            'id': 5116470423,
            # 'id': 5136990645,
            'address2': data.get('address2', ''),
            'address': data.get('address', ''),
            'city': data.get('city', ''),
            'cityCode': data.get('cityCode', ''),
            'cityInLocalLanguage': '',
            'contactPerson': data.get('contactPerson', ''),
            'country': data.get('country', ''),
            'countryName': data.get('countryName', ''),
            'encryptCpf': '',
            'encryptPassportNo': '',
            'features': {"mobile_no_verified": "false", "locale": "local"},
            'isDefault': '',
            'isForeigner': '',
            'mobileNo': data.get('mobileNo', ''),
            'phoneCountry': data.get('phoneCountry', ''),
            'province': data.get('province', ''),
            'provinceCode': data.get('provinceCode', ''),
            'provinceInLocalLanguage': '',
            'zip': data.get('zip', ''),
            # 巴西
            'cpf': data.get('cpf', ''),
            # 俄罗斯
            'firstName': data.get('firstName', ''),
            'middleName': data.get('middleName', ''),
            'lastName': data.get('lastName', ''),
            'passportNo': data.get('lastName', ''),
            'passportNoDate': data.get('passportNoDate', ''),
            'passportOrganization': data.get('passportOrganizatio', ''),
            'taxNumber': data.get('taxNumber', ''),
            'birthday': data.get('birthday', ''),
            'rutNo': data.get('rutNo', '')
        }
        res = self.session.post(url=self.url, data=data, headers=header_addr)
        # 成功 {"fieldErrorMessageList":[],"id":5116470423,"success":true}
        res_text = res.text
        logger.info(f'地址校验返回数据======={res_text}=======接收的数据{data}')
        res_dict = json.loads(res_text)
        if res_dict['success']:
            success_response = {
                'code': 0,
                'msg': '校验成功'
            }
            return success_response
        else:
            error_list = res_dict['fieldErrorMessageList']
            ret = []
            for error in error_list:
                error_dict = {
                    'name': error.get('name', ''),
                    'errorMessage': error.get('errorMessage', '')
                }
                ret.append(error_dict)

            error_response = {
                'code': 999,
                'msg': '校验失败',
                'data': ret
            }
            return error_response


if __name__ == '__main__':
    # res = IlogisticsAddress('haijun0425@126.com','haijun19840422@')
    data = {
        "_csrf_token_": "gV66KDSla2qQIbgxJ7pAxA",
        "useLocalAddress": "true",
        "id": 5116470423,
        # 'id': 5136990645,
        "address2": "",
        "address": "test test",
        "city": "Affiliated banks service co",
        "cityCode": 92286765545800000,
        "cityInLocalLanguage": "29 palms",
        "contactPerson": "TEST",
        "country": "US",
        "countryName": "United States",
        "encryptCpf": "",
        "encryptPassportNo": "",
        "features": {"mobile_no_verified": "false", "locale": "local"},
        "isDefault": "",
        "isForeigner": "",
        "mobileNo": "87654",
        "phoneCountry": "",
        "province": "",
        "provinceCode": "922867650000000000",
        "provinceInLocalLanguage": "California",
        "zip": "12345",
        # 巴西
        "cpf": "",
        # 俄罗斯
        "firstName": "",
        "middleName": "",
        "lastName": "",
        "passportNo": "",
        "passportNoDate": "",
        "passportOrganization": "",
        "taxNumber": "",
        "birthday": ""

    }
    res = IlogisticsAddress()
    print(res.submit_post(data))
