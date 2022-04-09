def check(text, position):
    if text[0] not in '0123456789':
        if ('@' not in text) or (text[:4] == "www.") and (text[-4:] == '.com' or text[-4:] == '.org' or text[-4:] == '.net' or text[-4:] == '.edu' or text[-4:] == '.gov' or text[-4:] == '.mil'):
            print("Web, ", position+1)
        else:
            text_ind = None
            for i in range(len(text)):
                if text[i] == '@':
                    text_ind = i + 1
                    break

            if (text[text_ind:] == 'gmail.com' or text[text_ind:] == 'yahoo.com' or text[text_ind:] == 'hotmail.com' or text[text_ind:] == 'outlook.com') and text_ind != None:
                print("Email, ", position+1)


file = open('text.txt', 'r')
text = file.read().splitlines()[1:]
for i in range(len(text)):
    check(text[i], i)
