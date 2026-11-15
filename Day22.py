# # Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
# import requests
# import json
# from bs4 import BeautifulSoup
# url= 'http://www.bu.edu/president/boston-university-facts-stats/'
# result=requests.get(url)
# print(result.status_code)
# soup=BeautifulSoup(result.text,'html.parser')
# print(soup.title)
# print(soup.find_all(['h1','h2','h3']))
# print(len(soup.find_all('p')))
# print(soup.prettify())
# print(soup.find_all('table'))
# for p in soup.find_all('p'):
#     print(repr(p.text))
# data={
#     'title':soup.title.text,
#     'heading':[h.text.strip() for h in soup.find_all(['h1','h2','h3'])],
#     'paragraph':[p.text.strip() for p in soup.find_all('p') if p.text.strip()]
# }
# with open('Bu_facts.json','w',encoding='utf-8') as f:
#     json.dump(data,f,ensure_ascii=False,indent=4)
#     print("datas successfuly converted into json")
# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# import requests
# import json
# from bs4 import BeautifulSoup
# url1='https://archive.ics.uci.edu/datasets'
# response=requests.get(url1)
# print(response.status_code)
# soup=BeautifulSoup(response.text,'html.parser')
# print(len('tables'))
# for tag in soup.find_all(['div','table','tr','td']):
#     print(tag.name,tag.get('class'))
# data=[]
# cards=soup.find_all('div',class_='rounded-box')
# for card in cards:
#     link=card.find('a',href=lambda x:x and '/dataset/'in x)
#     if link:
#         dataset={
#             'name':link.get_text(strip=True),
#             'url':'https://archive.ics.uci.edu/datasets'+link['href'],
#             'details':card.get_text(' ',strip=True)
#         }
#         data.append(dataset)
# with open('Datatable.json','w',encoding='utf-8') as f:
#     json.dump(data,f,ensure_ascii=False,indent=4)
#     print("succesfully crested json")
# print('total dataset',len(data))
# print(soup.prettify())
# # tables=soup.find_all('table',cellpadding=3)
# #table=tables[0]
# # data=[]
# #  for tr in table.find_all('tr'):
# #     row=[td.get_text(strip=True) for td in tr.find_all('td')]
# #     if row:
# #         data.append(row)
# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
import requests 
import json
from bs4 import BeautifulSoup
url2='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}
res=requests.get(url2,headers=headers)
print(res.status_code)
soup=BeautifulSoup(res.text,'html.parser')
print(len(soup.find_all('table')))
print(soup.find_all('table'))
tables=soup.find_all('table',class_='wikitable')
print("no of tables:",len(tables))
data=[]
for table in tables:
 for tr in table.find_all('tr'):
    row=[cell.get_text(' ',strip=True) for cell in tr.find_all(['th','td'])]
    if row:
        data.append(row)
with open('wikitable.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)
    print('succesfully created')
