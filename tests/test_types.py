import pytest
from src.data.test_data import TestData


@pytest.mark.parametrize("test_input, expected", TestData.test_data_types_positive)
def test_data_types_positive(test_input, expected):
    assert isinstance(test_input, expected)


@pytest.mark.xfail
@pytest.mark.parametrize("test_input, expected", TestData.test_data_types_negative)
def test_data_types_negative(test_input, expected):
    assert isinstance(test_input, expected)
