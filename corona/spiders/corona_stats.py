# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from corona.items import CoronaItem
from scrapy.selector import Selector

class CoronaStatsSpider(scrapy.Spider):
    name = 'corona_stats'
    allowed_domains = ['mygov.in']
    start_urls = ['https://mygov.in/covid-19/']
    def parse(self, response):
        date=response.xpath('//*[@class="info_title"]/span/text()').get()
        cleaned_date= date.split(':')[1].split(',')[0].strip()
        states=response.xpath('//*[@class="views-row"]')
        for state in states:
            state_name=state.xpath('.//*[@class="st_name"]//text()').get()
            state_number= state.xpath('.//*[@class="st_number"]//text()').get()
            Active_cases=state.xpath('.//*[@class="tick-active"]/small/text()').get()
            cured_cases=state.xpath('.//*[@class="tick-discharged"]/small/text()').get()
            Death_cases=state.xpath('.//*[@class="tick-death"]/small/text()').get()
            yield self.load_corona_item(response,data={'Date':cleaned_date,'Name':state_name,'Total':state_number,'Active_cases':Active_cases,'Cured':cured_cases,'Deaths':Death_cases})
        try:
            t_name='Total'
            total= response.xpath("//*[@class='icount']/text()").getall()
            t_active=(total[0])
            t_cured=(total[1])
            t_death=total[2]
            t_total=str(sum(map(int,total)))
            yield self.load_corona_item(response,data={'Date':cleaned_date,'Name':t_name,'Total':t_total,'Active_cases':t_active,'Cured':t_cured,'Deaths':t_death})
        except:
            yield None
    def load_corona_item(self,response,data):
            item_loader=ItemLoader(item=CoronaItem(),response=response)
            if(data):
                for i,j in data.items():
                    item_loader.add_value(i,j)
                    
            else:
                print('Data not Found!')
            return item_loader.load_item()




        
