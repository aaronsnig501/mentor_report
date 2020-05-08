"""
A helper module to facilitate the generation of the formulas to be used to
generate the rows in the Google Sheet invoice.
"""
def generate_formula(data, rate):
    """Generate the formula for Google Sheets

    This information will be added to a Google Sheet and this information.

    This function generates the formula that will insert the information into
    the Google Sheet in a CSV format.

    Args:
        data (dict): The dictionary format of a single record
        rate (int): The hourly rate of payment
    
    Returns:
        string: The formula formatted as a string
    """
    formula_format = '=SPLIT("{},,,{},{},{}", ",", TRUE, FALSE)'.format(
        "Mentor session - " + data['name'] + " " + str(data['date']),
        rate, data['duration'], data['total_billable']
    )
    return formula_format
