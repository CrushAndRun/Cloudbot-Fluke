#Grabs Current Info for bellyup4blues Stream

import requests
import re
from cloudbot import hook
import urllib
import urllib.request

url = "http://72.13.82.82:5100/7.html"


@hook.command("bu4b", autohelp=False)
def bellyup4blues(text):

    url = "http://72.13.82.82:5100/7.html"
    html = urllib.request.urlopen(url).read()
    htmlout = html[28:-15]
    pw_bytes = htmlout.decode("utf-8")
    filtered = pw_bytes.replace("&apos;", "'")
    filtered = "Now Playing at http://bellyup4blues.com/: " + filtered
    out = filtered
return out
