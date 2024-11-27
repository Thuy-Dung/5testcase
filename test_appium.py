import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

class AppiumTestCases(unittest.TestCase):

    def setUp(self):
        # Desired capabilities setup
        desired_caps = {
            "platformName": "Android",
            "app": "C:/Users/Hi/Downloads/app-debug.apk",  # Đường dẫn file APK
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # Chờ ngầm định

    def test_01_open_app(self):
        """Kiểm tra ứng dụng mở thành công"""
        self.assertTrue(self.driver.is_app_installed("com.example.app"), "App chưa được cài đặt.")

    def test_02_login_valid_credentials(self):
        """Kiểm tra đăng nhập với thông tin hợp lệ"""
        username_field = self.driver.find_element(AppiumBy.ID, "com.example.app:id/username")
        password_field = self.driver.find_element(AppiumBy.ID, "com.example.app:id/password")
        login_button = self.driver.find_element(AppiumBy.ID, "com.example.app:id/login_button")

        username_field.send_keys("valid_user")
        password_field.send_keys("valid_password")
        login_button.click()

        # Xác minh đăng nhập thành công
        welcome_message = self.driver.find_element(AppiumBy.ID, "com.example.app:id/welcome_message")
        self.assertEqual(welcome_message.text, "Welcome, valid_user!")

    def test_03_login_invalid_credentials(self):
        """Kiểm tra đăng nhập với thông tin không hợp lệ"""
        username_field = self.driver.find_element(AppiumBy.ID, "com.example.app:id/username")
        password_field = self.driver.find_element(AppiumBy.ID, "com.example.app:id/password")
        login_button = self.driver.find_element(AppiumBy.ID, "com.example.app:id/login_button")

        username_field.send_keys("invalid_user")
        password_field.send_keys("wrong_password")
        login_button.click()

        # Xác minh thông báo lỗi xuất hiện
        error_message = self.driver.find_element(AppiumBy.ID, "com.example.app:id/error_message")
        self.assertEqual(error_message.text, "Invalid credentials, please try again.")

    def test_04_navigate_to_settings(self):
        """Kiểm tra điều hướng đến màn hình Settings"""
        settings_button = self.driver.find_element(AppiumBy.ID, "com.example.app:id/settings_button")
        settings_button.click()

        # Xác minh tiêu đề Settings xuất hiện
        settings_title = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']")
        self.assertTrue(settings_title.is_displayed())

    def test_05_logout(self):
        """Kiểm tra chức năng đăng xuất"""
        logout_button = self.driver.find_element(AppiumBy.ID, "com.example.app:id/logout_button")
        logout_button.click()

        # Xác minh quay lại màn hình đăng nhập
        login_title = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Login']")
        self.assertTrue(login_title.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
