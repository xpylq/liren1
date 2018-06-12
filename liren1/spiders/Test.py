# /usr/bin/env python
# encoding=utf-8
# 这个爬虫可以爬取所有网页中的链接，根据rules匹配规则，确定是否做处理，并且确定是否follow
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class MySpider(CrawlSpider):
    name = "quotes_spider_craw"
    start_urls = ["https://dubai.dubizzle.com/motors/used-cars/"]

    def __init__(self, *a, **kw):
        self.shop_url_file = open("/Users/youzhihao/Downloads/phone.txt", "w", encoding="utf-8")
        super().__init__(*a, **kw)

    rules = (
        Rule(scrapy.linkextractors.LinkExtractor(allow="https://dubai.dubizzle.com/motors/used-cars/*"), callback="parse_bd", follow=True),
    )

    def parse_bd(self, response):
        if "shownumber" in response.url:
            self.shop_url_file.write(response.url + "\n")
            self.shop_url_file.flush()
        yield {
            "url": response.url
        }


if __name__ == "__main__":
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(MySpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
