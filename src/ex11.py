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
    time = []
    if tsec == 0:
        return '0s'
    else:
        thr = tsec // 3600
        if thr > 0:
            time.append(f'{thr}h')
        tsec = tsec - (thr * 3600)
        tmin = tsec // 60
        if tmin > 0:
            time.append(f'{tmin}m')
        tsec = tsec - (tmin * 60)
        if tsec > 0:
            time.append(f'{tsec}s')
    return ' '.join(time)
