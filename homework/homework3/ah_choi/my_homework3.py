# 문제 2

for i in reversed(range(1, 10)):
    for j in reversed(range(1, 10)):
        print(i*j)



# 문제 1

def checkio(data: str) -> bool:
    #replace this for solution
    if len(data) < 10:
        result1 = False
    else:
        result1 = True
    char = list(data)
    # for i in range(0, len(char)):
    #     print(char[i])
    char_d = list(data)
    char_l = list(data)
    char_u = list(data)
    for i in range(0, len(data)):
        char_d[i] = char[i].isdigit()
        # print(char_d[i])
    result2 = True in char_d
    for i in range(0, len(data)):
        char_l[i] = char[i].islower()
        # print(char_l[i])
    result3 = True in char_l
    for i in range(0, len(data)):
        char_u[i] = char[i].isupper()
        # print(char_u[i])
    result4 = True in char_u
    return result1 and result2 and result3 and result4

print(checkio('QwErTy911poqqqq'))