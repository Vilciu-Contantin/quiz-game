# importam 
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data: # trecem prin fiecare intrebare
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_question():
    quizbrain.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quizbrain.score}/ {len(question_bank)}")
