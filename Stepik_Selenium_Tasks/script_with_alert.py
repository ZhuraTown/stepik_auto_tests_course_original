#Работа со всплывающими окнами
#
#Код, для нажатия кнопки ОК во всплывающем окне
#
#alert = browser.switch_to.alert
#alert.accept()
#
#Чтобы получить текст из alert, используйте свойство text объекта alert:
#
#alert = browser.switch_to.alert
#alert_text = alert.text
#
#Для работы с окнмо где можно выбрать согласен или нет используй код:
#
#confirm = browser.switch_to.alert
#confirm.accept() #Согласится со всплывающим окном
#confirm.dismiss() # Кнопка нет на всплывающем окне
#
#
#Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():
#
#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()
#Для переключенйи между вкладками можно используй switch_to.window
#browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
#
#new_window = browser.window_handles[1]
#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
#
#first_window = browser.window_handles[0]

#from selenium import webdriver
#from time import sleep
#import math
#
#link = 'http://suninjuly.github.io/alert_accept.html'
#
#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    
#    #Находим волшебную кнопку
#    browser.find_element_by_xpath("//button [text()='I want to go on a magical journey!']").click()
#    
#    alert = browser.switch_to.alert
#    alert.accept()
#    sleep(0.5)
#    x = browser.find_element_by_css_selector("span[id='input_value']")
#    x = calc(x.text)
#
#    #Вводим наш ответ
#    browser.find_element_by_css_selector("input[name='text'][id='answer']").send_keys(x)
#    sleep(0.5)
#    #Жмякаем на кнопку отправки Submit
#    browser.find_element_by_xpath("//button[text()='Submit']").click()
#    sleep(0.5)
#    #Напечатаем значение из всплывающего окна сюда
#
#    number_from_alert = browser.switch_to.alert.text.split(': ')[-1]
#    print(number_from_alert)
#    browser.switch_to.alert.accept()
#
#except Exception as error:
#    print(f'Произошла ошибка : {error}')
#    
#
#finally:
#    sleep(5)
#    browser.quit()


from selenium import webdriver
from time import sleep
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Находим волшебную кнопку
    browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']").click()
    
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    
    browser.switch_to.window(new_window)
    
    x = browser.find_element_by_css_selector("span[id='input_value']")
    x = calc(x.text)

    #Вводим наш ответ
    browser.find_element_by_css_selector("input[name='text'][id='answer']").send_keys(x)
    sleep(0.5)
    #Жмякаем на кнопку отправки Submit
    browser.find_element_by_xpath("//button[text()='Submit']").click()
    sleep(0.5)
    #Напечатаем значение из всплывающего окна сюда

    number_from_alert = browser.switch_to.alert.text.split(': ')[-1]
    print(number_from_alert)
    browser.switch_to.alert.accept()

except Exception as error:
    print(f'Произошла ошибка : {error}')
    

finally:
    sleep(2)
    browser.quit()