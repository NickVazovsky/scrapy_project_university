import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
from parsers.items import ParsersItem
from twisted.internet import reactor


class LinksSpider(CrawlSpider):
    #start_url=["http://mospolytech.ru/"]
    name = "links_spider"
    allowed_domains = ["moscowpolytech.ru"]

    start_urls = [
        "http://moscowpolytech.ru/index.php"
    ]

    rules = (
        Rule(LinkExtractor(allow=".+"),follow=True),
        Rule(LinkExtractor(allow=".+"),callback='parse_links'),
    )

    def parse_links(self, response):
            item = ParsersItem()
            item['link'] = response.url
            return item
