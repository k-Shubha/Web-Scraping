# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:25:09 2019

@author: SiriRamana
"""
import time
import csv 
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

chrome_path = r"C:\Users\SiriRamana\Downloads\chromedriver_win32\chromedriver.exe"
df = pd.read_csv(r"C:\temp\cTAKES_HOME\cTAKES_HOME\apache-ctakes-4.0.0\Output\notes_out\management of sore throat.csv")
saved_column = df.preferred_text
data = saved_column.values
length = len(data)



def myFun(elements):
    for x in range(0,len(elements)):
        if elements[x].is_displayed():
            elements[x].click()
            time.sleep(3)
            if x == len(elements)-1:
                all_spans = driver.find_elements_by_xpath("//span[@class='treeLabel selectable-row']")
                for span in all_spans:
                     
                    with open('C://Users//SiriRamana//outputresult.txt', 'a') as f:
                         
                         f.write(span.text)
                         f.write("\n")
                         #writer = csv.writer(f)
                         #writer.writerows(temp)
                         time.sleep(5)
                         
                         
             
                        
            

driver = webdriver.Chrome(chrome_path)
driver.get("https://browser.ihtsdotools.org/?perspective=full&conceptId1=247441003&edition=en-edition&release=v20190131&server=https://prod-browser-exten.ihtsdotools.org/api/snomed&langRefset=900000000000509007")
time.sleep(10)
driver.find_element_by_xpath("//*[@id='accept-license-button-modal']").click()
  
time.sleep(5)
    
for i in range(0,length):
    with open('C://Users//SiriRamana//outputresult.txt', 'a') as f:
        f.write("\n")
        f.write(data[i])
        f.write("\n")
        f.write("--------------")
        f.close()
    driver.find_element_by_id("fh-search_canvas-searchBox").send_keys(data[i])
    driver.find_element_by_id("fh-search_canvas-searchBox").send_keys(Keys.ENTER)
    time.sleep(10)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='fh-search_canvas-resultsTable']/tr/td/span")))
        with open('C://Users//SiriRamana//outputresult.txt', 'a') as f:
                f.write("\n")
                f.write(data[i] + " has no results\n" )
                
                driver.find_element_by_id("fh-search_canvas-searchBox").clear()
    except TimeoutException :

            driver.find_element_by_xpath("//*[@id='fh-search_canvas-resultsTable']/tr[1]/td[1]/div/a").click()
        
            time.sleep(3)
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='fh-cd1_canvas-showChildren']/span"))).click()
            except TimeoutException as ex:
                with open('C://Users//SiriRamana//outputresult.txt', 'a') as f:
                    f.write("\n")
                    f.write("Element not found" + str(ex))
                    
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='home-children-fh-cd1_canvas-body']/span")))
                with open('C://Users//SiriRamana//outputresult.txt', 'a') as f:
                    f.write("\n")
                    f.write(data[i] + " has no children\n")
                    
                    driver.find_element_by_id("fh-search_canvas-searchBox").clear()
            except TimeoutException :
    
                    elements = driver.find_elements_by_css_selector('.glyphicon.treeButton.glyphicon-chevron-right')
                    with open('C://Users//SiriRamana//outputresult.txt', 'a') as f:
                        f.write("\n")
                        f.write(data[i] + "synomyms\n")
                        f.write("------------")
                    myFun(elements)
                    driver.find_element_by_id("fh-search_canvas-searchBox").clear()

            
            
            
                
                

         
                
                    
                    
            
           
            
                            
            
            
                 
                 
                 
                 
                 
     
    

    
    
        
        
            

    
  
    
    