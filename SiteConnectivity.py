"""
Simply checks if the inputted url can be connected to
"""

import urllib.request

def check_site(url):
    """
    Checks the connectivity of a website
    """
    print("Checking connectivity...")
    try:
        response = urllib.request.urlopen(url)
        print(f"Connected to {url} successfully!")
    except ValueError:
        print("The site cannot be connected to.")
    try:
        print(f"The response code is {response.getcode()}")
    except UnboundLocalError:
        print(f"The site does not exist.\nNo response code available.")
    

#starts program
print("This program will check the connectivity of a website.")
input_url = input("Please enter the url of the website you would like to check: ")
check_site(input_url)