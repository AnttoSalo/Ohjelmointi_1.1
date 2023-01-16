import random
code = ""
code2 = ""
for i in range(3):
    n=random.randint(0,9)
    code += str(n)
print(code)
for i in range(4):
    n=random.randint(1,6)
    code2 += str(n)
print(code2)