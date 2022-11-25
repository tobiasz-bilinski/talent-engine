class TestData:
    # DATA TYPES TESTS
    test_data_types_positive = [(1, int),
                                (2.5, float),
                                ("String", str),
                                (False, bool),
                                (["a", "b", "c"], list),
                                ({"a": 1, "b": 2}, dict),
                                ((1, 2, 3), tuple),
                                ({1, 2, 3}, set)]

    test_data_types_negative = [("1", int),
                                (2, float),
                                (True, str),
                                ([1, 2], bool),
                                ({"a", "b", "c"}, list),
                                ([1, 2, 3], dict),
                                ({"a": 1, "b": 2}, tuple),
                                ([1, 2, 3], set)]
    # USER TESTS
    USERNAME = "Tobiasz"
    BIRTH_YEAR = 1990
    # WEATHER API TESTS
    WEATHER_CORRECT_CITY = "Warsaw"
    WEATHER_WRONG_CITY = "Nonexistent"
    WEATHER_CORRECT_COUNTRY = "PL"
    EXPECTED_FORECAST_LENGTH = 40
    # GITHUB UI TESTS
    EXPECTED_LOGIN_PAGE_TITLE = "Sign in to GitHub · GitHub"
