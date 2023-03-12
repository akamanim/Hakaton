''' Название всех моделей.
2.Цену всех моделей
3.Изображение всех моделей
4.Краткое описание всех моделей
5.Записать все в csv файл '''
import requests
from bs4 import BeautifulSoup as BS
import csv
import time
def write_to_csv(data):
    with open('data_medium.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([data['car'],data['price_car'],data['title'],data['image']])
def get_html(url):
    responce = requests.get(url)
    return responce.text
def get_data(html):
    soup = BS(html, 'lxml')
    contents = soup.find('div',class_= 'search-results-table').find_all('div', class_='list-item list-label')
    print (contents)
    # print (contents)
    for content in contents:
        car = content.find('div',class_='block title').text
        price_car = content.find('div',class_= 'block price').find('p').text
        image = content.find('div',class_='thumb-item-carousel').find('img').get('data-src')
        title = content.find('div',class_='block info-wrapper item-info-wrapper').find('p').text
        data = {'car':car,'price_car':price_car,'title':title,'image':image}
        print(car.lstrip(),price_car.lstrip(),title.lstrip(),image.lstrip())
        write_to_csv(data)
with open('data_medium.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['car','price','title'])
def main():
    url = 'https://www.mashina.kg/search/jaguar/?currency=2&price_from=&price_to='
    html = get_html(url)
    get_data(html)
    print(get_data)
main()
