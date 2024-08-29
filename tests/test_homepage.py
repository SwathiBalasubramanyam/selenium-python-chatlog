from pages.homepage import HomePage


def test_01_homepage(driver):
    page = HomePage(driver)
    page.open()
    page.verify()
