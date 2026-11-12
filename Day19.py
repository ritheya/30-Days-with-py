# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# Read obama_speech.txt file and count number of lines and words
# Read michelle_obama_speech.txt file and count number of lines and words
# Read donald_speech.txt file and count number of lines and words
# Read melina_trump_speech.txt file and count number of lines and words
with open('./Datas/obama_speech.txt') as f:
 reading=f.read().splitlines()
 count=0
 for row in reading:
  count+=1
print("no of lines:",count)
coun=0
for word in reading:
    words=len(word.split())
    coun+=words
print("No of words:",coun)

with open('./Datas/milena_trump.txt') as f:
  read1=f.read().splitlines()
  counting=0
  for row in read1:
    counting+=1
print(counting)
counts=0
for wordi in read1:
  wording=len(wordi.split())
  counts+=wording
print(counts)
# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 10))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic'),
# (24, 'Spanish'),
# (9, 'Russian'),
# (9, 'Portuguese'),
# (8, 'Dutch'),
# (7, 'German'),
# (5, 'Chinese'),
# (4, 'Swahili'),
# (4, 'Serbian')]
# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]
import json
def most_spoken_language(f,num):
  with open(f) as f:
   reading=json.load(f)
  lang_count={}
  for lang in reading:
    for languages in lang['languages']:
      if languages in lang:
       lang_count[languages]+=1
      else:
        lang_count[languages]=1
  sorted_count=sorted(lang_count.items(),key=lambda x:x[1],reverse=True)
  result=sorted_count[:num]
  return result
print(most_spoken_language('./Datas/countries_data.json',10))
print(most_spoken_language('./Datas/countries_data.json',3))
  # Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
 # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10)
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]
# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]
import json
def most_populated_countries(f,num):
  with open(f) as f:
   reading=json.load(f)
  count_num=[]
  for country in reading:
     count_num.append({'country':country['name'],'population':country['population']})
  sorted_count=sorted(count_num,key=lambda x:x['population'],reverse=True)
  result=sorted_count[:num]
  return result
print(most_populated_countries('./Datas/countries_data.json',10))
# Exercises: Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
with open('./Datas/email_exchange_big.txt') as f:
  read_words=f.read()
  read_ex=r'From \s*([\w.-]+@[\w.-]+)'
  result=re.findall(read_ex,read_words,re.I)
  print(len(result))
  print(set(result))
# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
def  find_most_common_words(f,num):
  with open(f) as f:
   read=f.read().splitlines()
   count={}
   for lines in read:
      words=lines.split()
      for word in words:
       if word in count:
        count[word]+=1
       else:
        count[word]=1
  sor=sorted(count.items(),key=lambda x:x[1],reverse=True)
  result=[(frequency,word) for word,frequency in sor[:num]]
  return result
print(find_most_common_words('./Datas/sample.txt',10))
# Use the function, find_most_frequent_words to find:
# The ten most frequent words used in Obama's speech
# The ten most frequent words used in Michelle's speech
# The ten most frequent words used in Trump's speech
# The ten most frequent words used in Melina's speech
def find_most_frequent_words(f,num):
 with open(f) as f:
  reading=f.read().lower().split()
  count={}
  for word in reading:
    if word in count:
      count[word]+=1
    else:
      count[word]=1
  so=sorted(count.items(),key= lambda x:x[1],reverse=True)
  result=[(word,frequency) for word, frequency in so[:num]]
  return result
print(find_most_frequent_words('./Datas/obama_speech.txt',10))
# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
with open('./Datas/michelle_obama_speech.txt') as e:
 readsea1=e.read()
with open('./Datas/milena_trump.txt') as m:
  readsea2=m.read()
def clean_text(file):
  reg_ex=r'[^a-zA-Z0-9]'
  match=re.sub(reg_ex,' ',file)
  return match
from Datas.stop_words import stop_words
def remove_support(text,stop_words):
  words=[]
  for word in text.split():
     if word not in stop_words:
      words.append(word)
  return words
def comparison(a1,a2):
  set1=set(a1)
  set2=set(a2)
  common=set1.intersection(set2)
  total=set1.union(set2)
  if len(total)==0:
    return 0
  similarity=(len(common)/len(total))*100
  return similarity
clean1=clean_text(readsea1)
clean2=clean_text(readsea2)
proce1=remove_support(clean1,stop_words)
proce2=remove_support(clean2,stop_words)
result=comparison(proce1,proce2)
print("Michelle's speech words:", len(proce1))
print("Melina's speech words:", len(proce2))
print("Similarity:", round(result, 2), "%")
# Find the 10 most repeated words in the romeo_and_juliet.txt
with open('./Datas/romeo_juliet.txt') as r:
  rea=r.read().splitlines()
  count={}
  for lines in rea:
    words=lines.split()
    for word in words:
      word = re.sub(r'[^a-zA-Z]', '', word).lower()
      if word in count:
        count[word]+=1
      else:
        count[word]=1
  sor=sorted(count.items(),key=lambda x:x[1],reverse=True)
  print(sor[:10])
# Read the hacker news csv file and find out:
# Count the number of lines containing python or Python

import csv
with open('./Datas/hacker_news.csv','r',newline='',encoding='utf-8') as h:
  reader=csv.reader(h)
  count=0
  reg_ex=r'\bpython\b'
  for row in reader:
   line=' '.join(row)
   match=re.search(reg_ex,line,re.I)
   if match:
    count+=1
print(count)
# Count the number lines containing JavaScript, javascript or Javascript
import csv
with open('./Datas/hacker_news.csv','r',newline='',encoding='utf-8') as h:
  reader=csv.reader(h)
  count=0
  reg_ex=r'\bjavascript\b'
  for row in reader:
   line=' '.join(row)
   match=re.search(reg_ex,line,re.I)
   if match:
    count+=1
print(count)
 #Count the number lines containing Java and not JavaScript
import csv
import re
with open('./Datas/hacker_news.csv', 'r', newline='', encoding='utf-8') as h:
    reader = csv.reader(h)
    count = 0
    java = r'\bJava\b'
    javascript = r'\bJavaScript\b'
    for row in reader:
        line = ' '.join(row)
        if re.search(java, line, re.I) and not re.search(javascript, line, re.I):
            count += 1

print(count)
