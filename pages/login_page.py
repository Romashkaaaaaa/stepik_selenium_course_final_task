import faker
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = "fake123456789TEST"

        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)

        register_password_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        register_password_1.send_keys(password)

        register_password_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        register_password_2.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
#Пустая строчка снизу