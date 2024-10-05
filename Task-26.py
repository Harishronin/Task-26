"""
 Name : Harish kumar
 Date : 05-Oct-2024
 Program 1 : Using page object model explicit wait,expected conditions pytest and chrome web driver 
1.fill the data given in the input boxes,select boxes and drop down menu on the web page and do a search. 
2.Do not use sleep()method.
 """

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class IMDBSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators 
    SEARCH_NAME_INPUT = (By.ID, "name")
    SEARCH_DOB_INPUT = (By.ID, "birth_monthday")
    SEARCH_DOD_INPUT = (By.ID, "death_monthday")
    SEARCH_GENDER_DROPDOWN = (By.ID, "gender")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Search')]")

    # Methods 
    def enter_name(self, name):
        name_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)

    def enter_date_of_birth(self, dob):
        dob_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_DOB_INPUT))
        dob_input.clear()
        dob_input.send_keys(dob)

    def enter_date_of_death(self, dod):
        dod_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_DOD_INPUT))
        dod_input.clear()
        dod_input.send_keys(dod)

    def select_gender(self, gender_text):
        gender_dropdown = self.wait.until(EC.presence_of_element_located(self.SEARCH_GENDER_DROPDOWN))
        select = Select(gender_dropdown)
        select.select_by_visible_text(gender_text)

    def click_search(self):
        search_button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()


import pytest
from pages.imdb_search_page import IMDBSearchPage

@pytest.mark.usefixtures("init_driver")
class TestIMDBSearch:
    
    def test_search(self):
        # Initialize the search page
        imdb_search = IMDBSearchPage(self.driver)
        
        # Fill in the form with the details
        imdb_search.enter_name("Tom Hanks")
        imdb_search.enter_date_of_birth("07-09")
        imdb_search.enter_date_of_death("")  # Leave this blank for living individuals
        imdb_search.select_gender("Male")
        
        # Perform the search
        imdb_search.click_search()

        # Assert that the search was successful by checking the URL or page contents
        assert "name" in self.driver.current_url
