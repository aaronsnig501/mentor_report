"""
A helper module that will be responsible for generating the rate of each
session, based on the length of the session.

Most of the members here are private as they are not needed outside of the
scope of this module.
"""
from utils.decorator import accepts


@accepts(float, int)
def _calculate_rate(total_time: float, rate_per_hour: int) -> float:
    """Calculate the total amount earned

    Take the total amount of time on a call and calculate the total amount of
    payment due for that call.

    Args:
        total_time (float): The total amount of time spent on the call
        rate_per_hour (int): The hourly rate
    
    Returns:
        float: The total value of the call rounded to 2 decimal places
    """
    return round((rate_per_hour * total_time) / 60, 2)


@accepts(int, int)
def _total_number_of_minutes(hours: int, minutes: int) -> int:
    """Total times represented as minutes

    The number of hours needs to be converted to minutes and added to the
    existing number of minutes in order to be able to calculate the total

    Args:
        hours (int): The total number of hours worked on a call
        minutes (int): The amount of minutes spent on a call

    Returns:
        int: The hours converted to minutes summed with the remaining
        minutes
    """
    hours_as_minutes = hours * 60
    return hours_as_minutes + minutes


@accepts(int)
def _seconds_as_decimal_of_a_minute(seconds: int) -> float:
    """Convert seconds to a decimal value

    Return the number of seconds as a decimal of a minute in order to make
    it possible to work with the number as a percentage of 100 rather than 60

    Args:
        seconds (int): The number of seconds spent on a call
    
    Returns:
        float: the number of seconds as a float rounded to two places
    """
    return round(seconds / 60, 2)


@accepts(str)
def _split_formatted_time(formatted_time: str) -> tuple:
    """Splitted formatted time into individual integers

    Take the time from a string and return each piece as an entry in a tuple

    Args:
        formatted_time (str): The duration of the call in a %h:%m:%s format
    
    Returns:
        tuple: Each piece of the time format as a tuple of ints
    """
    time_pieces = formatted_time.split(':')
    return tuple(map(int, time_pieces))


@accepts(str, int)
def perform_rate_calculation(duration: str, rate_per_hour: int) -> float:
    """Perform the rate calculation

    Wrapper function that will execute the whole process of calculating
    the total amount payable for a session based on the duration provided
    from the API.

    Args:
        duration (str): The total duration of the call
        rate_per_hour (int): The hourly rate
    
    Returns:
        float: The total amount of money earned for the call, based on the
        length of the call and the hourly rate
    """
    hour, minute, second = _split_formatted_time(duration)
    total_seconds = _seconds_as_decimal_of_a_minute(second)
    total_minutes = _total_number_of_minutes(hour, minute)
    return _calculate_rate(total_minutes + total_seconds, rate_per_hour)