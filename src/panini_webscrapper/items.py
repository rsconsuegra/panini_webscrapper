# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class StoreItem(Item):
    product_name = Field()
    product_link = Field()
    product_page = Field()
