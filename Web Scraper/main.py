import bs4
from bs4 import BeautifulSoup
with open('../Web Scraper/home.html', 'r') as html_file:
    content=html_file.read()

    soup=BeautifulSoup(content, 'lxml')
    tags=soup.find_all('h5')

    cards=soup.find_all('div', class_="card") #we have to add class_ in order to distinguish from keyword - class

    for card in cards:
        card_topic=card.h5.text
        card_price=card.a.text.split()[-1]

        print(f'The cost of {card_topic} course is {card_price}')
