from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

# Instagram login credentials
username = "your_username"
password = "your_password"

# Set up WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)  # Wait for page to load

# Enter username
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)
time.sleep(1)

# Enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)
time.sleep(1)

# Submit the login form
password_input.send_keys(Keys.RETURN)
time.sleep(5)  # Wait for login to complete

# Navigate to a specific post (replace with the URL of the post you want to like)
post_url = "https://www.instagram.com/p/CODE/"
driver.get(post_url)
time.sleep(3)

# Like the post
like_button = driver.find_element(By.XPATH, "//span[@aria-label='Like']")
like_button.click()

# Optional: Close the browser after automation
time.sleep(5)
driver.quit()

