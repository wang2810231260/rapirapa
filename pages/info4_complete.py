import string
import time
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import logger
import random


class Info4CompletePage(BasePage):
    SUBMIT_BUTTON = BasePage.by_xpath("//*[@text='Continuar completando']")


    def info4_complete(self):
        BANK_TYPE = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@text="Por favor seleccione"]')
                                           ))
        if BANK_TYPE:
            self.click(BANK_TYPE)
            logger.info('点击银行类型输入框成功')
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.view.ViewGroup'))
            )
            # 获取选项
            options1 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')
            if options1:
                limchoice = random.choice(options1[:2])
                self.click(limchoice)
                logger.info('银行卡类型选项点击成功')
                BANK_NAME = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@text="Por favor seleccione"]')
                                                   ))
                if BANK_NAME:
                    self.click(BANK_NAME)
                    logger.info('点击银行名称输入框成功')
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, '//*[@text="Elige bancos"]')
                                                            )
                    )
                    options2 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')
                    # logger.info(f'options{options2}')
                    if len(options2) > 0:
                        limchoice = random.choice(options2[-8:])
                        self.click(limchoice)
                        logger.info('银行名称选项点击成功')
                        BANK_NO = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_all_elements_located((By.XPATH, '//*[@text="Por favor ingresa"]')
                                                                ))
                        if len(BANK_NO) >= 2:
                            bank_no = ''.join(random.choices(string.digits, k=9))
                            self.input_text(BANK_NO[0], bank_no)
                            self.input_text(BANK_NO[1], bank_no)
                            logger.info('银行卡号输入成功')
                            self.click(self.SUBMIT_BUTTON)
                            logger.info('点击提交按钮成功')
                            CONFIMAR_BUTTON = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@text="Confirmar"]')
                                                                    ))
                            if CONFIMAR_BUTTON :
                                self.click(CONFIMAR_BUTTON)
                                logger.info('点击确认按钮成功')




