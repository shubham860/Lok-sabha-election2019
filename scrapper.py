import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\\usr\\chromedriver")

def max_votes(n):
    for j in range(1,len(n),2):
           temp2.append(n[j].text)

cities = []
total_votes = []
winner_votes = []
temp1 = [] 
temp2 = []


for i in range(1,81):
    url = "http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS241.htm?ac={}".format(i)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content) 
    
    results = soup.findAll('th',attrs={'colspan':'9'})
    city = (results[0].text).replace('\n','') 
    cities.append(city.strip())
    
    total = soup.findAll('td',attrs={'style':'width:12%;'})
    total_votes.append(total[3].text)

    votes = soup.findAll('td',attrs={'style':'width:13%;'})
    max_votes(votes)
    
    
    
      
        

   

        

    