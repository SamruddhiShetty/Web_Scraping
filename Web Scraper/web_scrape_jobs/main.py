import bs4
from bs4 import BeautifulSoup
import requests as req
import pandas as pd
#provide url of website to be scraped
page=req.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.YHM1AOgzbIU')
soup=BeautifulSoup(page.content, 'html.parser')
week=soup.find(id="seven-day-forecast-body")


items = week.find_all(class_="tombstone-container")
print (items[0].find(class_="period-name").get_text())
print(items[0].find(class_="short-desc").get_text())
print(items[0].find(class_="temp").get_text())

period_names=[item.find(class_="period-name").get_text() for item in items]
short_descs=[item.find(class_="short-desc").get_text() for item in items]
temperatures=[item.find(class_="temp").get_text() for item in items]
# print(period_names)
# print(short_descs)
# print(temperatures)

weather=pd.DataFrame({'Period': period_names, 'Short Descriptions': short_descs, 'temperatures': temperatures})

print(weather)
weather.to_csv('weather.csv')
