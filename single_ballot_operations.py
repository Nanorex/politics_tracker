"""
Collection of operations on a single ballot
"""
import pandas

def add_output_faction(dict, faction_name):
    dict[faction_name] = {
        "membercount": 0,
        "turnout": 0,
        "invalid_votes": 0
    }
    return dict

def get_full_ballot_turnout(dataframe):
    output = {}
    for index in range(dataframe.shape[0]):
        current_party = dataframe["Fraktion/Gruppe"][index]
        if current_party not in output:
            output = add_output_faction(output, current_party)
        output[current_party]["membercount"] += 1
        if dataframe["ja"][index] == 1 or dataframe["nein"][index] == 1:
            output[current_party]["turnout"] += 1
        if dataframe["Enthaltung"][index] == 1 or dataframe["ungültig"][index] == 1 or dataframe["nichtabgegeben"][index] == 1:
            output[current_party]["invalid_votes"] += 1

    for party in output.keys():
        output[party]["turnout"] = output[party]["turnout"] / output[party]["membercount"]
        output[party]["invalid_votes"] = output[party]["invalid_votes"] / output[party]["membercount"]
    return output



if __name__ == "__main__":
    df = pandas.read_excel(r"D:\Projecte\Abstimmungsseite\Daten\Bundestag\Namentliche_Abstimmungen\20231110_3_xls.xlsx")
    result = get_full_ballot_turnout(df)
    print(result)
