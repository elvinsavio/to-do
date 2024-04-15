def name_to_url_safe(name:str = None) -> str:
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
