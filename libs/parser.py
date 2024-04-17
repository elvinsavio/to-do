"""
Parser lib
"""


def name_to_url_safe(name: str = None) -> str:
    """
    Converts a give string to url safe string
    args:
        name: name to covert

    return:
        name
    """
    if name is None:
        raise ValueError("Name cannot be empty")

    name = name.strip().split(" ")
    return "-".join(name)


def url_to_name(url: str) -> str:
    """
    Converts a give url to readable string
    args:
        url: url to covert

    return:
        url
    """
    if url is None:
        raise ValueError("url cannot be empty")

    url = url.split("-")
    return " ".join(url)
