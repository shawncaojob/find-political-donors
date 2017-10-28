import datetime


def is_valid_zip(s):
    """
    :param s: String
    :return: Boolean
    """
    if not isinstance(s, basestring): return False
    if len(s) == 5 or len(s) == 9:
        return all(char in "0123456789" for char in s)
    else:
        return False


def is_valid_date(d):
    """
    :param d: String. format of date in MMDDYYYYY format
    :return: Boolean
    """
    if len(d) != 8: return False
    try:
        datetime.datetime.strptime(d, '%m%d%Y')
        return True
    except ValueError:
        return False
