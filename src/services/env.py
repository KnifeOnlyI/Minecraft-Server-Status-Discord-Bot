import os


def get_string(key: str) -> str:
    """
    Get an environment variable and convert it to string

    :param key: The key

    :return: The founded value (None if not found)
    """

    try:
        value = os.environ[key]
    except KeyError:
        raise KeyError(f"Missing ENV variable : {key}")

    return value


def get_int(key: str) -> int:
    """
    Get an environment variable and convert it to int

    :param key: The key

    :return: The founded value (None if not found)
    """

    try:
        return int(get_string(key))
    except ValueError:
        raise ValueError(f"Cannot convert ENV variable {key} to int")
