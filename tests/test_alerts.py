
import time

def test_js_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    alert.accept()
    result = driver.find_element("id", "result").text
    assert "You successfully clicked an alert" in result

def test_js_confirm_ok(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()
    driver.switch_to.alert.accept()
    assert "You clicked: Ok" in driver.find_element("id", "result").text

def test_js_prompt_input(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element("xpath", "//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    alert.send_keys("hello")
    alert.accept()
    assert "You entered: hello" in driver.find_element("id", "result").text
