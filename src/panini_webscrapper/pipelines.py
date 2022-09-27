# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class PaniniWebscrapperPipeline:
    def __init__(self):
        self.con = sqlite3.connect("../databases/raw_store_dataset.db")
        self.cur = self.con.cursor()

        ## Create quotes table if none exists
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS raw_products(
            product_name TEXT,
            product_link TEXT,
            product_page TEXT
        )
        """
        )

    def process_item(self, item, spider):

        self.cur.execute(
            "select * from raw_products where product_name = ?", (item["product_name"],)
        )
        result = self.cur.fetchone()

        if result:
            return item

        ## Define insert statement
        self.cur.execute(
            """
            INSERT INTO raw_products (product_name, product_link, product_page) VALUES (?, ?, ?)
        """,
            (item["product_name"], item["product_link"], item["product_page"]),
        )

        ## Execute insert of data into database
        self.con.commit()
        return item
