from scrapy import Request
from scrapy.spiders import Spider

class S1(Spider):
    name = 's1'
    #allowed_domains
    start_urls = ["https://coinmarketcap.com/"]

    def parse(self, response):
        table = response.xpath('//*[@class = "rc-table-tbody"]')
        rows = table.xpath('//tr')
        ans=[]
        for row in rows:
            item = {}
            item['name'] = row.xpath('./td[position()=3]/a/div/div/p/text()').extract()
            item['market cap'] = row.xpath('./td[position()=4]/p/text()').extract()
            item['price'] = row.xpath('./td[position()=5]/div/a/text()').extract()
            item['link'] = row.xpath('./td[position()=3]/a/@href').extract()
            ans.append(item)
        return ans
