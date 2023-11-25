import time
from pages.base import BasePage
from pages.locators import SearchPageLocators


class SearchPageHelper(BasePage):
    def find_all_markets(self):
        all_list = self.find_elements(SearchPageLocators.MARKET_NAVI)
        markets = [x.text for x in all_list]
        return list(map(lambda x: x.split(' (')[0], markets))

    def prods_titles(self):
        all_list = self.find_elements(SearchPageLocators.PRODS_TITLES)
        return [x.text for x in all_list]

    def prods_markets(self):
        all_list = self.find_elements(SearchPageLocators.PRODS_MARKETS)
        return [x.text for x in all_list]

    def prods_prices(self):
        all_list = self.find_elements(SearchPageLocators.PRODS_PRICES)
        prices = [x.text for x in all_list]
        prices = list(map(lambda x: x.split(' ₽')[0], prices))
        prices = [p.replace(' ', '') for p in prices if p]
        prices = [float(p.replace(',', '.')) for p in prices if p]
        return prices

    def prods_pops_all_list(self):
        all_list = self.find_elements(SearchPageLocators.PRODS_POPS_ALL)
        return [x.text for x in all_list]

    def prods_pops(self):
        all_list = self.find_elements(SearchPageLocators.PRODS_POPS_ALL)
        return [int(x.text.split()[0]) for x in all_list]

    def prods_fbacks(self):
        all_list = self.find_elements(SearchPageLocators.PRODS_FBACKS)
        return [x.text for x in all_list]

    def prods_counts(self):
        all_list = self.find_elements(SearchPageLocators.PRODS_COUNTS)
        return [x.text[1] for x in all_list]

    def click_on_more_load_button(self):
        element = self.find_elements(SearchPageLocators.MORE_LOAD_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element.click()

    def choose_last_market(self, navi):
        for i in range(len(navi) - 1):
            element = self.find_elements(SearchPageLocators.MARKET_NAVI)[i]
            element.click()
            time.sleep(2)

    def choose_market_above(self, pm, navi):
        element_above = self.find_elements(SearchPageLocators.MARKET_NAVI)[pm - 1]
        element_above.click()
        time.sleep(2)
        element = self.find_elements(SearchPageLocators.MARKET_NAVI)[pm]
        element.click()
        time.sleep(2)

    def click_on_sort_by_price(self):
        element = self.find_element(SearchPageLocators.SORT_PRICE_BUTTON)
        element.click()
        time.sleep(2)

    def enter_min_price(self, min_price):
        min_pr = self.find_elements(SearchPageLocators.MIN_PRICE)[0]
        min_pr.click()
        min_pr.send_keys(min_price)
        return min_pr

    def enter_max_price(self, max_price):
        max_pr = self.find_elements(SearchPageLocators.MAX_PRICE)[0]
        max_pr.click()
        max_pr.send_keys(max_price)
        return max_pr