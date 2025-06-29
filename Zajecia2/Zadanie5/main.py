import random
from typing import List, Iterator

class SimpleChatbot:
    def __init__(self, questions: List[str]) -> None:
        self.original_questions = questions[:]  # zachowujemy oryginalną listę
        self.questions = []
        self.index = 0
        self.answers: List[str] = []

    def __iter__(self) -> Iterator[str]:
        self.questions = self.original_questions[:]
        random.shuffle(self.questions)   # losujemy kolejność pytań
        self.index = 0
        self.answers = []
        return self

    def __next__(self) -> str:
        if self.index >= len(self.questions):
            raise StopIteration
        question = self.questions[self.index]
        self.index += 1
        return question

    def store_answer(self, answer: str) -> None:
        self.answers.append(answer)

    def summary(self) -> None:
        print("\nTo była przyjemność z Tobą porozmawiać! Oto, co zapamiętałem:")
        for q, a in zip(self.questions, self.answers):
            print(f"- Na pytanie '{q}' odpowiedziałeś: \"{a}\"")
        print("\nMam nadzieję, że jeszcze porozmawiamy!")

# Przykład użycia:

bot = SimpleChatbot([
    "Jak się nazywasz?",
    "Jaki jest Twój ulubiony kolor?",
    "Co lubisz robić w wolnym czasie?",
    "Jaka jest Twoja ulubiona potrawa?"
])

for question in bot:
    print(question)
    answer = input()
    bot.store_answer(answer)

bot.summary()
