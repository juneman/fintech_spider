#!/usr/bin/env python3
# coding: utf-8
# File: cnki_patent_spider_wo_scrapy.py
# Author: lxw
# Date: 6/1/17 1:58 PM

import requests
import time
import urllib.parse


class CNKIPatentSpider:
    current_time = int(time.time() * 1000)

    def crawl(self):
        s = requests.Session()




        headers = {
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Host": "kns.cnki.net",
            "Referer": "http://kns.cnki.net/kns/brief/default_result.aspx",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            # "Cookie": 'cnkiUserKey=04eb89cc-50cb-8ca9-8fc1-fdaa81f0d4c5; kc_cnki_net_uid=87a8dbd6-1972-17da-6a36-53a5a8e7ef99; ASP.NET_SessionId=zo3yryqlt55ktqni20qac0od; SID_kns=123112; SID_klogin=125144; SID_crrs=125133; SID_kredis=125141; SID_krsnew=125134; IsLogin=; Ecp_ClientId=5170504215403262993; RsPerPage=50; LID=WEEvREcwSlJHSldRa1FhcTdWZDlrZytrdG1SK3ZGYnVFbWJaYkRuZ3BBcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhcTdWZDlrZytrdG1SK3ZGYnVFbWJaYkRuZ3BBcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=06/01/2017 17:59:32; c_m_expire=2017-06-01 17:59:32; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"zky311060","ShowName":"%e4%b8%ad%e5%9b%bd%e7%a7%91%e5%ad%a6%e9%99%a2%e8%bd%af%e4%bb%b6%e7%a0%94%e7%a9%b6%e6%89%80","UserType":"bk","r":"yzfDOC"}'
            # "Cookie": 'cnkiUserKey=04eb89cc-50cb-8ca9-8fc1-fdaa81f0d4c5; kc_cnki_net_uid=87a8dbd6-1972-17da-6a36-53a5a8e7ef99; ASP.NET_SessionId=zo3yryqlt55ktqni20qac0od; SID_kns=123112; SID_klogin=125144; SID_crrs=125133; SID_kredis=125141; SID_krsnew=125134; IsLogin=; Ecp_ClientId=5170504215403262993; RsPerPage=50; LID=WEEvREcwSlJHSldRa1FhcTdWZDlrZytrdG1SK3ZGYnVFbWJaYkRuZ3BBcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhcTdWZDlrZytrdG1SK3ZGYnVFbWJaYkRuZ3BBcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=06/01/2017 20:20:07; c_m_expire=2017-06-01 20:20:07; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"zky311060","ShowName":"%e4%b8%ad%e5%9b%bd%e7%a7%91%e5%ad%a6%e9%99%a2%e8%bd%af%e4%bb%b6%e7%a0%94%e7%a9%b6%e6%89%80","UserType":"bk","r":"yzfDOC"}'
            # "Cookie": 'cnkiUserKey=04eb89cc-50cb-8ca9-8fc1-fdaa81f0d4c5; kc_cnki_net_uid=87a8dbd6-1972-17da-6a36-53a5a8e7ef99; ASP.NET_SessionId=zo3yryqlt55ktqni20qac0od; SID_kns=123112; SID_klogin=125144; SID_crrs=125133; SID_kredis=125141; SID_krsnew=125134; IsLogin=; Ecp_ClientId=5170504215403262993; RsPerPage=50; LID=WEEvREcwSlJHSldRa1FhdXNXYXJwcFhZQUplaWFKVHZGTnNZQlhZNXl3Zz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhcTdWZDlrZytrdFdRZ2oyaGUwcXVQd25WY3pmWT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=06/01/2017 20:29:36; c_m_expire=2017-06-01 20:29:36; Ecp_LoginStuts={"IsAutoLogin":false,"UserType":"bk","r":"bNKYjp"}'
            "Cookie": 'ASP.NET_SessionId=zo3yryqlt55ktqni20qac0od; SID_kns=123112; RsPerPage=50;'
            # Ecp_LoginStuts={"IsAutoLogin":false,"UserType":"bk","r":"bNKYjp"}
        }
        """
        # TODO: PerPage看下最大是多少, 至少可以50
        Ecp_ClientId=4170504215902558260;
        RsPerPage=20;
        cnkiUserKey=eca75e30-81e1-2b85-3013-647b1379fd14;
        ASP.NET_SessionId=2wk4jijhu3zt1ziyifg03kih;
        SID_kns=123121;
        SID_klogin=125144;
        SID_crrs=125131;
        SID_krsnew=125131;
        SID_kredis=125143;
        IsLogin=;
        LID=
        """
        post_data = {
            "pagename": "ASP.brief_default_result_aspx",
            "dbPrefix": "SCOD",
            "dbCatalog": "%e4%b8%ad%e5%9b%bd%e5%ad%a6%e6%9c%af%e6%96%87%e7%8c%ae%e7%bd%91%e7%bb%9c%e5%87%ba%e7%89%88%e6%80%bb%e5%ba%93",  # "dbCatalog": "中国学术文献网络出版总库",
            "ConfigFile": "SCDBINDEX.xml",
            "research": "off",
            "t": repr(self.current_time),   # 就是curernt_time, 不是增加20分钟
            "keyValue": "%E5%B9%B3%E5%AE%89%E9%93%B6%E8%A1%8C%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8",   # "平安银行股份有限公司",
            "S": "1"
        }

        # url = "http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&dbPrefix=SCOD&dbCatalog=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%96%87%E7%8C%AE%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88%E6%80%BB%E5%BA%93&ConfigFile=SCDBINDEX.xml&research=off&t={0}&keyValue=%E4%B8%AD%E5%9B%BD%E5%B7%A5%E5%95%86%E9%93%B6%E8%A1%8C&S=1&queryid=11&skuakuid=11&turnpage=1&recordsperpage=50".format(int(time.time()*1000))    # OK
        url = "http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&dbPrefix=SCOD&dbCatalog=中国学术文献网络出版总库&ConfigFile=SCDBINDEX.xml&research=off&t={0}&keyValue=中国工商银行&S=1&queryid=11&skuakuid=11&turnpage=1&recordsperpage=50".format(int(time.time()*1000))  # OK
        # url = urllib.parse.quote(url, safe=":/=?&")
        print(url)

        """
        params = []
        for key, value in post_data.items():
            params.append("{0}={1}".format(key, value))
        url = url + "&".join(params)
        """

        # req = requests.Request("GET", url=url, data=post_data, headers=headers)
        req = requests.Request("GET", url=url, headers=headers)
        prepped = s.prepare_request(req)
        resp = s.send(prepped)
        print(resp.text)
        print("--" * 30)
        return

        s.cookies = resp.cookies
        print("Cookie:", dict(resp.cookies))
        req = requests.Request("GET", url=url, data=post_data, headers=headers)
        prepped = s.prepare_request(req)
        # proxy = "122.4.189.67:43184"
        # proxies = {"http": proxy, "https": proxy}  # NOTE: 这里"http"和"https"一定要都写，不能只写http或者是只写https
        # resp = s.send(prepped, proxies=proxies)
        resp = s.send(prepped)
        print(resp.text)

if __name__ == "__main__":
    spider = CNKIPatentSpider()
    spider.crawl()



