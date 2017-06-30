# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrademarkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TrademarkName = Field() #商标名
    RegistrationNumber = Field() #注册号
    Classification = Field() #国际分类
    ApplyDate = Field() #申请日期
    RegisterDate = Field() #注册日期
    TrademarkPic = Field() #商标图片
    ApplicantName = Field() #申请人名称
    ApplicantAddress = Field() #申请人地址
    PreliminaryNoticeNo = Field() #初审公告期号
    PreliminaryNoticeDate = Field() #初审公告日期
    RegisterNoticeNo = Field() #注册公告期号
    RegisterNoticeDate = Field() #注册公告日期
    ExclusiveRightTime = Field() #专用权期限
    Type = Field() #商标类型
    TogetherTrademark = Field() #是否共有商标
    Remark = Field() #备注
    AgentName = Field() #代理人名称
    Service = Field() #商品/服务
    SimilarGroups = Field() #类似群组
    Process = Field() #商标流程
