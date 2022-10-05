import requests
from bs4 import BeautifulSoup
import os

# OPTIONAL
KEYWORD = ''

# GET REQUEST FROM URL
def getdata(url):
    r = requests.get(url)
    return r.text
  
def scraperFunction(targetURL,folderName):
    try:
        os.mkdir(os.path.join(os.getcwd() + folderName))
    except:
        pass
    os.chdir(os.path.join(os.getcwd() + folderName))

    # TARGET URL TO GET IMAGES FROM
    htmldata = getdata(targetURL)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # LOOKING FOR A IMG TAG
    items = soup.find_all('img')

    #baseurl = "..."
    for item in items:
        name = item['alt']
        link = item['src']
        #if (link[0] != 'h'):
          #  link = baseurl + link
        with open(name.replace(' ','-').replace('/','').replace(',','').replace('?','') + '.jpg','wb') as f:
            im = requests.get(link)
            if (KEYWORD in name):
                print(f'found {KEYWORD} in name: '+ name)
                print('Downloading the image.. ' )
                f.write(im.content)
                
# ENTER THE URL OF TARGETED WEBSITE FOR IMAGE SCRAPE, NAME YOUR FOLDER WHERE THEY WILL BE DOWNLOADED
scraperFunction("<URL>","FolderName")
