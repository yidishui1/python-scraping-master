from selenium import webdriver


driver = webdriver.PhantomJS(executable_path='/Users/yujinyue/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get("http://en.wikipedia.org/wiki/Monty_Python")
assert "Monty Python" in driver.title
print("Monty Python was in the title")
driver.close()