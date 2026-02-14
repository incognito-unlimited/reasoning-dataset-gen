import random
import itertools
from core.formatter import build_question

PEOPLE = list("ABCDEFGH")

def valid(perms, clue):
    return [p for p in perms if clue(p)]

def unique_solution(clues):
    perms=list(itertools.permutations(PEOPLE))
    for c in clues:
        perms=valid(perms,c)
    return len(perms)==1, perms[0] if len(perms)==1 else None

def generate():
    # Step 1: create hidden truth
    solution=random.sample(PEOPLE,8)

    # Step 2: create many clues
    clues=[]
    text_clues=[]

    for _ in range(25):
        a,b=random.sample(PEOPLE,2)
        if solution.index(a)<solution.index(b):
            clues.append(lambda p,a=a,b=b: p.index(a)<p.index(b))
            text_clues.append(f"{a} sits to the left of {b}")
        else:
            clues.append(lambda p,a=a,b=b: p.index(a)>p.index(b))
            text_clues.append(f"{a} sits to the right of {b}")

    # Step 3: reduce clues while uniqueness preserved
    selected=[]
    selected_text=[]

    for c,t in zip(clues,text_clues):
        temp=selected+[c]
        ok,_=unique_solution(temp)
        if ok:
            selected.append(c)
            selected_text.append(t)

    # ask question
    ask=random.choice(PEOPLE)
    pos=solution.index(ask)+1

    question="Eight persons sit in a row.\n"
    question+="\n".join(selected_text)
    question+=f"\nWhat is the position of {ask} from the left?"

    correct=str(pos)

    all_positions=[str(i) for i in range(1,9)]
    distractors=[p for p in all_positions if p!=correct]
    random.shuffle(distractors)
    distractors=distractors[:3]


    return build_question(
        "Seating Arrangements (Linear, Circular)",
        question,
        correct,
        distractors,
        "Uniquely determined arrangement"
    )
