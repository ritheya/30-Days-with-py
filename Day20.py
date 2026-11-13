
#Exercises: Day 20
# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import re
import requests
url = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt'
response=requests.get(url)
print(response.status_code)
print(response.url)
print(response.text[:500])
count={}
for lines in response.text.splitlines():
    words=lines.lower().split()
    for word in words:
        word=re.sub(r'[^a-zA-Z0-9]','',word,flags=re.I)
        if word in count:
             count[word]+=1
        else:
            count[word]=1
sor=sorted(count.items(),key=lambda x:x[1],reverse=True)
print(sor[:10])
# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats
import statistics
import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("CAT_API_KEY")
headers = {
    "x-api-key": api_key
}
response = requests.get(
    "https://api.thecatapi.com/v1/breeds",
    headers=headers
)
data = response.json()
print(type(data))
print(len(data))
print(data[0]['weight'])
weights = []
for breed in data:
    weigh = breed['weight']['metric']
    if '-' in weigh:
        parts = weigh.split('-')
        minimum = (float(parts[0].strip()))
        maximum = (float(parts[1].strip()))
        median = (minimum + maximum) / 2
        weights.append(median)
print('min:', min(weights))
print('max:', max(weights))
print('mean:', statistics.mean(weights))
print('mid:', statistics.median(weights))
print('stddev:', statistics.stdev(weights))
# 2
lifespans = []
for breed in data:
    life = breed['life_span']
    if '-' in life:
        parts = life.split('-')
        minimum = float(parts[0].strip())
        maximum = float(parts[1].strip())
        midpoint = (minimum + maximum) / 2
        lifespans.append(midpoint)
print('Minimum lifespan:', min(lifespans))
print('Maximum lifespan:', max(lifespans))
print('Mean lifespan:', statistics.mean(lifespans))
print('Median lifespan:', statistics.median(lifespans))
print('Standard deviation:', statistics.stdev(lifespans))
# 3
coun ={}
for breed in data:
    country=breed['origin']
    if country in coun:
        coun[country]+=1
    else:
        coun[country]=1
sor=sorted(count.items(),key=lambda x:x[1],reverse=True)
for country,frequency in sor:
    print(country,frequency)
# Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
import requests
url = 'https://api.restcountries.com/countries/v5?limit=100'
headers = {
    'Authorization': 'Bearer rc_live_7415e8a6fb4c40b5b2756c76dbe71960'
}
response = requests.get(url, headers=headers)
print(response.status_code)
result = response.json()
data = result['data']['objects']
print(len(data))
print(type(data))
print(data)
countryies = []
for count in data:
    countryies.append({
        'country': count['names']['common'],
        'population': count['population']
    })
sor = sorted(countryies, key=lambda x: x['population'], reverse=True)
print(sor[:10])
count={}
for country in data:
  for language in country['languages']:
      lang=language['name']
      if lang in count:
          count[lang]+=1
      else:
         count[lang]=1
sor=sorted(count.items(), key=lambda x: x[1], reverse=True)
print(sor[:10])
print(len(count))
# UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response=requests.get(url)
print(response.status_code)
print(response.url)
soup=BeautifulSoup(response.text,'html.parser')
print(soup.title.text)