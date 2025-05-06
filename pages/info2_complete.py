import time

from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger
from selenium.webdriver.common.by import By
import random


class InfoCompletePage2(BasePage):
    SUBMIT_BUTTON = BasePage.by_xpath("//*[@text='Continuar completando']")

    def info2_complate(self):
        logger.info("进入info2_complate")
        # 联系人1
        INPUT = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@text="Por favor seleccione"]')
                                           ))
        self.click(INPUT)
        logger.info("点击联系人1输入框完成")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.view.ViewGroup'))
        )
        options1 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')
        if options1:
            limchoice = random.choice(options1[:2])
            self.click(limchoice)
            logger.info("联系人1关系选择成功")
            INPUT=WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]')
                                               ))
            self.click(INPUT[0])
            logger.info("手机号1通讯录图标点击完成")
            #         联系人页面
            WebDriverWait(self.driver, 300).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.FrameLayout')
                                                   ))
            contact1 = self.driver.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')

            if contact1:
                    # limchoice = random.choice(contact2[:3])
                    self.click(contact1[3])
                # limchoice = random.choice(contact1[:2])
                # self.click(contact1)
                    logger.info("联系人1完成")

        else:
            logger.info("联系人1关系选择失败")

        # 联系人2
        INPUT = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@text="Por favor seleccione"]')
                                           ))
        self.click(INPUT)
        logger.info("点击联系人2输入框完成")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.view.ViewGroup'))
        )
        options1 = self.driver.find_elements(By.CLASS_NAME, 'android.view.ViewGroup')
        if options1:
            limchoice = random.choice(options1[:2])
            self.click(limchoice)
            logger.info("联系人2关系选择成功")
            INPUT2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH,
                                                     '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView[2]')
                                                    ))
            self.click(INPUT2[0])
            logger.info("手机号2通讯录图标点击完成")
            #         联系人页面
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.FrameLayout')
                                               ))
            contact2 = self.driver.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
            if contact2:
                self.click(contact2[2])
            logger.info("联系人2完成")
            self.click(self.SUBMIT_BUTTON)
            logger.info("点击提交按钮完成")
        else:
            logger.info("联系人2关系选择失败")
