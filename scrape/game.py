from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


driver = webdriver.Edge()
driver.maximize_window()
links = ['https://sourceforge.net/directory/database/','https://sourceforge.net/directory/text-editors/',
        'https://sourceforge.net/directory/education/','https://sourceforge.net/directory/games-entertainment/',
        'https://sourceforge.net/directory/mobile/','https://sourceforge.net/directory/office-business/','https://sourceforge.net/directory/printing/',
        'https://sourceforge.net/directory/religion-and-philosophy/','https://sourceforge.net/directory/security/',
        'https://sourceforge.net/directory/software-development/','https://sourceforge.net/directory/terminals/',
        'https://sourceforge.net/directory/communications/','https://sourceforge.net/directory/desktop-environment/',
        'https://sourceforge.net/directory/formats-and-protocols/','https://sourceforge.net/directory/internet/',
        'https://sourceforge.net/directory/multimedia/','https://sourceforge.net/directory/other-nonlisted-topic/',
        'https://sourceforge.net/directory/productivity/','https://sourceforge.net/directory/scientific-engineering/',
        'https://sourceforge.net/directory/social-sciences/','https://sourceforge.net/directory/system/']

soft_link=[]

for link in links:
    
    for i in range(1,35):
        try:
            print(link,i)
            driver.get(f'{link}?sort=rating&page={i}')           

            wrappers = driver.find_elements(By.CLASS_NAME,'project-oss')
            for wrapper in wrappers:
                soft_link.append(wrapper.find_element(By.CLASS_NAME,'result-heading').find_element(By.TAG_NAME,'a').get_attribute('href'))
            time.sleep(1)
        except:
            break
    

data = pd.DataFrame(soft_link,columns=['Links'])
data.to_csv('links2.csv',index=False)

driver.close()





