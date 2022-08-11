import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../..'))
from externalSources.generalLibraries.constants import Constants

def test_constants():
    constants = Constants()
    assert constants != None

def test_ok():
    constants = Constants()
    assert constants.OK==0

def test_fail():
    constants = Constants()
    assert constants.FAIL==1

def test_eror():
    constants = Constants()
    assert constants.ERROR==-1

def test_no_data():
    constants = Constants()
    assert constants.NODATA==100

def test_info():
    constants = Constants()
    assert constants.INFOPROJECTS=="DATA"

def test_info_id():
    constants = Constants()
    assert constants.INFOID == "ID"
