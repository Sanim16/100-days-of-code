from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)


new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {new_quiz.score}/{new_quiz.question_number}")
