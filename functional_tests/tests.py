from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self): #2
        self.browser = webdriver.Chrome(r"E:\Programming Ebooks\Django\tdd_django\chapter-1\chromedriver.exe")

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, she is taken to a new URL,
        # and now the page lists "1: Buy peacock feathers" as an item in a
        # to-do list table

        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+') #
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # Now a new user, Francis, comes along to the site.
        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc #
        self.browser.quit()
        self.browser = webdriver.Firefox()
        # Francis visits the home page. There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...

        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        # Satisfied,
