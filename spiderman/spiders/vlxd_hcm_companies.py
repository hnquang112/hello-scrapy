# -*- coding: utf-8 -*-
import scrapy
from spiderman.items import CompanyItem

class CompaniesSpider(scrapy.Spider):
	name = "vlxd_hcm_companies"
	allowed_domains = ["yellowpages.vnn.vn"]
	start_urls = ['http://yellowpages.vnn.vn/class/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F_tp.-h%E1%BB%93-ch%C3%AD-minh-%28tphcm%29.html']

	def parse(self, response):
		for company in response.css('div.listing_box'):
			item = CompanyItem(
				name = company.css('h2.company_name a::text').extract_first().encode('utf-8'),
				link = company.css('h2.company_name a::attr(href)').extract_first(),
				address = company.css('p.listing_diachi::text').extract_first().encode('utf-8'),
				phone = company.css('p.listing_tel::text').extract_first()
			)
			yield item

		total_page = response.css('#paging a:nth-last-child(2)::text').extract_first()
		next_page_url = response.css('#paging a:last-child::attr(href)').extract_first()
		next_page = next_page_url.split('=')[1]
		
		if next_page_url is not None and int(next_page) <= int(total_page):
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(next_page_url, callback=self.parse)