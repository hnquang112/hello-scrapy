import scrapy
from spiderman.items import MarryItem

class MarryArticles(scrapy.Spider):
    name = 'marry_articles'
    start_urls = [
        'http://www.marry.vn/kinh-nghiem-cuoi/',
        # 'http://www.marry.vn/y-tuong-cuoi/',
        # 'http://www.marry.vn/ao-cuoi-dep/',
        # 'http://www.marry.vn/cong-dong/',
    ]

    def parse(self, response):
        for href in response.css('a.idea-text::attr(href)').extract():
            yield scrapy.Request(href, self.parse_post)

        next_page = response.css('a.nextpostslink::attr(href)').extract_first()

        if next_page is not None:
            yield scrapy.Request(next_page, self.parse)

    def parse_post(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        post = MarryItem()
        post['title'] = extract_with_css('h1.entry-title::text')
        post['desc'] = extract_with_css('.meta-article-desc::text')
        post['content'] = extract_with_css('.article-main-content')
        post['url'] = response.url
        post['category'] = extract_with_css('meta[property="article:section"]::attr(content)')
        post['avatar'] = extract_with_css('meta[property="og:image"]::attr(content)')
        post['published_time'] = extract_with_css('meta[property="article:published_time"]::attr(content)')
        post['modified_time'] = extract_with_css('meta[property="article:modified_time"]::attr(content)')

        yield post