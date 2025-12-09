# extract_doc_info.py

import os

from PyPDF2 import PdfReader

def extract_information(pdf_path):
    lines_to_ignore = [
        "Ja-Stimmen",
        "Nein-Stimmen",
        "Enthaltungen",
        "Ungültige",
        "Drs.",
        "Nicht abgegebene",
        "Endgültiges Ergebnis",
        "Deutscher Bundestag",
        "Ausschuss",
        "Seite:",
        "Ende:",
        "zu dem Antrag",
        "Fraktion",
        "Drucksachen",
        "Drucksache",
        "Drsn"
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Donnerstag",
        "Freitag"
        "Samstag",
        "Sonntag",
        "GRÜNEN",
        "FDP",
        "SDP"
        "CDU",
        "AfD",
        "Freitag,",
        "Drsn."
    ]
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        page = pdf.pages[0]
        text = page.extract_text()

    shards = text.split("\n")
    for line in shards:
        if any(element in line for element in lines_to_ignore):
            continue
        print(line)

    #print("\n")
    second_half = text.split("zu")[1]
    second_half = second_half.split("- Drucksachen")[0]
    second_half = second_half.split("\n")[1:]
    second_half = "".join(second_half)
    #print(second_half)

    return 0

if __name__ == '__main__':
    path = r'D:\Projecte\Abstimmungsseite\Daten\Debug_2\Scraped'
    #path = r'D:\Projecte\Abstimmungsseite\Daten\Bundestag\Abstimmungen_pdf\20240118_2.pdf'

    for file in os.listdir(path):
        if "xlsx" in file:
            continue
        #print(f"Title of {file}")
        extract_information(os.path.join(path, file))
        print("\n\n")