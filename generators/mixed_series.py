import random
import string
from core.formatter import build_question

letters=string.ascii_uppercase

def generate_pattern():
    start=random.randint(0,10)

    seq=[]
    for i in range(8):
        l=letters[(start+i*2)%26]
        n=(i*i)%10
        seq.append(f"{l}{n}")

    answer=f"{letters[(start+16)%26]}{(8*8)%10}"

    question="Find next term:\n"+", ".join(seq)+", ?"

    distractors=[
        f"{letters[(start+17)%26]}{(8*8)%10}",
        f"{letters[(start+16)%26]}{(7*7)%10}",
        f"{letters[(start+15)%26]}{(8*8)%10}"
    ]

    return build_question(
        "Mixed Series (Alphanumeric)",
        question,
        answer,
        distractors,
        "Alphabet + quadratic number pattern"
    )
