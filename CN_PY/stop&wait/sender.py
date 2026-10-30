import socket 
sender_socket = socket.socket() 
sender_socket.bind(('localhost', 12345)) 
sender_socket.listen(1) 
print("Sender: Waiting for a connection...") 
conn, addr = sender_socket.accept() 
print("Sender: Connected to receiver") 
# Input: Number of frames to send 
n = int(input("Enter the number of frames to send: ")) 
frames = list(range(1, n + 1)) 
for frame in frames: 
    while True: 
        print(f"Sender: Sending frame {frame}") 
        conn.send(str(frame).encode()) 
        # Set timeout for ACK 
        conn.settimeout(5.0) 
        try: 
            ack = conn.recv(8000).decode() 
            if ack == str(frame): 
                print(f"Sender: ACK {ack} received") 
                break 
        except socket.timeout: 
            print(f"Sender: Timeout. Resending frame {frame}") 
conn.close() 
sender_socket.close()



#output -
# connect both sender and reciever 
# THE NO. OF FRAME TO SEND - 3