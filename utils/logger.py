# utils/logger.py
import logging
from pathlib import Path


def setup_logger():
    """配置全局日志器"""
    logger = logging.getLogger("appium_test")
    logger.setLevel(logging.DEBUG)

    # 日志格式
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 控制台输出
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 文件输出（自动创建logs目录）
    log_file = Path(__file__).parent.parent / "logs/test.log"
    log_file.parent.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)

    # 防止日志重复
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


# 创建全局日志实例
logger = setup_logger()