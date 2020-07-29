import re
import random

emojis = [
    "꒰◍ᐡᐤᐡ◍꒱",
    "{ @❛ꈊ❛@ }",
    "6(◦･ω･◦)9",
    "UwU",
    "OwO",
    "@w@",
    "◕w◕"
]

def owoify(txt: str, ending_emoji: bool) -> str:
    txt = re.sub(pattern=r'(?:l|r)', repl='w', string=txt)
    txt = re.sub(pattern=r'(?:L|R)', repl='W', string=txt)
    txt = re.sub(pattern=r'n([aeiou])', repl='ny', string=txt)
    txt = re.sub(pattern=r'N([aeiou])|N(AEIOU)', repl="Ny", string=txt)
    txt = re.sub(pattern=r'ove', repl='uv', string=txt)
    txt = re.sub(pattern=r'nd(?= |$)', repl='ndo', string=txt)

    if ending_emoji:
        txt += " " + random.choice(emojis)

    return txt