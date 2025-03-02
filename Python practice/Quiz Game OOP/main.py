from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
    
for i in question_data:
    text = i["text"]
    answer = i["answer"]
    question = Question(text,answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()


while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score is {quiz.score}/{len(question_bank)}")

