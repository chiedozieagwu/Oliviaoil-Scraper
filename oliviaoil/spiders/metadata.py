import scrapy


class MetadataSpider(scrapy.Spider):
    name = 'metadata'
    allowed_domains = ['www.olivaoliva.com']
    start_urls = []
    urls = ['https://www.olivaoliva.com/es/',
    'https://www.olivaoliva.com/es/fabricantes',
    'https://www.olivaoliva.com/es/4-marcas-aceite-de-oliva-virgen-extra-espanolas',
    'https://www.olivaoliva.com/es/3-aceite-de-oliva',
    'https://www.olivaoliva.com/es/410-aceite-productos-gourmet',
    'https://www.olivaoliva.com/es/411-aceite-de-oliva-para-regalar']
    for url in urls:
        start_urls.append(url)

    def parse(self,response):
        sub_categories =  response.css('div.column.col-xs-12.col-sm-3 a::attr(href)').getall()
        for sub in sub_categories:
            sub_url = sub
            yield scrapy.Request(sub_url,callback=self.parse_all)

    def parse_all(self, response):
        meta_title = response.xpath("//title/text()").extract()
        try:
            page_desc = response.css('div.catDescription_description ::text').get()
        except:
            page_desc = ''
        try:
            content_type = response.headers['Content-Type']
        except:
            content_type = ''
        try:
            meta_description = response.xpath("//meta[@name='description']/@content")[0].extract()
        except:
            meta_description = ''
        try:
            meta_keywords = response.xpath("//meta[@name='keywords']/@content")[0].extract()
        except:
            meta_keywords = ''
        try:
            meta_generators = response.xpath("//meta[@name='generator']/@content")[0].extract()
        except:
            meta_generators = ''

        yield{
            'Meta Title': meta_title,
            'Page Description': page_desc,
            'Meta Desc' : meta_description,
            'Meta Keywords': meta_keywords,
            'Meta Generators': meta_generators,
            'Content Type': content_type
        }

    
