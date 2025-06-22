from question_model import Question
from data import question_data, question_data1
from quiz_brain import QuizBrain

question_bank = []
for index in question_data:
    q_text = index["text"]
    q_answer = index["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

question_bank1 =[]
for index in question_data1:
    question_asked = index["question"]
    correct_answer = index["correct_answer"]
    newer_question = Question(question_asked, correct_answer)
    question_bank1.append(newer_question)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz, Your final score was {quiz.score}/{quiz.question_number}")

quiz2 = QuizBrain(question_bank1)
while quiz2.still_has_questions():
    quiz2.next_question()

print(f"You've completed the quiz, Your final score was {quiz2.score}/{quiz2.question_number}")