from bs4 import BeautifulSoup
import matplotlib.pyplot as p
import requests
x=[]
petrol=[]
diesel=[]
url="http://www.mycarhelpline.com/index.php?option=com_latestnews&view=detail&n_id=1401&Itemid=10"
data=requests.get(url)
soup=BeautifulSoup(data.text,"html.parser")
data1=soup.find_all('table')[2]
data2=data1.find_all('td',{'class':'xl65'})[4:]
data3=data1.find_all('td',{'class':'xl66'})
j=0
for i in data2:
    s=i.get_text()
    s=s.replace('Rs','')
    if j%2 ==0:
        petrol.append(float(s))
        j+=1
    else:
        diesel.append(float(s))
        j+=1
for i in data3:
    x.append(i.get_text())
fig=p.figure()
fig.set_size_inches(20,10)
graph=fig.add_subplot(1,1,1)
graph.plot(x,petrol,label="Petrol/Litre")
graph.plot(x,diesel,label="Diesel/Litre")
p.subplots_adjust(left=0.05,right=0.98,top=0.94,bottom=0.07)
p.title("Prices of Petrol and Diesel in India for last 15 Years")
p.xlabel("month-year")
p.ylabel("price in Rs")
p.legend(title='Legend',loc='lower right')
p.savefig('Petrol and Diesel increase rate.png')


