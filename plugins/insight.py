from cloudbot import hook
import random
import textwrap

quotes = """Crowded elevator always smell different to midget.
Dumb man climb tree to get cherry, wise man spread limbs.
Don't drink and park - accidents cause people.
State of pregnancy exist when woman takes seriously something poked in fun.
He who buries a man's wife alive, should not expect to sit at that man's dinner table without the subject coming up.
He who plays with self, pulls boner.
Baseball all wrong -- man with four balls cannot walk.
House without toilet is uncanny.
Man trapped in brothel get jerked around.
Man's wife his better half, his mistress his better whole.
Panties not best thing on earth, but next to it.
It is good for girl to meet boy in park, but better for boy to park meat in girl.
Man have more hair on chest than woman, but on whole woman have more.
Man who cut self while shaving, lose face.
Man who eats photo of father, soon spitting-image of father.
Man who lay woman on ground gets piece on earth.
Man who plays with self pulls boner.
Man who take sleeping pill and laxative on the same night will wake up in deep shit.
Man who pushes piano down mineshaft get tone of A flat miner.
Man who sneezes without tissue takes matters in his own hands.
Wise man never play leapfrog with unicorn.
Man who suck woman's tit make clean breast of things.
Man who walk in middle of road get run over by bus.
Wife not part of furniture, until screwed on bed.
Woman laid in tomb may soon become mummy.
Man who fall in vat of molten glass make spectacle of self.
Man who jizz in cash register come into money.
Man with tight trousers is pressing his luck.
Man who gets kicked in testicles, left holding bag.
Man who crosses the ocean twice without washing is a dirty double crosser.
Man who drive like hell, bound to get there.
Man trapped in pantry have ass in jam.
Don't sweat the petty stuff ... and don't pet the sweaty stuff.
Woman who wear jockstrap have make believe ballroom.
Woman who slides down banister makes monkey shine.
Man who scratches ass should not bite fingernails.
Man who tell one too many light bulb jokes soon burn out.
Woman who puts detergent on top shelf, jump for Joy.
Man bobbing up and down in corn field is not planting grain.
Man trapped in pantry have ass in jam.
Man who abuse computer get bad bytes.
Man who cooks carrots and peas in same pot, very unsanitary.
Man who drop watch in toilet have crappy time.
Man who drop watch in whisky wasting time.
Man who eat cookie in bed wake up feeling crumby.
Man who eat many prunes get good run for money.
Man who eat many prunes sit on toilet many moons. 
Man who eat sweets take up two seats.
Man who fart in church must sit in own pew.
Man who have head up ass, have crappy outlook on life.
Man who get kicked in testicles left holding bag. 
Man who pee on electric fence receive shocking news.
Man who make love to exhaust pipe of car have hot rod. 
Man who sit on hot stove will rise again.
Man who sit on tack get point.
Man who run behind car get exhausted.
Man who run in front of car, get tired.
Nail on board is not good as screw on bench. 
People who make Confucius joe-ks speak bad English.
Two wrongs not make right, three lefts do.
Virgin like balloon - one prick, all gone. 
War does not determine who is right - war determine who is left.
Wife who put husband in doghouse soon find him in cathouse.
Woman who fly airplane upside down have crackup.
Woman who make love in treehouse put ass out on limb.
Woman who spring on innerspring this spring have offspring next spring.
Woman who spends much time on bedspring, may have offspring.
Man with one chopstick go hungry.
Man with no legs bums around."""

# Number of chars to split by
n = 300

@hook.command
def insight(conn, nick, chan):
    # split lines
    splitquotes = quotes.split("\n")
    # Pick random quote.
    reply = random.choice(splitquotes)
    # Insert nick here so we don't get highlighted more than once. Also splits per n chars.
    reply = textwrap.wrap("("+nick+") "+reply, n, break_long_words=False)
    for i in reply:
        conn.cmd("PRIVMSG " + chan + " :" + i)
