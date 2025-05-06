import os
from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import logger
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs/screenshots')

    def click(self, locator):
        """点击元素（自动等待可点击状态）"""
        try:
            logger.info(f"Attempting to click: {locator}")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            ).click()
            logger.info(f"Successfully clicked: {locator}")
        except Exception as e:
            screenshot_path = self.take_screenshot("click_error")
            logger.info(f"Click failed on {locator}. Screenshot: {screenshot_path}")
            raise

    def input_text(self, target, text, mask_sensitive=True):
        """
        输入文本，兼容传入 locator 或 WebElement。
        :param target: 元素定位器 (By, value) 或已定位的 WebElement
        :param text: 要输入的文本
        :param mask_sensitive: 是否遮挡敏感信息
        """
        try:
            # 遮挡敏感信息（如果需要）
            display_text = f"{text[:3]}***" if mask_sensitive and len(text) > 3 else text
            logger.info(f"Inputting text '{display_text}' to {target}")

            # 判断 target 是 locator 还是 WebElement
            if isinstance(target, tuple):
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(target)
                )
            else:
                if not isinstance(target, WebElement):
                    raise TypeError(f"Expected WebElement but got {type(target)}")
                element = target  # 直接使用传入的 WebElement

            # 清空并输入文本
            element.clear()
            element.send_keys(text)
            logger.info(f"Text input completed (length: {len(text)})")

        except Exception as e:
            # 错误时截图并记录日志
            screenshot_path = self.take_screenshot("input_error")
            logger.error(f"Input failed. Screenshot: {screenshot_path}. Error: {str(e)}")
            raise

    def take_screenshot(self, name):
        """保存截图到logs/screenshots目录"""
        os.makedirs(self.screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(self.screenshot_dir, filename)

        try:
            self.driver.save_screenshot(path)
            logger.info(f"Screenshot saved: {path}")
            return path
        except Exception as e:
            logger.info(f"Failed to take screenshot: {str(e)}")
            return None


    def swipe_up(self, duration=500, ratio=0.75):
        """
        使用 W3C Actions 实现屏幕上滑
        :param duration: 滑动持续时间（毫秒）
        :param ratio: 滑动距离占屏幕高度的比例（默认 0.75）
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        start_x = width // 2
        start_y = int(height * 0.8)
        end_y = int(height * (1 - ratio))  # 通常在屏幕顶部 0.2 左右

        # 初始化触摸输入
        finger = PointerInput("touch", "finger")
        builder = ActionBuilder(self.driver)

        # 使用 ActionBuilder 来创建动作链
        action = builder.pointer_action
        action.move_to_location(start_x, start_y)
        action.pointer_down()
        action.pause(duration / 1000)  # 秒
        action.move_to_location(start_x, end_y)
        action.pointer_up()

        # 执行操作
        builder.perform()

    # 新增常用定位器类型
    @staticmethod
    def by_accessibility_id(value):
        """通过accessibility_id定位"""
        return (AppiumBy.ACCESSIBILITY_ID, value)

    @staticmethod
    def by_id(value):
        """通过resource-id定位"""
        return (AppiumBy.ID, value)

    @staticmethod
    def by_xpath(value):
        """通过xpath定位"""
        return (AppiumBy.XPATH, value)
    @staticmethod
    def by_class(value):
        """通过class定位"""
        return (AppiumBy.CLASS_NAME, value)
