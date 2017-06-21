from cloudbot import hook
import random

fourtwentys = ['OMG THANKS!', 
               'grips it and rips it, THANKS!', 
		       'puff puff pass!', 
		       'much appreciated', 
		       'AWESOMESAUCE', 
		       'AWW YEE ( \u0361o \u035C\u0296 \u0361o)', 
		       'THANKS!', 
		       '420 HARDER!', 
		       'OMFG ITS FUCKING 420!!1', 
		       'I CAN HAZ WEED?', 
		       'all your weeds are belong to me.', 
		       'everybody must get stoned, sing it if you know the words! \:)'
	]

@hook.command("420", "bubbler", "bong", "MJ", "bonghit", "hashish", autohelp=False)
def fourtwenty(message, conn):
    """Get the bot high with your choice: 420, bubbler, bong, MJ, bonghit, hashish."""
    message(random.choice(fourtwentys))
