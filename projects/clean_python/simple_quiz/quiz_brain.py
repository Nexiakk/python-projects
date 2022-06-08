class QuizBrain:
    def __init__(self, question_list=None):
        self.question_number = 0
        self.question_list = question_list
        self.points = 0
        
    def next_question(self):
        ans = input("Q.{}: {} (True/False): ".format(self.question_number+1, self.question_list[self.question_number].question))
        return ans
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, q_answer):
        question_number = self.question_number
        self.question_number += 1
        return q_answer.lower() == self.question_list[question_number].answer.lower()
    
    def add_points(self):
        self.points +=1
        
    def end_quiz(self):
        print("""
-----------------------------------------------------
Congrats you've got {}/{} ({}%) correct!
-----------------------------------------------------
""".format(self.points, self.question_number, round(self.points/self.question_number*100), 2))
        