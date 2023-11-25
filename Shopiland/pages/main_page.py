import random
from pages.base import BasePage
from pages.locators import MainPageSearchLocators


class MainPageSearchHelper(BasePage):
    def choice_city(self):
        choice_city = self.find_element(MainPageSearchLocators.CHOICE_CITY)
        choice_city.click()
        city_list = [x.text for x in self.find_elements(MainPageSearchLocators.CITY_LIST)]
        random_city = random.randint(0, len(city_list))
        city = self.find_elements(MainPageSearchLocators.CITY_LIST)[random_city]
        return city

    def choice_search_word(self):
        search_word = self.find_elements(MainPageSearchLocators.SEARCH_WORD)
        return [x.text for x in search_word]

    def enter_word(self, word):
        search_field = self.find_element(MainPageSearchLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_search_button(self):
        return self.find_element(MainPageSearchLocators.SEARCH_BUTTON, time=2).click()