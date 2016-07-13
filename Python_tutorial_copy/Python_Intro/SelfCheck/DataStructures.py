import Quizzer

quiz_list = []

#Question 1
q_lines = ["Which are legitimate ways of accessing the Python dictionary below?:",
            "my_d= {1:'a', 2:'b', 3:'c'}",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"my_d[0]":False,
                            "my_d['a']":False,
                            "my_d('1')": False,
                            "my_d['1']": False,
                            "my_d[1]":True }
                }
                )

#Question 2
q_lines = ["Assuming x0 = [1,2,3] and x1 = [3, 4, 5]",
            "Which of the following list operations are allowed?",
            "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"x0 + x1":True,
                            "x0 - x1":False,
                            "x1 * x0":False,
                            "x0 / x0":False,
                            "x1 * 10":True
                            }
                }
                )


test = Quizzer.selfTest(quiz_list=quiz_list)
