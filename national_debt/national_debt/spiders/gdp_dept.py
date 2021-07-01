# -*- coding: utf-8 -*-
import scrapy


class GdpDeptSpider(scrapy.Spider):
    name = 'gdp_dept'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        rows = response.xpath("//tbody[@class='jsx-2642336383']/tr")
        for row in rows:
            
            country_name = row.xpath(".//td[1]/a/text()").get()
            gdp_debt = row.xpath(".//td[2]/text()").get()

            yield{
                'country_name': country_name,
                'gdp_debt': gdp_debt
                }
