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
from sys import exit
import configparser

from data_io import is_prop_user, read
from geo import calc_dist, deg2rad, is_prop_latlon

if __name__ == '__main__':
    """Start of program execution."""

    # Read configuration file...
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Read customer records from file...
    cust_records = read(join(config['DEFAULT']['DATA_DIR'],
                        config['DEFAULT']['GIST_FILE']))
    # Convert intercom office coordinates from degrees to radians...
    off_lat_deg = config['INPUTS']['OFFICE_LAT']
    if is_prop_latlon(off_lat_deg, True):
        off_lat = deg2rad(float(off_lat_deg))
    else:
        print("Intercom Office latitude is not in a proper float format.")
        print("Exitiing application.")
        exit()

    off_lon_deg = config['INPUTS']['OFFICE_LON']
    if is_prop_latlon(off_lon_deg, False):
        off_lon = deg2rad(float(off_lon_deg))
    else:
        print("Intercom Office longitude is not in a proper float format.")
        print("Exitiing application.")
        exit()

    # Loop through all records, find distance from intercom office,
    # and store the customer records in a dictionary who is within 100 kms...
    mat_cust_dict = dict()
    for cust_record in cust_records:
        cust_rec_json = loads(cust_record)
        
        user_id_str = cust_rec_json['user_id']
        if (is_prop_user(user_id_str)):
            user_id = int(user_id_str)
        else:
            print("The record {} does not have user ID in integer format.".format(cust_record))
            print("Exitiing application.")
            exit()
        
        lat_deg = cust_rec_json['latitude']
        if is_prop_latlon(lat_deg, True):
            lat = deg2rad(float(lat_deg))
        else:
            print("Customer {}'s latitude is not in a proper float format.".format(user_id))
            print("Exitiing application.")
            exit()

        lon_deg = cust_rec_json['longitude']
        if is_prop_latlon(lon_deg, False):
            lon = deg2rad(float(lon_deg))
        else:
            print("Customer {}'s longitude is not in a proper float format.".format(user_id))
            print("Exitiing application.")
            exit()

        dist = calc_dist(float(config['DEFAULT']['EARTH_RAD']),
                         off_lat, off_lon, lat, lon)
        if (dist < 100):
            mat_cust_dict[user_id] = \
                cust_rec_json['name']

    # Sort the customer records wrt their IDs and print...
    for user_id in sorted(iterkeys(mat_cust_dict)):
        print('{}: {}'.format(user_id, mat_cust_dict[user_id]))
