from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from script import SCRIPT_DARG_AND_DROP

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_element_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator):
        """Ожидать, что элемент станет невидимым"""
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    def is_element_visible(self, locator):
        """Проверить, виден ли элемент на странице (возвращает True/False)"""
        try:
            self.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False
    
    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        """Найти все элементы с ожиданием видимости первого из них"""
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        """Клик по элементу через ActionChains"""
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    def text_input_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)
    
    def wait_for_url_contains(self, text):
        """Ожидать, что URL содержит текст"""
        self.wait.until(EC.url_contains(text))

    def drag_and_drop_element(self, locator_from, locator_to):
        elem_from = self.find_element_with_wait(locator_from)
        elem_to = self.find_element_with_wait(locator_to)

        if self.driver.capabilities.get("browserName") == "firefox":
            self.driver.execute_script(SCRIPT_DARG_AND_DROP, elem_from, elem_to)
        else:
            actions = ActionChains(self.driver)
            actions.click_and_hold(elem_from).move_to_element(elem_to).pause(0.5).release().perform()
    


    

    