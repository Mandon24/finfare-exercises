from src.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class GoogleFinancePage(BasePage):
    def __init__(self, driver, url="https://www.google.com/finance/"):
        super().__init__(driver, url)

    @property
    def stock_elements(self):
        """Simulate Page Factory behavior: find stock list items when accessed."""
        return self.find_elements(
            By.CSS_SELECTOR,
            "#yDmH0d > c-wiz.zQTmif.SSPGKf.ccEnac > div > div.e1AOyf > div > div > div.fAThCb > c-wiz:nth-child(1) > div > section > ul > li"
        )

    @property
    def stock_symbols(self):
        """Simulate Page Factory behavior: extract stock symbols."""
        symbols = []
        for li in self.stock_elements:
            symbol_element = li.find_element(
                By.CSS_SELECTOR, "a > div > div > div.iLEcy > div.rzR5Id > div > div"
            )
            symbols.append(symbol_element.text)
        return symbols
