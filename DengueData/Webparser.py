import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

link = Request("http://www.dengue.gov.sg/subject.asp?id=74", headers = {"User-Agent": "Chrome/53.0.2785.116"})
page = urlopen(link).read()

soup = BeautifulSoup(page, 'lxml')
soup.prettify()

all_tables=soup.find_all('table')
right_table=soup.find('table', class_='MsoNormalTable')

#print (right_table)
A = []
Locality = []
casesnew = []
casesold = []
location = []
cases = []
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    subcells = row.findAll('p')
    if len(cells)== 3:
        A.append(cells[0].find(text=True))
        Locality.append(cells[1].find(text=True))
        casesnew.append(cells[2].find(text=True))
        casesold.append(cells[3].find(text=True))
        if len(subcells)==1:
            location.append(subcells[0].find(text=True))
            cases.append(subcells[1].find(text=True))

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['Locality']=Locality
df['casesnew']=casesnew
df['casesold']=casesold
df['location']=location
df['No. of cases']=cases

print(df)

 
