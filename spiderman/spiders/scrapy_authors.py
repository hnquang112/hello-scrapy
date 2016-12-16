import scrapy

class ScrapyTutAuthors(scrapy.Spider):
    name = 'scrapy_authors'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('.author+a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), self.parse_author)

        next_page = response.css('li.next a::attr(href)').extract()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }