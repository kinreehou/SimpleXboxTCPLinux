import pickle
import socket

localhost = "127.0.0.1"
buffer_size = 1024
port=10001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((localhost, port))

while True:
    recvd_data = s.recv(buffer_size)
    data = pickle.loads(recvd_data)
    for idx in range(len(data)):
    	if data[idx]==0.:
    		data[idx]=' '
    print('CLIENT','time:',data[0],'connection:',data[1],'Left X/Y:',data[2],'/',data[3],'Right X/Y:',data[4],'/',data[5])
    if not data:
        break
s.close()