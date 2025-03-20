from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.kivano.kg/mobilnye-telefony'
respons = requests.get(URL)
html = respons.text
soup = bs(html, 'lxml')
telephone_list = soup.find_all('div', class_='product_text pull-left')
telephones = []
titles = []
desc = []

for telephone in telephone_list:
    # Извлекаем название телефона
    title = telephone.find('div', class_='listbox_title oh')
    if title:
        titles.append(title.text.strip().replace('\n', ''))
    
    description = telephone.find('strong')
    if description:
        desc.append(description.text.strip().replace('\n\n       ', ',').split(','))

print(titles)
print(desc)

