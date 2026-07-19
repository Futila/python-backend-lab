# Lib Request - is a third-party module that allows you to send HTTP requests using Python.
#  It is not included in the standard library, so you need to install it separately using pip.

# pip install requests


print("\n Importing and using a third-party module - Requests \n")

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
print("Response Status Code:", response.status_code)