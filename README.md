# real-time
python爬取中国商标网的信息

##  一些参考文献  

1. 【scrapy】学习Scrapy入门 http://www.jianshu.com/p/a8aad3bf4dc4  

2. 如何优化Python爬虫速度 https://www.zhihu.com/question/20145091  

3. 如何入门python爬虫 https://www.zhihu.com/question/20899988/answer/24923424?group_id=252360038  

4. 爬取豆瓣电影 http://www.cnblogs.com/Shirlies/p/4536880.html

   ## 起始网站  

   [中国商标网]([http://wsjs.saic.gov.cn/txnS01.do?locale=zh_CN])

   ## 考核标准

   1. 文档考核：

      > 给出爬虫的**软件架构文档、测试文档和网络架构文档**(测试文档需要满足下面的考核，方便测试人员，文档考核由测试人员给出  

   2. 代码考核：

      > **搜索条件，url抓取、网页解析、数据保存**四个模块做到**低耦合**  

   3. 实时性考核：

      > 给出一个关键字能够在**10秒**完成搜索为及格，**5秒**为良好，**3秒**为优秀  

   4. 健壮性考核：

      > 给出关键字列表，爬取的出错率在**1%以下**。

   5. 爬取完整性考核：

      >  随机抽取爬取的信息，需要维持**信息错误率在1%以下**。  

   6. 爬取效率考核：

      > 每日搜索量达到7.5W为及格，每日搜索达到15W为良好，达到25W为优秀。