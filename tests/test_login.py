import allure
import pytest
from pages.unlogin_home import HomePage
from pages.login_page import LoginPage
from  pages.login_home import LoginHomePage
from pages.info1_complete import InfoCompletePage
from pages.info2_complete import InfoCompletePage2
from pages.info3_complete import Info3Complete
from pages.info4_complete import Info4CompletePage
from pages.live import Live
from utils.logger import logger


@allure.feature("登录功能")
class TestLogin:
    @allure.story("登录功能")
    @allure.title("测试随机手机号登录")
    @allure.description("测试随机手机号登录")
    @allure.severity('blocker')
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.login_home_page = LoginHomePage(driver)
        self.info_complete_page1 = InfoCompletePage(driver)
        self.info_complete_page2 = InfoCompletePage2(driver)
        self.info_complete_page4 = Info4CompletePage(driver)
        self.info_complete_page3 = Info3Complete(driver)
        self.live = Live(driver)
        logger.info("===== 测试开始 =====")

    def test_login(self):
        try:
            # logger.info("用例: 测试随机手机号登录")
            self.home_page.click_login()
            self.login_page.login()
            # logger.info("断言: 检查登录后页面")
            logger.info('进入登录首页')
            self.login_home_page.application()
            self.info_complete_page1.application_click()
            logger.info('info1填写成功')
            self.info_complete_page2.info2_complate()
            logger.info('info2进入成功')
            self.info_complete_page3.info3_complete()
            logger.info('info3进入成功')
            self.info_complete_page4.info4_complete()
            logger.info('info4进入成功')
            self.live.live()
            logger.info('live进入成功')





        except Exception as e:
            logger.error(f"测试失败: {str(e)}")
            raise
        finally:
            logger.info("===== 测试结束 =====")