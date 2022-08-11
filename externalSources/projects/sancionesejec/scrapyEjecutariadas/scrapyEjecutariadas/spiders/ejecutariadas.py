# -*- coding: utf-8 -*-
import scrapy
import logging
import sys
import json
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from libraries.constants import Constants as SpecificCons
 
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../..'))
from generalLibraries.constants import Constants as GeneralCons


class EjecutariadasSpider(scrapy.Spider):
    """
        This class allows to scrape the Sanciones Ejecutoriadas page.
        Sanciones Ejecutoriadas: En esta sección se publican las sanciones administrativas ejecutoriadas aplicadas a las entidades reguladas por la Unidad de Análisis Financiero.

        Para consultar los datos se hace por medio de una peticion HTTP mediante el metodo POST, que deberia tener la siguiente estructura: 

                {

                    "jsonUserData":"{\"rowId\":1}",

                    "spider_name":"ejecutariadas",

                    "start_requests": "True"

                    }


        Los datos retornados por el Scraper estan en formato JSON, con una estructura similar a:

               {
            "ID": 1,
            "DATA": {
                "listadoSancionados": [
                    {
                        "numeroRol": "001-2019",
                        "personaNaturaloJuridica": "VPI INMOBILIARIA LTDA.  ",
                        "sectorEconomico": "Corredores de propiedades ",
                        "causal": "Fiscalización in situ",
                        "fechaResolucion": "28-10-2019"
                    },
                    {
                        "numeroRol": "002-2018",
                        "personaNaturaloJuridica": "INVERSIONES ALTIRO S.A.",
                        "sectorEconomico": "Usuarios de zonas francas",
                        "causal": "Fiscalización in situ",
                        "fechaResolucion": "02-10-2019"
                    },....

        Si no se encontraron resultados se retorna un formato JSON, con una estructura similar a:

                {
                    "DATA": {
                        "respuesta": [
                            {
                                "mensaje": "Tabla no Encontrada"
                            }
                        ]
                    },
                    "ID": 1
                }
    """

    specificCons = SpecificCons()
    generalCons = GeneralCons()

    name = "ejecutariadas"
    initUrl = "https://www.uaf.cl/prensa/sanciones_new.aspx"
    
    startUrls = [initUrl]
    jsonUserData = None
    __allowed = ("jsonUserData")

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
        logger.setLevel(logging.ERROR)
        super(EjecutariadasSpider, self).__init__(*args, **kwargs)

        for k, v in kwargs.items():
            if( k in self.__class__.__allowed):
                setattr(self, k, v)
        
        self.jsonUserData = json.loads(self.jsonUserData)


    def start_requests(self):

        """
        Allows to consult the main page of Conalpe. Returns the response of the page.
        """
        for url in self.startUrls:
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        print("Response",response)
        """
        Allows to scrape the terms and conditions page by sending
        the necessary form to go to the next page.

        Parameters:
            response: response of the page consulted in the start_requests method.

        Exit:
            Response that returns the scraping to the terms and conditions page.
        """

        infotable = response.xpath('//*[@id="contenido"]/table/tbody[1]/tr')
        lista_data = []
        if infotable != None or infotable != []:            
           
            for  i in range (1,3):        
                infotable = response.xpath('//*[@id="contenido"]/table/tbody['+str(i)+']/tr')  
                                                

                for element in infotable:            

                    jsonData = json.loads(self.specificCons.JSONRESULT.format(

                        numero_rol =  element.xpath('./td[1]/text()').get(default=""),

                        persona_natural_juridica =  element.xpath('./td[2]/text()').get(default=""),

                        sector_economico =  element.xpath('./td[3]/text()').get(default=""),

                        causal =  element.xpath('./td[4]/text()').get(default=""),

                        fecha_resolucion =  element.xpath('./td[5]/text()').get(default="")

                    ))                        
                    
                    lista_data.append(jsonData) 

            lista_data.pop(0)
            lista_sancionados = {self.specificCons.INFORELECTRICISTA: lista_data}

            yield {self.generalCons.INFOID: self.jsonUserData["rowId"], self.generalCons.INFOPROJECTS: lista_sancionados}
                   
        else:
            jsonData = json.loads(self.specificCons.JSONRESULT.format(
                mensaje = "Tabla no Encontrada"
            ))                        
        
            lista_data.append(jsonData)        
            
            lista_sancionados = {self.specificCons.INFORELECTRICISTA: lista_data}

            yield {self.generalCons.INFOID: self.jsonUserData["rowId"], self.generalCons.INFOPROJECTS: lista_sancionados}