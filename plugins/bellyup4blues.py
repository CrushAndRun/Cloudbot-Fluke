#Grabs Current Info for bellyup4blues Stream

import requests
import re
from cloudbot import hook
import urllib
import urllib.request

url = "http://72.13.82.82:5100/7.html"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)',
        'Referer': 'http://www.thereeftank.com/forums/'}

@hook.command("bu4b", autohelp=False)
def bellyup4blues(text):

    req = urllib.request.Request(url, data=None, headers=headers)
    html = urllib.request.urlopen(req).read()
    song = str(html).split("<body>")[1].split("</body>")[0].split(",")[6]
    filtered = "Now Playing at http://bellyup4blues.com/: " + song "Add http://72.13.82.82:5100/listen.pls to your media player."
    out = filtered
    return out
