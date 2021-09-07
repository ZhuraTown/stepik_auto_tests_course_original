from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_css_selector(".nowrap[id='num1']")
    x = int(x.text)
    
    y = browser.find_element_by_css_selector(".nowrap[id='num2']")
    y = int(y.text)
    
    sleep(2)
    
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(x+y))
    sleep(1)
    
    browser.find_element_by_xpath("//button[text()='Submit'][@type='submit']").click()
    
except Exception as error:
    print(f"Произошла ошибка, обрати внимание: {error}")


finally:
    sleep(5)
    browser.close()
    browser.quit()


