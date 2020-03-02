import requests
from requests_html import HTMLSession
import csv
session=HTMLSession()
r=session.get('https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs')
listerList=r.html.find('.list')
Title=listerList.find('.list_item h4 a')
Time=listerList.find('time')
Genre=listerList.find('.cert-runtime-genre span')
image=listerlist.find('.image img poster shadowed')
print(image.attrs['src'])
#for x in range(0,7):
#    print(Title[x].text)
#    print(Time[x].text)
#    print(Genre[x].text,end=" ")
 