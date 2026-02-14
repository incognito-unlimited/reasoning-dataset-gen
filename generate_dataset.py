import random
from core.file_manager import append_json

from generators import mixed_series, syllogism, blood_relation, seating

GENERATORS=[
    mixed_series.generate_pattern,
    syllogism.generate,
    blood_relation.generate,
    seating.generate
]

def generate_batch(n=100):
    questions=[]
    answers=[]

    for _ in range(n):
        gen=random.choice(GENERATORS)
        q,a=gen()
        questions.append(q)
        answers.append(a)

    append_json("dataset/questions.json",questions)
    append_json("dataset/answers.json",answers)

    print(f"Added {n} new samples")

if __name__=="__main__":
    generate_batch(100)
