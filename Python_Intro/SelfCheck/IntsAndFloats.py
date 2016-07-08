import Quizzer

quiz_list = []

#Question 1
q_lines = ["Assume x = 5 and y = 4",
            "What is the result of following operations?",
	    "[x**y] and [x*y]",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"544 and 54":False,
                            "625 and 20":True,
                            "20 and 625": False,
                            "45 and 455": False,
                            "20 and 20": False 
                            }
                }
                )

#Question 2
q_lines = ["Assume x = 5.0 and y = 4.0",
            "What is the result of following operations?",
	    "[x+y] and [x-y]",
            "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"9.0 and 1.0":True,
                            "9 and 1":False,
                            "0.9 and 0.1":False,
                            "[9] and [1]":False,
                            "[9.0] and [1.0]":False
                            }
                }
                )

#Question 3
q_lines = ["Assume x = 5 and y = 4",
            "What is the result of following operations?",
	    "[x+y] and [x-y]",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"9.0 and 1.0":False,
                            "9 and 1":True,
                            "0.9 and 0.1":False,
                            "[9] and [1]":False,
                            "[9.0] and [1.0]":False 
                            }
                }
                )
#Question 4
q_lines = ["Assume x = 5.0 and y = 4.0",
            "What is the result of following operations?",
	    "[x//y] and [x%y]",
            "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"1.0 and 1.0":True,
                            "1.25 and 0":False,
                            "0 and 1.25":False,
                            "1 and 1":False,
                            "0.8 and 0":False
                            }
                }
                )

#Question 5
q_lines = ["Assume x = 5 and y = 4",
            "What is the result of following operations?",
	    "[x//y] and [x%y]",
            "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"1.0 and 1.0":False,
                            "1.25 and 0":False,
                            "0 and 1.25":False,
                            "1 and 1":True,
                            "0.8 and 0":False
                            }
                }
                )
#Question 6
q_lines = ["Assume x = 5.0 and y = 4.0",
            "What is the result of following operations?",
	    "[x/y]",
            "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"1.25":True,
                            "1":False,
                            "0.8":False,
                            "1.0":False,
                            "[1]":False
                            }
                }
                )

#Question 7
q_lines = ["Assume x = 5 and y = 4",
            "What is the result of following operations?",
	    "[x/y]",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"1.25":False,
                            "1":True,
                            "1.0":False,
                            "[1]":False
			    }
                }
                )

#Question 8
q_lines = ["Assume x = 5.0 and y = 4.0",
            "What is the result of following operations?",
	    "[x**y] and [x*y]",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"544 and 54":False,
                            "625.0 and 20.0":True,
                            "625 and 20": False,
                            "20 and 625": False,
                            "20.0 and 20.0": False }
		}
		)


test = Quizzer.selfTest(quiz_list=quiz_list)






