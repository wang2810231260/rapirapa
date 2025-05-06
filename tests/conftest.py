import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.driver_manager import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()