#!usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser(
    prog="clowo",
    description="Pass regular english text and turn it into a furry poetic masterpiece",
    usage="clowo -t Hello, how are you?"
)

parser.add_argument(
    '--text','-t',
    type=str,
    nargs='+',
    default="Please provide text to owoify",
    required=True,
    help="Text to be owoified"
)

def to_owo(txt: str) -> str:
    txt = re.sub(pattern=r'(?:l|r)', repl='w', string=txt)
    txt = re.sub(pattern=r'(?:L|R)', repl='W', string=txt)
    txt = re.sub(pattern=r'n([aeiou])', repl='ny', string=txt)
    txt = re.sub(pattern=r'N([aeiou])|N(AEIOU)', repl="Ny", string=txt)
    txt = re.sub(pattern=r'ove', repl='uv', string=txt)
    txt = re.sub(pattern=r'nd(?= |$)', repl='ndo', string=txt)

    return txt

args = parser.parse_args()
args = " ".join(args.text)
print(to_owo(args))