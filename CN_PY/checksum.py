s1 = input("Enter the string of 0's and 1's as submit 1: ") 
s2 = input("Enter the string of 0's and 1's as submit 2: ") 
s1 = s1[::-1] 
s2 = s2[::-1] 
res = "" 
ans = "" 
c = '0' 
for i, j in zip(s1, s2): 
    if i == '0' and j == '0' and c == '0': 
        res += '0' 
        c = '0' 
    elif i == '0' and j == '0' and ce == '1':   # ERROR: ce 
        res += '1' 
        c = '0' 
    elif i == '0' and j == '1' and c == '0': 
        res += '1' 
        c = '0' 
    elif i == '0' and j == '1' and c == '1': 
        res += '0' 
        c = '1' 
    elif i == '1' and j == '0' and c == '0': 
        res += '1' 
        c = '0' 
    elif i == '1' and j == '0' and c == '1': 
        res += '0' 
        c = '1' 
    elif i == '1' and j == '1' and c == '0': 
        res += '0' 
        c = '1' 
    else: 
        res += '1' 
        c = '1' 
if c == '1': 
    ans = "" 
    for i in res: 
        if i == '0':   ans += '1' 
        else: ans += '0' 
    c = '0' 
    if i == '1' and c == '0': ans += '0' 
    elif i == '1' and c == '1':  ans += '1' 
else: ans = "" 
final = "" 
for i in res: 
    if i == '1': final += '0' 
    else:  final += '1' 
print("Checksum of two subnets:", final[::-1])

#output - 
# 1 - 01011101
# 2 - 10101110