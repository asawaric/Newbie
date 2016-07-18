from random import shuffle
import ConfigParser
import os
import cPickle as pickle
from collections import OrderedDict

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class selfTest:
    def __init__(self, userDir="Users", questDir="Questions"):
        self.ans_labels     = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.quizzes        = {}
        self.user_hist      = {"uid":"", "results":{}}
        self.user_fn        = None
        if not os.path.isdir(userDir):
            os.mkdir(userDir)
        self.userDir        = userDir
        self.questDir       = questDir
        self.menuOpts       = None

    def init_user_name(self):
        """
        Obtain user name to make user record
        """
        prompt          = "What is your userID: e.g. john smith lee)?\n"
        response        = raw_input(prompt)
        try:
            self.user_hist["uid"] = ''.join([l.lower() for l in response if l.isalpha()])
        except:
            print "Error with name. Exiting!"
        self.user_fn    = os.path.join(self.userDir, self.user_hist["uid"]+".pkl")

    def init_menu(self):
        """
        Initialize menu options
        """
        quizNames       = self.quizzes.keys()
        for qn in quizNames:
            if qn not in self.user_hist["results"].keys():
                probKeys = self.quizzes[qn]["problems"].keys()
                self.user_hist["results"][qn] = {p:[] for p in probKeys}
        numQuizzes          = len(quizNames)
        options    = {str(o):c for o,c in zip(range(1,numQuizzes+1), quizNames)}
        options.update({"Q":"QUIT"})
        #Add additional options here. Have to have alphabet keys
        self.menuOpts = {k:v for k,v in sorted(options.items(), key=options.get)}

    def print_menu(self):
        """
        Print options in menu for user selection
        """
        self.print_decorated_txt("MAIN_MENU", dec="=")
        digitkeys   = [k for k in self.menuOpts.keys() if k.isdigit()]
        alphakeys   = [k for k in self.menuOpts.keys() if k.isalpha()]
        digitkeys.sort()
        alphakeys.sort()
        for k in digitkeys:
            probNames = self.quizzes[self.menuOpts[k]]["problems"].keys()
            numProbs = len(probNames)
            should_not_test = self.find_problems_not_to_test(self.menuOpts[k])
            should_test = set(probNames) - set(should_not_test)
            txt = k.ljust(2) + self.menuOpts[k].ljust(30,"-") + ("%d questions"%(numProbs)).ljust(15)
            if len(should_test) > 0:
                txt += bcolors.FAIL + "(Incomplete)" + bcolors.ENDC
            else:
                txt += bcolors.OKGREEN + "(Done)" + bcolors.ENDC
            self.print_colored_txt(txt, bcolors.OKBLUE)
        for k in alphakeys:
            self.print_colored_txt(k.ljust(2)+self.menuOpts[k], bcolors.BOLD)

    def main_loop(self):
        """
        Menu selection for quizzes
        """
        self.init_user_name()
        self.read_user_record()
        self.find_quizzes()
        self.parse_all_quizzes()
        self.init_menu()
        # Main WHILE loop of the menu
        while True:
            self.print_menu()
            response = raw_input()
            try:
                if response.isdigit():
                    self.take_quiz(self.menuOpts[response])
                    self.write_user_record()
                elif (response.lower() == "q"):
                    print "Exiting quiz taker!"
                    break
                else:
                    print "Unrecognized option. Exiting quiz taker!"
                    break
            except:
                print "Main loop failed for unknown reasons. Exiting quiz taker!"
                break

    def find_quizzes(self):
        """
        Find all quiz files in questDir and its subdirectories with file extension *.cfg
        """
        for root, dirs, files in os.walk(self.questDir):
            for f in files:
                if f.endswith("cfg"):
                    fname   = os.path.splitext(f)[0]
                    a_path  = os.path.join(root, f)
                    curr_d  = {"filePath":a_path}
                    self.quizzes.update({fname:curr_d})

    def attempt_problem(self, quizName, probName):
        """
        Attempt a particular problem in a particular quiz
        """
        to_test     = self.quizzes[quizName]["problems"][probName]
        choices     = to_test['choices'].items()
        shuffle(choices)
        question    = 80*"*" + "\n" + to_test['question']
        question    += "\n" + 20*"-" + "\n"
        solutions   = []
        for l,c in zip(self.ans_labels[:len(choices)],choices):
            question += "(%s) %s\n"%(str(l), c[0])
            if c[1] is True:
                solutions.append(str(l))
        if len(solutions) > 1 :
            question += "Separate your answers by commas if there multiple correct answers.\n"
        #Ask question
        response    = set([t.upper() for t in raw_input(question) if t.isalpha()])
        if response.issubset(solutions) and (len(response)>0):
            self.update_user_hist(quizName, probName, 1)
            self.print_colored_txt("Correct!", bcolors.OKGREEN)
        else:
            self.print_colored_txt("Incorrect!", bcolors.FAIL)
            self.update_user_hist(quizName, probName, 0)
        print ""

    def update_user_hist(self, quizName, probName, val):
        curr_keys = self.user_hist["results"][quizName].keys()
        if probName not in curr_keys:
            self.user_hist["results"][quizName][probName] = [val]
        else:
            self.user_hist["results"][quizName][probName].append(val)

    def take_quiz(self, quizName):
        """
        Only test problems that test-taker last got wrong
        Shuffle order of questions before issuing quiz
        """
        probNames   = self.quizzes[quizName]["problems"].keys()
        should_not_test = self.find_problems_not_to_test(quizName)
        should_test = list(set(probNames) - set(should_not_test))
        if len(should_test) == 0 :
            retest = self.yesno("No problems need to be tested. Retest all anyway?")
            if retest:
                shuffle(probNames)
                for n,p in enumerate(probNames):
                    self.print_colored_txt("Question %d of %d"%(n+1, len(probNames)), bcolors.WARNING)
                    print quizName
                    self.attempt_problem(quizName, p)
                self.show_results(quizName)
        else:
            if len(should_test) > 1: shuffle(should_test)
            for n,p in enumerate(should_test):
                self.print_colored_txt("Question %d of %d"%(n+1, len(should_test)), bcolors.WARNING)
                self.attempt_problem(quizName, p)
            self.show_results(quizName)

    def yesno(self, qn):
        """
        Function to return a yes or no response to a question
        """
        qn += "[y/n only]\n"
        ret_val = False
        while True:
            response = raw_input(bcolors.FAIL + qn + bcolors.ENDC)
            if (response.lower() == 'n'):
                ret_val = False
                break
            elif (response.lower() == 'y'):
                ret_val = True
                break
            else:
                print "Unrecognized response. Try again"
        return ret_val

    def print_decorated_txt(self, txt, col=bcolors.OKBLUE, dec="=", lineWidth=80):
        print col + lineWidth*dec
        print txt.center(lineWidth, dec)
        print lineWidth*dec	+ bcolors.ENDC

    def print_colored_txt(self, txt, col):
        print col + txt + bcolors.ENDC

    def find_problems_not_to_test(self, quizName):
        """
        Find problems in a quiz for which user last tested incorrectly
        """
        quiz_hist   = self.user_hist["results"][quizName]
        should_not_test = []
        for k,v in quiz_hist.iteritems():
            if (len(v) == 0):
                pass
            elif (v[-1] == 0):
                pass
            else:
                should_not_test.append(k)
        return should_not_test

    def show_results(self, quizName):
        """
        Print results from taking the quiz
        """
        results = self.user_hist["results"][quizName]
        self.print_decorated_txt("RESULTS", col=bcolors.WARNING, dec="*")
        for k,v in results.iteritems():
            print "Q:", k.ljust(30,"-"), str(int(sum(v))).ljust(3), "correct of ", str(len(v)).ljust(3), "attempts"
        print "\n"

    def reset_results(self, quizName):
        pass

    def write_user_record(self):
        """
        Writes user record to file. Prompts before overwriting existing records
        """
        if self.user_fn is None:
            self.print_colored_txt("User file name not initialized", bcolors.FAIL)
        elif os.path.isfile(self.user_fn):
            overwrite       = self.yesno("Overwrite user record?")
            if overwrite:
                with open(self.user_fn, "wb") as fp:
                    pickle.dump(self.user_hist, fp)
                    self.print_colored_txt("User record overwritten", bcolors.OKGREEN)
        else:
            with open(self.user_fn, "wb") as fp:
                pickle.dump(self.user_hist, fp)
                self.print_colored_txt("User record written", bcolors.OKGREEN)

    def read_user_record(self):
        """
        Reads user records. Reports if record not found
        """
        if self.user_fn is None:
            self.print_colored_txt("User file name not initialized", bcolors.FAIL)
        elif os.path.isfile(self.user_fn):
            with open(self.user_fn, "rb") as fp:
                self.user_hist = pickle.load(fp)
                self.print_colored_txt("User record loaded", bcolors.OKGREEN)
        else:
            self.print_colored_txt("User record not file", bcolors.FAIL)

    def parse_quiz(self, quizName):
        """
        Parse quiz files and load them into heap
        """
        fileName    = self.quizzes[quizName]["filePath"]
        config      = ConfigParser.ConfigParser()
        config.read(fileName)
        prob_list    = {}
        for section in config.sections():
            (choices, curr_prob)    = ({}, {})
            #print "Found question named:", section
            for opt in config.options(section):
                if opt == "statement":
                    res = config.get(section, opt)
                    curr_prob["question"] = res
                else:
                    res = config.get(section, opt).split("~~")
                    if res[1].lower().lstrip().rstrip() == "true":
                        choices[res[0]] = True
                    elif res[1].lower().lstrip().rstrip() == "false":
                        choices[res[0]] = False
                    else:
                        print "Error in the following input"
                        print quizName, section
                        print res
            curr_prob.update({'choices':choices})
            prob_list.update({section:curr_prob})
        self.quizzes[quizName].update({"problems":prob_list})

    def parse_all_quizzes(self):
        for k in self.quizzes.keys():
            self.parse_quiz(k)


if __name__ == "__main__":
    q = selfTest()
    q.main_loop()
