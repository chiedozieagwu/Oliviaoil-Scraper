import scrapy


class ManuSpider(scrapy.Spider):
    name = 'manu'
    start_urls = ['https://www.olivaoliva.com/es/fabricantes']

    def parse(self, response):
        manufacturers = response.css('a.btn.btn-default.button.exclusive-medium::attr(href)').extract()
        for manufacturer in manufacturers:
            manu_link = manufacturer
            yield scrapy.Request(manu_link, callback=self.parse_links)

    def parse_links(self,response):
        product_link = response.css('a.product-name::attr(href)').extract()
        for product in product_link:
            product_url = product
            yield scrapy.Request(product_url, callback=self.parse_products)

    def parse_products(self,response):
        try:
            name = response.css('h1::text').get()
        except:
            name = ''
        try:
            description = response.css('div.rte ::text').getall().strip()
        except:
            description = ''
        try:
            image = response.css('img.img-responsive.jqzoom2::attr(src)').get()
        except:
            image = ''
        try:
            price = response.css('span#our_price_display::text').get().replace('€','').strip()
        except:
            price = ''
        try:
            Tipo =  response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Tipo:")]/following-sibling::div/text()').get()
        except:
            Tipo = ''
        try:
            Variedad = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Variedad:")]/following-sibling::div/text()').get()
        except:
            Variedad = ''
        try:
            Cultivo = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Cultivo:")]/following-sibling::div/text()').get()
        except:
            Cultivo = ''
        try:
            Zona = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Zona:")]/following-sibling::div/text()').get()
        except:
            Zona = ''
        try:
            do = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "D.O.:")]/following-sibling::div/text()').get()
        except:
            do = ''
        try:
            Cosecha = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Cosecha:")]/following-sibling::div/text()').get()
        except:
            Cosecha = ''
        try:
            Formato = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Formato:")]/following-sibling::div/text()').get()
        except:
            Formato = ''
        try:
            Capacidad = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Capacidad:")]/following-sibling::div/text()').get()
        except:
            Capacidad = ''
        try:
           Composición = response.xpath('//div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3 opcion" and contains(., "Composición:")]/following-sibling::div/text()').get()
        except:
            Composición = ''
        try:
            Marca = response.css('div.col-lg-8.col-md-8.col-sm-8.col-xs-8>a::text').get()
        except:
            Marca = ''
        try:
            Marca_url = response.css('div.col-lg-8.col-md-8.col-sm-8.col-xs-8>a::attr(href)').get()
        except:
            Marca_url = ''
        try:
            meta_description = response.xpath("//meta[@name='description']/@content")[0].extract()
        except:
            meta_description = ''

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
        
            
