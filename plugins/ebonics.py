from cloudbot import hook
import random

myebonics = ['HOTEL - I gave my girlfriend da crabs and the HOTEL everybody.', 
               'RECTUM - I had two Cadillacs, but my old lady RECTUM both.', 
		           'DISAPPOINTMENT - My parole officer toh me if I miss DISAPPOINTMENT they gonna send me back to the big house.', 
		           'FORECLOSE - If I pay alimony this month, they be no money FORECLOSE.', 
		           'CATACOMB - Don King was at the fight the other night, Man, somebody give that CATACOMB.', 
		           'PENIS - I went to da doctor and he handed me a cup and said PENIS.', 
		           'ISRAEL - Alonso tried to sell me a Rolex, I said Man, that looks fake. He said, No, ISRAEL.', 
		           'UNDERMINE - There is a fine lookin hoe livin in the apartment UNDERMINE.', 
		           'TRIPOLI - I was gonna buy my old lady a bra but I couldnt find no TRIPOLI.', 
		           'STAIN - My mother-in-law axed if I was STAIN for dinner again.', 
		           'ODYSSEY - I told my bro, you ODYSSEY the tits on this hoe.',
			         'HORDE - My sister got into trouble because she HORDE around in school.',
			         'INCOME - I just got in bed wit dis hoe and INCOME my wife.',
			         'HONOR - At the rape trial, the judge axed my buddy, who be HONOR first?',
			         'FORTIFY - I axed da hoe how much? And she say FORTIFY.',
			         'DICTATE - Hey girl! How my DICTATE?',
			         'HONOR ROLL - We was playin poker on the stoop the other day, man I was HONOROLL.',
			         'PLANET - I got me some seed to grow weed, so I PLANET in the backyard.',
			         'DISMAY - I went for a blood test, the doctor pulled out a big needle. He said, "DISMAY hurt a little."',
			         'OMELETTE - Every time I start a new job, OMELETTE go after a week.',
			         'STAIRWAY - When me and my homies get high, we STAIRWAY into space.',
			         'MOBILE - I went to buy crack, I was short on cash, my man said, "Gimme one MOBILE."',
			         'DEFENSE - I ran from the cops, and hopped DEFENSE and got away.',
			         'AFRO - I got so mad at my bitch, AFRO a lamp at her.',
			         'AFTERMATH - I like to be high in school, so AFTERMATH I go to the field and smoke weed.',
			         'LOCKET - I slam the door so hard, I LOCKET.',
			         'DOMINEERING - My girlys birthday was yesterday, I got her a DOMINEERING.',
			         'KENYA - I needed change fo the subway, so I axe a stranger KENYA spare some change.',
			         'DERANGE - DERANGE is where da deer and antelope play.',
			         'DATA - At my basketball game, I scored thirty points. My coach said, "DATA boy!"',
			         'COPULATE - I called 911 and an hour later when they show up, I said, "COPULATE!"',
			         'FASCINATE - My girlys titties are so big. Her shirt has ten buttons, she can only FASCINATE.',
			         'BEWARE - I asked the man at the unemployment office, "Is this BEWARE I get a job?"',
			         'DIMENSION - I be tall, dark, handsome and not DIMENSION hung like a horse.',
			         'COATROOM - The judge said, "One more outburst like that, and youll be thrown out the COATROOM."',
			         'DECIDE - I like Wanda and Yolanda, but I like to have a couple of bitches on DECIDE. ',
		           'SELDOM - My cousin gave me two tickets to the Knicks game, so I SELDOM.'
	]

@hook.command("ebonics", autohelp=False)
def myebonics(message, conn):
    """Have the bot post a random ebonic phrase."""
    message(random.choice(myebonics))
