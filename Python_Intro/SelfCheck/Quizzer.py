from random import shuffle

example_quiz = {'question':"What is the largest prime number from 1 to 10?\n", \
                'choices': {"1":False, "10":False, "11": False, "7":True }}


class selfTest:
    """
    Base class for creating quiz questions
    """
    def __init__(self, quiz_list=None):
        self.score          = 0
        self.ans_labels     = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.num_tested     = 0
        self.num_attempts   = 0
        if quiz_list is None:
            self.quiz_list = []
        else:
            self.quiz_list = quiz_list

    def load_quiz(self, quiz=example_quiz):
        self.quiz_list.append(quiz)

    def run_single_quiz(self, qnum):
        to_test     = self.quiz_list[qnum]
        choices     = to_test['choices'].items()
        shuffle(choices)
        question    = 80*"*" + "\n"
        question    += to_test['question']
        solutions   = []
        for l,c in zip(self.ans_labels[:len(choices)],choices):
            question += "(%s) %s\n"%(str(l), c[0])
            if c[1] is True:
                solutions.append(str(l))
        #Ask question
        response    = raw_input(question)
        if response.upper() in solutions:
            self.score += 1
            print "Correct!"
        else:
            print "Incorrect!"
        self.num_tested += 1

    def run_all_quizzes(self):
        if self.score != 0:
            self.reset_quiz()
        #Shuffle the order of quizzes and run them
        quiz_order = range(len(self.quiz_list))
        shuffle(quiz_order)
        for qn in quiz_order:
            self.run_single_quiz(qn)
        self.num_attempts += 1
        self.report_score()

    def report_score(self):
        print  80*"*"
        print "Number of attempts at this quiz: %d "%(self.num_attempts)
        print "Number of correct answers in last attempt: %d out of %d questions"%(self.score, self.num_tested)

    def reset_quiz(self):
        print "Resetting scores"
        self.score      = 0
        self.num_tested = 0
