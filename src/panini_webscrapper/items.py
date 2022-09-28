"""Define here the models for your scraped items
See documentation in:
https://docs.scrapy.org/en/latest/topics/items.html"""

from scrapy import Field, Item


class StoreItem(Item):  # pylint: disable=too-few-public-methods
    """Class that models a product in store"""

    product_name = Field()
    product_link = Field()
    product_page = Field()
