from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_lambdatest_radio_button_demo_values():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    driver.find_element(By.XPATH, "//input[@value='Male' and @name='gender']").click()
    driver.find_element(By.XPATH, "//input[@value='0 - 5' and @name='ageGroup']").click()
    driver.find_element(By.XPATH, "//button[text()='Get values']").click()
    elements = driver.find_elements(By.TAG_NAME, "p")
    for index, element in enumerate(elements):
        print(f"Found text at index {index}: {element.text}")

    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(., 'Gender :')]")))

    gender_text = driver.find_element(By.XPATH, "//p[contains(., 'Gender :')]").text
    age_text = driver.find_element(By.XPATH, "//p[contains(., 'Age :')]").text
    print("Extracted Gender Text:", gender_text)
    print("Extracted Age Text:", age_text)

    # Validate output correctly
    assert "Gender : Male" in gender_text, f"Expected 'Gender : Male', but got '{gender_text}'"
    assert "Age : 0 - 5" in age_text, f"Expected 'Age : 0 - 5', but got '{age_text}'"

    driver.quit()  # Ensure browser closes after execution
