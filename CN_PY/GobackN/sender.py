import socket 
import time 
# Create sender socket 
s = socket.socket() 
s.bind(("localhost", 8086)) 
s.listen(1) 
c, addr = s.accept() 
print("Connected to:", addr) 
# User input 
n = int(input("Enter number of frames to send: ")) 
N = int(input("Enter window size: ")) 
base = 1 
next_frame = 1 
while base <= n: 
    # Send frames within the window 
    while next_frame < base + N and next_frame <= n: 
        print("Sender: Sending frame", next_frame) 
        c.send(str(next_frame).encode()) 
        next_frame += 1 
    # Wait for ACK 
    try: 
        c.settimeout(3) 
        ack = c.recv(1024).decode() 
        if not ack: 
            break 
        ack = int(ack) 
        if ack >= base: 
            print( 
                f"Sender: ACK {ack} received, sliding window" 
            ) 
            base = ack + 1 
        else: 
            print( 
                f"Sender: Unexpected ACK {ack}, " 
                f"expected {base}. Ignoring!" 
            ) 
    except socket.timeout: 
        print( 
            f"Sender: Timeout! Resending from frame {base}" 
        )
               # Go-Back-N retransmission 
        next_frame = base 
c.close() 
s.close()

