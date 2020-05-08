from utils.calculator import (
    _split_formatted_time, _seconds_as_decimal_of_a_minute,
    _total_number_of_minutes, _calculate_rate, perform_rate_calculation)


def test_split_formatted_string():
    assert _split_formatted_time("00:08:00") == (0, 8, 0)


def test_seconds_as_decimal_of_a_minute():
    assert _seconds_as_decimal_of_a_minute(30) == 0.5


def test_total_number_of_minutes():
    assert _total_number_of_minutes(1, 5) == 65


def test_calculate_rate():
    assert _calculate_rate(60.0, 50) == 50


def test_perform_rate_calculation():
    assert perform_rate_calculation("01:00:00", 50) == 50