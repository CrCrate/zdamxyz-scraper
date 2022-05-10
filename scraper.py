import requests
from bs4 import BeautifulSoup
import os
 
pageinfo = []
pageid = int(input("start page id: "))
endid = int(input("end page id: "))
 
while pageid <= endid:
    pageinfo = []
    try:
        sheet = requests.get("https://zdam.xyz/" + str(pageid))
        page = sheet.text
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('li'):
            if link.get('class') == ['breadcrumb-item']:
                try:
                    pageinfo.append(link.string.strip())
                except:
                    print("")
        for link in soup.find_all('img'):
            if link.get('class') == ['img-fluid']:
                imgurl = link.get('src')
                imgtitle = link.get('alt')[0:32]
        print("saving", pageid)
        print(pageinfo)
        
        filedir = pageinfo[0]+"/"+pageinfo[1]+"/"
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        r = requests.get(imgurl)  
        with open(filedir + imgtitle + ".png", 'wb') as f:
            f.write(r.content)
        
    except:
        print(sheet.status_code)
    pageid = pageid + 1