import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"]

    def parse(self, response):

        series = response.css("li.ipc-metadata-list-summary-item")

        for serie in series:

            title = serie.css("h3.ipc-title__text.ipc-title__text--reduced::text").get()
            year = serie.css("span.sc-caa65599-7.eeMIpC.cli-title-metadata-item::text").get()

            yield {
                'title': title,
                'year': year,
            }
