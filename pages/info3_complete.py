import time

from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import logger
import random


class Info3Complete(BasePage):
    # 相机按钮
    CAMERA_BUTTON = (By.XPATH, '//*[@text="Tomar una foto"]')
    # 相册按钮
    ALBUM_BUTTON = (By.XPATH, '//*[@text="Seleccionar desde la galería"]')
    SUBMIT_BUTTON = BasePage.by_xpath("//*[@text='Continuar completando']")

    def random_rut(self):
        return "9" + str(random.randint(10_000_000, 99_999_999))  # 9 + 8位随机数

    def info3_complete(self):
        time.sleep(2)
        self.click(self.CAMERA_BUTTON)
        logger.info('相机按钮点击成功')
        success = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView')
                                           ))
        if success:
            self.click(success)
            logger.info('拍照按钮点击成功')
            SEX_BUTTON = WebDriverWait(self.driver, 50).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.RadioButton')
                                               ))
            if SEX_BUTTON:
                logger.info('性别选项识别成功')
                item=random.choice(SEX_BUTTON)
                self.click(item)
                logger.info('性别选择成功')
                NORBRE_INPUT = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')
                                                        ))
                if NORBRE_INPUT:
                    self.input_text(NORBRE_INPUT[0], 'adaad')
                    logger.info('名输入成功')
                    BasePage.swipe_up(self)
                    APELIDO_INPUT = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')
                                                            ))
                    if APELIDO_INPUT:
                        self.input_text(APELIDO_INPUT[1], 'afafa')
                        logger.info('姓输入成功')
                        RUT_INPUT = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')
                                                                ))
                        if RUT_INPUT:
                            rut_element = RUT_INPUT[2]
                            rut_text = self.random_rut()
                            self.input_text(rut_element, rut_text)
                            logger.info('身份证输入成功')
                            BIRTHDAY_INPUT = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@text="Por favor seleccione"]')
                                                               ))
                            if BIRTHDAY_INPUT:
                                self.click(BIRTHDAY_INPUT)
                                logger.info('生日输入框点击成功')
                                CONFIMR_BUTTON = WebDriverWait(self.driver, 10).until(
                                    EC.presence_of_element_located((By.XPATH, '//*[@text="Confirmar"]')
                                                                   ))
                                if CONFIMR_BUTTON:
                                    self.click(CONFIMR_BUTTON)
                                    logger.info('确认按钮点击成功')
                                    self.click(self.SUBMIT_BUTTON)


        else:
            logger.info('拍照按钮点击失败')
