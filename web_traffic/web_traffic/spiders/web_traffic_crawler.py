# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from time import sleep
from web_traffic.items import WebTrafficItem
from scrapy.loader import ItemLoader

class WebTrafficCrawlerSpider(scrapy.Spider):
    name = 'web_traffic_crawler'
    allowed_domains = ['gtmetrix.com/top1000.html','similarweb.com']
    start_urls = [
        'https://gtmetrix.com/top1000.html']
   

    def parse(self, response):
        self.driver=webdriver.Chrome(r'C:/Users/study/Desktop/web scraping/chromedriver.exe')
        self.driver.get(response.url)
        item=WebTrafficItem()
        count=0
        while(True):
            try:
                sleep(10)
                sel=scrapy.selector.Selector(text=self.driver.page_source)
                all_det=sel.xpath('//tbody/tr[@role="row"]')
                for det in all_det:
                    domain=det.xpath('.//*[@data-th="URL"]//a/text()').get().split('.',1)[-1]
                    
                    pagespeed=(det.xpath('.//*[@data-th="PageSpeed"]//text()').get()[:-1])
                    
                    yslow=(det.xpath('.//*[@data-th="YSlow"]//text()').get()[:-1])
                    
                    onload=(det.xpath('.//*[@data-th="Onload"]//text()').get())
                    
                    full_load=(det.xpath('.//*[@data-th="Fully Loaded"]//text()').get())
                    
                    requests=(det.xpath('.//*[@data-th="Requests"]//text()').get())
                    
                    total_size=(det.xpath('.//*[@data-th="Total Size"]//text()').get()[:-2])
                    
                    yield self.load_item(response,domain,pagespeed,yslow,onload,full_load,requests,total_size)
                next_page=self.driver.find_element_by_css_selector('.next')
                c=sel.css('.next').xpath('@class').get()
                if('disabled' in c.split()):
                    self.logger.info('End of Results!!!')
                    driver.quit()
                    break
                next_page.click()
            except:
                break
                
    def load_item(self,response,domain,pagespeed,yslow,onload,full_load,requests,total_size):
        item_loader=ItemLoader(item=WebTrafficItem(),response=response)
        item_loader.add_value('Domain',domain)
        item_loader.add_value('Pagespeed',pagespeed)
        item_loader.add_value('Yslow',yslow)
        item_loader.add_value('Onload',onload)
        item_loader.add_value("Full_load",full_load)
        item_loader.add_value('Requests',requests)
        item_loader.add_value('Total_size',total_size)
        return item_loader.load_item()
     
        
        
