import requests 
from bs4 import BeautifulSoup 
import re 
import mysql.connector
from collections import OrderedDict
from sklearn import tree
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
cnx = mysql.connector.connect(user='',password='',
                              host='',
                              database='')


Getting=[]
Gettingcode=[]
result=[]
cursor= cnx.cursor()
query = 'SELECT * FROM '
cursor.execute (query)
le = preprocessing.LabelEncoder()
for row in cursor :
    Getting.append(row[0:3])
    result.append(row[3])
for item in Getting:
    le.fit(item)
    newitem=le.transform(item)
    Gettingcode.append(newitem)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(Gettingcode,result)
Type=input('Write one of these type (Apartment, Villa , Townhouse , Duplex , Penthouse): ')
Rooms=input('Write number of Rooms: ')
Meter=input('Write area of the house: ')
newdata=(Type, Rooms, Meter+' / sqft')
le.fit(newdata)
newda=le.transform(newdata)
answer=clf.predict([newda])
print('Price for these customs is: ', answer)
