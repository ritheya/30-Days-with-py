# Read the hacker_news.csv file from data directory
import pandas as pd
news=pd.read_csv('Datas/hacker_news.csv')
# Get the first five rows
print(news.head())
# Get the last five rows
print(news.tail())
# Get the title column as pandas series
print(news.columns)
tit_col=pd.Series(news['title'])
print(tit_col)
# Count the number of rows and columns
print(news.shape)
# Filter the titles which contain python
print(news[news['title'].str.contains('python',case=False,na=False)]['title'])
# Filter the titles which contain JavaScript
print(news[news['title'].str.contains('javascript',case=False,na=False)]['title'])
# Explore the data and make sense of it
import pandas as pd 
re=pd.read_csv("Datas/weight_height.csv")
print(re.columns)
def cal_bmi():
    weight=re['Weight']
    height=re['Height']
    bmi=[]
    for w,h in zip(weight,height):
        b=w/(h**2)
        bmi.append(b)
    return bmi
bmi=cal_bmi()
re['BMI']=bmi
re['BMI']=round(re['BMI'],3)
print(re)
re.to_csv('Datas/weight_height.csv')
