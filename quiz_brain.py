class QuizBrain():
    def __init__(self, question):
        self.question_number = 0
        self.question_list = question
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.q_text}: (True/ False) ")
        self.checkanswer(user_answer, current_question.q_answer)

    def checkanswer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            print("you got it right")

        else:
            print("that was wrong answer")
        print(f"correct answer was {correct_answer}")
        print(f"your score is {self.score} / {self.question_number}")
        print("\n")