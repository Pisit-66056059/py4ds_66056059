"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    thr = int(tsec/3600)
    tsec = tsec - (thr*3600)
    tmin = int(tsec / 60)
    tsec = tsec -(tmin * 60)
    if thr == 0:
        if tmin == 0:
            return f'{tsec}s'
        elif tsec !=0:
            return f'{tmin}m {tsec}s'
        else:
            return f'{tmin}m'
    else:
        if tmin == 0 and tsec == 0:
            return f'{thr}h'
        elif tmin != 0 and tsec == 0:
            return f'{thr}h {tmin}m'
        elif tmin == 0 and tsec != 0:
            return f'{thr}h {tsec}s'
        else:
            return f'{thr}h {tmin}m {tsec}s'


