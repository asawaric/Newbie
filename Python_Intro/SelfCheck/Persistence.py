import Quizzer

quiz_list = []

#Question 1
q_lines = ["What is the result of following operations?",
	    ">>> x0 = 12",
            ">>> y0 = x0 + 1",
            ">>> x0 += 1",
            ">>> z0 = x0 + 1",
            ">>> print [y0, z0]",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"13 and 14":False,
                            "[13, 14]":True,
                            " 13, 13": False,
                            " 13, 14": False,
                            "[14, 14]": False 
                            }
                }
                )

test = Quizzer.selfTest(quiz_list=quiz_list)

