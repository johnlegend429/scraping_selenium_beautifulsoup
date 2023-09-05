import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.salonboutique.net/contact/')

some = []
name = []

# Load the page source into BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for span in soup.find_all(attrs={'class':'fusion-button-text'}):   
    if span not in some:
        some.append(span.string)
    
for span in soup.find_all(attrs={'class':'menu-text'}):
    if span not in name:
        name.append(span.string)    
       
print(f'{some}')
print(f'{name}')

series1 = pd.Series(some, name='Some')
series2 = pd.Series(name, name='Name')
df = pd.DataFrame({'Some' : series1, 'Name' : series2})
df.to_excel('span.xlsx', index=False)

df.to_csv('span.csv', index=False, encoding='utf-8')