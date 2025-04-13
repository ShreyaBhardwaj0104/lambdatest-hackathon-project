
def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element("id", "username").send_keys("tomsmith")
    driver.find_element("id", "password").send_keys("SuperSecretPassword!")
    driver.find_element("css selector", "button[type='submit']").click()
    assert "You logged into a secure area!" in driver.find_element("id", "flash").text

def test_invalid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element("id", "username").send_keys("wrong")
    driver.find_element("id", "password").send_keys("wrong")
    driver.find_element("css selector", "button[type='submit']").click()
    assert "Your username is invalid!" in driver.find_element("id", "flash").text
