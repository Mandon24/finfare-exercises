from src.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class GoogleFinancePage(BasePage):
    def __init__(self, driver, url="https://www.google.com/finance/"):
        super().__init__(driver, url)

    def get_stock_symbols(self):
        # find all ul elements matching
        stock_elements = self.find_elements(
            By.CSS_SELECTOR,
            "#yDmH0d > c-wiz.zQTmif.SSPGKf.ccEnac > div > div.e1AOyf > div > div > div.fAThCb > c-wiz:nth-child(1) > div > section > ul > li",
        )

        # extract and return only the stock symbol text
        stock_symbols = []
        for li in stock_elements:
            symbol_element = li.find_element(
                By.CSS_SELECTOR, "a > div > div > div.iLEcy > div.rzR5Id > div > div"
            )
            stock_symbols.append(symbol_element)

        return stock_symbols
