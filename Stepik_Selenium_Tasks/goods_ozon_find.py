from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Готовим драйвер к работе 
browser = webdriver.Chrome()
url = 'https://google.com'


try:
    #Находим поисковое окно для ввода запроса
    browser.get(url)
    #search = browser.find_element_by_tag_name('input')
    search = browser.find_element_by_css_selector('input.gsfi')
    sleep(1)
    #Вводим свой запрос
    for i in 'ozon.ru':
        search.send_keys(i)
        sleep(0.5)
    #search.send_keys('ozon.ru')
    search.send_keys(Keys.RETURN)
    #Находим первую ссылку на сайт озона
    browser.find_element_by_partial_link_text('OZON').click()
    sleep(2)
    
    #Ждем когда появятся кнопки "Добавить в корзину"
    wait = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[type='addToCartButton']")))
    
    for i in range(1,3):
        browser.find_element_by_css_selector(
            f"div.a1p4.a3j0.a1p6:nth-child({i}) div[type='addToCartButton'] button").click()
        sleep(0.8)
        
    browser.find_element_by_css_selector("a[href='/cart']").click()
    
    
    WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".container:nth-child(3) .a7m4")))
    
    goods = browser.find_elements_by_css_selector('.container:nth-child(3) .a7m4')
    
    assert len(goods) == 2, 'Количество выбранных отличается от 2'
    
except Exception as error:
    print(f'Произошла ошибка, вот её трайсбэк: {error} ')
    
finally:
    sleep(5)
    browser.close()
    browser.quit()


