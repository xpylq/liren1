# /usr/bin/env python
# encoding=utf-8
import scrapy
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


# 爬取指定关键词的shopUrl
class ShopUrl(scrapy.Spider):
    name = "shopurl"

    def __init__(self, name=None, **kwargs):
        self.init_flag = False
        self.catalog_url_list = []
        self.shop_url_file = open("/Users/youzhihao/PycharmProjects/liren1/liren1/doc/shop_url.txt", "w", encoding="utf-8")
        catalog_file = open("/Users/youzhihao/PycharmProjects/liren1/liren1/doc/catalog.txt", "r", encoding="utf-8")
        for catalog_url in catalog_file.readlines():
            self.catalog_url_list.append(catalog_url.replace("\n", ""))
        super().__init__(name, **kwargs)

    def start_requests(self):
        url = "http://sz.meituan.com/"
        yield scrapy.Request(url=url, callback=self.parse, meta={"cookiejar": 1})

    def parse(self, response):
        if not self.init_flag:
            self.init_flag = True
            for catalog_url in self.catalog_url_list:
                yield scrapy.Request(url=catalog_url, callback=self.parse, dont_filter=True,
                                     meta={"cookiejar": response.meta["cookiejar"]})
        else:
            for shop_url in response.css(".abstract-item .abstract-pic::attr(href)"):
                self.shop_url_file.write("http:" + shop_url.extract() + "\n")
                self.shop_url_file.flush()
            next_url = self.fetch_next_url(response)
            if next_url:
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True, meta={"cookiejar": response.meta["cookiejar"]})

    def fetch_next_url(self, response):
        next_item = response.css(".right-arrow::attr(href)")
        if next_item:
            return "http:" + next_item.extract_first()
        else:
            return None


if __name__ == "__main__":
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(ShopUrl)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
