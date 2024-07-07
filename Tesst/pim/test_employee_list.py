import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Teardown WebDriver
    driver.quit()

def test_add_employee(driver):
    # Navigate to login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login as Admin
    login(driver)
    
    # Navigate to PIM -> Add Employee
    navigate_to_add_employee(driver)
    
    # Add Employee Test Case
    add_employee(driver)

def login(driver):
    # Perform login
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    driver.find_element(By.ID, "btnLogin").click()

def navigate_to_add_employee(driver):
    # Navigate to PIM -> Add Employee
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewPimModule"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_addEmployee"))).click()

def add_employee(driver):
    # Fill in employee details
    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Smith")
    driver.find_element(By.ID, "btnSave").click()
    
    # Verification - Check if employee is added successfully (you can add assertions here)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-pic")))

    # Optional: Log out after adding employee (uncomment if needed)
    # logout(driver)

def logout(driver):
    # Logout functionality
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "welcome"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

