import pandas
df = pandas.read_excel(r"D:\Projecte\Abstimmungsseite\Daten\Bundestag\Namentliche_Abstimmungen\20231110_3_xls.xlsx")

#print the column names
print(df.columns)

#get the values for a given column
values = df['Wahlperiode'].values

for index in range(10):
    print(values[index])

#get a data frame with selected columns
#FORMAT = ['Col_1', 'Col_2', 'Col_3']
#df_selected = df[FORMAT]

selected_party = "AfD"
#print(get_party_voring_tournout(selected_party, collected_data))

