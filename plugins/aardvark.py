import requests
import re
from cloudbot import hook
import urllib
import urllib.request

@hook.command("aardvark", autohelp=False)
def aardvark(text):

    url = "http://orion.prostreaming.net:8288/7.html"
    html = urllib.request.urlopen(url).read()
    htmlout = html[35:-14]
    pw_bytes = htmlout.decode("utf-8")
    filtered = pw_bytes.replace("&apos;", "'")
    filtered = "Now on the Aardvark Radio Stream: " + filtered
    out = filtered
    return out
