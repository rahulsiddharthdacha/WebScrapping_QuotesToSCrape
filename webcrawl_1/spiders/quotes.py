import scrapy
from ..items import Webcrawl1Item
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']
    def start_requests(self):
        url='https://quotes.toscrape.com/page/{}/'
        for i in range(1,11):
            yield scrapy.Request(url.format(i),callback=self.parse)
    def parse(self, response):
        items=Webcrawl1Item()
        rows=response.xpath('//div[@class="quote"]')
        for row in rows:
            quote = "".join(row.xpath('span[@class="text"]/text()').extract())
            author = "".join(row.xpath('span/small[@class="author"]/text()').extract())
            tags=",".join(row.xpath('div[@class="tags"]/a[@class="tag"]/text()').extract())
            tags_url=",".join(row.xpath('div[@class="tags"]/a[@class="tag"]/@href').extract())
            page_url=response.url
            items['quote']=quote
            items['author']=author
            items['tags']=tags
            items['tags_url']=tags_url
            items['page_url']=page_url
            yield items

        
