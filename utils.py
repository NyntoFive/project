import os
from lxml import html
import unicodedata
from dataclasses import dataclass
import json
from csv import DictReader, DictWriter
from w3lib.html import remove_tags
from typing import List, Optional
from requests_html import HTMLSession
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

def demo(f=None, q="Atlanta"):
    base_url = 'https://nominatim.openstreetmap.org/search?'
    params = {"q": q}
    if f and f in ["xml", "json", "jsonv2", "geojson", "geocodejson"]:
        params['format']=f
    session = HTMLSession()
    result = session.get(base_url, params=params)
    if result.status_code != 200:
        print(f"Error: {result.status_code}")
        return result
    return result

def read_csv(path):
    '''read csv and return it as a list of dicts'''
    with open(path, 'r') as f:
        return list(DictReader(f))

def write_csv(data, path, mode='w'):
    '''write data to csv or append to existing one'''
    if mode not in 'wa':
        raise ValueError("mode should be either 'w' or 'a'")
    with open(path, mode) as f:
        writer = DictWriter(f, fieldnames=data[0].keys())
        if mode == 'w':
            writer.writeheader()
        for row in data:
            writer.writerow(row)


#####################
# OSCommerce models

url = "https://github.com/osCommerce/oscommerce2/tree/master/catalog/includes/OSC/Schema"
selector = '//div[@role="rowheader"]/span/a/@href'
raw_selector = '//a[@id="raw-url"]/@href'