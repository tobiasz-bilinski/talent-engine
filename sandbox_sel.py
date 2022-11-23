from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.google.com")
assert driver.title == "GitHub: Let's build from here - GitHub"
