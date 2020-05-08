"""app.py - This module is the entry point into the `mentor report`

This is the module where routes and defined and where the app is run from.

In order to execute this file, run::

    $ python app.py
"""
import os
import json
from bottle import route, run, default_app
from utils.api_handler import get_data
from utils.formulas import generate_formula

application = default_app()


@route('/sessions/<rate:int>/<month>/<year>')
def sessions(rate, month, year):
    """Get sessions

    The endpoint that will be retrieve the data and return it the caller.

    Args:
        rate (int): The rate of payment per hour
        month (str): The month that wish to generate the report for
        year (str):  The year that wish to generate the report for
    
    Returns:
        JSON: A JSON representation of the sessions, including the formula that will be used
        in the Google Sheet

    Examples:
        In order to generate a report with a rate of 50 euro per hour for the month of March, 2020::

            $ curl http://127.0.0.1:8080/sessions/50/3/2020
        
        Or, in Python using requests::

            >>> import requests
            >>> response = requests.get("http://127.0.0.1:8080/sessions/50/3/2020")
            >>> response.status_code
            200
    
    Example Output:
        An example of what the data structure looks like::

            [
                {
                    "duration": "0:26:00",
                    "date": "02/03/2020",
                    "total_billable": 21.67,
                    "name": "Eamonn Smyth",
                    "formula": "=SPLIT(\"Mentor session - Eamonn Smyth 02/03/2020,,,50,0:26:00,21.67\", \",\", TRUE, FALSE)"
                }
            ]

    """
    endpoint = os.getenv('API_ENDPOINT').format(month, year)
    session_data = [entry for entry in get_data(endpoint, 50)]
    [entry.update({"formula": generate_formula(entry, rate)}) for entry in session_data]
    return json.dumps(session_data, ensure_ascii=False).encode('utf8')


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=os.getenv("DEBUG", False), reloader=True)