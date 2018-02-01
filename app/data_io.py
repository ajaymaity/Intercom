"""This program is written as part of Intercom Take Home Test.

File: data_io.py
Purpose: Data related logic
Author: Ajay Maity
Started: 31 Jan 2018, 20:42
"""

from sys import exit


def read(data):
    """Read data from file.
    
    Args:
        data: the data file which is to be read (str)
    Returns:
        list where each item is a line
    """
    try:
        with open(data, 'r') as data_file:
            read_data = data_file.readlines()
    except IOError:
        print("The file does not exist. Please check the file path or name.")
        print("Exiting application.")
        exit()

    return read_data


def is_prop_user(user_id):
    """Check if the user ID is proper.

    Args:
        user_id: user ID to check (str)
    Returns:
        (boolean) True if user ID is proper, else False
    """
    try:
        int(user_id)
        return True
    except:
        return False