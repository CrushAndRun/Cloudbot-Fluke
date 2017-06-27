import re
from util import hook, http, misc
from BeautifulSoup import BeautifulSoup


@hook.command(autohelp=False)
def wotd(inp, say=False, nick=False):
    "wotd -- Gets the word of the day from merriam-webster.com."
    page = http.get('http://merriam-webster.com/word-of-the-day')

    soup = BeautifulSoup(page)

    wotd = soup.find('strong', {'class': 'main_entry_word'}).renderContents()
    function = soup.find('p', {'class': 'word_function'}).renderContents()

    #definitions = re.findall(r'<span class="ssens"><strong>:</strong>'
    #                        r' *([^<]+)</span>', content)

    say("(%s) The word of the day from merriam-webster.com is:"\
" \x02%s\x02 (%s)" % (nick, word, function))
