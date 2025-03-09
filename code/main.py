import random
from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def shuffle_questions(questions, total_questions):
    """Shuffle the list of questions if it contains the correct number of elements."""
    if len(questions) == total_questions:
        random.shuffle(questions)
    else:
        raise ValueError("Error: Invalid number of questions")

def load_questions_into_stack(questions, stack):
    """Load the given questions into the stack."""
    for question in questions:
        stack.push(question)

def ask_question(stack, question_number):
    """Ask a question by retrieving an item from the stack."""
    if stack.is_empty():
        print("No more questions available.")
        return
    
    country = stack.pop()
    print(f"Question {question_number}: What is the country?")
    print(country)
    answer = input("Your answer: ")
    
    if answer in countries:
        if answer == country:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer was {country}.")
    else:
        raise ValueError("Error: Invalid input")

# Game settings
total_questions = 4
countries = ["France", "Spain", "Italy", "Germany"]

# Initialize the game
question_stack = Stack()
shuffle_questions(countries, total_questions)
load_questions_into_stack(countries, question_stack)

# Ask the questions
for i in range(1, total_questions + 1):
    ask_question(question_stack, i)