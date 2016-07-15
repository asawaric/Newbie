import Quizzer

quiz_list = []

#Question 1
q_lines = ["Which of the following are legitimate Python lists?",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"['at', 'the', ['library']]":True,
                            "('at', 'the', 'library')":False,
                            "[1250, 3412, 6225, 4525]":True,
                            "{'a', 'b', 'c', 'd'}": False,
                            "['a', 'b', 'c', 'd']":True }
                }
                )

#Question 2
q_lines = ["Let lst = [[4,2], [['a', ['answer']], 3, 4]]",
	    "How do you access the answer variable in this lst?",
            "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"lst[1[0]]":False,
                            "lst[1[0[1]]]":False,
                            "lst[1][0][1]":True,
                            "[1][0][1]":False,
                            "lst(1(0(1)))":False
                            }
                }
                )

#Question 3
q_lines = ["Assume x = ['a', 'b'] and y = ['c', 'd', 'e']",
	   "Which operations are allowed in Python?",
	   "[x+y, x-y, x*y, x**y, x/y, x//y, x%y]",
            "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"all the above":False,
                            "only x+y":True,
                            "x+y and x*y":False,
                            "only x*y":False,
                            "None of the above":False
                            }
                }
                )

#Question 4
q_lines = ["Assume x = 'hello' and y = 'world'",
	   "Which operations are allowed in Python?",
	   "[x+y, x-y, x*y, x**y, x/y, x//y, x%y]",
           "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"none of the above":False,
                            "only x*y":False,
                            "only x+y":True,
                            "all the above":False,
                            "x+y, x-y ad x//y":False
                            }
                }
                )


#Question 5
q_lines = ["Let lst = ['a', ['c',[42, ['answer'], 'b']]",
    "Which of the following correctly accesses the answer variable?",
        "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices' : { "lst(1)(2)(1)(1)" :False,
                              "lst[1][2][1][1]" :False,
                              "lst[2][0][0][1]" :False,
                              "lst(1)(1)(1)(0)":False,
                              "lst[1][1][1][0]":True,
                              }
                }
                )

#Question 6
q_lines = ["let lst = ['a', 'b', 'c', 'd']",
    "Which of the following commands would print the list backwards?",
        "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices': {"lst[-1:0:-1]":False,
                            "lst[1:0:1]":False,
                            "lst[-1::-1]":True,
                            "lst[3::1]":False,
                            "lst[3::-1]":False,
                            }
                }
                )



test = Quizzer.selfTest(quiz_list=quiz_list)
