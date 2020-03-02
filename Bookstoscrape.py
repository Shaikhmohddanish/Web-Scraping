from bs4 import BeautifulSoup
import requests
import csv
header=['Title','Price','Poster']
data=open('BooksDetail.csv','w')
writer=csv.writer(data)
writer.writerow(header)
#source=HTMLSession()
for i in range(0,51):
    url='http://books.toscrape.com/catalogue/page-{}.html'.format(i)
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'lxml')
    #print(soup.prettify())
    books=soup.find_all('article',class_="product_pod")
 
    for book in books:
        title=book.h3.a.attrs['title']
        price=book.find('div',class_="product_price")
        image=book.find('div',class_="image_container")
        a='http://books.toscrap.com/{}'.format(image)
        print(title,price.p.text,image.a.img.attrs['src'])
        li=[title,price.p.text,image.a.img.attrs['src']]
        writer.writerow(li)