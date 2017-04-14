import scrapy
from products_spider.items import ProductsSpiderItem
import json
from scrapy.pipelines.images import ImagesPipeline

#DOWNLOAD_HANDLERS = { 's3' : None, }


class ProductSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.ikea.com"]
    #IKEA PS 2017 collection
    start_urls = ['http://www.ikea.com/us/en/catalog/categories/departments/dining/collections/12041/']

    def parse(self, response):

        all_products = response.css('div.product')

        #filename = 'product'
        #with open(filename, 'w') as f:

        for product in all_products:
        
            #item = ProductsSpiderItem()
            productId = product.css('div ::attr(id)').extract_first(),
            productTitle = product.css('.productTitle ::text').extract_first(),
            productDesp = product.css('.productDesp ::text').extract_first(),
            productPrice = product.css('.regularPrice ::text').extract_first(),
            imageURL = 'http://www.ikea.com' + product.css('img ::attr(src)').extract_first()

            yield ProductsSpiderItem(prod_id=productId, title=productTitle, description=productDesp, price=productPrice, file_urls=[imageURL])
            #if item['file_urls']:
                #yield scrapy.Request(item['file_urls'])
                #json.dumps(item, f, indent=4)


