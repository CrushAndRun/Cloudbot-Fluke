from cloudbot import hook
import random

bubblers = ['Fires up the bubbler and passes it around.', 
               'Packs the bubbler and gets everyone high.', 
		       'Loads the bubbler for all RLM peeps.', 
		       'SUCK MY BUBBLER!', 
		       'Loads bubbler with dank RLM weed and shares.', 
		       'Steals the dankest weed from Grimnirs stash and fires up the bubbler.', 
		       'OMFG I thought you would never ask! PUFF PUFF PASS.',
			   'Steals robwerks bubbler and get RLM high.'
	]

@hook.command("bubbles", "fireitup", autohelp=False)
def bubbles(message, conn):
    """Have the bot fire up the bubbler and pass it around: bubbles, fireitup."""
message(random.choice(bubblers)
