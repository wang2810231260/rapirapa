import string
import time
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import logger
class Live(BasePage):
    # 确认按钮
    # CONTINUAR_BUTTOM=BasePage.by_xpath("//*[@text='Continuar']")
    def live(self):
        max_attempts = 3
        attempt = 0
        while attempt < max_attempts:
            try:
                logger.info('开始查找继续按钮')
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@text="Continuar"]')
                                                   ))
                continura_button = self.driver.find_element(By.XPATH,"//*[@text='Continuar']")
                logger.info('找到继续按钮')
                if continura_button.is_displayed():
                    self.click(continura_button)
                    logger.info(f"点击继续按钮 - 第 {attempt + 1} 次")
                    time.sleep(10)
                    attempt += 1
                else:
                    logger.info('活体通过')
                    break
            except Exception as e:
                logger.info('活体通过（按钮找不到）')
                break
        else:
            logger.warning('已尝试 3 次点击继续按钮，仍未通过活体识别')





