import os
from lxml import html
import unicodedata
from dataclasses import dataclass
import json
from w3lib.html import remove_tags
from typing import List, Optional

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from sqlmodel import Field, SQLModel, create_engine


mypath = '/mnt/d/_pages'
files = [os.path.join(mypath, file) for file in os.listdir(mypath) if file.endswith('.html')]

class Knifekits(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    link: str
    sku: str
    name = Field()
    price = Field()
    description = Field()
    images = Field()
    main_image = Field()
    breadcrumbs = Field()
    title = Field()
    short_desc = Field()
    keywords = Field()
    manufacturer = Field()

class DemoLoader(ItemLoader):
    item = Knifekits()
    item['link'] = "https://knifekits.com/vcom/" + file
    item['sku'] = page.xpath('//a[@class="thumbnail"]/@data-title')[0]
    item['description'] = clean_desc(page.xpath('//div[@itemprop="description"]/descendant-or-self::text()').text_content())
    item['all_images'] = page.xpath('//a[@class="thumbnail"]/@data-image')
    item['name'] = page.xpath('//h1')[0].text_content().split('Stock')[0]
    item['price'] = page.xpath('//h1')[0].text_content().split("$")[-1].strip()
    item['keywords'] = page.xpath('//meta[@name="keywords"]/@content')[0]
    item['short_desc'] = page.xpath('//meta[@name="description"]/@content')[0]
    item['main_image'] = page.xpath('//div[@class="piGalMain"]/img/@src')[0]
    item['breadcrumbs'] = page.xpath('//*[@class="breadcrumb"]')[0].text_content().split('\n')

folder = "h:/_pages"
saved = [os.path.join(folder, file) for file in os.listdir(folder)]
results=[]
for fname in saved:
    url = fname
    fields = {
        "link": '//*[@rel="canonical"]/@href',
        "sku": '//span[@itemprop="model"]/descendant-or-self::text()',
        "name": '//h1/descendant::span[@itemprop="name"]/text()',
        "main_image": '//div[@class="piGalMain"]/img/@src',
        "image_urls": '//*[@class="thumbnail"]/@data-image',
        "description": '//div[@itemprop="description"]',
        "price": './/*[@itemprop="price"]/text()',
        "breadcrumbs": './/*[@class="breadcrumb"]',
        "title": "/html/head/title/text()",
        "keywords": './/meta[@name="keywords"]/@content',
        "short_desc": '//meta[@name="description"]/@content',
        "discount_tiers": './/*[@class="DiscountPriceQty"]/descendant-or-self::text()',
        "discount_amount": './/*[@class="DiscountPrice"]/descendant-or-self::text()',
        "products_id": '//input[@name="products_id"]/@value',
        }
