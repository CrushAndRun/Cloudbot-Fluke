import random

rules = { 1: "Do not talk about /b/.",
          2: "You do NOT talk about /b/.",
          3: "We are Anonymous.",
          4: "Anonymous is legion.",
          5: "Anonymous does not forgive, Anonymous does not forget.",
          6: "Anonymous can be a horrible, senseless, uncaring monster.",
          7: "Anonymous is still able to deliver.",
          8: "There are no real rules about posting.",
          9: "Always register with your local service provider.",
          10: "If you enjoy any rival sites — DON'T.",
          11: "All your carefully picked arguments can easily be ignored.",
          12: "Anything you say can and will be used against you.",
          13: "Anything you say can be turned into something else. - fixed",
          14: "Do not argue with trolls — it means that they win.",
          15: "The harder you try, the harder you will fail.",
          16: "If you fail in epic proportions, it may just become a winning failure.",
          17: "Every win fails eventually.",
          18: "Everything that can be labeled, can be hated.",
          19: "The more you hate it, the stronger it gets.",
          20: "Nothing is to be taken seriously.",
          21: "Original content is original only for a few seconds before getting old.",
          22: "Copy 'n paste is made to ruin every last bit of originality.",
          23: "Copy 'n paste is made to ruin every last bit of originality.",
          24: "Every repost is always a repost of a repost.",
          25: "Relation to the original topic decreases with every single post.",
          26: "Any topic can be turned into something totally unrelated.",
          27: "Always question a person's sexual preferences without any real reason.",
          28: "Always question a person's gender - just in case it's really a man.",
          29: "On the internet, all girls are men, and all kids are undercover FBI agents or Perverted Justice Decoys.",
          30: "There are NO girls on the internet.",
          31: "TITS or GTFO - the choice is yours.",
          32: "You must have pictures to prove your statements.",
          33: "Lurk moar — it's never enough.",
          34: "There is porn of it, no exceptions.",
          35: "If no porn is found of it, it will be made.",
          36: "There will always be more fucked up shit than what you just saw.",
          37: "You can not divide by zero (just because the calculator says so).",
          38: "No real limits of any kind apply here — not even the sky.",
          39: "CAPSLOCK IS CRUISE CONTROL FOR COOL.",
          40: "EVEN WITH CRUISE CONTROL YOU STILL HAVE TO STEER.",
          41: "Needs moar Desu. No exceptions.",
          42: "Nothing is Sacred.",
          43: "The more beautiful and pure a thing is, the more satisfying it is to corrupt it.",
          44: "Trying to edit the rules of the Internet with Japanese characters is like trying to make “2 girls, 1 cup” acceptable in society. It only works at A-con.",
          45: "When one sees a lion, one must get into the car.",
          46: "There is furry porn of it. No exceptions.",
          47: "The pool is always closed due to AIDS (and stingrays, which also have AIDS).",
          48: "A cat is fine too.",
          49: "One cat leads to another.",
          50: "Another cat leads to Zippo Cat.",
          51: "No matter what it is, it is somebody's fetish. No exceptions.",
          52: "It is delicious cake. You must eat it.",
          53: "It is delicious trap. You must hit it.",
          54: "/b/ sucks today.",
          55: "If you have time to make up new rules, you have no life.",
          56: "They will not bring back Snacks.",
          57: "You will never have sex.",
          58: "Desu isn't funny. Seriously guys. It's worse than Chuck Norris jokes.",
          59: "No one does it like Gaston. No exceptions.",
          60: "It needs more pumpkin. No exceptions.",
          61: "It needs moar cowbell. No exceptions.",
          62: "It has been cracked and pirated. No exceptions.",
          63: "For every male character there is a female version. No Exceptions.",
          64: "Don't copy that floppy.",
          65: "Anonymous is not your personal army.",
          66: "The cake is a lie.",
          67: "Anonymous does not 'buy', he downloads.",
          68: "Milhouse will never be a meme. Ever. No matter what your post ends with. No exceptions. Ever. No.",
          69: "LOL SIXTY NINE AMIRITE?",
          70: "Do not talk about the 100M GET failure.",
          71: "The internet is SERIOUS FUCKING BUSINESS.",
          72: "Darth Vader is your father. No exceptions.",
          73: "If there isn't enough just ask for Moar.",
          74: "If you post it, they will cum.",
          75: "Rule 75 is a lie. OHSHI--",
          76: "Twinkies are the answers to life's problems.",
          77: "The internet makes you stupid.",
          78: "It will always need moar sauce.",
          79: "Ceilingcat IS watching you masturbate.",
          80: "Interwebz177 did it. No exceptions.",
          81: "Anonymous is a virgin by default.",
          82: "Nobody tells the truth on the Internet",
          83: "Only clusterfucks start Edit Wars.",
          84: "All rules ARE true, including this one.",
          85: "Retarded rules are forbidden.",
          86: "The term 'sage' does not refer to the spice.",
          87: "If you get pepperoni ever again, I swear I'll blow this joint sky-high!"
          88: "Anonymous rules the internet. No exceptions.",
          89: "Bruce Lee was a hero to us all.",
          90: "It's never lupus.",
          91: "There is gay porn of it, no exceptions.",
          92: "[Chuck Norris (redacted)] Theodore Roosevelt is the exception to rule 91. No exceptions.",
          93: "Refer to Rule 93.3",
          93:3. "Rule 899 is rule 93. (This is not)",
          94: "This is rule 94. It was definitely not deleted by SOPA.",
          95: "Anonymous did NOT, under any circumstances, tk him 2da bar?",
          96: "If you express astonishment at someone's claim, it is most likely just a clever ruse.",
          97: "The government, The CIA, Everything is a lie.",
          98: "Only Zippocat is truth.",
          99: "All numbers are at least 100 but always OVER NINE THOUSAAAAAND.",
          100: "Faggotry will not be tolerated.",
          899: "No one intentionally sees their first dickgirl. No exceptions."
  }

 def getRule(self, e):
     if e.input:
          if isIntegerValue(e.input) and int(e.input) >= 1 and int(e.input) <= len(rules):
               e.output = "Internet Rule #"+str(e.input)+": "+rules[int(e.input)]
          else:
               e.output = "Stop making up rules!."
     else:
          random_rule = random.randint(1, len(rules))
          e.output = "Internet Rule #"+str(random_rule)+": "+rules[random_rule]
     return e
     
def isIntegerValue(v):
     try:
          int(v)
          return True
     except ValueError:
          return False

getRule.command = "irule"
getRule.helptext = "irule <number> :Retrieves internet rule 1-100 by <number>. irule :Retrieves a random internet rule."
