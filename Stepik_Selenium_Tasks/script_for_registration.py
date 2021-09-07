from selenium import webdriver
from time import sleep

#link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    information = ['Vladislav','Zhuravskiy', 'Stalner@yandex.ru']
    #Код заполнения формы регистрации
    set_1 = browser.find_element_by_css_selector('.first_block input.first')
    set_1.send_keys(information[0])
    
    set_2 = browser.find_element_by_css_selector('.first_block input.second')
    set_2.send_keys(information[1])
    
    set_3 = browser.find_element_by_css_selector('.first_block input.third')
    set_3.send_keys(information[2])
    #Ждем 2 секунды после чего нажимаем кнопку
    sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(1)
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = browser.find_element_by_tag_name("h1").text
    
    assert "Congratulations! You have successfully registered!" == welcome_text

#Вывод ошибки во время тестирования, с этой структурой не выводит ошибку NoSuchElementException, просто пишет что неверный селектор
#except Exception as error:
#    print(f'Обрати внимание! Произошла ошибка во время тестирования!Ошибка: {error}')


finally:
    sleep(10)
    browser.close()
    browser.quit()