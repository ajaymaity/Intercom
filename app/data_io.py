"""This program is written as part of Intercom Take Home Test.

File: data_io.py
Purpose: Data related logic
Author: Ajay Maity
Started: 31 Jan 2018, 20:42
"""


def read(data):
    """Read data from file.
    
    Args:
        data: the data file which is to be read (str)
    Returns:
        list where each item is a line
    """
    with open(data, 'r') as data_file:
        read_data = data_file.readlines()
    return read_data
