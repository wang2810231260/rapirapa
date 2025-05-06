from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.logger import logger
import random


class LoginPage(BasePage):
    PHONE_INPUT = BasePage.by_xpath( "//*[@text='Número telefónico']")
    CODE_INPUT = BasePage.by_xpath( "//*[@text='Código de verificación']")
    SUBMIT_BUTTON = BasePage.by_xpath( "//*[@content-desc='Acceder']")

    def random_phone(self):
        return "9" + str(random.randint(10_000_000, 99_999_999))  # 9 + 8位随机数
    def login(self, phone=None, code="3796"):
        phone = phone or self.random_phone()
        self.input_text(self.PHONE_INPUT, phone)
        logger.info("----手机号输入成功！------")
        self.input_text(self.CODE_INPUT, code)
        logger.info("----验证码输入成功！------")
        logger.info("尝试点击登录按钮")
        self.click(self.SUBMIT_BUTTON)
        logger.info("----登录按钮点击成功！------")
