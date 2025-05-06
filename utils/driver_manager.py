from appium import webdriver
from appium.options.android import UiAutomator2Options
import yaml
from utils.logger import logger
import os
from pathlib import Path
def get_driver():
    # 获取项目根目录
    BASE_DIR = Path(__file__).resolve().parent.parent

    # 构建绝对路径
    config_path = os.path.join(BASE_DIR, 'config', 'devices.yaml')
    try:
        with open(config_path) as f:  # ✅ 使用绝对路径
            config = yaml.safe_load(f)['android']
        logger.debug("正在初始化Appium驱动...")
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = config['device_name']
        options.app_package = config['app_package']
        options.app_activity = config['app_activity']
        options.new_command_timeout = config['new_command_timeout']
        options.no_reset = config['no_reset']

        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        logger.info(f"Appium驱动初始化成功，设备: {options.device_name}")
        return driver
    except Exception as e:
        logger.critical(f"驱动初始化失败: {str(e)}")
        raise