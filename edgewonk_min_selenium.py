from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

LOGIN_URL = "https://edgewonk.app/login"
DRIVER_PATH = '/Users/talksik/Downloads/chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
wait = WebDriverWait(driver, 10)

# Login functionality
driver.get(LOGIN_URL)
MY_EMAIL = 'patel.arjun50@gmail.com'
MY_PASSWORD = '@4kLew2!JG!9FK!'
email = driver.find_element_by_id('mat-input-0').send_keys(MY_EMAIL)
password = driver.find_element_by_id('mat-input-1').send_keys(MY_PASSWORD)
driver.find_element_by_xpath('//button').click()

# select second account - the one I mainly want to mine
second_account = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[mat-button]'))
)
second_account[2].click()
print('clicked the second account')

# go through each account to mine each one as a wrapper for loop
# in the future
# accounts_list = driver.find_elements_by_xpath('//@mat-button')
# print(accounts_list)

# Navigate to the Journal Page
journal_nav = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/journal']"))
)
journal_nav.click()
print('navigating to the trade journal page')


# Mine each trade in each page
# mine each page
is_last_page = False
while not is_last_page:
    # mine each trade in the current page
    driver.implicitly_wait(2) # seconds

    trades_on_this_page = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.ag-row[role='row'][row-index]"))
    )

    # if the next page button is disabled, stop  
    is_last_page = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[ref='btNext']"))
    ) 
    is_last_page = is_last_page.get_attribute('aria-disabled') == 'true'

    for trade_element in trades_on_this_page:
        # print all data that I need first
        row_index = trade_element.get_attribute('row-index')
        print(row_index)

        grid_cells = trade_element.find_elements_by_css_selector("span")
        # for grid_cell in grid_cells:
        #     print(grid_cell.text())
        # dump current trade into csv
        # click on the trade to get more metadata
        # dump more data that I need
        # click on cancel

    # navigate to the next page if not the last_page
    if not is_last_page:
        next_page_arrow = driver.find_element_by_css_selector("div[ref='btNext']")
        next_page_arrow.click()
        print('going to the next page for more trades')
    else:
        print('done...last page')
        
        
# print(driver.page_source)

# original_stdout = sys.stdout # Save a reference to the original standard output

# # output to file in same directory
# with open('output.html', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print('This message will be written to a file.')
#     sys.stdout = original_stdout # Reset the standard output to its original value

