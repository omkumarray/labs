import socket 
import time 
# Connect to sender 
s = socket.socket() 
time.sleep(1) 
s.connect(("localhost", 8086)) 
expected = 1 
while True:
    try: 
            frame = s.recv(1024).decode() 
            if not frame: 
                break 
            frame = int(frame) 
            print(f"Receiver: Frame {frame} received") 
            if frame == expected: 
                print(f"Receiver: ACK {frame} sent") 
                s.send(str(frame).encode()) 
                expected += 1 
            else: 
                print( 
                    f"Receiver: Frame {frame} discarded, " 
                    f"expected {expected}" 
                ) 
                # Send ACK for previous correctly received frame 
                s.send(str(expected - 1).encode()) 
    except Exception: 
        break 
s.close()

#output
#connect both the sender & reciever
# no. of frame sent - 3 
# window size - 2 
 