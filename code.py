from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("E:\jugant\PRO-127\chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Proper name", "Distance (ly)","Mass (M☉)","Radius (R☉)"]
    planet_data = []
    for i in range(0, 107):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr", attrs={"..."}):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]').click()
    with open("scrapper3.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()