# extract_doc_info.py

from PyPDF2 import PdfReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        page = pdf.pages[0]
        text = page.extract_text()

    shards = text.split("\n")
    for line in shards:
        print(line)

    print("\n")
    print(shards[5])

    return 0

if __name__ == '__main__':
    #path = r'D:\Projecte\Abstimmungsseite\Daten\Bundestag\Abstimmungen_pdf\20240202_1.pdf'
    path = r'D:\Projecte\Abstimmungsseite\Daten\Bundestag\Abstimmungen_pdf\20240118_2.pdf'
    extract_information(path)