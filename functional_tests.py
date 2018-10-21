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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retreive_it_later(self): #4
        #Edith has heard about a cool new online
        #to check out its homepage

        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table


        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')


        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')




        # She types "Buy peacock feathers" into a text box (Edith's hobby)
        # is tying fly-fishing lures


        # When she hits enter, the page update, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table




        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')


        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly' ,
            [row.text for row in rows]
        )
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')
        #she notices the page title and header mention todo lists


        #She is invited to enter a to-do item straight away



if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8
