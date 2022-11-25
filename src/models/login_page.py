from selenium.webdriver.common.by import By


class LoginPage:
    username_field = (By.ID, "login_field")
    password_field = (By.ID, "password")
    login_button = (By.NAME, "commit")
