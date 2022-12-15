from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

inputsText = "inputtext class"
inputsBox = "inputbox class"
submitbutton = "submit button class"


url = "url of form"



def answerText(driver,element_class):
    text_questions = driver.find_elements(By.CLASS_NAME, element_class)
    text_answers = ["word to say"]
    for a,q in zip(text_answers,text_questions):
        try:
            q.send_keys(a)
        except:
            print("f")
    return driver

def answerCheckBox(driver, element_class):
    checkboxes = driver.find_elements(By.CLASS_NAME, element_class)
    for q in checkboxes:
        try:
            q.click()
        except:
            print("f")
            
    return driver

def submit(driver, element_class):
    submit = driver.find_elements(By.CLASS_NAME, element_class)
    for q in submit:
        try:
            q.click()
        except:
            print("f")
    
    return driver

while True:
   
    driver.get(url)
    answerText(driver,inputsText)
    answerCheckBox(driver,inputsBox)
    submit(driver,submitbutton)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(2)
    
    
    
    


    

        
