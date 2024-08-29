from locators.en_locators import HOMEPAGE_HEADER

BASE_URL = "https://chatlog.onrender.com/"


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def verify(self):
        ele = self.driver.find_element(*HOMEPAGE_HEADER)
        import pdb
        pdb.set_trace()
