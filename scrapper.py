import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\\usr\\chromedriver")
                 
cities = []
total_votes = []
winner_votes = []
winner_name = []
winning_party = []
temp1 = [] 
temp2 = []
temp3 = []
temp4 = []
index = []

#def max_votes(n):
#    for j in range(1,len(n),2):
#           temp2.append(n[j].text)           
#           
#    for k in range(0,len(temp2)): 
#        temp2[k] = int(temp2[k]) 
#    x = max(temp2)
#    return x


for i in range(1,81):
#    url = "http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS2480.htm?ac={}".format(i)
    url = "http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS2480.htm?ac=80"

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content) 
    
#    results = soup.findAll('th',attrs={'colspan':'9'})
#    city = (results[0].text).replace('\n','') 
#    cities.append(city.strip())
#    
#    total = soup.findAll('td',attrs={'style':'width:12%;'})
#    total_votes.append(total[3].text)

#    votes = soup.findAll('td',attrs={'style':'width:13%;'})
#    winner_votes.append(max_votes(votes))
    
    table = soup.findAll('tr',attrs={'style':'font-size:12px;'})
    for o in range(0,len(table)):
        no = table[o]
        temp3.append(no.contents[5].text)
        temp4.append(no.contents[1].text)
        
        for k in range(0,len(temp3)): 
            temp3[k] = int(temp3[k])
        x = max(temp3)
        
    for m in range(0,len(temp4)):
        if(temp3.index(max(temp3)) == m):
            winner_name.append(temp4[temp3.index(max(temp3))])
      
        
    winner_votes.append(x)

            
        
        



    
      
        

   

        

    