# Ожидание называется неявным (Implicit wait), так как его не надо явно указывать каждый раз, 
# когда мы выполняем поиск элементов, оно автоматически будет применяться при вызове каждой последующей команды.
# Улучшим наш тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep()
# и добавить одну строчку с методом implicitly wait:


#Про ошибки во время тестирования:
#Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
#Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, 
#то получим StaleElementReferenceException. Например, мы нашли элемент 
#Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. 
#Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
#Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), 
#и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.


#Примеры кода:
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#
#    browser = webdriver.Chrome()
#
#    browser.get("http://suninjuly.github.io/wait2.html")
#    
#    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#    button = WebDriverWait(browser, 5).until(
#            EC.element_to_be_clickable((By.ID, "verify"))
#        )
#    button.click()
#    message = browser.find_element_by_id("verify_message")
#    
#    assert "successful" in message.text

#from selenium import webdriver
#
#browser = webdriver.Chrome()
## говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5) #!!!!!!!!!!!!
#
#browser.get("http://suninjuly.github.io/wait1.html")
#
#button = browser.find_element_by_id("verify")
#button.click()
#message = browser.find_element_by_id("verify_message")
#
#assert "successful" in message.text
#
#browser.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    
    browser.find_element_by_css_selector("button[id='book']").click()
    
    x_element = browser.find_element_by_css_selector("label span[id='input_value']")
    x = x_element.text
    x = calc(x)
    
    browser.find_element_by_css_selector("input[id='answer']").send_keys(str(x))
   
    browser.find_element_by_xpath("//button[@id='solve'][text()='Submit']").click()
    
    number_from_alert = browser.switch_to.alert.text.split(": ")[-1]
    print(number_from_alert)
   
except Exception as error:
    print(f"Ошибка бро, вот она _ {error}")


finally:
    sleep(1)
    browser.quit()


#class CustomBrowser(webdriver.Chrome):
#
#    def solve_captcha(self):
#        value_x = int(self.find_element_by_id("input_value").text)
#        value_x = math.log(abs(12*math.sin(value_x)))
#        field_input = self.find_element_by_id("answer").send_keys(str(value_x))