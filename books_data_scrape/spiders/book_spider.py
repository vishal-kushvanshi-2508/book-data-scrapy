import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    def start_requests(self):
        print("start_requests run")

        yield scrapy.Request(url='https://books.toscrape.com/', callback=self.parse)


    def parse(self, response):
        print("parse run")
        base_url = "https://books.toscrape.com/"
        # print(response.body)
        all_product = response.xpath("//article[@class='product_pod']")
        # print(all_product)
        print(len(all_product))
        for book in all_product:
            # print(image_url)
            book_name = book.xpath(".//h3//a/@title").get()
            # print(book_name)
            price = book.xpath(".//p[@class='price_color']/text()").get()
            # print(price)
            image_url = base_url + book.xpath(".//div[@class='image_container']//img/@src").get()
            availabe = book.xpath(".//p[@class='instock availability']/text()")[1].get().replace("\n", "").replace(" ", "")
            # print(availabe)
            # print(type(availabe))
            yield{
                "book_name" : book_name,
                 "price" : price,
                 "image_url" : image_url,
                 "availabe" : availabe
            }
            # break


