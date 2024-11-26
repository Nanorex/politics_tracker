
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



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://www.bundestag.de/parlament/plenum/abstimmung/liste")
# Wait for the website to fully load everything
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table bt-table-data']")))
# Select the tale of interest
download_table = driver.find_element(By.XPATH, "//table[@class='table bt-table-data']")

driver.close()
