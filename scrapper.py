import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\\usr\\chromedriver")
                 
cities = []
total_votes = []
winner_votes = []
winner_name = []
winning_party = []
winner_vote_per = []
EVM_voting = []
postal_voting = []

temp1 = [] 
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []

#def max_votes(n):
#    for j in range(1,len(n),2):
#           temp2.append(n[j].text)           
#           
#    for k in range(0,len(temp2)): 
#        temp2[k] = int(temp2[k]) 
#    x = max(temp2)
#    return x


for i in range(1,81):
    url = "http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS2480.htm?ac={}".format(i)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content) 
    
    results = soup.findAll('th',attrs={'colspan':'9'})
    city = (results[0].text).replace('\n','') 
    cities.append(city.strip())
    
    total = soup.findAll('td',attrs={'style':'width:12%;'})
    total_votes.append(total[3].text)
    
    total_evm = soup.findAll('td',attrs={'style':'width:12%;'})
    EVM_voting.append(total[1].text)
    
    total_postal = soup.findAll('td',attrs={'style':'width:12%;'})
    postal_voting.append(total[2].text)

#    votes = soup.findAll('td',attrs={'style':'width:13%;'})
#    winner_votes.append(max_votes(votes))
    
    table = soup.findAll('tr',attrs={'style':'font-size:12px;'})
    
    for o in range(0,len(table)):
        no = table[o]
        temp3.append(no.contents[5].text)
        temp4.append(no.contents[1].text)
        temp5.append(no.contents[2].text)
        temp6.append(no.contents[6].text)
        
        for k in range(0,len(temp3)): 
            temp3[k] = int(temp3[k]) 
            
        for z in range(0,len(temp6)): 
            temp6[z] = float(temp6[z])  
            
        x = max(temp3)
    winner_votes.append(x)  
    
    for m in range(0,len(temp4)):
        if(temp3.index(max(temp3)) == m):
            winner_name.append(temp4[temp3.index(max(temp3))])
            
    for n in range(0,len(temp5)):
        if(temp3.index(max(temp3)) == n):
            winning_party.append(temp5[temp3.index(max(temp3))]) 
                       
    for p in range(0,len(temp6)):
        if(temp3.index(max(temp3)) == p):
            winner_vote_per.append(temp6[temp3.index(max(temp3))])
    
#for s in range(0,len(EVM_voting)): 
#            EVM_voting[s] = int(EVM_voting[s])
#            
#for t in range(0,len(postal_voting)): 
#        postal_voting[t] = int(postal_voting[t])
#        
#for u in range(0,len(total_votes)): 
#        total_votes[u] = int(total_votes[u]) 
#        
##for w in range(0,len(total_)): 
##        total_[w] = int(total_[w])  
##        
##for s in range(0,len(avg)): 
##        avg[s] = float(avg[s])            
##       
###for b in range(0,len(postal_voting)):
###    total_ = postal_voting[b] + EVM_voting[b]
###    avg = (total_/total_votes[b])*100
###voting_per.append(avg)        
###    

dataset = pd.DataFrame({'District': cities, 'Total votes': total_votes, 'EVM votes': EVM_voting, 'Postal votes': postal_voting,'Winner': winner_name ,'votes of winner': winner_votes ,'Winner votes %':winner_vote_per ,'winning party': winning_party })            
dataset.to_csv('UP_2019.csv' 'Data.csv',index=False,encoding='utf-8')       
        



    
      
        

   

        

    