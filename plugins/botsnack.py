from cloudbot import hook
import random

snacks = ['OMG THANKS!', 
          'moar nummies!', 
		  'OMNOMNOMNOM', 
		  'much appreciated', 
		  'AWESOMESAUCE', 
		  'AWW YEE ( \u0361o \u035C\u0296 \u0361o)', 
		  'THANKS!, check out these boobs \( o Y o )\ ', 
		  'SNACK HARDER!', 
		  'OMFG A FUCKING BOTSNACK!!1', 
		  'I CAN HAZ SNACKS?', 
		  'all your botsnacks are belong to me.', 
		  'yummy thanks \:)'
	]

@hook.command("botsnack", "nummies", "moar_nummies", "skittles", "jellybeans", "smores", "bubblegum", "bacon", autohelp=False)
def botsnack(message, conn):
    """Reward the bot with a snack, snacks include: botsnack, nummies, moar_nummies, skittles, jellybeans, smores, bubblegum, bacon."""
    message(random.choice(snacks))
