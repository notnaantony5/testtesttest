import json


def get_questions(path: str = "questions.json") -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    user_name = input("Ваше имя:")
    questions = get_questions()
    points = 0
    for q in questions:
        print(q["question"])
        user_input = input(": ")
        if user_input.strip() == q["answer"]:
            points += 1
    print(f"Вы набрали {points} баллов")


if __name__ == "__main__":
    main()
