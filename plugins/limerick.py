from cloudbot import hook
import random

limericks = ['There once was a woman named Jill who swallowed an exploding pill.. They found her vagina in North Carolina and her tits in a tree in Brazil.', 
               'There was a man from Madrass whose balls were made out of brass..On a Stormy Weather they Banged together and sparks flew out of his ass.', 
		       'A worried young fellow McDoole found some red spots on his tool..His doctor a cynic said get out of my clinic and wipe off the lipstick you fool.', 
		       'There once was a man named Bright who traveled much faster than light..He left one day in a relative way and came back the previous night. ', 
		       'A young small plane pilot named Sanger got a girl alone in his hangar..When she asked where in Maine he was flying his plane he said he was going to Bangor.', 
		       'On the chest of a barmaid from Vail was tattooed all the prices of ale..Whilst on her behind for the sake of the blind was precisely the same but in braille.', 
		       'A limerick of classic proportion should have meter and rhyme and a portion..of humor quite lewd and a frightfully crude impossible sexual contortion.',
			   'There once was a fellow McSweeny who spilled some gin on his weenie..Just to be couth he added vermouth then slipped his girlfriend a martini.',
			   'Twas a crazy old man called Okeef who caused local farmers much grief..To their cows he would run and cut their legs off for fun then say Look I just invented ground beef!',
			   'Mary had a little pig she kept it fat and plastered..and when the price of pork went up she shot the little bastard.',
		       'There was once a pirate history relates has was scuffling around with some of his mates..When he slipped on a cutlass which rendered him nutless and practically useless on dates.',
			   'To his friend Ned said while blue my wife Edith just told me we are through..she says I am too fat so his friend told him that You can not have your cake and Edith, too.',
			   'A woman whose clothing was strewed around the beach where she sunbathed nude..Saw a man come along and unless I am quite wrong You expected this line to be lewd.',
			   'There was a young woman from Crewe who filled her vajayjay with glue..She said with a grin If they pay to get in they must pay to get out again too.',
			   'Ignoring all medical rumors a man used Monsanto fumors..When the judging was done his flowers had won and all of his children had tumors.',
			   'There was a woman from Devizes who had breast of different sizes..One was quite small almost nothing at all and the other was big and won prizes.',
			   'From the depths of the crypt at St Giles came a scream that resounded for miles..Said the vicar Good gracious has Father Ignatius forgotten the bishop has piles?',
			   'There was a young woman named Sally who loved an occasional dally..she sat on the lap of a well endowed chap and said WOW you are right up my alley!',
			   'There once was a man from Brighton who said to his girl you have a tight one..She said pardon my soul but you're in the wrong hole there is plenty of room in the right one.',
			   'There once was a man from Peru who fell asleep in his canoe..As he dreamt of Venus he played with his penis and woke up with a handful of goo. ',
			   'There was a young feller called Garr who had a habit of goosing his ma..Go pester your sister she said when he kissed her I have enough trouble with your pa.',
			   'There was a young lady from Twickenham loved penises and never grew sick of them..She knelt on some sod and prayed to her God to lengthen and strengthen and thicken them.',
			   'There was an old sailor from Wales an expert in pissing in gales..He could piss in a jar from a topgallant spar without ever wetting the sails.',
			   'A large-breasted lady from Leeds was incredibly fond of her tweeds..Her smart tartan bra was the largest by far yet still didn't cover her needs.',
			   'There once was a poet named Dan whose poetry just did not scan..When told this was so he replied yes I know But I always try to get as many words in the last line as I possibly can.',
			   'There was a young man from Australia on his arse tattooed an azalea..An exquisite design and the color was fine but the smell was a total failure. ',
			   'It was a sunny fine day in June it must have been mid afternoon..As time flew by I let out a sigh and decided to go to the saloon.',
			   'There was a young girl named Louise her pubes hung down to her knees..The crabs got together to knit her a sweater so in winter her twat would not freeze.',
			   'There once was a lady from Redding who gave good advice at a wedding..She said you will find if you go in from behind it makes less of a mess on the bedding.',
			   'Young farmer Riley had a fat cow he wanted to milk it but did not know how..he pulled on the cows tail instead of the tit..Riley got covered in a lot of cow shit.',
			   'There once was a man from Nantucket..uh you probably know the rest.',
			   'There was a young lover of rubbermaid long hours and late nights she slaved..To make an obscene vibrating machine then locked in her bedroom she stayed.',
			   'There once was a man from Peru who had a lot of growing up to do..he would ring a doorbell then run like hell until the owner shot him with a .22',
			   'A canner who is exceedingly canny one morning remarked to his granny..A canner can can anything that he can but a canner can not can a can can he?.',
			   'I would rather have fingers than toes I would rather have ears than a nose..And as for my hair I am glad it is all there I will be awfully sad when it goes.',
			   'A newspaper man named Fling could make copy from any old thing..But the copy he wrote to make five dollar notes got him a one way ticket to Sing Sing.',
			   'A man and his lady love Jen skated out where the ice was quite thin..Had a quarrel no doubt for I hear they fell out what a blessing they did not fall in!',
			   'I am really determined and keen to start giving this house a spring clean..I will do it I say I will do it today well I will do it tomorrow I mean. ',
			   'A painter who lived in Great Britain interrupted two girls with their knitting..He said with a sigh that park bench uh well I just painted it right where you are sitting.',
			   'An elderly man called Keith mislaid his set of false teeth..He had laid them in his chair and forgot they were there sat down and was bitten beneath.',
			   'An amoeba named Max and his brother were sharing a drink with each other... In the midst of their quaffing they split themselves laughing and each of them now is a mother.',
		       'There once was a girl dating Jerry devoid of her sweet little cherry..certainly not a sin she still had the box it came in which kept them both very merry.'
	]

@hook.command("limerick", autohelp=False)
def limerick(message, conn):
    """Have the bot recite a limerick enter @bot limerick."""
    message(random.choice(limericks))
