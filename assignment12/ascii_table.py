def recodnition(strr):
    upper = 0
    lower = 0
    for s in strr:
        if 65 <= ord(s) <= 90:
            upper += 1
        elif 97 <= ord(s) <= 122:
            lower += 1
        
    return upper, lower,
string = input("enter your word:\n")
upper, lower, = recodnition(string)
print("number of upper letters:", upper)
print("number of lower letters: ", lower)
