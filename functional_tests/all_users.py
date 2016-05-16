# import python lib for testing
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        """
        initialize the test, it opens browser and it waits for 3 seconds
        if needs to(if the page is not loaded)

        this method runs at the beginning and the end of each test
        """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """
        this method runs after each test. It closes the browser
        this method runs at the beginning and the end of each test
        """
        self.browser.quit()

    def test_it_worked(self):
        """
        this method starts with test and that asserts that the title if the
        webpage has Welcome to Django in it
        """
        self.browser.get("http://localhost:8000")
        self.assertIn("Welcome to Django", self.browser.title)

"""
only if Python runs the file directly(not imported), it will execute the function
unittest.main()

this function launches the unittest Test runner, that identifies the different
tests defined by looking for methods that start with test
"""
if __name__ == '__main__':
    """
    call the function below with an optional parameter warnings='ignore' to
    avoid a Resource Warning message
    """
    unittest.main(warnings='ignore')
