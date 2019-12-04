import requests
from bs4 import BeautifulSoup
import time


def scrape_data():
    more_pages = True
    page = 0
    countries = []
    while(more_pages):
        r = requests.get(f'http://example.webscraping.com/places/default/index/{page}')
        soup = BeautifulSoup(r.text, features="lxml")
        
        # scrapes data from td
        tds = soup.findAll('td')
        for td in tds:
            countries.append(str(td.text).strip())

        # Check if there is another page
        print(page)
        As = soup.find('div',{'id': 'pagination'})
        As = As.findAll('a')
        more_pages = False
        for a in As:
            if 'Next' in str(a.text):
                next_page = True
            else:
                next_page = False
        
        if next_page != False:
            more_pages = True
            page+= 1
        time.sleep(1)
    
    return countries

def main():
    ''' This program is created to teach users how to build a simple scraper to obtain data.
        It is part of data engineering course
    '''

    data = scrape_data()

    print(data)

main()


    