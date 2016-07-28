my_list = []

while True:
    input = raw_input("Enter a string to be appended to this list. Type q to discontinue\n")
    if input not in ['q']:
         my_list.append(input)
    else:
        break

for i in reversed(my_list):
    print i
