from scrapy import Request
from scrapy.spiders import Spider

class S2(Spider):
    name = 'crypto'
    handle_httpstatus_list = [404, 403]
    allowed_domains = ['coinmarketcap.com']
    start_urls = ["https://coinmarketcap.com/"]
    custom_settings = {'DOWNLOAD_DELAY': 4}

    def parse(self, response):
      table = response.xpath('//*[@class = "rc-table-tbody"]')
      rows = table.xpath('//tr')
      items=[]
      for row in rows:
          item = {}
          item['name'] = row.xpath('./td[3]/a/div/div/p/text()').extract()
          item['market cap'] = row.xpath('./td[4]/p/text()').extract()
          item['price'] = row.xpath('./td[5]/div/a/text()').extract()
          item['link'] = row.xpath('./td[3]/a/@href').extract()
          if len(item['link']) == 0:
              continue
          else:
              url = item['link'][0]
              base = 'https://coinmarketcap.com'
              req = Request(base+url, callback = self.parse_2)
              req.meta['data'] = item
              items.append(req)
      return items

    def parse_2(self, response):
      item = response.meta['data']
      item['Circulating Supply'] = response.xpath("//tbody/tr[6]/td/text()").extract()
      item['Total Supply'] = response.xpath("//tbody/tr[7]/td/text()").extract()
      item['Max Supply'] = response.xpath("//tbody/tr[8]/td/text()").extract()
      item['All Time High'] = response.xpath("//tbody/tr[9]/td/div/text()").extract()
      item['All Time Low'] = response.xpath("//tbody/tr[10]/td/div/text()").extract()
      return item
