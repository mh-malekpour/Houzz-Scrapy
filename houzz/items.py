# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouzzItem(scrapy.Item):
    title = scrapy.Field()
    image1_url = scrapy.Field()
    image2_url = scrapy.Field()
    keywords = scrapy.Field()
    category = scrapy.Field()
