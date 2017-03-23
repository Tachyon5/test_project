#this is a python web scraper that yejun will build :)
import scrapy

# class IkeaProduct(Item):
# 	productTitle = Field()
# 	productDesp = Field()
# 	price = Field()
    

class IkeaSpider(scrapy.Spider):
	name = "ikea"
	allowed_domains = ["ikea.com"]
	start_url = ["http://www.ikea.com/us/en/catalog/categories/departments/decoration/collections/12041/"]

	def parse(self, res): 
		page = response.url.split("/")[-2]
		filename = 'Ikea_page.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)

		#hxs = HtmlXPathSelector(res)

	def scrape_url(root_url):
		'''this function will scrape this url and child pages 
		scrape for images and text surounding the images'''
		yield scrapy.Request(url=root_url, callback=self.parse)

