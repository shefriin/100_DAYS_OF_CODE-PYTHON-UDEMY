from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    in_text = item["question"]
    in_answer = item["correct_answer"]
    # in_text = item["text"]
    # in_answer = item["answer"]
    question_obj = Question(in_text,in_answer)
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

quiz_ended = False
while not quiz_ended:
    quiz.next_question()
    quiz_ended = quiz.still_has_questions()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")