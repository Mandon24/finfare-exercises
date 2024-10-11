from src.page_objects.google_finance_page import GoogleFinancePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# initialize webdriver
options = ChromeOptions()

driver = webdriver.Chrome(options=options)

# initialize data
given_data = {"NFLX", "MSFT", "TSLA"}
finance_page = GoogleFinancePage(driver)
finance_page.open_url()
stock_symbols = finance_page.stock_symbols
stock_symbol_set = set(stock_symbols)

print(
    f"Stock symbols in both given data and finance page: {stock_symbol_set.intersection(set(given_data))}"
)
print(
    f"Stock symbols in given data not in finance page: {given_data.difference(set(stock_symbol_set))}"
)
print(
    f"Stock symbols in finance page not in given data: {stock_symbol_set.difference(set(given_data))}"
)
