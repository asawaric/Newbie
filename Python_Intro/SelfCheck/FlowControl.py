import Quizzer

quiz_list = []

#Question 1
q_lines = ["Which of the following Python code will produce the following output?",
           "[2, 4, 6, 8, 10]",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"range(2,11,2)":True,
                            "range(10,0,-2)":False,
                            "range(2,12,2)":True,
                            "range[2,2,10]": False,
                            "range(2,2,10)":False }
                }
                )

#Question 2
q_lines = ["Which is the correct answer to the MYSTERY LINE below?",
           '>>> lst = ["apple", 1, 4.]',
           ">>> MYSTERY LINE", 
           ">>>     print elem",
           '>>> "apple"',
           ">>> 1",
           ">>> 4.0?",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"for elem in lst:":True,
                            "elem = '\n'.join(lst)":False,
                            "for n, elem in enumerate(lst):":True,
                            "for n, elem in zip(lst, lst):":True,
                            "None of the above":False }
                }
                )

#Question 3
q_lines = ["Which is the correct answer to the MYSTERY LINE below?",
           ">>> lst = range(5)",
           ">>> MYSTERY LINE", 
           ">>>     print n + elem",
           ">>> 0",
           ">>> 2",
           ">>> 4",
           ">>> 6",
           ">>> 8",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"for n, elem in lst():":False,
                            "for n, elem in enumerate(lst,  0):":True,
                            "for elem in lst":False,
                            "for n, elem in enumerate(lst, 2)": False}
                }
                )
#Question 4
q_lines = ["Which is the correct answer to the MYSTERY LINE below?",
           ">>> my_dict = {1:'a', 2:'b', 3:'c'}",
           ">>> MYSTERY LINE", 
           ">>>     print k, v",
           ">>> 1 a",
           ">>> 2 b",
           ">>> 3 c",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"for (k,v) in my_dict.items():":True,
                            "[(k, v) in my_dict.iteritems()]":False,
                            "for k, v in my_dict.iteritems():":True,
                            "for k in my_dict.keys():": False,
                            "k, v in my_dict.items()":False }
                }
                )

#Question 5
q_lines = ["What is the ouptput from this Python code?",
           ">>> for i in range(10):",
           ">>>    if i < 3: ", 
           ">>>        continue",
           ">>>    print i",
           ">>>    if i > 5:",
           ">>>        break",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"3 4 5 6":True,
                            "3 4 5":False,
                            "[3, 4, 5]":False,
                            "[3, 4, 5, 6]": False,
                            "1 2 4":False }
                }
                )
#Question 6
q_lines = ["What is the ouptput of the following?",
           ">>> sum([i**(i%2) for i in range(50) if (i%2) == 0])",
           "\n"]
quiz_list.append(
                {
                'question':'\n'.join(q_lines),
                'choices':  {"25":True,
                            "5**5":False,
                            "27":False,
                            "24": False,
                            "49":False }
                }
                )

#Question 7
q_lines = ["What is the ouptput of the following?",
           ">>> [i**(i%2) for i in range(5) if (i%2) == 1]",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"[1, 3]":True,
                            "[1, 1, 3, 9]":False,
                            "[1, 1, 1, 1, 1, 1, 3, 9, 27, 81]":False,
                            "(1, 3)": False,
                            "None of the above":False }
                }
                )
#Question 8
q_lines = ["What is the ouptput of the following?",
           ">>> print [[i,j] for i in range(3) for j in range(i)]",
           "\n"]
quiz_list.append(
                {
                'question': '\n'.join(q_lines),
                'choices':  {"This produces an error":False,
                            "[[1, 0], [2, 0], [2, 1]]":True,
                            "[[0, 0], [1, 0], [2, 0]]":False,
                            "[[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]":False,
                            "[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]":False }
                }
                )

test = Quizzer.selfTest(quiz_list=quiz_list)














