import random

LETTERS = ["A","B","C","D"]

def ensure_four_options(correct, distractors):
    """
    Ensures we always have 3 unique distractors
    even if generator produces fewer
    """
    distractors = list(set(distractors) - {correct})

    # If not enough distractors, auto-generate generic ones
    while len(distractors) < 3:
        fake = correct + str(random.randint(1,9))
        if fake not in distractors:
            distractors.append(fake)

    return distractors[:3]


def build_question(topic, question, correct_answer, distractors, explanation):

    distractors = ensure_four_options(correct_answer, distractors)

    options = distractors + [correct_answer]
    random.shuffle(options)

    answer_letter = LETTERS[options.index(correct_answer)]
    choices = [f"{LETTERS[i]}) {options[i]}" for i in range(4)]

    question_json = {
        "topic": topic,
        "question": question,
        "choices": choices,
        "expected_answer": answer_letter,
        "explanation": explanation
    }

    answer_json = {
        "answer": answer_letter,
        "reasoning": ""
    }

    return question_json, answer_json
