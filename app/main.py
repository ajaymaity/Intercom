"""This program is written as part of Intercom Take Home Test.

File: main.py
Purpose: Main program logic
Author: Ajay Maity
Started: 31 Jan 2018, 20:19
Problem Description: EMail from Ewa Zajac (TCD ID)
"""
from __future__ import print_function
from json import loads
from os.path import join
from six import iterkeys
import configparser

from data_io import read
from geo import calc_dist, deg2rad

if __name__ == '__main__':
    """Start of program execution."""

    # Read configuration file...
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Read customer records from file...
    cust_records = read(join(config['DEFAULT']['DATA_DIR'],
                        config['DEFAULT']['GIST_FILE']))
    # Convert intercom office coordinates from degrees to radians...
    off_lat = deg2rad(float(config['INPUTS']['OFFICE_LAT']))
    off_lon = deg2rad(float(config['INPUTS']['OFFICE_LON']))

    # Loop through all records, find distance from intercom office,
    # and store the customer records in a dictionary who is within 100 kms...
    mat_cust_dict = dict()
    for cust_record in cust_records:
        cust_rec_json = loads(cust_record)
        lat = deg2rad(float(cust_rec_json['latitude']))
        lon = deg2rad(float(cust_rec_json['longitude']))
        dist = calc_dist(float(config['DEFAULT']['EARTH_RAD']),
                         off_lat, off_lon, lat, lon)
        if (dist < 100):
            mat_cust_dict[int(cust_rec_json['user_id'])] = \
                cust_rec_json['name']

    # Sort the customer records wrt their IDs and print...
    for user_id in sorted(iterkeys(mat_cust_dict)):
        print('{}: {}'.format(user_id, mat_cust_dict[user_id]))
