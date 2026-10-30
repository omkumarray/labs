u = list(map(int, input("Enter 7 bits data of 0's and 1's separated by spaces: ").split())) 
rec = list(map(int, input("Enter the received 11 data bits of 0's and 1's separated by spaces: ").split())) 

u = u[::-1] 
u = [0, 0] + [u[0]] + [0] + u[1:4] + [0] + u[4:7] 
u[0] = (u[2] + u[4] + u[6] + u[8] + u[10]) % 2 
u[1] = (u[2] + u[5] + u[6] + u[9] + u[10]) % 2 
u[3] = (u[4] + u[5] + u[6]) % 2 
u[7] = (u[8] + u[9] + u[10]) % 2 

rec = rec[::-1] 
s1 = (rec[0] + rec[2] + rec[4] + rec[6] + rec[8] + rec[10]) % 2 
s2 = (rec[1] + rec[2] + rec[5] + rec[6] + rec[9] + rec[10]) % 2 
s3 = (rec[3] + rec[4] + rec[5] + rec[6]) % 2 
s4 = (rec[7] + rec[8] + rec[9] + rec[10]) % 2 

bit = str(s4) + str(s3) + str(s2) + str(s1) 
bit = int(bit, 2) 

if bit: 
    print("Received data is having error at position:", bit) 
else: 
    print("Received data doesn't have any error")
    
#OUTPUT 
# 1 1 1 0 1 1 0
# 1 1 1 1 0 1 1 0 0 1 1

# 1 1 1 0 1 1 0
# 1 1 1 1 0 1 0 0 0 1 1