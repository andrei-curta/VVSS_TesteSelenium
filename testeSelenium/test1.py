#!/usr/bin/env python3
from selenium import webdriver
p = "ParolaUnitbv1"


# driver.set_page_load_timeout(10)
# driver.get("http://google.com")
# driver.find_element_by_name("q").send_keys("vadim")
# driver.find_element_by_class_name("btnK").click()


"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    # driver = webdriver.Chrome(r"E:/Facultate/Anul_III/VVSS/chromedriver.exe")
    # driver.set_page_load_timeout(10)
    # driver.get("http://google.com")
    # driver.find_element_by_name("q").send_keys("vadim tudor")
    # driver.find_element_by_name("btnK").click()

    driver = webdriver.Chrome(r"E:/Facultate/Anul_III/VVSS/chromedriver.exe")
    driver.set_page_load_timeout(10)
    driver.get("https://elearning.unitbv.ro/login/index.php")
    driver.find_element_by_name("username").send_keys("andrei.curta@student.unitbv.ro")
    driver.find_element_by_name("password").send_keys(p)
    driver.find_element_by_id("loginbtn").click()
    driver.find_element_by_class_name("column c1").click()
    driver.find_element_by_class_id("module-64466").click()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()