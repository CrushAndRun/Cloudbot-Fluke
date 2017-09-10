from cloudbot import hook
import textwrap
import re
from bs4 import BeautifulSoup
import urllib
import urllib.request

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)',
        'Referer': 'http://www.thereeftank.com/forums/'}

n = 300

@hook.command("bash", autohelp=False)
def bash(text, conn, nick, chan):
    """[<id>] Returns a random geek quote from bash.org; the optional argument <id> specifies which quote to retrieve."""
    url = 'http://bash.org/?'
    if text:
        text = text.split(" ")
    else:
        text = "random"
    try:
        text = int(text[0])
    except:
        text = 'random'
    url = url+str(text)
    req = urllib.request.Request(url, data=None, headers=headers)
    html_str = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html_str, "html.parser")
    thequote = soup.find("p", { "class" : "qt" })
    if text != "random":
        quote_number = "#"+str(text)
    else:
        quote_header = soup.find("p", { "class" : "quote" })
        ahref = quote_header.find("a", href=True)
        quote_number = str(ahref.find("b"))
        quote_number = quote_number.lstrip("<b>").rstrip("</b>")
    if thequote == None:
        thequote = 'Quote #' + str(text) + ' does not exist.'
    else:
        thequote = str(thequote)
        thequote = thequote.replace('<p class="qt">', '' )
        thequote = thequote.replace('</p>', '' )
        thequote = thequote.replace('<br />', '' )
        thequote = thequote.replace('<br/>', '' )
        thequote = thequote.replace('<br>', '' )
        thequote = thequote.replace('</br>', '' )
        thequote = thequote.replace('&lt;', '<')
        thequote = thequote.replace('&gt;', '>')
        thequote = thequote.replace('\n', ' // ')
    targetnick = nick
    reply = "("+targetnick+") "+quote_number+": "+thequote
    reply = textwrap.wrap(reply, n, break_long_words=False)
    for i in reply:
        conn.cmd("PRIVMSG " + chan + " :"+i)
