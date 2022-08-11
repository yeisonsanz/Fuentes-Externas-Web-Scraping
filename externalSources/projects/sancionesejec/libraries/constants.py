#!/usr/bin/python



__author__ = "Ultracom"

__license__ = "Users authorized by Bancolombia"

__credits__ = "Ultracom-Bancolombia"

__version__ = "1.0"

__maintainer__ = "Ultracom-Bancolombia"


class Constants:

    """

    Class that allows to manage the constant variables of the program,

    is carried out as a class and using the hint @properties to ensure

    that the value is not modified during the time of execution.

    """

    def __init__(self):

        self.__JSONRESULT = '''{{"numeroRol":"{numero_rol}","personaNaturaloJuridica":"{persona_natural_juridica}","sectorEconomico":"{sector_economico}","causal":"{causal}","fechaResolucion":"{fecha_resolucion}"}}'''
        
        self.__INFORELECTRICISTA = "listadoSancionados"


    @property

    def JSONRESULT(self):

        """

        Allows to create a base json that contains the validation information

        of the forms for the pages that are scraped.

        """

        return self.__JSONRESULT
        

    @property

    def INFORELECTRICISTA(self):

        """

        Allows to return the name affiliation section.

        """

        return self.__INFORELECTRICISTA

