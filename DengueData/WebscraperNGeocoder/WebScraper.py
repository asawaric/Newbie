import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Request a link.
wiki = Request("http://www.dengue.gov.sg/subject.asp?id=74", headers = {"User-Agent": "Chrome/53.0.2785.116"})
page = urlopen(wiki).read()                 # Read a link webpage.

# Extract webpage info using lxml parser.
soup = BeautifulSoup(page, 'lxml')
soup.prettify()                          # Neatly arrange the file content.

#Find all the table tags in html file.
all_tables=soup.findAll('table')
right_table=soup.find('table', class_='MsoNormalTable')    # Find the table to parse by specifying class.

data = {
         'Location' : [],
          'cases' : []
       }

# Find table tags in right_table.
rows = right_table.findAll("table")

# Find the rows of table:
for row in rows:
    cells = row.findAll('tr')[1:]         # Omit the 1st row of each table.
    for i in cells:
        cols = i.findAll('td')            # Find the table data cell.
        data['Location'].append( cols[0].get_text().strip() )    # append cell content to the corresponding value list. 
        data['Location'] = [item.replace("\r\n", "") for item in data['Location']]
        data['cases'].append( cols[1].get_text().strip() )
        
    DengueData = pd.DataFrame( data )
    DengueData.loc[:,'Date'] = [datetime.date.today()] * len(DengueData)  
    DengueData.to_csv("DC20170223.csv", index=False) 
f = open('DengueClusters.csv', 'a')
DengueData.to_csv(f, header=False, index=False)
            
DengueData
