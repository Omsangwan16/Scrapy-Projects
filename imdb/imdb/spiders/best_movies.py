import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating']
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a "), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths='(//*[@class="lister-page-next next-page"])[1]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
    
            'title' : response.xpath('(//h1/text())[1]').get().strip(),
            'year' : response.xpath('//span[@id="titleYear"]/a/text()').get(),
            'duration' : response.xpath('normalize-space((//time/text())[1])').get(),
            'rating' : response.xpath('//*[@itemprop="ratingValue"]/text()').get(),
            'director' : response.xpath('(//*[@class="credit_summary_item"]/h4/following-sibling::a)[1]/text()').get(),
            'movie_url' : response.url
        }
        