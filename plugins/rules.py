from cloudbot import hook

ruleslist = {"spam": "Your issue was too long. Go to http://pastebin.com and link your issue from there.",
"nick": "Please change your nick by entering /nick newnick",
"nocoop": "You've been helped on the matter and will receive no further help or advice. Thank you for your (non-existent) cooperation.",
"abuse": "Please refrain from abusing the bot as it might cause you to be kicked from the channel, thanks.",
"monologue": "Please take your monologue elsewhere other than this channel, maybe you could start a blog..thanks.",
"enter": "Enter is not a spacebar, please try to form complete sentences to avoid being kicked by a bot or appearing as though you're just spamming.",
"pastie": "Please don't paste all that content here, go to http://pastie.org/ and link your issue instead..thanks.",
"caps": "Please refrain from using all or mostly caps, failure to adhere to this notice may result in your nick being quieted or fbanned.",
"network help": "If you need help with channel/nick/network issues please /join #crushandrun and state your issue."}

# Generate the rules list reply.
# Beginning phrase.
ruleslistreply = "The rules I have loaded are: "
# Make the list of entries.
rulesactuallist = list(ruleslist.keys())
# Alphabetize it.
rulesactuallist.sort()
# Generate the reply.
for i in rulesactuallist:
	# Probably a better way of handling this... Don't need a comma at the start.
	if ruleslistreply.endswith(": ") == True:
	    ruleslistreply = ruleslistreply+i
	# The rest of the list.
	else:
		ruleslistreply = ruleslistreply+", "+i
# Finish phrase.
ruleslistreply = ruleslistreply+"."

@hook.command(permissions=["rules"])
def rules(text, nick, chan, conn):
	# Check for a category name.
	if text:
		# Split by spaces if they exist.
		text = text.split(" ")
		# Make category name lowercase.
		command = text[0].lower().strip()
		# Check if there's a target nick.
		try:
			targetnick = text[1]
		except IndexError:
			targetnick = None
		# Check to see if category exists.
		try:
			reply = ruleslist[command]
		except KeyError:
			reply = ruleslistreply
		# Category doesn't exist:
		if reply == ruleslistreply:
			conn.cmd("PRIVMSG " + nick + " :"+ruleslistreply)
		# Category exists:
		else:
			# Target nick exists:
			if targetnick !=None:
				conn.cmd("PRIVMSG " + chan + " :"+targetnick+": "+reply)
			else:
				return reply
	# No category name, return list of categories.
	else:
		conn.cmd("PRIVMSG " + nick + " :"+ruleslistreply)

@hook.command(permissions=["rules"])
def listrules(conn, nick):
	conn.cmd("PRIVMSG " + nick + " :"+ruleslistreply)
