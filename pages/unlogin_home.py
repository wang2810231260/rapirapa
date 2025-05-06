from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.logger import logger


class HomePage(BasePage):

    LOGIN_BUTTON=BasePage.by_accessibility_id("Iniciar sesión")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        logger.info("----未登录首页按钮点击成功！------")