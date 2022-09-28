"""Scraper to panini store products"""
from typing import Iterator, Type

import scrapy
from panini_webscrapper.items import StoreItem

response_type = Type[scrapy.http.response.html.HtmlResponse]


class PaniniSpider(scrapy.Spider):  # pylint: disable=too-few-public-methods
    """Webscraper of Panini Store"""

    name = "panini"
    allowed_domains = ["tiendapanini.com.mx"]
    start_urls = ["https://tiendapanini.com.mx/coleccionables/item-3?"]
    page = 1

    def parse(self, response: response_type) -> Iterator[StoreItem]:
        """
        Get items from Panini mx Store pages, iterating over all availables

        Parameters
        ----------
        response : request containing page information
        Yields
        ------
        StoreItem
            A product from the store
        """
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
