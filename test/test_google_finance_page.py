import pytest
from src.page_objects.google_finance_page import GoogleFinancePage


@pytest.fixture
def finance_page(driver):
    return GoogleFinancePage(driver)


@pytest.fixture
def stock_symbols(finance_page):
    finance_page.open_url()
    return finance_page.get_stock_symbols()


@pytest.fixture
def stock_names_input():
    return {"NFLX", "MSFT", "TSLA"}


class TestGoogleFinanceStocks:
    def test_google_finance_page_title(self, finance_page):
        finance_page.open_url()

        assert (
            finance_page.get_title()
            == "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
        )

    # this tests the symbols that in the google finance page and in the given data
    def test_stock_symbols_in_both_given_data_and_finance_page(self, stock_symbols, stock_names_input):
        # iterate over the retrieved stock symbols and put them in a list
        stock_symbol_set = set([stock_element.text for stock_element in stock_symbols])

        stock_inter = stock_symbol_set.intersection(set(stock_names_input))
        print(f"Stocks in both the google finance page and the given test data: {stock_inter}")

        assert len(stock_inter) > 0, "No common stock symbols found between given data and Google Finance page."

    # this tests the symbols that are in the google finance page but not in given data
    def test_stock_symbols_in_finance_page_not_in_given_data(self, stock_symbols, stock_names_input):
        # iterate over the retrieved stock symbols and put them in a list
        stock_symbol_set = set([stock_element.text for stock_element in stock_symbols])

        stock_diff = stock_symbol_set.difference(stock_names_input)
        print(f"Stocks in the google finance page that are not in the given test data: {stock_diff}")

        assert len(stock_diff) > 0, "No different stocks found between Google Finance page and given test data."

    # this tests the symbols that are in the given data but not in the google finance page
    def test_stock_symbols_in_given_data_not_in_finance_page(self, stock_symbols, stock_names_input):
        # iterate over the retrieved stock symbols and put them in a list
        stock_symbol_set = set([stock_element.text for stock_element in stock_symbols])

        stock_diff = stock_names_input.difference(stock_symbol_set)
        print(f"Stocks that are in the given test data but not in the google finance page: {stock_diff}")

        # assert that there is at least some given stocks that are not in the finance page
        assert len(stock_diff) > 0, "All given stocks found on Google Finance page, expected some to be missing."

    # tests scenario where no given data is provided
    def test_stock_symbols_with_no_given_data(self, stock_symbols):
        # iterate over the retrieved stock symbols and put them in a list
        stock_symbol_set = set([stock_element.text for stock_element in stock_symbols])

        stock_diff = stock_symbol_set.difference(set())
        print(f"Stocks that are in the google finance page, given no test data: {stock_diff}")
        assert stock_diff == stock_symbol_set, "No stock symbols found on Google Finance page."
