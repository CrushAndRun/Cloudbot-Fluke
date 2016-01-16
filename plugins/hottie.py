import random
import requests
from cloudbot import hook

@hook.command(autohelp=False)
def hottie():
    """Lets get a hot girl for you"""
    while True:
        responsepre = "/girl/"
        while ("/girl/" in responsepre):
            attempts = 0
            try:
                r = requests.get("http://best-hot-girls.com/random/")

            except:
                if attempts > 2:
                    randerrmsg = random.randint(0,2)

                        if randerrmsg == 0:
                            return "There was an error finding a hot girl for you."
                        elif randerrmsg == 1:
                            return "You don't deserve a hot girl."
                        elif randerrmsg == 2:
                            return "No hot girl for you today."
                        else:
                            return "There was an error finding a hot girl for you."
                                
                else:
                    attempts += 1
                    continue
            responsepre = r.url

        response = responsepre

        total = len(response) + 1

        appendix1 = "http://best-hot-girls.com/"
        appendix1_length = len(appendix1)

        randomIdentifier = response[appendix1_length:total]

        hottieurl = "http://i.best-hot-girls.com/"+randomIdentifier+".jpg"

        randseed = random.randint(0,10)

        if randseed == 0:
            return "Let's have fun tonight! {}".format(hottieurl)
        elif randseed == 1:
            return "Wanna invite me over? {}".format(hottieurl)
        elif randseed == 2:
            return "I've got you on my radar babe~ {}".format(hottieurl)
        elif randseed == 3:
            return "Are you ready for me? {}".format(hottieurl)
        elif randseed == 4:
            return "Hello sweetheart :* {}".format(hottieurl)
        elif randseed == 5:
            return "Wanna touch me at inappropriate places? {}".format(hottieurl)
        elif randseed == 6:
            return "Let's break your bed~ {}".format(hottieurl)
        elif randseed == 7:
            return "Show me what you've got! {}".format(hottieurl)
        elif randseed == 8:
            return "You should get to know me better~ {}".format(hottieurl)
        elif randseed == 9:
            return "Do you like me? {}".format(hottieurl)
        elif randseed == 10:
            return "Wanna make out? {}".format(hottieurl)
        else:
            return "Wanna make out? {}".format(hottieurl)
