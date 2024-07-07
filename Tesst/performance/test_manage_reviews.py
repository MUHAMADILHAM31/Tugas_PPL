import unittest
from selenium import webdriver

class TestManageReviews(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
    
    def test_manage_reviews(self):
        driver = self.driver
        # Log in
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        
        # Navigate to Manage Reviews
        driver.find_element_by_id("menu__Performance").click()
        driver.find_element_by_id("menu_performance_ManageReviews").click()
        
        # Add or update a review
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("saveReview").send_keys("Excellent performance.")
        driver.find_element_by_id("btnSave").click()
        
        # Verify review is saved
        review_list = driver.find_element_by_id("resultTable").text
        self.assertIn("Excellent performance.", review_list)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
