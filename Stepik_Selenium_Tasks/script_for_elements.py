from selenium import webdriver
import time

url = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys('My answer')
        
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

except Exception as error:
     print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(20)
    
    browser.close()
    browser.quit()
    