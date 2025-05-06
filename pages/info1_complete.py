from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from utils.logger import logger
import random
from selenium.webdriver.common.by import By


class InfoCompletePage(BasePage):

    # 邮箱输入框
    EMAIL_INPUT = BasePage.by_xpath("//*[@text='Por favor ingresa']")
    # 提交按钮
    SUBMIT_BUTTON = BasePage.by_xpath("//*[@text='Continuar completando']")

    def application_click(self):
        # 进入info
        self.input_text(self.EMAIL_INPUT, 'test@163.com')
        logger.info('邮箱输入成功')
        # 获取输入框
        INPUT = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@text="Por favor seleccione"]'))
        )
        self.click(INPUT[0])
        logger.info('教育程度输入框点击成功')
        #   等待元素出现
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.view.ViewGroup'))
        )
        # 获取选项
        options1 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')
        if options1:
            limchoice = random.choice(options1[:3])
            self.click(limchoice)
        logger.info('教育程度选项点击成功')

        INPUT = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@text="Por favor seleccione"]'))
        )
        # logger.info(INPUT)
        self.click(INPUT[0])
        logger.info('婚姻状况输入框点击成功')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.view.ViewGroup'))
        )
        options2 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')

        if options2:
            limchoice = random.choice(options2[:2])
            self.click(limchoice)
        logger.info('婚姻状态选项点击成功')
        INPUT = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@text="Por favor seleccione"]'))
        )
        self.click(INPUT[0])
        logger.info('岗位输入框点击成功')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.view.ViewGroup'))
        )
        options3 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')

        if options3:
            limchoice = random.choice(options3[:3])
            self.click(limchoice)
        logger.info('岗位选项点击成功')
        INPUT = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@text="Por favor seleccione"]'))
        )
        self.click(INPUT[0])
        logger.info('薪资输入框点击成功')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.view.ViewGroup'))
        )
        options4 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')

        if options4:
            limchoice = random.choice(options4[:3])
            self.click(limchoice)
        logger.info('薪资选项点击成功')
        self.click(self.SUBMIT_BUTTON)
        logger.info('提交按钮点击成功')

