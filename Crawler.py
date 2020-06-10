import urllib.request,urllib.error,urllib.parse
from xlwt import Workbook 
from bs4 import BeautifulSoup
from datetime import datetime
url=input("Enter site to get links\n")
links=[]
while(len(url)==0):
    url=input("Enter site to get links\n")
try:
    html_data=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html_data,'html.parser')
    tags=soup('a')
    for tag in tags:
            if tag.has_attr('href'):
                links.append(tag['href'])
except:
    print("Please check the URL properly")
if(len(links)==0):
    print("No links to fetch")
else:
    wb=Workbook()
    sheet1 = wb.add_sheet('Links')
    for i in range(0,len(links)):
        sheet1.write(i,0,links[i])
    data_time=datetime.now()
    current_time = str(data_time.strftime("%H-%M-%S"))
    wb.save('links for '+current_time+'.xls')
    print("Done writing data to excel sheet")
# 