import json
from pathlib import Path

QUESTIONS_FILE = "dataset/questions.json"
ANSWERS_FILE = "dataset/answers.json"
OUTPUT_FILE = "dataset/train_sharegpt.json"


def build_user_prompt(q):
    choices = "\n".join(q["choices"])

    prompt = (
        "Solve the following multiple choice reasoning question.\n\n"
        f"{q['question']}\n\n"
        f"Choices:\n{choices}\n\n"
        "Respond ONLY in JSON format:\n"
        '{ "answer": "A/B/C/D", "reasoning": "short explanation" }'
    )
    return prompt


def build_assistant_response(a):
    return json.dumps({
        "answer": a["answer"],
        "reasoning": a.get("reasoning","")
    }, ensure_ascii=False)


def main():

    questions = json.load(open(QUESTIONS_FILE))
    answers   = json.load(open(ANSWERS_FILE))

    assert len(questions)==len(answers), "Mismatch Q/A"

    conversations=[]

    for q,a in zip(questions,answers):

        user = build_user_prompt(q)
        assistant = build_assistant_response(a)

        conversations.append({
            "conversations":[
                {"role":"user","content":user},
                {"role":"assistant","content":assistant}
            ]
        })

    Path("dataset").mkdir(exist_ok=True)

    with open(OUTPUT_FILE,"w",encoding="utf-8") as f:
        json.dump(conversations,f,indent=2,ensure_ascii=False)

    print(f"Saved {len(conversations)} training samples → {OUTPUT_FILE}")


if __name__=="__main__":
    main()
