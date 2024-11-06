
import os
import pandas
#df = pandas.read_csv(r"C:\Projekte\altbacken\20231110_3_xls.csv")

class ballot_database():
	def __init__(self):
		print("I am alive")
		self.data = {}

	def import_csv(self, import_path, ballot_name):
		with open(filepath, "r") as file:
			data = file.read()
		lines = data.split("\n")

def read_csv(filepath):
	with open(filepath, "r") as file:
		data = file.read()
	lines = data.split("\n")
	dataframe = []
	n = 0
	for line in lines:
		dataframe.append(["", "", "", "", "", "", "", "", "", "", "", "", "", ""])
		shards = line.split(";")
		for index, item in enumerate(shards):
			dataframe[n][index] = item
		n += 1
	return dataframe


def get_party_voring_tournout(party, data):
	results = {}
	n = 0
	total_members = 0
	total_voters = 0
	total_tournout = 0
	min_tournout = 101
	max_tournout = -1
	#TODO add error
	for ballot in data:
		n += 1
		results[n] = {}
		member_count = 0
		voters = 0
		is_in_section = False
		for participant in ballot:
			if participant[3] != party:
				if is_in_section:
					break
				else:
					continue
			else:
				is_in_section = True
				member_count += 1
				total_members += 1
				if participant[7] == "1" or participant[8] == "1":
					voters += 1
					total_voters += 1
		results[n]["member_count"] = member_count
		results[n]["voters"] = voters
		temp_tournout = voters / member_count * 100
		results[n]["tournout_percent"] = temp_tournout
		total_tournout += results[n]["tournout_percent"]
		if temp_tournout < min_tournout:
			min_tournout = temp_tournout
		if temp_tournout > max_tournout:
			max_tournout = temp_tournout
	results["total"] = {
		"member_count": total_members / n,
		"voters": total_voters / n,
		"mean_tournout_percent": total_tournout / n,
		"min_tournout": min_tournout,
		"max_tournout": max_tournout
	}

	return results

def count_party_invalid_votes(party, data):
	invalid_counter = 0
	for ballot in data:
		is_in_section = False
		for participant in ballot:
			if participant[3] != party:
				if is_in_section:
					break
				else:
					continue
			else:
				is_in_section = True
				if participant[10] == "1":
					invalid_counter += 1
	return invalid_counter

def get_participants_decisions(name, surname, data):
	decisions = []
	for ballot in data:
		temp_decision = "None"
		for participant in ballot:
			if participant[4] == name and participant[5] == surname:
				if participant[7] == "1":
					temp_decision = "ja"
				elif participant[8] == "1":
					temp_decision = "nein"
				elif participant[9] == "1":
					temp_decision = "Enthaltung"
				elif participant[10] == "1":
					temp_decision = "invalid"
				elif participant[11] == "1":
					temp_decision = "nicht_abgegeben"
				decisions.append(temp_decision)
				break
	return decisions

def get_party_oppinions(party, data):
	opinions = {}
	n = 0
	for ballot in data:
		n += 1
		members = 0
		positives = 0
		negatives = 0
		no_opinion = 0
		not_participated = 0
		is_in_section = False
		for participant in ballot:
			if participant[3] != party:
				if is_in_section:
					break
				else:
					continue
			else:
				is_in_section = True
				members += 1
				if participant[7] == "1":
					positives += 1
				elif participant[8] == "1":
					negatives += 1
				elif participant[9] == "1":
					no_opinion += 1
				elif participant[10] == "1":
					not_participated += 1
				elif participant[11] == "1":
					not_participated += 1
		if positives >= members * 0.75:
			opinions[n] = "ja"
		elif positives >= members * 0.5:
			opinions[n] = "mostly yes"
		elif negatives >= members * 0.75:
			opinions[n] = "nein"
		elif negatives >= members * 0.5:
			opinions[n] = "mostly no"
		elif no_opinion >= members * 0.5:
			opinions[n] = "unentschlossen"
		elif not_participated >= members * 0.5:
			opinions[n] = "nicht Teilgenommen"
		else:
			opinions[n] = "ERROR"
	return opinions



if __name__ == "__main__":
	sourcepath = r"C:\Projekte\altbacken"
	collected_data = []
	for data_file in os.listdir(sourcepath):
		data_temp = read_csv(os.path.join(sourcepath, data_file))
		collected_data.append(data_temp)

	selected_party = "AfD"
	print(get_party_voring_tournout(selected_party, collected_data))
	print(count_party_invalid_votes(selected_party, collected_data))
	print(get_party_oppinions(selected_party, collected_data))
	print(get_participants_decisions("Merz", "Friedrich", collected_data))

	data_collection = ballot_database()


"""
#print the column names
print(df.columns)

#get the values for a given column
values = df['Wahlperiode'].values

for index in range(10):
    print(values[index])

#get a data frame with selected columns
#FORMAT = ['Col_1', 'Col_2', 'Col_3']
#df_selected = df[FORMAT]
"""