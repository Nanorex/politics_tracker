
import os
import urllib.request as urlrequest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def download_content(active_driver, output_path):
    """
    Downloads all files of the table. Checks also, if elements have already been downloaded
    :param webdriver.Firefox active_driver: the Webdriver
    :param string output_path: where to store the download files
    :return int: return codes (0 all fine, 1 skipped further downloads)
    """
    name_pf_active_table = "bt-slide col-xs-12 bt-standard-content slick-slide slick-current slick-active"
    name_of_content_table = "table bt-table-data"

    already_downloaded = os.listdir(output_path)
    active_table = active_driver.find_element(By.XPATH, f"//div[@class='{name_pf_active_table}']")
    download_table = active_table.find_element(By.XPATH, f".//table[@class='{name_of_content_table}']")
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

        # pdf_name = pdf_link.split("/")[-1]
        # xlsx_name = xlsx_link.split("/")[-1]
        document_tite = document_tite.replace("/", "--")
        pdf_name = f"{document_tite}.pdf"
        xlsx_name = f"{document_tite}.xlsx"

        if pdf_name in already_downloaded:
            print("downloaded all missing files, program is done!")
            return 1

        # _, _ = urlrequest.urlretrieve(f"{web_root}{pdf_link}", os.path.join(file_save_path, pdf_name))
        # _, _ = urlrequest.urlretrieve(f"{web_root}{xlsx_link}", os.path.join(file_save_path, xlsx_name))
        _, _ = urlrequest.urlretrieve(pdf_link, os.path.join(output_path, pdf_name))
        _, _ = urlrequest.urlretrieve(xlsx_link, os.path.join(output_path, xlsx_name))

    return 0


if __name__ == "__main__":

    web_root = "https://www.bundestag.de"
    file_save_path = r"D:\Projecte\Abstimmungsseite\Daten\Debug"

    driver = webdriver.Firefox()
    driver.get("https://www.bundestag.de/parlament/plenum/abstimmung/liste")
    # Wait for the website to fully load everything
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table bt-table-data']")))

    return_code = download_content(driver, file_save_path)
    if return_code == 1:
        driver.close()
        exit()

    # move to the next page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2 -300)")
    actions = ActionChains(driver)

    for i in range(4):
        time.sleep(2)   # Sleep for page change
        previous_page_button = driver.find_element(By.XPATH, "//button[@class='slick-next slick-arrow']")
        actions.move_to_element(previous_page_button)
        actions.click(previous_page_button)
        actions.perform()

        time.sleep(2)   # Sleep for page change
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table bt-table-data']")))
        return_code = download_content(driver, file_save_path)
        if return_code == 1:
            break

    driver.close()
