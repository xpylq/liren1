# /usr/bin/env python
# encoding=utf-8
import scrapy
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from liren1.items import ImageItem
import requests


# 爬取指定关键词的shopUrl
class Bmlink(scrapy.Spider):
    name = "bmlink"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

    def start_requests(self):
        for i in range(1, 2):
            url = "https://www.bmlink.com/company/search/p" + str(i) + ".html/"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if "/company/search" in response.url:
            company_url_list = response.css(".company a::attr(href)")
            for company_url in company_url_list:
                list.append(company_url)
                yield scrapy.Request(url="https:" + company_url.extract() + "certificate", callback=self.parse)
        else:
            company_name = response.css(".head-product h2::text").extract_first()
            img_url = response.css(".company_rzimg img::attr(src)").extract_first()
            item = ImageItem()
            item['image_url'] = img_url
            item['image_name'] = company_name
            yield item
            # res = requests.get(img_url)
            # with open("F:\\img\\" + company_name + ".jpg", 'wb') as f:
            #     f.write(res.content)


if __name__ == "__main__":
    list = []
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(Bmlink)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
    print("没去重,", list.__len__())
    print("去重,", set(list).__len__())
