"""A module that contains helper functions for JotForm API"""

# Libraries
from jotform.JotformAPIClient import JotformAPIClient

# ------------------------------------------------------------------------------------


def pull_submissions(API, filter_array, limit=0, order_by=None, offset=0):
    """Send a request to JotForm API and receive a response the given folder ID.

    Args:
        filter_array (dict): Filters the query results to fetch a specific form range.
        limit (int, optional): Number of results in each result set for form list.
            Defaults to 0.
        order_by (str, optional): Order results by a form field name. Defaults to None.
        API (str): JotForm API Key with Full Access permissions.
        offset (int, optional): Start of each result set for form list. Defaults to 0.

    Returns:
        list: List of submissions dictionaries.
    """
    jotformAPIClient = JotformAPIClient(API)
    submissions = jotformAPIClient.get_submissions(
        offset=offset, limit=limit, filterArray=filter_array, order_by=order_by
    )

    return submissions


def reformat_submission_list(submission_list):
    """Re-format the response from JotForm API, remove extra data
      and return a list of dictionaries.

    Args:
        submission_list (list):  A list of dictionaries received from Jotform API.

    Returns:
        list: A new list of dictionaries
            i.e.    [
                {
                    "typeA21": "Cascadia",
                    "Model": "Cascadia",
                },
                {
                    "typeA21": "Ford",
                    "Model": "Ford",
                },
            ]
    """
    new_submission_list = []
    for submission in submission_list:
        submission_data = {}
        submission_data['created_at'] = submission['created_at']
        for answer in submission["answers"].values():
            if "answer" in answer and "name" in answer:
                # Column Name i.e "name":"column8"
                column_name = str(answer["name"]).strip()
                # Column header text i.e "text":"Policy Number"
                column_text = str(answer["text"]).strip()
                # Column value/text i.e "answer": "3334343433"
                cell_text = str(answer["answer"]).strip()
                submission_data[column_name] = cell_text
                submission_data[column_text] = cell_text
        if submission_data:
            new_submission_list.append(submission_data)
    return new_submission_list


def create_date_from_dict(dict_date):
    """Convert a date dictionary to a string.

    Args:
        dict_date (dict):  A dictionary having 'month', 'day', and 'year' keys

        i.e: {
              "month": "02",
              "day": "14",
              "year": "1997"
           }

    Returns:
        str: Formatted as "month/day/year"
    """
    if not dict_date:
        return None

    day = dict_date["day"]
    month = dict_date["month"]
    year = dict_date["year"]

    date = f"{month}/{day}/{year}"

    return date
