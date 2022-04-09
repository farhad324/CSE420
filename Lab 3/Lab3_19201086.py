import re

inp_count = int(input())
regex_list = []

for i in range(inp_count):
    regex_list.append(input())

count2 = int(input())
str_list = []

for i in range(count2):
    str_list.append(input())

for i in range(len(str_list)):

    for j in range(len(regex_list)):
        state = re.match(regex_list[j], str_list[i])
        if state is not None:
            print('YES', str(j + 1))
            break
        elif j == len(regex_list) - 1 and state is None:
            print('NO, 0')
            break
