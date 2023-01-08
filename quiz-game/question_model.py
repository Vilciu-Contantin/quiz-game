class Question:
    def __init__(self, q_test, q_answer):
        self.text = q_test 
        self.answer = q_answer

new_question = Question("2 + 5 = 5", "True")
print(new_question.text)
print(new_question.answer)
