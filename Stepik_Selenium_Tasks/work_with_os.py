#import os
#
#current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
#
#file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла 
# 
#print(current_dir)
#
#print(file_path)
import os
from selenium import webdriver
from time import sleep


link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Находим путь к нашему файлу file.txt
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    info = ['Vlad', "Ivanov", 'dog@mail.ru',file_path]
    css_selectors = ["input[name='firstname']","input[name='lastname']","input[name='email']","input[type='file'][id='file']"]
    
    i = 0
    for selector in css_selectors:
        browser.find_element_by_css_selector(selector).send_keys(info[i])
        i += 1
        
    #Ищем кнопку и жмём отправить
    browser.find_element_by_xpath("//button[text()='Submit']").click()


except Exception as error:
    print(f"В ходе тестирования произошла ошибка {error}")
    
finally:
    sleep(6)
    browser.quit()
    
    