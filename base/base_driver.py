import time


class BaseDriver():
    def __init__(self,driver):
        self.driver = driver

    def page_scroll(self):
                # Scroll to the top of the page
        pageLength = self.driver.execute_script("window.scrollTo(0, 0);")

        # Rest of the code remains the same
        match = False
        while not match:
            lastCount = pageLength
            time.sleep(1)
            pageLength = self.driver.execute_script("window.scrollTo(0, 0);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)

    def locate_element(self,locator_type,locator):
        element = self.driver.find_element(locator_type,locator)
        return element



