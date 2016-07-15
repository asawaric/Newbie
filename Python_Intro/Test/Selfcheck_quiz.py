#import quizParser
import quizParser_all

#start menu
print "Hello!"

class Session()
""" A Session of quiz to check the record of existing quiz_taker.
    If name of the quiz_taker is not available then initializing new record for new quiz_taker"""
    def prompt_for_name(userlist, username)
        userlist = []
        username = raw_input("Enter your name:")
        userlist.append(username)
        if username not in userlist:
            def initialize_record()
        
        else:
            def read_record()
        
            def find_all_quizes()

            def print_quiz_choices()

            def run_quiz()

class Quiz(object):
    """ Quiz to find the questions to test as per the userrecord criterion and
        ask these questions"""
    Quiz_list = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7']
    def __init__(self, name)
        self.name = name
    def ask_question(self, userrecord, question):
        self.userrecord = userrecord
        Quiz_choice = raw_input("Which quiz you want to take? Enter any quiz number from Q1 to Q7:")

    def find_question_to_test(self, quiz)    
        self.quiz = quiz
        #for quiz_number in str(Quiz_list):
        if Quiz_choice in str(Quiz_list):
            Quiz_question = raw_input("Which questions you want to answer? Enter one of these choices-All or Not_cleared:")
    def ask_these_questions(self, list_attempts, *Q)
            if Quiz_question = "All":
                print[Q1]
            elif Quiz_question = "Not_cleared":
                print[list_attempts]
            else:
                break
        else:
            print "Enter acceptable quiz number"
