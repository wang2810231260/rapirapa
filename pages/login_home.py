from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger
from selenium.webdriver.common.by import By
class LoginHomePage(BasePage):
    # 申请按钮
    def application(self):
        OK_BUTTON = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@text='OK']")
                                           ))
        if OK_BUTTON:
            self.click(OK_BUTTON)
            APPLICATION_BUTTON = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Aplicar']")
                                               ))
            self.click(APPLICATION_BUTTON)
            logger.info("点击申请按钮成功")
        else:
            APPLICATION_BUTTON = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Aplicar']")
                                               ))
            self.click(APPLICATION_BUTTON)
            logger.info("点击申请按钮成功")


