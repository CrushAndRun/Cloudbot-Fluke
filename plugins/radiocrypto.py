import requests
import re
from cloudbot import hook
import urllib
import urllib.request

@hook.command("radiocrypto", autohelp=False)
def radiocrypto(text):

    url = "http://104.131.121.96:8000/7.html"
    html = urllib.request.urlopen(url).read()
    htmlout = html[30:-14]
    pw_bytes = htmlout.decode("utf-8")
    filtered = pw_bytes.replace("&apos;", "'")
    filtered = "Now on the http://radiocrypto.com/ Radio Stream: " + filtered
    out = filtered
return out
