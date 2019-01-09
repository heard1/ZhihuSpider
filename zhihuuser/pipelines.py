# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
path = "/Users/admin/Desktop/zhihuSpider/info/"

class ZhihuuserPipeline(object):
    def process_item(self, item, spider):
        try:
            #简化
            tem=""
            for i in range(len(item['educations'])):
                try:
                    tem += item['educations'][i]['major']['name']+' '
                except:
                    pass
                try:
                    tem += item['educations'][i]['school']['name']+' '
                except:
                    pass    
            item['educations'] = tem

            tem=""
            for i in range(len(item['employments'])):
                try:
                    tem += item['employments'][i]['company']['name']+' '
                except:
                    pass
                try:
                    tem += item['employments'][i]['job']['name']+' '
                except:
                    pass
            item['employments'] = tem

            tem=""
            for i in range(len(item['locations'])):
                tem += item['locations'][i]['name']+' '
            item['locations'] = tem
        except:
            pass
        tempath = path + item['url_token'] +".txt"
        out = open(tempath,'w')
        out.write(str(item))
        out.close()

        tempath = path + "NEXT"
        out = open(tempath,'w')
        out.write(item['url_token'])
        out.close()

        return item
