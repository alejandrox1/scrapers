from time import sleep
from selenium import webdriver

# rpp is the results per page (10, 25, 50)
# po is the page offset. If rpp=50, po=0 is 1st page, po=50 is the 2nd page, so
# on.
url ="https://www.regulations.gov/docketBrowser?rpp=50&so=DESC&sb=commentDueDate&po=0&dct=PS&D=USCIS-2010-0012"


driver = webdriver.Chrome()

driver.get(url)
sleep(3)

elems = driver.find_elements_by_xpath("//a[@href]")
comments = [ e.get_attribute("href") 
        for e in elems if "document?D=USCIS-" in e.get_attribute("href") ]

driver.quit()

comments = list(set(comments))
for c in comments:
    print(c)
