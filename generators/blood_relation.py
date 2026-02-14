import random
from core.formatter import build_question

def generate():
    names=["A","B","C","D","E","F"]

    question=(
    "A is the father of B. "
    "B is the sister of C. "
    "C is the son of D. "
    "D is the wife of E. "
    "E is the brother of F. "
    "How is A related to F?"
    )

    correct="Brother-in-law"

    distractors=["Uncle","Father","Grandfather"]

    return build_question(
        "Blood Relations and Family Tree",
        question,
        correct,
        distractors,
        "Multi-hop relation composition"
    )
