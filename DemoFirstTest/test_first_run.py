from selenium import webdriver

def test_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://lambdatest.com/selenium-playground/")
    print("Title:",driver.title)


def test2_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print("Title:",driver.title)