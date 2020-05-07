"""
A utility module responsible for retrieving the necessary data from
API.
"""
from datetime import datetime
from datetime import timedelta
import requests
from .calculator import perform_rate_calculation


def _call_api(url):
    """
    Retrieve the data from the API using the relevant month and year
    only return the relevant JSON data
    """
    print('retrieving results')
    return requests.get(url).json()['details']


def _parse_duration(duration):
    """
    Parse the duration of the session from a string to a timedelta
    """
    duration_items = [int(date_item) for date_item in duration.split(':')]
    return str(timedelta(hours=duration_items[0], minutes=duration_items[1], seconds=duration_items[2]))


def get_data(url, rate):
    """
    Handle the data that comes from the API and return a parsed dataset to the
    consumer
    """
    print(_call_api(url))
    api_data = _call_api(url)

    print('data retrieved successfully. generating data records')
    for row in api_data:
        data = {
            'duration': _parse_duration(row['duration']),
            'date': row['date'],
            'total_billable': perform_rate_calculation(row['duration'], rate),
            'name': row['student_name']
        }
        yield data