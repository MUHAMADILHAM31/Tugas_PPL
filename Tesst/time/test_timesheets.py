import unittest
from selenium import webdriver

class TestTimesheets(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
    
    def test_submit_timesheet(self):
        driver = self.driver
        # Log in
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        
        # Navigate to Timesheets
        driver.find_element_by_id("menu_time_viewTimeModule").click()
        driver.find_element_by_id("menu_time_Timesheets").click()
        
        # Submit timesheet
        driver.find_element_by_id("btnAddTimesheet").click()
        driver.find_element_by_id("time_date").send_keys("2024-07-10")
        driver.find_element_by_id("btnAdd").click()
        
        # Verify timesheet is submitted
        confirmation = driver.find_element_by_css_selector(".message.success").text
        self.assertIn("Timesheet Created", confirmation)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
