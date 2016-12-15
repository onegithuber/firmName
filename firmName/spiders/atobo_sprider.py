from scrapy.contrib.spiders import CrawlSpider


class AtoboSprider(CrawlSpider):
    name = 'atoto'

    allowed_domains = ['atobo.com.cn']
    start_urls = ['http://www.atobo.com.cn/Companys/']