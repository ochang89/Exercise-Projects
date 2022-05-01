
class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.q_num]
        self.q_num += 1
        ans = input(f"Q.{self.q_num}: {current_q.text} (True/False)?: ")
        print(ans)
        self.check_answer(ans, current_q.answer)

    def still_has_questions(self):
        return self.q_num < len(self.question_list)
           
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
            print(f'Score: {self.score}/{self.q_num}')
        else:
            print("Wrong!")
            print(f'Score: {self.score}/{self.q_num}')


        
            

