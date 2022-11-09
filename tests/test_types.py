import pytest


def test_int_positive():
    assert isinstance(1, int)


def test_float_positive():
    assert isinstance(2.5, float)


def test_str_positive():
    assert isinstance("String", str)


def test_bool_positive():
    assert isinstance(False, bool)


def test_list_positive():
    assert isinstance(["a", "b", "c"], list)


def test_dict_positive():
    assert isinstance({"a": 1, "b": 2}, dict)


def test_tuple_positive():
    assert isinstance((1, 2, 3), tuple)


def test_set_positive():
    assert isinstance({1, 2, 3}, set)


@pytest.mark.xfail
def test_int_negative():
    assert isinstance("1", int)


@pytest.mark.xfail
def test_float_negative():
    assert isinstance(2, float)


@pytest.mark.xfail
def test_str_negative():
    assert isinstance(True, str)


@pytest.mark.xfail
def test_bool_negative():
    assert isinstance([1, 2, 3, 4], bool)


@pytest.mark.xfail
def test_list_negative():
    assert isinstance({"a": 1, "b": 2}, list)


@pytest.mark.xfail
def test_dict_negative():
    assert isinstance((1, 2, 3), dict)


@pytest.mark.xfail
def test_tuple_negative():
    assert isinstance([1, 2, 3], tuple)


@pytest.mark.xfail
def test_set_negative():
    assert isinstance([1, 2, 3], set)
