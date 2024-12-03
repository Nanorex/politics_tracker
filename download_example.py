
"""
import urllib.request as urlrequest

#url = "https://www.bundestag.de/resource/blob/1025324/86abe84f8129655f5116f34d4ecebec9/20241018_8.pdf"
url = r"https://www.bundestag.de/parlament/plenum/abstimmung/liste"
filename = "Ablehnung_des_Antrages.pdf"

path, headers = urlrequest.urlretrieve(url, filename)
for name, value in headers.items():
    print(name, value)


fp = urlrequest.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)

assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
"""

import os
import urllib.request as urlrequest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web_root = "https://www.bundestag.de"
file_save_path = r"D:\Projecte\Abstimmungsseite\Daten\Debug"

driver = webdriver.Firefox()
driver.get("https://www.bundestag.de/parlament/plenum/abstimmung/liste")
# Wait for the website to fully load everything
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table bt-table-data']")))
# Select the tale of interest
download_table = driver.find_element(By.XPATH, "//table[@class='table bt-table-data']")
rows = download_table.find_elements(By.TAG_NAME, "tr")

index = -1
for row in rows:
    index += 1
    if index == 0:
        continue
    try:
        current_element = row.find_element(By.TAG_NAME, "span")
        document_tite = current_element.text
    except(EC.NoSuchElementException):
        current_element = row.find_element(By.TAG_NAME, "strong")
        document_tite = current_element.text
        document_tite = document_tite.split(": ")[-1]
    current_element = row.find_elements(By.TAG_NAME, "a")
    pdf_link = current_element[0].get_dom_attribute("href")
    xlsx_link = current_element[1].get_dom_attribute("href")

    #pdf_name = pdf_link.split("/")[-1]
    #xlsx_name = xlsx_link.split("/")[-1]
    document_tite = document_tite.replace("/", "--")
    pdf_name = f"{document_tite}.pdf"
    xlsx_name = f"{document_tite}.xlsx"

    _, _ = urlrequest.urlretrieve(f"{web_root}{pdf_link}", os.path.join(file_save_path, pdf_name))
    _, _ = urlrequest.urlretrieve(f"{web_root}{xlsx_link}", os.path.join(file_save_path, xlsx_name))

driver.close()
