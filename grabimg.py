#coding = utf-8
import sys
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8') #coverts bytes type to string
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" alt='
    imgre = re.compile(reg)
    imglist = imgre.findall(html)

    x = 0
    for imgurl in imglist:
        seg = imgurl.split("/") # download name
        urllib.request.urlretrieve(imgurl, seg[-1])
        x+=1
    return imglist

html = getHtml(sys.argv[1])
print (getImg(html))
