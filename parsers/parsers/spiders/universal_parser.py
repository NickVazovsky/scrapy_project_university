import scrapy
import time

# from request_http import starts_url
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from parsers.items import ParsersItem,SeoItem,YandexSearch,GoogleSearch
import re
import random

Countries = {
    'ru' : 'countryRU'
}

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }


class PagesSpider(CrawlSpider,scrapy.Spider):
    name = "universal_page"
    start_urls = [
        "http://mospolytech.ru/"
    ]
    check_urls =[]
    check_google = []
    url = 'https://yandex.ru/search/?text=московский политех'
    rules = (
      Rule(LinkExtractor(),callback='parse_asd'),
      Rule(LinkExtractor(allow=".+"),follow=True),
    )

    def parse_asd(self, response):
        item = SeoItem()
        for quote in response.css('html'):
            counters_anal = quote.css('script').extract()
            if 'https://www.google-analytics.com/analytics.js' in str(counters_anal):
                yee = 'yes'
            else:
                yee = 'no'
            if 'mc.yandex.ru/metrika' in str(counters_anal):
                res = 'yes'
            else:
                res = 'no'

            item['title'] = quote.css('title::text').extract_first(),
            item['keyword'] = quote.css(
                'meta[name*=Keywords]::attr(content), meta[name*=keywords]::attr(content)').extract(),
            item['description'] = quote.css(
                'meta[name*=description]::attr(content), meta[name*=Description]::attr(content)').extract(),
            item['link'] = response.url
            item['h1'] = quote.css('h1::text').extract(),
            item['h2'] = quote.css('h2::text, H2::text').extract(),
            item['text'] = quote.css('p::text, span::text').extract(),
            item['googl_anal'] = yee,
            item['yandex_metrick'] = res,
            # print(item
            if len(item['keyword'][0]) > 0:
                keywords = item['keyword'][0][0].split(',')
                print(keywords[0])

                for i in range(1):
                    url = 'https://yandex.ru/search/?text=' + str(keywords[i] + '&lr=213')
                    urls = 'https://www.google.com/search?q=' + str(keywords[i])
                    if url not in self.check_urls:
                        self.check_urls.append(url)
                        print(url)
                        #yield scrapy.Request(url=url, callback=self.google_search)
                        yield scrapy.Request(url=url,headers=headers_Get, callback=self.parse_yandex)
                        yield scrapy.Request(url=urls, headers=headers_Get, callback=self.google_search)
                        #print(url)
                 #   url = 'https://yandex.ru/search/?text=московский политех'
            yield item


    def ss_yandex(self,response):
        yield scrapy.Request(url=self.url, callback=self.parse_yandex, method='GET')


    def parse_yandex(self, response):
        item = YandexSearch()
        title = response.xpath('//li[contains(@class, "t-construct-adapter__legacy")]/div/h2/a').extract(),
        yasearchlink= response.xpath('//li[contains(@class, "t-construct-adapter__legacy")]/div/h2/a/@href').extract(),
        desc = response.xpath('//li[contains(@class, "t-construct-adapter__legacy")]/div/div[2]').extract(),
        domain = 'http://mospolytech.ru'
        page = response.xpath('//span[@class="pager__item pager__item_current_yes pager__item_kind_page"]/text()').extract(),

        i = 0
        for i in range(len(title[0])):
            if domain in title[0][i]:
                index = i
                item['linky'] = yasearchlink[0][index]
                item['titley'] = re.sub(r'(?:<).*?(?:>)', '', str(title[0][index]))
                item['descriptiony'] = re.sub(r'(?:<).*?(?:>)', '', str(desc[0][index]))
                index += 1
                item['index'] = index
                #item['title'] = tit
                #item['link'] = links
                #item['description'] = descr
                item['pagey'] = page
                out = random.randrange(2,5,1)
                time.sleep(out)
                yield item
                print(''
              '******************************'
              '******************************'
              '******************************'
              '******************************'
              '******************************'
              '******************************'
              '******************************'
              '******************************'
              '******************************'
              )

    def google_search(self,response):
        item = GoogleSearch()
        title = response.xpath('//h3/a[not(contains(@class,"sla"))]').extract(),
        description = response.xpath('//span[@class="st"]').extract(),
        google_search_links_list = response.xpath('//div/h3/a[not(contains(@class,"sla"))]').extract(),
        links = response.xpath('//div[@class="kv"]//*').extract(),

        domain = 'http://mospolytech.ru'
        i = 0
        for i in range(len(google_search_links_list[0])):
            if domain in google_search_links_list[0][i]:
               index = i
               item['title'] = re.sub(r'(?:<).*?(?:>)', '', title[0][index])
               item['description'] = re.sub(r'(?:<).*?(?:>)', '', description[0][index])
               item['google_link'] =  re.sub(r'(?:<).*?(?:>)', '', links[0][index])
               index += 1
               item['index'] = index
               out = random.randrange(2, 5, 1)
               time.sleep(out)
               print('//////////////////////////////'
                     '//////////////////////////////'
                     '//////////////////////////////'
                     '//////////////////////////////'
                     '//////////////////////////////'
                     '//////////////////////////////'
                     '//////////////////////////////'
                     '//////////////////////////////'
                     '//////////////////////////////'
                     )
               yield item
