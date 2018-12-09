################################################################################
# AISHA MCLEAN 09 12 2018 ######################################################

# Requires chromedriver to be in PATH or same directory as script

################################################################################
# USING ########################################################################

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

################################################################################
# VARIABLES ####################################################################

name = "Aisha McLean"

# set debug mode
debug = False
if len(sys.argv) > 1 and sys.argv[1] == "debug":
    debug = True

# test function with test array
test_array = [10, 15, 5, 7, 1, 24, 36, 2] # answer = index 5, value 24

################################################################################
# FUNCTIONS ####################################################################

# Once you have each array, write a function that is able to return the index of the array
# where the sum of integers at the index on the left is equal to the sum of integers on the right.
# If there is no index return null

def array_center_finder(array):
    answer = None
    if debug:
        print("\nArray: ",array)
    for array_index in range(len(array)):
        item = array[array_index]
        left = array[0:array_index]
        right = array[array_index+1:len(array)]
        sum_left = sum(left)
        sum_right = sum(right)
        if debug:
            print("index: ",array_index,", value: ",item)
            print(" > left: ", left, ", sum:", sum_left)
            print(" > right: ", right,", sum:", sum_right)
        if sum_left is sum_right:
            if debug:
                print("\nCenter of array is index ", array_index, "( which has a value of ",item,").\n")
            answer = array_index
            break
    return answer

# function to submit test results
def submit_results(answer_1, answer_2, answer_3):
    # get elements
    answer_space_1 = driver.find_element_by_xpath("//*[@data-test-id='submit-1']")
    answer_space_2 = driver.find_element_by_xpath("//*[@data-test-id='submit-2']")
    answer_space_3 = driver.find_element_by_xpath("//*[@data-test-id='submit-3']")
    answer_space_4 = driver.find_element_by_xpath("//*[@data-test-id='submit-4']")
    submit = driver.find_element_by_xpath("//*[@id='challenge']/div/div/div[2]/div/div[2]/button")
    # fill answers
    answer_space_1.send_keys(answer_1)
    answer_space_2.send_keys(answer_2)
    answer_space_3.send_keys(answer_3)
    answer_space_4.send_keys(name)
    # submit
    submit.send_keys(Keys.RETURN)
    print("\nSubmitted answers and name: ",answer_1,answer_2,answer_3,name)

################################################################################
# WEBDRIVER ####################################################################

# Test site
webpage = "http://localhost:3000/"

# Driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 100)

################################################################################
# RUN SCRIPT ###################################################################

driver.get(webpage)
print("Opening page: ",driver.title)

try:
    render_challenge = driver.find_element_by_xpath("//button[@data-test-id='render-challenge']")
    render_challenge.send_keys(Keys.RETURN)

    # Challenge
    challenge = driver.find_elements_by_xpath("//section[@id='challenge']/div/div/h1")
    challenge_title = challenge[0].get_attribute("innerText")
    print("\nSection heading: ", challenge_title)

    # Read in whole data table
    table = driver.find_element_by_xpath("//*[@id='challenge']/div/div/div[1]/div/div[2]/table")

    # read in each row
    array_1 = driver.find_element_by_xpath("//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[1]").get_attribute("innerText").split()
    array_2 = driver.find_element_by_xpath("//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[2]").get_attribute("innerText").split()
    array_3 = driver.find_element_by_xpath("//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[3]").get_attribute("innerText").split()

    # convert to ints
    array_1 = [int(i) for i in array_1]
    array_2 = [int(i) for i in array_2]
    array_3 = [int(i) for i in array_3]

    # find center of array
    if debug:
        center_test = array_center_finder(test_array)
    center_1 = array_center_finder(array_1)
    center_2 = array_center_finder(array_2)
    center_3 = array_center_finder(array_3)

    # print results to console
    if debug:
        print("Center of test array: ",center_test)
    print("Center of array 1: ",center_1)
    print("Center of array 2: ",center_2)
    print("Center of array 3: ",center_3)

    # submit answers
    submit_results(center_1,center_2,center_3)

# catch errors and print
except ValueError as err:
    print(err)

# Close driver regardless
finally:
    if debug:
        usr_input = input("Press enter to quit")
    driver.close()
