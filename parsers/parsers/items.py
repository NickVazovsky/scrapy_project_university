# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ParsersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    linksp = scrapy.Field()

class SeoItem(scrapy.Item):
    title = scrapy.Field()
    keyword = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    text = scrapy.Field()
    googl_anal = scrapy.Field()
    yandex_metrick = scrapy.Field()
    count_analytics = scrapy.Field()

class YandexSearch(scrapy.Item):
    titley = scrapy.Field()
    yasearchlink = scrapy.Field()
    descriptiony = scrapy.Field()
    linky = scrapy.Field()
    pagey = scrapy.Field()
    index = scrapy.Field()

class GoogleSearch(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    google_link = scrapy.Field()
    links = scrapy.Field()
    index = scrapy.Field()

#class PagesSpider(CrawlSpider):
    """
    the Page Spider for wikipedia
    """

 #   name = "wikipedia_pages"
  #  allowed_domains = ["moscowpolytech.ru"]

#    start_urls = [
 #       "http://moscowpolytech.ru/index.php"
  #  ]

#    rules = (
 #       Rule(LinkExtractor(allow=".+"),
  #           callback='parse_wikipedia_page'),
   # )

#    def parse_wikipedia_page(self, response):
 #       item = SeoItem()
  #      for quote in response.css('html'):
   #         counters_anal = quote.css('script').extract()
    #        if 'https://www.google-analytics.com/analytics.js' in str(counters_anal):
     #           yee = 'yes'
      #      else:
       #         yee = 'no'
        #    if 'mc.yandex.ru/metrika' in str(counters_anal):
         #       res = 'yes'
          #  else:
           #     res = 'no'

            #item['title'] = quote.css('title::text').extract_first(),
            #item['keyword'] = quote.css(
             #   'meta[name*=Keywords]::attr(content), meta[name*=keywords]::attr(content)').extract(),
            #item['description'] = quote.css(
             #   'meta[name*=description]::attr(content), meta[name*=Description]::attr(content)').extract(),
            #item['h1'] = quote.css('h1::text').extract(),
            #item['h2'] = quote.css('h2::text, H2::text').extract(),
            #item['text'] = quote.css('p::text, span::text').extract(),
            #item['googl_anal'] = yee,
            #item['yandex_metrick'] = res,
            #yield item