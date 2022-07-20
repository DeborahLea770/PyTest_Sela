import pytest
import HomeWork4
import logging
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture
def test_init():
    mylogger.info("test for init function")
    assert HomeWork4.Date(1, 1, 2001)

@pytest.mark.homeWork4
def test_str():
    mylogger.info("test for str function")
    d = HomeWork4.Date(23, 6, 2013)
    assert HomeWork4.Date.__str__(d) == "23/6/2013"

@pytest.mark.homeWork4
def test_sub():
    mylogger.info("test for sub function")
    d1 = HomeWork4.Date(7, 12, 2000)
    d2 = HomeWork4.Date(17, 12, 2000)
    assert HomeWork4.Date.__sub__(d1, d2) == 10

@pytest.mark.homeWork4
def test_eq():
    mylogger.info("test for eq function")
    d1 = HomeWork4.Date(7, 12, 2000)
    d2 = HomeWork4.Date(7, 12, 2000)
    assert HomeWork4.Date.__eq__(d1, d2)

@pytest.mark.homeWork4
def test_ne():
    mylogger.info("test for ne function")
    d1 = HomeWork4.Date(7, 12, 2000)
    d2 = HomeWork4.Date(17, 12, 2000)
    assert HomeWork4.Date.__ne__(d1, d2)

@pytest.mark.homeWork4
def test_gt():
    mylogger.info("test for gt function")
    d1 = HomeWork4.Date(17, 12, 2000)
    d2 = HomeWork4.Date(7, 12, 2000)
    assert HomeWork4.Date.__gt__(d1, d2)

@pytest.mark.homeWork4
def test_lt():
    mylogger.info("test for lt function")
    d1 = HomeWork4.Date(7, 12, 2000)
    d2 = HomeWork4.Date(17, 12, 2000)
    assert HomeWork4.Date.__lt__(d1, d2)

@pytest.mark.homeWork4
def test_ge():
    mylogger.info("test for ge function")
    d1 = HomeWork4.Date(17, 12, 2000)
    d2 = HomeWork4.Date(7, 12, 2000)
    assert HomeWork4.Date.__ge__(d1, d2)
    assert HomeWork4.Date.__ge__(d1, d1)

@pytest.mark.homeWork4
def test_le():
    mylogger.info("test for le function")
    d1 = HomeWork4.Date(7, 12, 2000)
    d2 = HomeWork4.Date(17, 12, 2000)
    assert HomeWork4.Date.__le__(d1, d2)
    assert HomeWork4.Date.__le__(d2, d2)

@pytest.mark.homeWork4
def test_isValid():
    mylogger.info("test for isValid function")
    assert HomeWork4.Date.isValid(HomeWork4.Date(1, 12, 2001))

@pytest.mark.homeWork4
def test_getNextDay():
    mylogger.info("test for getNextDay function")
    d = HomeWork4.Date(24, 1, 2016)
    assert HomeWork4.Date(23, 1, 2016).getNextDay() == d

@pytest.mark.homeWork4
def test_getNextDays():
    mylogger.info("test for getNextDays function")
    d = HomeWork4.Date(27, 1, 2016)
    assert HomeWork4.Date(23, 1, 2016).getNextDays(4) == d

