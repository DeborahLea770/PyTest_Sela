import pytest
import HomeWork3
import logging

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger(

@pytest.fixture
def create_data_set():
    data_set = {
        324271256: {"name": "tal", "age": 9, "sex": "female"},
        206910424: {"name": "dan", "age": 21, "sex": "male"},
        206910425: {"name": "levy", "age": 21, "sex": "mle"},
        206910426: {"name": "lea", "age": 23, "sex": "female"},
        206910427: {"name": "shire", "age": 26, "sex": "female"},
        206910428: {"name": "debora", "age": 64, "sex": "female"}
    }
    return data_set

@pytest.mark.homeWork3
def test_split_male_female(create_data_set):
    print("test for split male and female function")
    male, female = HomeWork3.split_male_female(create_data_set)
    assert len(male) + len(female) == len(create_data_set)

@pytest.mark.homeWork3
def test_find_median_average(create_data_set):
    print("test for find median average function")
    avg, median = HomeWork3.find_median_average(create_data_set)
    sum1 = 0
    for item in create_data_set.values():
        sum1 += item["age"]
    assert avg * len(create_data_set) == sum1

@pytest.mark.homeWork3
def test_print_value_above(create_data_set):
    print("test for print values above function")
    none = HomeWork3.print_value_above(create_data_set)
    assert (none, isinstance(none, type(None)))
