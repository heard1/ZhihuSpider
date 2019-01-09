本爬虫旨在爬取知乎用户的个人信息，并支持断点续爬。



**安装依赖**

​	pip3 install scrapy

​	pip3 install selenium

​	zhihuSpider/chromedriver替换为对应版本

**修改路径**

​	替换"/Users/admin/Desktop"为zhihuSpider所在目录：

​	zhihuSpider/zhihuuser/\_\_init__.py 第11行

​	zhihuSpider/zhihuuser/pipelines.py 第7行

​	zhihuSpider/zhihuuser/spiders/zhihu.py 第6行

**运行**

​	在terminal中进入zhihuSpider文件夹，输入

​		scrapy crawl zhihu

​	开始爬取



结果储存在zhihuSpider/info中，不可删除NEXT文件(断点续爬必需)

如出现中断，可能是IP被封

不登录也可爬取，而且没有被封号风险

​	 







