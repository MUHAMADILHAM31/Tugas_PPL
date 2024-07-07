import unittest
from selenium import webdriver

class TestCandidates(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
    
    def test_add_candidate(self):
        driver = self.driver
        # Log in
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        
        # Navigate to Candidates
        driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").click()
        driver.find_element_by_id("menu_recruitment_viewCandidates").click()
        
        # Add a new candidate
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("addCandidate_firstName").send_keys("Jane")
        driver.find_element_by_id("addCandidate_lastName").send_keys("Doe")
        driver.find_element_by_id("addCandidate_email").send_keys("jane.doe@example.com")
        driver.find_element_by_id("btnSave").click()
        
        # Verify candidate added
        candidate_list = driver.find_element_by_id("resultTable").text
        self.assertIn("Jane Doe", candidate_list)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
