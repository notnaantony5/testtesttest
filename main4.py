import json
from datetime import datetime


def get_questions(path: str = "questions.json") -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    user_name = input("Ваше имя: ")
    start = datetime.now()
    questions = get_questions()
    points = 0
    for q in questions:
        print(q["question"])
        user_input = input(": ")
        if user_input.strip() == q["answer"]:
            points += 1
    end = datetime.now()
    time = int((end - start).total_seconds())
    print(f"Вы набрали {points} баллов за {time} с")


if __name__ == "__main__":
    main()
