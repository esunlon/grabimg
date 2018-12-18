#coding = utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
html = getHtml("http://pic.yxdown.com/list/0_0_1.html")

print (html)
