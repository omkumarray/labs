import socket 
import time 
receiver_socket = socket.socket() 
time.sleep(2) 
receiver_socket.connect(('localhost', 12345)) 
expected_frame = 1 
while True: 
    try: 
        data = receiver_socket.recv(8000).decode() 
        if not data: 
            break 
        frame = int(data) 
        print(f"Receiver: Frame {frame} received") 
        if frame == expected_frame: 
            print(f"Receiver: Sending ACK {frame}") 
            receiver_socket.send(str(frame).encode()) 
            expected_frame += 1 
        else: 
            print( 
                f"Receiver: Duplicate or out-of-order frame {frame}, " 
                f"but expected {expected_frame}" 
            )  # Send ACK for the previous correctly received frame 
            receiver_socket.send(str(expected_frame - 1).encode()) 
    except Exception: 
        break 
receiver_socket.close()