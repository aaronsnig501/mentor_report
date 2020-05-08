"""
A utility module responsible for retrieving the necessary data from the
mentoring API.

Most properties of this module are private as they are only needed to parse
the information that comes from the API.
"""
from datetime import datetime
from datetime import timedelta
import requests
from .calculator import perform_rate_calculation


def _call_api(url):
    """Make the call to the API

    Retrieve the data from the API using the relevant month and year only
    return the relevant JSON data

    Args:
        url (str): The URL that the data will be retrieved from
    
    Returns:
        dict: The deserialized information in dictionary form
    """
    print('retrieving results')
    return requests.get(url).json()['details']


def get_data(url, rate):
    """
    Handle the data that comes from the API and return a parsed dataset to the
    consumer.

    Args:
        url (str): The URL that the data will be retrieved from
        rate (int): The hourly rate of payment
    
    Returns:
        iterator: The next row of data in dictionary format
    """
    print(_call_api(url))
    api_data = _call_api(url)

    print('data retrieved successfully. generating data records')
    for row in api_data:
        data = {
            'duration': row['duration'],
            'date': row['date'],
            'total_billable': perform_rate_calculation(row['duration'], rate),
            'name': row['student_name']
        }
        yield data