import scrapy
from ..items import HouzzItem
import json


class HouzzSpider(scrapy.Spider):
    name = 'houzz'

    # 36 product per page -> 36 * pagecount
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 0}

    start_urls = [
        'https://www.houzz.com/products/desks',
        'https://www.houzz.com/products/beds',
        'https://www.houzz.com/products/chairs',
        'https://www.houzz.com/products/sofas'
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, response, **kwargs):
        try:
            category = response.css(".mb0::text").get()[:-1]
        except:
            pass

        all_div_product = response.css(
            ".hz-product-card.hz-track-me.hz-product-card--medium.hz-br-container--three-grid.hz-product-card__browse"
            "-redesign")

        for href in all_div_product.css("a.hz-product-card__link::attr(href)"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_product_contents, meta={'category': category})

        next_page = response.css('.hz-pagination-link--next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    @staticmethod
    def parse_product_contents(response):
        item = HouzzItem()

        # Product title:
        item['title'] = response.css('.view-product-title::text').extract()

        # Product images urls:
        image_urls = response.css('.alt-images__thumb img::attr(src)').extract()
        for i in range(len(image_urls)):
            if '_' in image_urls[i]:
                id_ = image_urls[i][27:48]
                id_ = id_.split('_')
                image_urls[i] = f'https://st.hzcdn.com/simgs/{id_[0]}_4-{id_[1]}/home-design.jpg'
        item['image1_url'] = image_urls[0] if len(image_urls) > 0 else None
        item['image2_url'] = image_urls[1] if len(image_urls) > 1 else None

        # This Product Has Been Described As:
        keywords = response.css(".product-keywords ul li::text").extract()
        json_string = json.dumps(keywords)
        item['keywords'] = json_string

        # Category:
        item['category'] = response.meta.get('category')

        yield item
