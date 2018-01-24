# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import GreatschoolsItem
from urlparse import urlparse

class GschoolssSpider(scrapy.Spider):
    name = 'gschoolss'
    allowed_domains = ['greatschools.org']
    start_urls = ['https://www.greatschools.org/schools/districts/New_York/NY/']

   
    
    def parse(self, response):
        source_page = response.url
        print source_page
        rows = response.xpath('//tr/td[@class="city-district-link"]/a')
        for row in rows:
            # temp_link = row.xpath('@href').extract()
            # link = response.urljoin(''.join(temp_link))
            temp_link = row.xpath('@href').extract_first()
            link = response.urljoin(temp_link)
            yield Request(link, callback=self.parse_item, meta={'source_page': source_page})
            #print link

    def parse_item(self, response):
        item = GreatschoolsItem()
        # link = response.url
        # print link
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        school_name= response.xpath('//h1[@class="dark-grey notranslate"]/text()').extract_first()
        item['school_name'] = school_name
        grades= response.xpath('//div[@class="fl prm fl"]/span/text()')[-1].extract()
        item['grades'] = grades
        location = response.xpath('//div[@class="col-lg-6 prl"]/text()').extract()
        street = location[0].strip()
        item['street_address'] = street
        item['csz'] = location[1].strip()
        phoneweb = response.xpath('//div[@class="col-lg-6"]/text()').extract()
        phone = phoneweb[0].strip()
        phone = phone.replace('Phone:', '')
        item['phone'] = phone
        website = response.xpath('//div[@class="col-lg-6"]/a/@href').extract()
        website = ''.join(website)
        item['website'] = website
        parsed_uri = urlparse(website)
        domain = parsed_uri.netloc
        domain = domain.replace('www.', '')
        item['domain'] = domain
        #print school_name
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        yield item
