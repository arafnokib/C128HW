from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("/Users/arafnokib/Downloads/Whitehat/Python/C128HW/chromedriver")
browser.get(START_URL)
time.sleep(10)

headers = ["name", "distance", "mass", "radius"]
star_data = []
new_planet_data = []
soup = BeautifulSoup(browser.page_source, "html.parser")

def scrape():
    for i in range(1, 457):

        for tr_tag in soup.find_all("tr"):
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
            hyperlink_td_tag = td_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs"+hyperlink_td_tag.find_all("a", href=True)[0]["href"])
            new_planet_data.append(temp_list)
        print(" page done ")
        
    with open("scraper_1.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(new_planet_data)
    print(new_planet_data)


def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planet_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)
    
scrape()