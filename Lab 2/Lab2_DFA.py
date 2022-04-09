c = (int(input()))
strings = []
for j in range(c):
    strings.append(input())

for j in range(len(strings)):

    flag = False

    email = strings[j]
    if "@" in email and not email.startswith("www.") and not email[0].isnumeric() and not email.startswith(
            '.') and not '..' in email and not " " in email:
        state = 0
        char_email = list(email)
        for i in char_email:
            if state == 0 and i.isalpha():
                state = 1
                # print("state1")
            elif state == 1 and i.isalpha() and not i.isnumeric():
                state = 1
                # print("state1")

            elif state == 1 and i == "@":
                state = 2
                # print("state2")

            elif state == 2 and i.isalpha():
                state = 3
                # print("state3")
            elif state == 2 and i.isnumeric() and i == "@" and i == ".":
                state = 6

                # print("state6")
            elif state == 3 and i.isalpha():
                state = 3
                # print("state3")
            elif state == 3 and i == ".":
                state = 4
                # print("state4")
            elif state == 3 and i.isnumeric() and i == "@":
                state = 6

                # print("state6")
            elif state == 4 and i.isalpha():
                state = 5
                # print("state5")
            elif state == 4 and i.isnumeric() and i == "@" and i == ".":
                state = 6

                # print("state6")
            elif state == 5 and i.isalpha():
                state = 5
                flag = True
                # e=st[0]
                # print("state5")
            elif state == 5 and i.isnumeric() and i == "@" and i == ".":
                state = 6

                # print("state5")
            elif state == 6 and i.isalpha() and i.isnumeric() and i == "@" and i == ".":
                state = 6
        if flag == True:
            # print("valid" )
            print("Email, " + str(j+1))

    flag = False

    email = strings[j]
    fg = "fl"
    if email.startswith('www.') and not email[0].isnumeric() and not '..' in email and not " " in email and (
            email.endswith('.com') or email.endswith('.org') or email.endswith('.edu') or email.endswith('.info')):
        state = 0
        char_web = list(email)
        for i in char_web:
            if state == 0 and i.isalpha() and not i.isnumeric():
                state = 1
            elif state == 1 and i.isalpha():
                state = 1
                # print("state7w")
            elif state == 1 and i.isnumeric() and i == "@" and i == ".":
                state = 6
                # print("state6w")
            elif state == 1 and i == ".":
                state = 2
                # print("state8w")
            elif state == 2 and i.isalpha() and i.isnumeric() and i == "@":
                state = 6
                # print("state6w")
            elif state == 2 and i.isalpha():
                state = 3
                # print("state9w")
            elif state == 3 and i == "@" and i == ".":
                state = 6
                # print("state6w")
            elif state == 3 and i.isalpha() and i.isnumeric():
                state = 3
                # print("state9w")
            elif state == 3 and i == "@" and i == ".":
                state = 6
                # print("state6w")
            elif state == 3 and i == ".":
                state = 4
                # print("state10w")
            elif state == 4 and i.isalpha() and i.isnumeric() and i == "@":
                state = 6
                # print("state6w")
            elif state == 4 and i.isalpha():
                state = 5
                # print("state11w")

            elif state == 5 and i.isalpha():
                state = 5
                # print("state11w")
                flag = True

            elif state == 5 and i.isnumeric() and i == "@" and i == ".":
                state = 6

        if flag == True:
            # print("valid" )
            print("Web, " + str(j+1))

