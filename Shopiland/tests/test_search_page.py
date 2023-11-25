import pytest
from pages.main_page import MainPageSearchHelper
from pages.search_page import SearchPageHelper
import time

"""Проверим, что во всех маркетплейсах имеются товары и найденные товары
соответствуют поисковому запросу, для каждого маркетплейса
по отдельности, начиная с последнего в списке"""

@pytest.mark.parametrize('word', ['iphone 14','Шар'])
def test_search_kazan(browser, word):
    """Проверим, что найденные товары соответствуют
    поисковому запросу"""
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word(word)
    main_page.click_on_search_button()
    browser.implicitly_wait(10)
    market_navi = search_page.find_all_markets()
    print(market_navi)

    # Начинаем с последнего маркетплейса из списка
    search_page.choose_last_market(navi=market_navi)
    time.sleep(5)
    prod_markets = search_page.prods_markets()
    pm = len(market_navi) - 1
    for market in prod_markets:
        msg = 'Not only products from "{}" in result'\
            .format(market_navi[pm])
        assert market_navi[pm] in market, msg

    prod_titles = search_page.prods_titles()
    msg = 'No products from "{}" in result'.format(market_navi[pm])
    assert len(prod_titles) > 0, msg

    for title in prod_titles:
        msg = 'Wrong product in market "{}"'.format(market_navi[pm])
        for i in word.split():
            assert i.lower() in title.lower(), msg

@pytest.mark.parametrize('word', ['iphone 14', 'Шар'])
def test_search_sber(browser, word):
    """Проверим, что найденные в СберМегамаркет товары соответствуют
    поисковому запросу"""
    # поднимаемся по одному вверх:
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word(word)
    main_page.click_on_search_button()
    browser.implicitly_wait(10)

    market_navi = search_page.find_all_markets()
    # Начинаем с последнего маркетплейса из списка
    search_page.choose_last_market(navi=market_navi)

    pm = len(market_navi) - 1
    search_page.choose_market_above(pm, navi=market_navi)
    time.sleep(5)

    prod_markets = search_page.prods_markets()

    for market in prod_markets:
        msg = 'Not only products from "{}" in result'\
            .format(market_navi[pm - 1])
        assert market_navi[pm - 1] in market, msg

    prod_titles = search_page.prods_titles()
    msg = 'No products from "{}" in result'.format(market_navi[pm - 1])
    assert len(prod_titles) > 0, msg

    for title in prod_titles:
        msg = 'Wrong product in market "{}"'.format(market_navi[pm - 1])
        assert word.split()[0].lower() in title.lower(), msg

@pytest.mark.parametrize('word', ['iphone 14', 'Шар'])
def test_search_ya(browser, word):
    """Проверим, что найденные в Яндекс Маркет товары соответствуют
    поисковому запросу"""
    # поднимаемся по одному вверх:
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word(word)
    main_page.click_on_search_button()
    browser.implicitly_wait(10)

    market_navi = search_page.find_all_markets()
    # Начинаем с последнего маркетплейса из списка
    search_page.choose_last_market(navi=market_navi)
    pm = len(market_navi) - 1
    for i in range(pm, pm - 2, -1):
        search_page.choose_market_above(pm=i, navi=market_navi)

    prod_markets = search_page.prods_markets()

    for market in prod_markets:
        msg = 'Not only products from "{}" in result'\
            .format(market_navi[pm - 2])
        assert market_navi[pm - 2] in market, msg

    prod_titles = search_page.prods_titles()
    msg = 'No products from "{}" in result'.format(market_navi[pm - 2])
    assert len(prod_titles) > 0, msg

    for title in prod_titles:
        msg = 'Wrong product in market "{}"'.format(market_navi[pm - 2])
        assert word.split()[0].lower() in title.lower(), msg

@pytest.mark.parametrize('word', ['iphone 14', 'Шар'])
def test_search_wb(browser, word):
    """Проверим, что найденные в Wildberries товары соответствуют
    поисковому запросу"""
    # поднимаемся по одному вверх:
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word(word)
    main_page.click_on_search_button()
    browser.implicitly_wait(10)

    market_navi = search_page.find_all_markets()
    # Начинаем с последнего маркетплейса из списка
    search_page.choose_last_market(navi=market_navi)
    time.sleep(5)

    pm = len(market_navi) - 1
    for i in range(pm, pm - 3, -1):
        search_page.choose_market_above(pm=i, navi=market_navi)

    prod_markets = search_page.prods_markets()

    for market in prod_markets:
        msg = 'Not only products from "{}" in result'\
            .format(market_navi[pm - 3])
        assert market_navi[pm - 3] in market, msg

    prod_titles = search_page.prods_titles()
    msg = 'No products from "{}" in result'.format(market_navi[pm - 3])
    assert len(prod_titles) > 0, msg

    for title in prod_titles:
        msg = 'Wrong product in market "{}"'.format(market_navi[pm - 3])
        assert word.split()[0].lower() in title.lower(), msg

