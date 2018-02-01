"""This program is written as part of Intercom Take Home Test.

File: geo.py
Purpose: Geography related logic
Author: Ajay Maity
Started: 31 Jan 2018, 20:42
"""

from math import acos, cos, fabs, radians, sin


def _cen_angle(lat1, lon1, lat2, lon2):
    """Calculate central angle between two geographic coordinates.

    Args:
        lat1: latitude of coordinate 1 (float)
        lon1: longitude of coordinate 1 (float)
        lat2: latitude of coordinate 2 (float)
        lon2: longitude of coordinate 2 (float)
    Returns:
        (float) the central angle between two coordinates
    """
    return acos(sin(lat1) * sin(lat2) + cos(lat1) *
                cos(lat2) * cos(fabs(lat2 - lat1)))


def deg2rad(deg):
    """Convert degrees to radians.

    Args:
        deg: the angle in degress (float)
    Returns:
        float, the angle in radians
    """
    return radians(deg)


def calc_dist(rad, lat1, lon1, lat2, lon2):
    """Calculate distance between two geographic coordinates.

    Args:
        rad: radius of sphere (float)
        lat1: latitude of coordinate 1 (float)
        lon1: longitude of coordinate 1 (float)
        lat2: latitude of coordinate 2 (float)
        lon2: longitude of coordinate 2 (float)
    Returns:
        (float) the distance between two coordinates
    """
    return rad * _cen_angle(lat1, lon1, lat2, lon2)

def is_prop_latlon(latlon, mode=True):
    """Check if the latitude/longitude is proper.

    Args:
        latlon: latitude to check in degrees (str)
        mode: runs the method to check properness of latitude or longitude.
            if True, the method runs for latitude; else for longitude.
    Returns:
        (boolean) True if latitude is proper, else False
    """
    if latlon == 'NaN': return False
    if mode: val = 90
    else: val = 180
    try:
        l = float(latlon)
        if ((l > val) or (l < -val)): return False
        return True
    except ValueError:
        return False