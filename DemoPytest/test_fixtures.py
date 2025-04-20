import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
  print("Start Test With Automatic Fixture")

@pytest.fixture()
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.find_element(By.ID, "input-email").send_keys("pytestlearningselenium@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("DP9eznQHLCKjY@n")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    print("Log In")

    # Wait until 'Logout' is clickable (means login succeeded)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Logout"))
    )

    yield

    # Wait and click logout safely
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Logout"))
        ).click()
        print("Log Out")
    except Exception as e:
        print(f"Error during logout: {e}")


def test1_order_history_title(setup_teardown):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Order"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.title_is("Order History")
    )
    assert driver.title == "Order History"
    print("Test 1 Is Complete")


def test2_change_password_title(setup_teardown):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Password"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.title_is("Change Password")
    )
    assert driver.title == "Change Password"
    print("Test 2 Is Complete")
