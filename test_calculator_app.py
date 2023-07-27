from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import time

# Import necessary modules for explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Disable SSL certificate verification
WebDriver.DEFAULT_SECURE_SSL = False

desired_caps = {
    'deviceName': 'Android',
    'platformName': 'Android',
    'appPackage': 'com.google.android.calculator',  # Update with the correct app package name
    'appActivity': 'com.android.calculator2.Calculator',
    # Update with the correct launchable activity name
    'newCommandTimeout': 600,
    'uiautomator2ServerLaunchTimeout': 60000
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Create a WebDriverWait object for explicit waits with a timeout of 20 seconds
wait = WebDriverWait(driver, 20)

button1 = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, '5')))
button1.click()
button0 = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, '0')))
button0.click()

plus = wait.until(EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/op_add')))
plus.click()

button2 = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, '5')))
button2.click()

equal = wait.until(EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/eq')))
equal.click()


clear = wait.until(EC.element_to_be_clickable((By.ID,'com.google.android.calculator:id/clr')))
clear.click()

minus1= wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, '2')))
minus1.click()

minus2 = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, '0')))
minus2.click()

minus = wait.until(EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/op_sub')))
minus.click()

minus3= wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, '1')))
minus3.click()

minus4 = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, '0')))
minus4.click()

equal1 = wait.until(EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/eq')))
equal1.click()

clear2 = wait.until(EC.element_to_be_clickable((By.ID, 'com.google.android.calculator:id/clr')))
clear2.click()

print("Thanks For Using Our Calculator")

time.sleep(5)
driver.quit()