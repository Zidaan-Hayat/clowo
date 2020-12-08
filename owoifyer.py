import re, random

_str_emojis = [
    "꒰◍ᐡᐤᐡ◍꒱",
    "{ @❛ꈊ❛@ }",
    "6(◦･ω･◦)9",
    "UwU",
    "OwO",
    "@w@",
    "◕w◕"
]

def owoify(*, txt: str, ending_emoji: bool = False) -> str:
    """
    `txt`: The text you wish to 'owoify'

    `ending_emoji`: Whether you wish to add an
    emoji at the end of your text to make it 
    especially stand out 
    """

    replacements = {
        r"(?:l|r)": "w",
        r'(?:L|R)': "W",
        r'n([aeiou])': "ny",
        r'N([aeiou])|N(AEIOU)': "Ny",
        r"ove": "uv",
        r'nd(?= |$)': "ndo"
    }

    for pattern, replacement in list(replacements.items()):
        txt = re.sub(pattern=pattern, repl=replacement, string=txt)

    if ending_emoji:
        txt += " " + random.choice(_str_emojis)

    return txt