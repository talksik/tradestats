from bs4 import BeautifulSoup
import requests
import sys

login_URL = "https://edgewonk.app/login"
page = requests.get(login_URL)


print('This message will be displayed on the screen.')

original_stdout = sys.stdout # Save a reference to the original standard output

# output to file in same directory
with open('output.html', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('This message will be written to a file.')
    print(page.text)
    sys.stdout = original_stdout # Reset the standard output to its original value
