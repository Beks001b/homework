from bs4 import BeautifulSoup as bs
import requests 

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
telephone_list = soup.find_all('div', class_='item product_listbox oh')
telephones = []
titles = []
desc = []


for telephone in telephone_list:
    desc.append(telephone.find('div', class_='product_text pull-left').text.strip().replace('\n\n       ', ',').split(','))
    # titles.append(telephone.find('div', class_='listbox_title oh').text.replace('\n', ''))
    # desc.append(telephone.find('div', class_='product_text pull-left').text.replace('\n', ''))

print(desc)
# print(telephones)





    
