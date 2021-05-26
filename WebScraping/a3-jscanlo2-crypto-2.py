from scrapy import Request
from scrapy.spiders import Spider

class S2(Spider):
    name = 'crypto'
    handle_httpstatus_list = [404, 403]
    #allowed_domains = ['coinmarketcap.com']
    start_urls = ["https://coinmarketcap.com/currencies/bitcoin/"]

    def parse(self, response):
        item = {}
        item['Circulating Supply'] = response.xpath("//tbody/tr[6]/td/text()").extract()
        item['Total Supply'] = response.xpath("//tbody/tr[7]/td/text()").extract()
        item['Max Supply'] = response.xpath("//tbody/tr[8]/td/text()").extract()
        item['All Time High'] = response.xpath("//tbody/tr[9]/td/div/text()").extract()
        item['All Time Low'] = response.xpath("//tbody/tr[10]/td/div/text()").extract()

        return item
