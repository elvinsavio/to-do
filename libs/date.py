"""
Date lib
"""

from datetime import datetime


def parse_date(_format: str = None, date: str = None) -> str:
    """
    Formats a given string into a specified format

    args:
        format: the type
        date: the date to parse

    """
    if _format is None:
        raise ValueError("Format not specified")

    if date is None:
        raise ValueError("Date not specified")

    datetime_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

    match _format:
        case "dBY":
            return datetime_obj.strftime("%d %B, %Y")
        case _:
            raise ValueError("Undefined format")

