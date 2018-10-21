from selenium import webdriver

browser = webdriver.Chrome(r"E:\Programming Ebooks\Django\tdd_django\chapter-1\chromedriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title
