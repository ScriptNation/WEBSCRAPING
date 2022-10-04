import requests
from bs4 import BeautifulSoup

# GET REQUEST FROM URL + RETURNING RESPONSE.text
def getdata(url):
    r = requests.get(url)
    return r.text

# USING GETDATA FUNCTION WITH TEST URL TO GET IMAGES FROM
htmldata = getdata("https://www.geeksforgeeks.org/")
# BeautifulSoup GIVES US OBJECT - DOCUMENT AS NESTED DATA STRUCTURE
soup = BeautifulSoup(htmldata, 'html.parser')

# LOOKING FOR A IMG TAG FROM GIVEN SITE
items = soup.find_all('img')
for item in items:
    print(item['src'])