@pytest.mark.parametrize('word', ['iphone 14', 'Шар'])
def test_search_ali(browser, word):
    """Проверим, что найденные в AliExpress товары соответствуют
    поисковому запросу"""
    # поднимаемся по одному вверх:
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word(word)
    main_page.click_on_search_button()
    browser.implicitly_wait(10)

    market_navi = search_page.find_all_markets()
    # Начинаем с последнего маркетплейса из списка
    search_page.choose_last_market(navi=market_navi)
    time.sleep(5)

    pm = len(market_navi) - 1
    for i in range(pm, pm - 4, -1):
        search_page.choose_market_above(pm=i, navi=market_navi)

    prod_markets = search_page.prods_markets()

    for market in prod_markets:
        msg = 'Not only products from "{}" in result'\
            .format(market_navi[pm - 4])
        assert market_navi[pm - 4] in market, msg

    prod_titles = search_page.prods_titles()
    msg = 'No products from "{}" in result'.format(market_navi[pm - 4])
    assert len(prod_titles) > 0, msg

    for title in prod_titles:
        msg = 'Wrong product in market "{}"'.format(market_navi[pm - 4])
        for i in word.split():
            assert i.lower() in title.lower(), msg

@pytest.mark.parametrize('word', ['iphone 14', 'Шар'])
def test_search_ozon(browser, word):
    """Проверим, что найденные в Ozon товары соответствуют
    поисковому запросу"""
    # поднимаемся по одному вверх:
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word(word)
    main_page.click_on_search_button()
    browser.implicitly_wait(10)

    market_navi = search_page.find_all_markets()
    # Начинаем с последнего маркетплейса из списка
    search_page.choose_last_market(navi=market_navi)
    time.sleep(5)

    pm = len(market_navi) - 1
    for i in range(pm, pm - 5, -1):
        search_page.choose_market_above(pm=i, navi=market_navi)

    prod_markets = search_page.prods_markets()

    for market in prod_markets:
        msg = 'Not only products from "{}" in result'\
            .format(market_navi[pm - 5])
        assert market_navi[pm - 5] in market, msg

    prod_titles = search_page.prods_titles()
    print(prod_titles)
    msg = 'No products from "{}" in result'.format(market_navi[pm - 5])
    assert len(prod_titles) > 0, msg

    for title in prod_titles:
        msg = 'Wrong product in market "{}"'.format(market_navi[pm - 5])
        assert word.split()[0].lower() in title.lower(), msg

def test_check_sort_by(browser):
    """Проверим, что популярность использует только отзывы или продаж"""
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word('iphone 14')
    main_page.click_on_search_button()
    browser.implicitly_wait(10)
    pops_all = search_page.prods_pops_all_list()
    for pops in pops_all:
        assert 'отзывов' or 'продаж' in pops.split()[1]
        # Магазин Aliexpress использует слово продаж, остальные отзывов

def test_check_sort_by_pops(browser):
    """Проверим корректность механизма сортировки по кол-ву отзывов"""
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word('iphone 14')
    main_page.click_on_search_button()
    browser.implicitly_wait(10)

    pops = search_page.prods_pops()
    assert pops == sorted(pops, reverse=True), "Sort by popular doesn't work!"

def test_check_sort_by_price(browser):
    """Проверим корректность механизма сортировки по цене по возрастанию
    и по убыванию"""
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word('iphone 14')
    main_page.click_on_search_button()
    browser.implicitly_wait(10)

    search_page.click_on_sort_by_price()
    prices = search_page.prods_prices()
    assert prices == sorted(prices), "Sort by price doesn't work!"

    search_page.click_on_sort_by_price()
    prices = search_page.prods_prices()
    assert prices == sorted(prices, reverse=True), "Sort by price doesn't work!"

def test_check_min_max_price_sorting(browser):
    """Проверим, что сортировка от мин до макс цены работает корректно"""
    main_page = MainPageSearchHelper(browser)
    search_page = SearchPageHelper(browser)
    main_page.go_to_site()

    main_page.enter_word('iphone 14')
    main_page.click_on_search_button()
    time.sleep(10)

    prices = search_page.prods_prices()
    min_price = 0.25 * (max(prices) - min(prices))
    max_price = 0.75 * (max(prices) - min(prices))

    search_page.enter_min_price(min_price)
    search_page.enter_max_price(max_price)
    search_page.click_on_sort_by_price()
    browser.implicitly_wait(10)

    prices_new = search_page.prods_prices()
    assert min(prices_new) >= min_price, "min price limit doesn't work"
    assert max(prices_new) <= max_price, "max price limit doesn't work"