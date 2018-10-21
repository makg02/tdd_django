from selenium import webdriver
import unittest

#browser = webdriver.Chrome(r"E:\Programming Ebooks\Django\tdd_django\chapter-1\chromedriver.exe")
#browser.get('http://localhost:8000')

#assert 'To-Do' in browser.title

#browser.quit()

class NewVisitorTest(unittest.TestCase): #1

    def setUp(self): #2
        self.browser = webdriver.Chrome(r"E:\Programming Ebooks\Django\tdd_django\chapter-1\chromedriver.exe")
        self.browser.implicity_wait(3)


    def tearDown(self): #3
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self): #4
        #Edith has heard about a cool new online
        #to check out its homepage

        self.browser.get('http://localhost:8000')

        #she notices the page title and header mention todo lists
        self.assertIn('To-Do', self.browser.title) #5
        self.fail('Finish the test') #6

        #She is invited to enter a to-do item straight away


if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8
