import Quizzer

quiz_list = []

#Question 1
q_lines = ["Assume x = ('a', 'b') and y = ('c',)",
	   "Which of the following operations are allowed in Python?",
	   "[x+y, x-y, x*y, x**y, x/y, x//y, x%y]",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"None of the above":False,
                            "x+y and x**y":False,
                            "only x*y":False,
                            "x+y and x*y": False,
                            "only x+y":True }
                }
                )

#Question 2
q_lines = ["What is the result of the following?",
           ">>> (x,y,) = (100,200)",
           ">>> print x+y",
           "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"300":True,
                            "(300)":False,
                            "[300]":False,
                            "(x)+(y)":False,
                            "set([300])":False
                            }
                }
                )

#Question 3
q_lines = ["Let lst = ((4,2), (('a', ('answer')), 3, 4))",
           "How do you access the answer variable in this tuple?",
           "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"lst[1][0][1]":True,
                            "lst[-1][-3][-1]":True,
                            "lst[1]":False,
                            "lst(1)":False,
                            }
                }
                )

#Question 4
q_lines = ["Assume x = ('a', 'b',)", 
           "Which is the correct way of adding 'c' to this tuple?",
           "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"(x, 'c')":False,
                            "x = x + ('c',)":True,
                            "x += 'c',":True,
                            "(x)+(c)":False,
                            "x + 'c'":False
                            }
                }
                )
#Question 5
q_lines = ["Assume x = ('a', 'b', 'c')", 
           "Which is the correct way of removing 'c' from this tuple?",
           "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices': {"Tuples are immutable, hence it doesn't support removing and deletion of an item ":True,
                            "x.remove('c')":False,
                            "del(x[c])":False,
                            "x-('c',)":False,
                            "x -= 'c',":False
                            }
                }
                )

test = Quizzer.selfTest(quiz_list=quiz_list)
