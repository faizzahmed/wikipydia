# ______________________________________________________________________________________________________
#                                      Wiki-py-dia 
# shell script to get first paragraph of wikipedia page 
# $ python wiki.py -string
# ______________________________________________________________________________________________________
from bs4 import BeautifulSoup
import sys
import requests

class wiki():

    WIKI_URL = 'https://en.wikipedia.org/wiki/'

    def __init__(self,data):
        self.data = data
        self.page = requests.get(self.WIKI_URL + self.data)
        self.wiki = BeautifulSoup(self.page.content, 'html.parser')
        self.all_p = self.wiki.find('div',attrs={"class":"mw-parser-output"}).findAll('p')
        # print(self.all_p)

    def get_firstpara(self):
        if len(self.all_p) < 2:
            return 'too many possibilities!!!!'
        else:    
            return self.all_p[2].text

# invoke main
if __name__ == "__main__":

    print ( 'Argument List:', str(sys.argv[1]) )

    wiki1 = wiki(str(sys.argv[1]))
    print (wiki1.get_firstpara())
    # call_wiki(str(sys.argv[1]))
