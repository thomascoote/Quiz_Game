from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
import random

question_bank = []
answer_bank = []

for i in question_data:
    temp_q = i["question"]
    temp_q = html.unescape(temp_q)
    temp_a = i["correct_answer"]
    question = Question(temp_q,temp_a)
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score was {quiz.score}/{quiz.question_number}")