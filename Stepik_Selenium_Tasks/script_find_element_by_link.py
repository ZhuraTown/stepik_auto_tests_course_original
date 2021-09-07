import time
import math

from selenium import webdriver

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    links = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    links.click()
    
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Vladislav")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Zhuravskiy")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Saint-Peterburg")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
except Exception as error:
     print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    

finally:
    time.sleep(30)
    browser.quit()

#Пустая строка чтобы скрипт работал в окне