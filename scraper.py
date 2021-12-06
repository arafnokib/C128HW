from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/arafnokib/Downloads/Whitehat/Python/C127HW/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "distance", "mass", "radius"]
    star_data = []
    for i in range(0, 97):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr", attrs={"class", "wikitable sortable jquery-tablesorter"}):
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
            star_data.append(temp_list)
        
    with open("scraper_1.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
    print(star_data)
    
def scrape_more_data():
    try:
        headers = ["name", "distance", "mass", "radius"]
        url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        star_table = soup.find_all('table')
        temp_list = []
        table_rows = star_table[7].find_all('tr')
        table_data = []
        
       
        
        for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
        table_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data()
        
    with open("scraper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(table_data)
    
        

scrape()