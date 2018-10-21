from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#browser = webdriver.Chrome(r"E:\Programming Ebooks\Django\tdd_django\chapter-1\chromedriver.exe")
#browser.get('http://localhost:8000')

#assert 'To-Do' in browser.title

#browser.quit()

class NewVisitorTest(unittest.TestCase): #1

    def setUp(self): #2
        self.browser = webdriver.Chrome(r"E:\Programming Ebooks\Django\tdd_django\chapter-1\chromedriver.exe")
        self.browser.implicitly_wait(3)


    def tearDown(self): #3
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self): #4
        #Edith has heard about a cool new online
        #to check out its homepage

        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        seslf.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby)
        # is tying fly-fishing lures
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page update, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )


        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')
        #she notices the page title and header mention todo lists
        #self.assertIn('To-Do', self.browser.title) #5
        #self.fail('Finish the test') #6

        #She is invited to enter a to-do item straight away


if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8
