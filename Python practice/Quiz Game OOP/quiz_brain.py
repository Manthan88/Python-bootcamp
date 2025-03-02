class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.score = 0
        self.question_no = 0

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no} {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_questions(self):
        return self.question_no < len(self.question_list)
            
    def check_answer(self, user_answer, actual_answer):
        if user_answer ==  actual_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")
        print(f'You current score is {self.score}/{self.question_no}')
        print("\n")

