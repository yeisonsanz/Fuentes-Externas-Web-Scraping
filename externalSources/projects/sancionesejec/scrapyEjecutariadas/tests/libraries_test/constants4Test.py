import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from libraries.constants import Constants as SpecificCons

class Constants():
    __doc__ = '\n    Class that allows to manage the constant variables of the program,\n    is carried out as a class and using the hint @properties to ensure\n    that the value is not modified during the time of execution.\n    '

    specificCons = SpecificCons()

    def __init__(self):
        self.JSONPARAMSCONALPE = ''' {{          
            "rowId":"{rowId}"
        }} '''
        self._Constants__URL = 'https://www.uaf.cl/prensa/sanciones_new.aspx'
    

    @property
    def USERDATAJSON(self):
        """
        Allows to create a base json that contains the basic information
        taken from service body request.
        """
        userdata = self.JSONPARAMSCONALPE.format(           
            rowId = 1
        )
        return json.loads(userdata)

    
    @property
    def URL(self):
        """
        Allows to create a start url point to scrape the site.
        """
        return self._Constants__URL

