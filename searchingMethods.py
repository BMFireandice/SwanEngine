from bs4 import BeautifulSoup
import requests

# https://scholar.google.com/scholar?hl=en&as_sdt=0%2C30&q=lma&btnG=
#                                                         ^ query up to the &btnG=

def searchLink(query, pageNum):

    url = f'https://scholar.google.com/scholar?start={pageNum}&q={query}&hl=en&as_sdt=0,30' # plug in query and page number to Scholar
    response = requests.get(url, headers={"Content-Type":"text"}) # holds all the html of the response
    soup = BeautifulSoup(response.content,'lxml')

    allResults = []

    for item in soup.select('[data-lid]'):
        try:

            allResults.append(item.select('a')[0]['href']) # adds all links to a list

        except Exception as e:
            print('')
            
    return allResults # returns the list

def searchTitles(query, pageNum):
 
    url = f'https://scholar.google.com/scholar?start={pageNum}&q={query}&hl=en&as_sdt=0,30' # plug in query and page number to Scholar
    response = requests.get(url, headers={"Content-Type":"text"})# holds all the html of the response
    soup = BeautifulSoup(response.content,'lxml')

    allResults = []

    for item in soup.select('[data-lid]'):
        try:
            allResults.append(item.select('h3')[0].get_text()) # adds all titles to a list
        except Exception as e:
            print('')
    return allResults # returns the list

def searchMinorText(query, pageNum):

    url = f'https://scholar.google.com/scholar?start={pageNum}&q={query}&hl=en&as_sdt=0,30'# plug in query and page number to Scholar
    response = requests.get(url, headers={"Content-Type":"text"}) # holds all the html of the response
    soup = BeautifulSoup(response.content,'lxml')

    allResults = []


    for item in soup.select('[data-lid]'):
        try:
            allResults.append(item.select('.gs_rs')[0].get_text()) # adds all subtext to a list

        except Exception as e:
            print('')
    return allResults # returns the list
    
def searchAuthor(query, pageNum):

    url = f'https://scholar.google.com/scholar?start={pageNum}&q={query}&hl=en&as_sdt=0,30'# plug in query and page number to Scholar
    response = requests.get(url, headers={"Content-Type":"text"}) # holds all the html of the response
    soup = BeautifulSoup(response.content,'lxml')

    allResults = []


    for item in soup.select('[data-lid]'):
        try:
            allResults.append(item.select('.gs_a')[0].get_text()) # adds all authors to a list

        except Exception as e:
            print('')
    return allResults # returns the list
    
