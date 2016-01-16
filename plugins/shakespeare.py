#
# Shakespeare insult plugin
#
# Copyright (C) 2015 Sindastra <https://github.com/sindastra>
#
# The above copyright notice and this notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# """

from cloudbot import hook
from random import randint

@hook.command()
def shakespeare(text, message):

	a = ["Away I say", "Bathe thyself", "Be not deaf", "Behold thy mirror",
		"Beware my sting", "Clean thine ears", "Drink up eisel", "Eat a crododile",
		"Eat my knickers", "Fie upon thee", "Forsooth say I", "Get thee gone",
		"Get thee hence", "Grow unsightly warts", "Hear me now", "Hear this pox alert",
		"I’ll see thee hang’d", "Kiss my codpiece", "Lead apes in hell",
		"Methinks you stinks", "My finger in thine eye", "»Phui« I say",
		"Remove thine ass hence", "Resign not thy day gig", "Sit thee on a spit",
		"Sorrow on thee", "Swim with leeches", "Thou dost intrude",
		"Thy mother wears armor", "Trip on thy sword", "Tune thy lute",
		"Why, how now putz", "Wipe thy ugly face"]

	b = ["artless", "bawdy", "beslubbering", "bootless", "cankerous", "churlish",
		"cockered", "clouted", "craven", "currish", "dankish", "dissembling",
		"droning", "errant", "fawning", "fobbing", "fool-born", "froward",
		"frothy", "gleeking", "goatish", "gorbellied", "ill-nurtured",
		"impertinent", "incestuous", "incurable", "infectious", "jarring",
		"loggerheaded", "lumpish", "loutish", "mammering", "mangled", "mewling",
		"paunchy", "pribbling", "puking", "puny", "qualling", "rank", "reeky",
		"roguish", "rump-fed", "ruttish", "saucy", "spleeny", "spongy", "surly",
		"tardy-gaited", "tottering", "unmuzzled", "vain", "venomed", "warped",
		"wayward", "weedy", "whoreson", "wretched", "yeasty"]

	c = ["addlepated", "base-court", "bat-fowling", "beef-witted", "beetle-headed",
		"boil-brained", "clapper-clawed", "clay-brained", "codpiece-sniffing",
		"common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted",
		"dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked",
		"flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "foul-practicing",
		"full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born",
		"hell-hated", "idle-headed", "ill-breeding", "ill-nurtured", "knotty-pated",
		"mad-brained", "milk-livered", "motley-minded", "onion-eyed", "plume-plucked",
		"pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing",
		"rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied",
		"tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted",
		"weather-bitten"]

	d = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear",
		"bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb",
		"codpiece", "death-token", "dewberry", "dotard", "flap-dragon",
		"flax-wench", "flea", "flirt-gill", "foot-licker", "fustilarian",
		"giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast",
		"hugger-mugger", "jolthead", "knave", "lewdster", "lout", "maggot-pie",
		"malt-worm", "mammet", "measle", "minnow", "miscreant", "moldwarp",
		"mumble-news", "nit", "nut-hook", "pigeon-egg", "pignut", "pumpion",
		"puttock", "ratsbane", "rudesby", "scut", "skainsmate", "strumpet",
		"varlot", "vassal", "wagtail", "water-fly", "whey-face",
		"winter-cricket"]

	ai = a[randint(0,len(a)-1)]
	bi = b[randint(0,len(b)-1)]
	ci = c[randint(0,len(c)-1)]
	di = d[randint(0,len(d)-1)]

	beginning = ""

	if text:
		beginnging = text + ", " + ai.lower()
	else:
		beginnging = ai

	message( beginnging + ", thou " + bi + " " + ci + " " + di + "!" )
