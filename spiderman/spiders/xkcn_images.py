import scrapy

class XkcnImages(scrapy.Spider):
    name = 'xkcn_images'

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        urls = ['http://xkcn.info/page/%s' % page for page in xrange(0, 520)]

        for link in urls:
            yield scrapy.Request(link, self.parse, headers = headers)

    def parse(self, response):
        for image in response.css('.photo-wrapper-inner'):
            yield {
                'url': image.css('img::attr(src)').extract_first(),
                'page': response.url,
            }