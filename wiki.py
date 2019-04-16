# ______________________________________________________________________________________________________
#                                      Wiki-py-dia 
# shell script to get first paragraph of wikipedia page 
# $ python wiki.py -string
# ______________________________________________________________________________________________________
from bs4 import BeautifulSoup
import argparse
import requests

WIKI_URL = 'https://en.wikipedia.org/wiki/'

# get the page 
def call_wiki(search_text):
    page = requests.get( WIKI_URL + search_text)
    return page

# a function to get teh first paragraph 

def get_first_para(page):
    return

# invoke main
if __name__ == "__main__":
    # parse argument
    call_wiki(search_text)
