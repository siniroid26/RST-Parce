from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = 'https://rst.ua/ukr/oldcars/?task=newresults&make%5B%5D=0&year%5B%5D=0&year%5B%5D=0&engine%5B%5D=0&engine%5B%5D=0&gear=0&fuel=0&z=0&s=0&price%5B%5D=4000&price%5B%5D=6000&d=0'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

car_list = soup.find_all('div', {'class': 'rst-ocb-i'})
for car in car_list:
    title = car.find('a', {'class': 'rst-ocb-i-h'})
    if title:
        print('Title:', title.text.strip())
    price = car.find('span', {'class': 'rst-ocb-i-cp'})
    if price:
        print('Price:', price.text.strip())
    year = car.find('div', {'class': 'rst-ocb-i-y'})
    if year:
        print('Year:', year.text.strip())
    print('-----------------------------------')

driver.quit()
