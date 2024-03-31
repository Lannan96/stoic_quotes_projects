import scrapy


class StoicQuotesSpiderSpider(scrapy.Spider):
    name = "stoic_quotes_spider"
    allowed_domains = ["dailystoic.com"]
    start_urls = ["https://dailystoic.com/stoic-quotes/"]

    def parse(self, response):
        
        
        # Extracting the quotes
        for quote in response.xpath('//*[@id="post-347"]/blockquote').getall():
            quote_text = quote.xpath('p/text()').get()
            quote_author = quote.xpath('/p/a/@href').get()
            yield {
                'quote': quote_text,
                'author': quote_author
            }



        

