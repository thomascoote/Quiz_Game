from question_model import Question
from data import question_data
import random

question_bank = []

for i in question_data:
    temp_q = i["text"]
    temp_a = i["answer"]
    question = Question(temp_q,temp_a)
    question_bank.append(question)

print(question_bank[0].text)