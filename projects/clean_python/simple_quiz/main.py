from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(x['text'], x['answer']) for x in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()
    if quiz.check_answer(answer):
        quiz.add_points()
        print("Correct!")
    else:
        print("Wrong!")
    print("Your current score is {}/{} ({}%)".format(quiz.points, quiz.question_number, round(quiz.points/quiz.question_number*100), 2))
    
quiz.end_quiz()
