import scrapy
from ..items import MyItem
    
# This is a spider that scrapes a directory for all results matching a keyword in a specific location and outputs results into csv format

class MySpider(scrapy.Spider):
    name = '#spidername'
    page_number = 2
    start_urls = ["#starturl"]
    
    # export results 
    custom_settings = {"FEEDS": {"#": {"format": "csv"}}}
    
    def parse(self, response):    
        items = MyItem()
        
        for res in response.css('#'):

            items['Name'] = res.css('#').get()
            items['Phone'] = res.css('#').get()
            items['Address'] = res.css('#').get()
            items['Location'] = res.css('#').get()
            items['Website'] = res.css('#').get()
                        
            yield items
            
        next_page = '#' + str(MySpider.page_number)
        if MySpider.page_number <= 5:
            yield response.follow(next_page, callback = self.parse)
            MySpider.page_number += 1

