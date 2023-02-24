from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import os


driver = webdriver.Edge()
driver.maximize_window()

links = pd.read_csv('links2.csv')
print(len(links))


links = links['Links'].values.tolist()

data = []

i = 1
for link in links:
    print(i)
    i += 1
    try:
        driver.get(link)
        try:
            description = driver.find_element(By.CLASS_NAME,'description').text
            
        except:
            description = ''
        try:
            des = driver.find_element(By.XPATH,'//div[contains(@class,"small-12 columns")]').text
        except:
            des =''
        try:
            
            categories = driver.find_element(By.XPATH,"//div[ contains(@class,'small-12 medium-5 columns')]").text
        except:
            categories = None
        
        data.append([description+des,categories])
        
        time.sleep(1)
        if i%100 == 0:
            data = pd.DataFrame(data,columns=['Description','Category'])

            data.to_csv(f'appdata{i}.csv',index = False)
            
            data = []

    except:
        continue
    
driver.close()

df =[]

li = os.getcwd()
for files in os.listdir(li): 
    if files.find('appdata')>-1:
        data = pd.read_csv(files)
        df.append(data)
        
df = pd.concat(df)
df.to_csv('final_data.csv',index=False)
