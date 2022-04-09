with open('input.txt') as input_test:
    lines = input_test.read().replace(',', ' ,').replace(';', ' ;')
input_test.close()

keywords = ["auto", "break", "case", "char", "const", "continue", "default",
            "do", "double", "else", "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return", "short", "signed",
            "sizeof", "static", "struct", "switch", "typedef", "union",
            "unsigned", "void", "volatile", "while"]

numerics = []
others = []
math_ops = []
logical_ops = []
identifiers = []
key = []
a = False

for ch in lines.split():

    try:
        i.isnumeric()
        a = True
    except ValueError:
        a = False

    if a:
        if i not in numerics:
            numerics.append(i)
    elif (ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')' or ch == '{' or ch == '}'):
        if ch not in others:
            others.append(ch)
    elif (ch == '+' or ch == '-' or ch == '=' or ch == '*' or ch == '/' or ch == '%'):
        if ch not in math_ops:
            math_ops.append(ch)
    elif (ch == '>' or ch == '<' or ch == '&&' or ch == '||' or ch == '!' or ch == '%'):
        if ch not in logical_ops:
            logical_ops.append(ch)
    elif ch in keywords:
        if ch not in key:
            key.append(ch)
    else:
        if ch not in identifiers:
            identifiers.append(ch)


output_text = open('output.txt', 'w')
output_text.write(f"Keywords: ")
output_text.write(", ".join(key))
output_text.write(f"\n")
output_text.write(f"Identifiers: ")
output_text.write(", ".join(identifiers))
output_text.write(f"\n")
output_text.write(f"Math Operators: ")
output_text.write(", ".join(math_ops))
output_text.write(f"\n")
output_text.write(f"Logical Operators: ")
output_text.write(", ".join(logical_ops))
output_text.write(f"\n")
output_text.write(f"Numerical Values: ")
output_text.write(", ".join(numerics))
output_text.write(f"\n")
output_text.write(f"Others: ")
output_text.write(" ".join(others))

output_text.close()
input_test.close()
