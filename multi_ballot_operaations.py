"""
Collection of operations on multiple ballots
"""
import os

import pandas
import numpy as np

import single_ballot_operations


def add_output_faction(dict, faction_name):
    dict[faction_name] = {
        "ballot_count": 0,
        "overall_turnout": 0,
        "overall_invalid_votes": 0,
        "turnout_list": np.asarray([]),
        "invalid_votes_list": np.asarray([])
    }
    return dict


def collect_turnout_statistics(datapath):
    out_data = {}
    files = os.listdir(datapath)
    for file in files:
        current_path = os.path.join(datapath, file)
        current_data = pandas.read_excel(current_path)
        ballot_turnout = single_ballot_operations.get_full_ballot_turnout(current_data)
        for faction in ballot_turnout.keys():
            if faction not in out_data:
                out_data = add_output_faction(out_data, faction)
            out_data[faction]["ballot_count"] += 1
            out_data[faction]["turnout_list"] = np.append(out_data[faction]["turnout_list"],
                                                          ballot_turnout[faction]["turnout"])
            out_data[faction]["invalid_votes_list"] = np.append(out_data[faction]["invalid_votes_list"],
                                                                ballot_turnout[faction]["invalid_votes"])
    for faction in out_data.keys():
        out_data[faction]["overall_turnout"] = np.sum(out_data[faction]["turnout_list"]) / out_data[faction][
            "ballot_count"]
        out_data[faction]["overall_invalid_votes"] = (np.sum(out_data[faction]["invalid_votes_list"]) /
                                                      out_data[faction]["ballot_count"])

    return out_data

if __name__ == "__main__":
    input_path = r"D:\Projecte\Abstimmungsseite\Daten\Bundestag\Namentliche_Abstimmungen"
    output = collect_turnout_statistics(input_path)
    for faction in output:
        print(faction)
        print(f"Overall turnout: {output[faction]['overall_turnout']}")