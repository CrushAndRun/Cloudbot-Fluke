import random

from cloudbot import hook


@hook.command("beam","bmu")
def beam(text, nick, message):
    """beams <user> to a random location"""
    target = text.strip()

    # Use {N} to represent the person's nickname who is performing the action
    # Use {T} to represent the person's nickname who is the target of the action
    beaming = [
            "{N} transports {T} to hillary clintons panties.",
            "{N} beams {T} to Spotted Lake in BC for mineral treatments.",
            "{N} sends {T} the Giants Causeway in N. Ireland to count polygon columns.",
            "{N} transports {T}'s ass directly over Thors Well in Oregon.",
            "{N} beams {T} to Lake Hillier in W. Australia for a bath..you smell!",
            "{N} sends {T} to the Tianzi mountains in China with a backpack filled with old rope..have fun!",
            "{N} transports {T} to Cat Island in China to get some pussy.",
            "{N} beams {T} to their new home inside a guano factory.",
            "{N} sends {T} down to Bringloid V to assist in repopulating the colonies.",
            "{N} transports {T} to the Mutara Sector to meet KKHHHHAAAAAAAAAAAANNNN!",
            "{N} beams {T} over to Qo’noS to make nice with the Klingons.",
            "{N} sends {T} to the Petrifying Lake in Tanzania for a swim.",
            "{N} transports {T} to Slope Point on South Island New Zealand for a blow job."
            "{N} beams {T} to the Huashan Mountain trail in China for some tea."
    ];

    out = "{}".format(random.choice(beaming))
    out = out.replace("{N}", nick)
    out = out.replace("{T}", target)

    message(out)
