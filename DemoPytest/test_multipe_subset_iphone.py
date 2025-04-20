from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.XPATH, "//input[@placeholder='Search For Products']").send_keys("iphone")
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    search_value = driver.find_element(By.XPATH, "//h1[contains(text(),'Search')]").text
    assert "iphone" in search_value, f"Expected 'Iphone' in search value, but got '{search_value}'"
    driver.quit()  # Ensure browser closes after execution 
    
def test_add_to_cart():
    result = 1
    print("Add to cart test result:", result)
    assert result == 3 