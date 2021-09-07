from selenium import webdriver
from time import sleep
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
#Для задачи https://stepik.org/lesson/165493/step/5?unit=140087
#link = 'http://suninjuly.github.io/math.html'
#Для задачи https://stepik.org/lesson/165493/step/7?unit=140087
#link = 'http://suninjuly.github.io/get_attribute.html' 
link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Ищем значение X
    #Для 1-ой задачи
    x_element = browser.find_element_by_css_selector("label span[id='input_value']")
    #Для 2-ой задачи
    #x_element = x_element.get_attribute("valuex")
    #Для 1-ой задачи
    x = x_element.text 
    #Решаем задачу
    x = calc(x)
    browser.find_element_by_css_selector("input[id='answer']").send_keys(str(x))
    #Ищем и добавляем в окно ввода новое значение
    #find_answer = browser.find_element_by_css_selector(".form-group input[id='answer']")
    #find_answer.send_keys(str(y))
    sleep(1)
    
    ##Жмякаем на кнопу I am the robot
    #browser.find_element_by_css_selector("[id='robotCheckbox']").click()
    #
    ##Жмякаем на Robots rule
    #browser.find_element_by_xpath("//input[contains(@id,'robotsRule')]").click()
    ## //input[contains(@id,'robotsRule')] для XPATH
    #sleep(0.5)
    ##Жмякаем на кнопку Submit
    #browser.find_element_by_xpath("//button[text()='Submit']").click()
    list_1 = [browser.find_element_by_css_selector("[id='robotCheckbox']"),
    browser.find_element_by_xpath("//input[contains(@id,'robotsRule')]"),
    browser.find_element_by_xpath("//button[text()='Submit']")
    ]
    
    for command in list_1:
        browser.execute_script("return arguments[0].scrollIntoView(true);", command)
        command.click()
    
        
    
    
except Exception as error:
    print(f'Появилась ошибка, вот инфа: {error}')


finally:

    sleep(10)
    browser.quit()