# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
#coding=utf-8
from scrapy import Selector
from scrapy.spiders import BaseSpider
import re

class DetailSpider(BaseSpider):
    name = "test_url"
    start_urls = ["http://www.tm.cn/search/detail?r=16156624&sort=01"]
    def parse(self, response):
        #print response.text
        select = Selector(text=response.text)

        div_list = select.xpath("//div[@class='container']/div[@class='info_table_box info_box']/div[@class='zxzc_tit']")
        for div in div_list:
            div_string_list = div.xpath("string(.)").extract()
            div_string = "".join(div_string_list)
            div_string = div_string.strip()
            print div_string
        
        tr_list = select.xpath("//div[@class='container']/div[@class='info_table_box info_box']/div[@class='sort_sec clearfix']/div[@class='w_515 sort_sec_table']/table/tbody/tr")
        #base_dict = {}
        i = 0
        for tr in tr_list:
            i = i+1
            tr_string_list = tr.xpath("string(.)").extract()
            tr_string = "".join(tr_string_list)
            tr_string = tr_string.strip()
            print i
            print tr_string
            if i==1:
                registernumber=tr_string
            elif i==2:
                classification=tr_string
            elif i==3:
                applydate=tr_string
            else:
                register=tr_string

        t_list = select.xpath("//div[@class='container']/div[@class='info_table_box info_box']/div[@class='sort_sec sort_sec_table']/table[@width='100%']/tbody/tr")
        for t in t_list:
            i = i+1
            t_string_list = t.xpath("string(.)").extract()
            t_string = "".join(t_string_list)
            t_string = t_string.strip("\n").lstrip("\n").rstrip("\n")
            print i
            print t_string
            print(t_string.replace('\t','').split('\n'))
