import Quizzer

quiz_list = []

#Question 1
q_lines = ["Which of the following are correct ways of creating a dictionary?",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"d = {}":True,
                            'dict([("age", 25)])':True,
                            "dict(Grapes = 1000, Apple = 100, Melon = 10)": True,
                            'dict{[("age", 25)]}': False,
                            "dict([])":True }
                }
                )

#Question 2
q_lines = ["Let d = {'correct':1, 'incorrect':'answer' }",
	   "How do you print the 'answer' string in this Python dictionary?",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {'d["incorrect"]':True,
                            'd.values("incorrect")':False,
                            "d.values{1}": False,
                            "d{'answer'}": False,
                            "'answer' in d.values()":False }
                }
                )

#Question 3
q_lines = ["Let d0 = {'a':1, 'b':2} and d1 = {'a':3, 'c':10}",
           "Which of the following Python operations are supported?"
           "d0+d1, d1*d1, d0-d1, None of the Above",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"d0+d1":False,
                            "d0-d1":False,
                            "d0*d1": False,
                            "all of the above": False,
                            "None of the above":True,
                            }
                }
                )

#Question 4
q_lines = ["Let d0 = {'a':1, 'b':2}", 
           "Which of these are legitimate ways of adding the following key,value {'d':3}?",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"d0{'d'= 3}":False,
                            "d0['d'] = 3":True,
                            "d0.update({'d':3})": True,
                            "d0.add{d:3}": False,
                            "d0.append('d':3)":False }
                }
                )
#Question 5
q_lines = ["What is the output of the following?",
           ">>> d0 = {'a': 10, 'b':100}",
           ">>> d0.update({'a': 1000, 'c':10})",
           ">>> print d0['a']?",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"a = 1000":False,
                            "1000":True,
                            "10": False,
                            "a = 10": False,
                            "[1000]":False }
                }
                )
#Question 6
q_lines = ["What is the output of the following?",
           ">>> d0 = {'a': 10, 'b':100}",
           ">>> print d0.items()",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"[('a', 10), ('b', 100)]":True,
                            "a = 10, b = 100":False,
                            "(a=10),(b=100)":False,
                            "{a=10, b=100}": False,
                            "{a,b,10,100}":False }
                }
                )

test = Quizzer.selfTest(quiz_list=quiz_list)
