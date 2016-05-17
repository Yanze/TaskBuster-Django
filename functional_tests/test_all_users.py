# import python lib for testing
from selenium import webdriver
# import unittest
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class HomeNewVisitorTest(StaticLiveServerTestCase):
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

    def get_full_url(self, namespace):
        # self.live_server_url gives the local host url.
        # reverse gives the relative url of a given namespace /
        return self.live_server_url + reverse(namespace)

    # this method tests the homepage title contains the words TaskBuster
    # if exists, it means that the template has been loaded corrctly
    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgba(200, 50, 255, 1)")

    # def test_it_worked(self):
    #     """
    #     this method starts with test and that asserts that the title if the
    #     webpage has Welcome to Django in it
    #     """
    #     self.browser.get("http://localhost:8000")
    #     self.assertIn("Welcome to Django", self.browser.title)

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
