import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
    ]

    def parse(self, response):
        # From table, link to each company's website to get the twitter handle.
        # columns = response.xpath('//tr')
        for company in response.xpath("(//td[2])"):
            companyName = company.xpath("./a/text()").get()
            website = company.xpath("./a/@href").get()
            if website is not None:
                response.follow(website, callback=self.getTwitterHandle)

    def getTwitterHandle():