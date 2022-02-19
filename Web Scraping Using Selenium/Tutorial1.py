
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Path of the respective chrome driver file
PATH="/Volumes/Dev T7/vscode/projects/Pythonvscode/Web scraping/selenium/chromedriver"
#create an instance for webdriver
driver=webdriver.Chrome(PATH)
#link of website which is to be interacted with.
driver.get("https://techwithtim.net")
#prints title of the site
print(driver.title)
#searches the element by name in the html code
search=driver.find_element_by_name("search")
#enter key in the search instance(interacts)
search.send_keys("test")
#enters the key
search.send_keys(Keys.RETURN)

#this code block is used to instruct the program to wait until the elements have loaded in the web drower. Not using this can lead to exceptions.
#Full explanation can be found in selenium documentation.
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles=main.find_elements_by_tag_name("article")
    for article in articles:
        header=article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()



