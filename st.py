from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AbdullahWebsiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("https://rgates574717459-canary.azurewebsites.net/") 

    def test_about_section_content(self):
        about_section = self.driver.find_element(By.ID, "about")
        self.assertTrue(about_section.is_displayed())

        about_text = about_section.find_element(By.TAG_NAME, "p").text
        self.assertNotEqual(about_text, "")  # Check if about section text is not empty

    def test_contact_section_content(self):
        contact_section = self.driver.find_element(By.ID, "contact")
        self.assertTrue(contact_section.is_displayed())

        contact_info = contact_section.find_elements(By.TAG_NAME, "p")
        self.assertTrue(len(contact_info) >= 4)  # Ensure there are at least 4 contact information items

    def test_navigation_links(self):
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, "nav a")
        self.assertEqual(len(nav_links), 4)  # Ensure there are 4 navigation links
        
        for link in nav_links:
            href = link.get_attribute("href")
            self.assertNotEqual(href, "")  # Check if the href attribute is not empty

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
