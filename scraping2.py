import requests 
from bs4 import BeautifulSoup 
import re 
import mysql.connector
from collections import OrderedDict
from sklearn import tree
Meters=[]
Types=[]
Rooms=[]
prices=[]
basic_info = []
cnx = mysql.connector.connect(user='',password='',
                              host='',
                              database='')


url = 'https://www.propertyfinder.ae/en/buy/dubai/properties-for-sale.html'
for i in range (1,10):
    query = {'page': i} 
    urllink = requests.get(url, params=query) 
    soup =BeautifulSoup(urllink.text, 'html.parser')
    Type=soup.find_all('p',attrs={'class':'card__property-amenity card__property-amenity--property-type'})
    for item in Type:
        key=(re.sub('\s+' , ' ' , item.text).strip())
        if re.search(r'^[A-Z][a-z]*$', key )!=None:
            Types.append(key)
        else:
            Types.append('None')
    Room=soup.find_all('p',attrs={'class':'card__property-amenity card__property-amenity--bedrooms'})
    for item in Room:
        key=re.sub('\s+' , ' ' , item.text).strip()
        if re.search(r'^[0-9]*$', key )!=None:
            Rooms.append(key)
        else:
            Rooms.append('None')
    meter=soup.find_all('p',attrs={'class':'card__property-amenity card__property-amenity--area'})
    for item in meter:
        key=re.sub('\s+' , ' ' , item.text).strip()
        if re.search(r'^[0-9,]+[\s/a-z]+$', key )!=None:
            Meters.append(key)
        else:
            Meters.append('None')
    price=soup.find_all('span',attrs={'class':'card__price-value'})
    for item in price:
        key=re.sub('\s+' , ' ' , item.text).strip()
        if re.search(r'^[0-9,]*$', key )!=None:
            prices.append(key)
        else:
            prices.append('None')

cursor= cnx.cursor()
mycursor.execute"CREATE TABLE   (Modo VARCHAR(300), Rooms varchar(300) , Meter varchar (300) , Price varchar(300))"
sql = 'INSERT INTO  ( Modo, Rooms , Meter , Price ) VALUES (%s, %s , %s , %s)'
for x,y,z,h in zip(Types,Rooms,Meters,prices):
    if x!='None' and y!='None' and z!='None' and h!='None':
        cursor.execute ( sql, (x , y , z, h) )
        cnx.commit()

cnx.close()