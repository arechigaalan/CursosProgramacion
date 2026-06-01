class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.question_list = questions_list
        self.score = 0

    def next_question(self):
        user_answer = input(f'Q.{self.question_number + 1} {self.question_list[self.question_number].question} (True/False): ')
        self.check_answer(user_answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer):
        if user_answer.capitalize() == self.question_list[self.question_number].answer:
            print('You got it right!')
            self.score += 1
        else:
            print(f'That\'s wrong. The correct answer was {self.question_list[self.question_number].answer}')
        print(f'Your current score is {self.score}/{self.question_number + 1}')
        print('\n\n')
