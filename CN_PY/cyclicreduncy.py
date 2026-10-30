def xor(x, y): 
    ans = "" 
    for i in range(len(y)): 
        if x[i] == y[i]: 
            ans += '0' 
        else: 
            ans += '1' 
    return ans 
def divide(dividend, divisor): 
    q = len(divisor) 
    temp = dividend[:q] 
    while q < len(dividend): 
        if temp[0] == '1': 
            temp = xor(divisor, temp) + dividend[q] 
        else: 
            temp = xor('0' * len(divisor), temp) + dividend[q] 
        temp = temp[1:] 
        q += 1 
    if temp[0] == '1': 
        temp = xor(divisor, temp) 
    else: 
        temp = xor('0' * len(divisor), temp) 
    return temp[1:] 
# Input 
key = input("Enter the CRC divisor (key): ") 
send = input("Enter the binary dividend data to send (frame): ") 
rec = input("Enter the binary data at receiver side: ") 
# Sender side 
length = len(key) 
send1 = send + '0' * (length - 1) 
rem = divide(send1, key) 
print("Remainder at sender side (CRC bits):", rem) 
# Receiver side 
ans = divide(rec, key) 
print("Remainder at receiver side:", ans) 
# Error detection 
if ans == '0' * (len(key) - 1): 
    print("No error in received data.") 
else: 
    print("Frame error detected in received data.") 

#OUTPUT
# KEY - 1101
# FRAME - 100100
# RECIVER SIDE - 100100001
