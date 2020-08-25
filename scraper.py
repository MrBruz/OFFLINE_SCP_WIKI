import requests
import urllib.request
import bz2
import os
import sys
from bs4 import BeautifulSoup

site = "http://www.scpwiki.com/"
scp = "scp-127"
command = ""


def scrape (URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find('div', id='main-content')
    for getimgtag in content.findAll('img',src=True):
        imgLink = getimgtag['src']
        if ".jpg" in imgLink or ".jpeg" in imgLink or ".png" in imgLink or ".gif" in imgLink or ".bmp" in imgLink or ".webp" in imgLink:
            imgTag = imgLink.split('/')
            imgTag2 = imgTag[len(imgTag)-1]
            #urllib.request.urlretrieve(imgLink, 'WebsiteTemp/SCPImages/' + imgTag2)
            img_urls = getimgtag['src'].replace(imgLink, 'SCPImages/' + imgTag2)
            getimgtag['src'] = img_urls
    for getatag in content.findAll('a',href=True):
        aLink = getatag['href']
        if '/scp-' in aLink and not 'scp-wiki.net' in aLink:
            finalLink = '/scp/?scp=' + aLink.split('/scp-')[1]
            a_urls = getatag['href'].replace(aLink, finalLink)
            getatag['href'] = a_urls

    return bz2.compress(content.encode())

def write(data,filename):
    with open(filename, "wb") as f:
        f.write(data)

def read(filename):
    with open(filename, "rb") as f:
        return bz2.decompress(f.read()).decode()

def writeWebpage(decomp):
    f_old = open("SCP Foundation.html")
    f_new = open("static/build.html", "w", encoding="utf-8")
    global scpNum
    for line in f_old:
        f_new.write(line)
        if '<!-- Put main-content here -->' in line:
            f_new.write(str(decomp) + "\n")
        if '<!-- Put title here -->' in line:
            f_new.write('<title>SCP-' + scpNum + ' - SCP Foundation</title>' + "\n")

    f_old.close()
    f_new.close()

def resetWebpage():
    f = open("static/build.html", "w")
    f.write("")

def massScrape():
    for i in range(6000):
        print('Scraping SCP-' + f'{i:03}')
        scp = "scp-" + f'{i:03}'
        if not os.path.isfile('SCPscrapes/' + scp + '.bz2'):
            try:
                write(scrape(site + scp),'SCPscrapes/' + scp + '.bz2')
            except:
                print("Failed to download " + scp)


#write(scrape(site + scp),'SCPscrapes/' + scp + '.bz2')
#print(read('SCPscrapes/' + scp + '.bz2'))
def scp(scpNum):
    resetWebpage()
    scpText = 'scp-' + scpNum
    #write(scrape(site + scpText),'SCPscrapes/' + scpText + '.bz2')
    writeWebpage(read('SCPscrapes/' + scpText + '.bz2'))

massScrape()
