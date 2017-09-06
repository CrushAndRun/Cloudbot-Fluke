from cloudbot import hook
from bs4 import BeautifulSoup
import random
import urllib
import urllib.request

URL = 'http://www.food.com/'

def parseRecipePage(html):
    soup = BeautifulSoup(html, "html.parser")
    breadcrumbs = soup.find('div', 'breadcrumbs')
    if not breadcrumbs:
        return (None, None)
    title = soup.title.string
    if title:
        title = title.split('-')[0] # strip '- Food.com' from the title
    return title

@hook.command("food", autohelp=False)
def food(text):
    """Gets a random recipe from food.com"""
    url = URL + str(random.randint(2670, 100000))
    response = urllib.request.urlopen(url)
    html = response.read()
    title = parseRecipePage(html)
    return "Recipe: "+title+" | URL: "+url
