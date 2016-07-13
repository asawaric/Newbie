import Quizzer

quiz_list = []

#Question 1
q_lines = ["Assume x = set(['a', 'b']) and y = set(['a', 'd', 'e'])",
           "What is the output of the following?",
            ">>>print [x+y, x-y, y-x]",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"TypeError: unsupported operand type(s) for +: 'set' and 'set":True,
                            "set(['b'])":False,
                            "set(['e', 'd'])":False,
                            "{b} and {d,e}": False,
                            "['b'],['d','e']":False }
                }
                )

#Question 2
q_lines = ["Which of the following Python code can remove duplicates from the list?",
           "lst = [1,2,1,2,3,4,2,1,1]",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"lst.remove(1) and lst.remove(2)":False,
                            "del(lst[1]) and del(lst[2])":False,
                            "lst.remove(1,2)": False,
                            "set[lst]": False,
                            "set(lst)":True }
                }
                )

#Question 3
q_lines = ["Let y = set(['a', 'd', 'e'])",
            "How do you remove 'a' from y?",
            "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"y.remove('a')":True,
                            "y.discard('a')":True,
                            "del('a')": False,
                            "y = y[1:]":True,
                            "del(y[0])":False }
                }
                )

test = Quizzer.selfTest(quiz_list=quiz_list)
