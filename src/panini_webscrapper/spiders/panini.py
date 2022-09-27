import scrapy
from panini_webscrapper.items import StoreItem


class ExampleSpider(scrapy.Spider):
    name = "panini"
    allowed_domains = ["tiendapanini.com.mx"]
    start_urls = ["https://tiendapanini.com.mx/coleccionables/item-3?"]
    page = 1

    def parse(self, response):
        next_page = '//*[@class="action  next"]/@href'
        products = response.xpath(
            '//*[contains(@href, "https")][@class="product-item-link"]'
        )
        for product in products:
            manga = StoreItem()
            manga["product_link"] = product.xpath("@href").get()
            manga["product_name"] = product.xpath("text()").get()
            manga["product_page"] = self.page
            yield manga

        self.page = self.page + 1
        if self.page % 20 == 0:
            print(f"Page {self.page}")
        if response.xpath(next_page).get():
            yield scrapy.Request(response.xpath(next_page).get())
