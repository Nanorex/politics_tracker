"""
Output gets handled in this file
"""

import os

import csv

def write_active_party_data(data, output_path):
    out_string = "party_name,seats,mean_tournout\n"
    for faction in data.keys():
        out_string = out_string + "{},{},{}\n".format(faction, data[faction]["seats"], data[faction]["overall_turnout"])

    full_out_path = os.path.join(output_path, "active_parties.csv")
    with open(full_out_path, "w") as file:
        file.write(out_string)


def write_turnout_statistics(data, output_path):
    out_string = ""
    for faction in data.keys():
        datastring = ','.join(['%.5f' % num for num in data[faction]["turnout_list"]])
        out_string = out_string + "{},{}\n".format(faction, datastring)

    full_out_path = os.path.join(output_path, "turnout_data.csv")
    with open(full_out_path, "w") as file:
        file.write(out_string)