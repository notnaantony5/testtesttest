from datetime import datetime


class User:
    def __init__(self, name: str):
        self.name = name


class Question:
    def __init__(self, question: str, answer: str, difficulty: int):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def print(self):
        print(self.question)

    def check_answer(self, user_answer: str) -> bool:
        return self.answer.lower() == user_answer.lower()


class Game:
    def __init__(self, user: User, questions: list[Question]):
        self.score = 0
        self.user = user
        self.start_time = datetime.now()
        self.questions = questions
        self.index_of_questions = 0
        self.last_index = len(questions) - 1

    def print_question(self):
        self.current_question = self.questions[self.index_of_questions]
        self.current_question.print()

    def user_answer(self):
        user_input = input(": ")
        if self.current_question.check_answer(user_input):
            self.score += self.current_question.difficulty
            print("ОК")
        else:
            print("НЕ ОК")
        self.index_of_questions += 1


def main():
    name = input("Имя: ")
    user = User(name)
    questions = [
        Question("Столица России?", "Москва", 1),
        Question("Столица Франции?", "Париж", 2),
    ]
    game = Game(user, questions)
    while game.index_of_questions <= game.last_index:
        game.print_question()
        game.user_answer()


main()
