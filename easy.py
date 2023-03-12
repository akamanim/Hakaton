'''  получить:
1. Наименование всех телефонов
2. Цену каждого продукта(в KGS)
3. И ссылка к фотографии
4. Все это записать в CSV файл '''
import requests
from bs4 import BeautifulSoup as BS
import csv
import time
def write_to_csv(data):
    with open('data_easy.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([data['alo'],data['price'],data['image']])
def get_html(url):
    responce = requests.get(url)
    return responce.text
def get_total_pages(html):
    soup = BS(html, 'lxml')
    page_list = soup.find('div',class_='pager-wrap').find('ul',class_='pagination pagination-sm').find_all('li')
    last_page = page_list[-1].text
    # print(last_page)
    return int(last_page)
def get_data(html):
    soup = BS(html, 'lxml')
    contents = soup.find('div', class_= 'list-view').find_all('div', class_='item product_listbox oh')
    for content in contents:
        alo = content.find('div', class_='listbox_title oh').text
        price = content.find('div', class_= 'listbox_price text-center').find('strong').text
        image = 'https://www.kivano.kg' + str(content.find('div', class_= 'listbox_img pull-left').find('img').get('src'))
        data = {'alo':alo,'price':price,'image':image}
        write_to_csv(data)
        # print (alo,price,image)
with open('data_easy.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['alo','price','image'])
def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    html = get_html(url)
    pages = '?page='
    get_data(html)
    number = get_total_pages(html)
    for i in range (2, number+1):
        url_with_page = url + pages + str(i)
        print (i)
        # print(url_with_page)
        html = get_html(url_with_page)
        get_data(html)

while True:
    main()
    time.sleep(3600) 

