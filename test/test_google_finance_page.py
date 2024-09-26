from src.page_objects.google_finance_page import GoogleFinancePage


class TestGoogleFinancePage:
    def test_google_finance_page_title(self, driver):
        finance_page = GoogleFinancePage(driver)

        finance_page.open_url()

        assert (
            finance_page.get_title()
            == "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
        )
