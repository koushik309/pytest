import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AssertionsTest(softest.TestCase):

    def test_lambdatest_radio_button_demo_values(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

        # Select the gender radio button
        driver.find_element(By.XPATH, "//input[@value='Male' and @name='gender']").click()

        # Select the correct age group radio button
        driver.find_element(By.XPATH, "//input[@value='0 - 5' and @name='ageGroup']").click()

        # Click on 'Get values' button
        driver.find_element(By.XPATH, "//button[text()='Get values']").click()

        # Print all paragraph elements for debugging
        elements = driver.find_elements(By.TAG_NAME, "p")
        #for index, element in enumerate(elements):
        #    print(f"Found text at index {index}: {element.text}")

        # Wait for the result text to be present
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(., 'Gender :')]")))

        # Extract the correct gender and age text
        gender_text = driver.find_element(By.XPATH, "//p[contains(., 'Gender :')]").text
        age_text = driver.find_element(By.XPATH, "//p[contains(., 'Age :')]").text

        # Print extracted values
        #print("Extracted Gender Text:", gender_text)
        #print("Extracted Age Text:", age_text)

        # Soft Assertions
        self.soft_assert(self.assertIn, "Gender : Male", gender_text, f"Expected 'Gender : Male', but got '{gender_text}'")
        self.soft_assert(self.assertIn, "Age : 0 - 5", age_text, f"Expected 'Age : 0 - 5', but got '{age_text}'")

        # Perform all soft assertions
        self.assert_all()

        driver.quit()  # Ensure the browser closes after execution
