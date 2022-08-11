import os
import sys
import json

stepDir = os.path.dirname(sys.path[0])
sys.path.append(os.path.join(stepDir, 'libraries_test'))
from libraries_test.constants4Test import Constants as TestSpecificCons
dirRelativeParents = '.'
sys.path.append(os.path.normpath(os.path.join(stepDir, dirRelativeParents)))
from scrapyEjecutariadas.spiders.ejecutariadas import EjecutariadasSpider
from scrapy.http import Request, TextResponse
import mocks


class Test_EjecutariadasSpider:
    __doc__ = "\n    This class allows to test the 'Conalpe' page spider: https://www.conalpe.gov.co/tramitesyservicios/Consulta-Inscritos"

    # Setup configurations
    testSpecificCons = TestSpecificCons()
    testJsonForm = testSpecificCons.USERDATAJSON
    
    spider = EjecutariadasSpider(jsonUserData=(json.dumps(testJsonForm)))
    actual_response = None
    

    def test_start_request(self):
        response_dummy = mocks.mock_response('response_start.html')
        response = TextResponse(str(next(self.spider.start_requests()).url))

        self.actual_response = response
        assert str(response_dummy) == str(response)


    def test_parse(self):
        ## prueba con numero de identidad 
        response_dummy = mocks.mock_response('response_start.html')
        response = next(self.spider.parse(response_dummy))

        #assert response.url == "https://www.conalpe.gov.co/api/ConsultarInscrito/estado?docIdentidad=1053826089&matricula=&radicado="
        #assert response.method == "GET"
        

    # def test_parse_filter_not_found(self):
    #     response_dummy = mocks.mock_response('response_data.json')
    #     response_dummy.status = 404
    #     response = next(self.spider.parse_filter(response_dummy))

       



        
