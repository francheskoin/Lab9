import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def _make_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


def test_example_com_title():
    driver = _make_driver()
    try:
        driver.get("https://example.com")
        assert "Example Domain" in driver.title
    finally:
        driver.quit()