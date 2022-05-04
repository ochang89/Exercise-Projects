from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for d in question_data:
    q = Question(d['text'], d['answer'])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
