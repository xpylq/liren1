# /usr/bin/env python
# encoding=utf-8
import scrapy
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


# 爬取指定关键词的shopUrl
class Img(scrapy.Spider):
    name = "img"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

    def start_requests(self):
        url = "http://www.meituan.com/"
        yield scrapy.Request(url=url, callback=self.parse, meta={"cookiejar": 1})

    def parse(self, response):
        print(response.text)
        yield scrapy.Request(url="http://www.meituan.com/deal/47840801.html", callback=self.parse, dont_filter=True, meta={"cookiejar": response.meta["cookiejar"]})


if __name__ == "__main__":
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(Img)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
