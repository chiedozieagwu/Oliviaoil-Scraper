import scrapy


class OoSpider(scrapy.Spider):
    name = 'oo'
    allowed_domains = ['www.olivaoliva.com']
    start_urls = []
    urls = ['https://www.olivaoliva.com/es/3-aceite-de-oliva','https://www.olivaoliva.com/es/410-aceite-productos-gourmet','https://www.olivaoliva.com/es/411-aceite-de-oliva-para-regalar','https://www.olivaoliva.com/es/412-aceite-cosmetica-leche-corporal']
    for url in urls:
        start_urls.append(url)

    def parse(self, response):
        products = response.css('a.product-name::attr(href)').extract()
        for product in products:
            url = product
            yield scrapy.Request(url,callback=self.parse_urls)
          
        next_page = 'https://www.olivaoliva.com' + response.css('li.pagination_next>a::attr(href)').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_urls(self,response):
        name = response.css('h1::text').get()
        description = response.css('div.primary_block.row h2::text').get()
        image = response.css('img.img-responsive.jqzoom2::attr(src)').get()
        price = response.css('span#our_price_display::text').get().replace('€','').strip()
        Tipo =  response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Tipo:")]/following-sibling::div/text()').get()
        Variedad = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Variedad:")]/following-sibling::div/text()').get()
        Cultivo = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Cultivo:")]/following-sibling::div/text()').get()
        Zona = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Zona:")]/following-sibling::div/text()').get()
        do = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "D.O.:")]/following-sibling::div/text()').get()
        Cosecha = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Cosecha:")]/following-sibling::div/text()').get()
        Formato = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Formato:")]/following-sibling::div/text()').get()
        Capacidad = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Capacidad:")]/following-sibling::div/text()').get()
        Composición = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Composición:")]/following-sibling::div/text()').get()
        Marca = response.css('div.col-lg-8.col-md-8.col-sm-8.col-xs-8>a::text').get()
        Marca_url = response.css('div.col-lg-8.col-md-8.col-sm-8.col-xs-8>a::attr(href)').get()
        meta_description = response.xpath("//meta[@name='description']/@content")[0].extract()

        yield{
            'Product Title': name,
            'Product Description': description,
            'Price': price,
            'Image URL': image,
            'Tipo': Tipo,
            'Variedad': Variedad,
            'Cultivo': Cultivo,
            'Zona': Zona,
            'D.O': do,
            'Cosecha': Cosecha,
            'Formato': Formato,
            'Capacidad': Capacidad,
            'Composición': Composición,
            'Marca': Marca,
            'Marca URL': Marca_url,
            'Meta Description': meta_description
        }