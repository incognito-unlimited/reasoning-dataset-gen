import random
from core.formatter import build_question

TERMS=["A","B","C","D","E","F","G"]

def generate():
    A,B,C,D=random.sample(TERMS,4)

    statements=[
        f"All {A} are {B}",
        f"Some {B} are {C}",
        f"No {C} are {D}",
        f"All {D} are {A}"
    ]

    question="Statements:\n"+"\n".join(statements)+"\nConclusion: Some "+B+" are not "+D

    correct="Follows"

    distractors=["Does not follow","Possibly follows","None"]

    return build_question("Syllogisms",question,correct,distractors,"Set contradiction reasoning")
