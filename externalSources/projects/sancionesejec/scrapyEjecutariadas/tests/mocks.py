import os
import sys

stepDir = os.path.dirname(sys.path[0])
sys.path.append(os.path.join(stepDir, 'libraries_test'))
from libraries_test.constants4Test import Constants as TestSpecificCons

dirRelativeParents = '.'
sys.path.append(os.path.normpath(os.path.join(stepDir, dirRelativeParents)))
from scrapy.http import Request, TextResponse

testSpecificCons = TestSpecificCons()

def mock_response(file_name=None, url=None, request=None):
        """Create a Scrapy fake HTTP response from a HTML file"""
        if not url:
            url = testSpecificCons.URL
        if not request:
            request_ = Request(url=url)
        else:
            request_ = Request(url=url, body=request)
        if file_name:
            if not file_name[0] == '/':
                responses_dir = os.path.dirname(os.path.realpath(__file__))
                file_path = os.path.join(responses_dir, "mockResponses", file_name)
            else:
                file_path = file_name
            file_content = open(file_path, 'r', encoding='utf-8').read()
        else:
            file_content = ''
        response = TextResponse(url=url, request=request_, body=file_content,
                                encoding='utf-8')
        return response