from __future__ import print_function
import xbox

import pickle
import socket
import time



# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)

#Instantiate the controller
joy = xbox.Joystick()


localhost = "127.0.0.1"
buffer_size = 1024
port = 10001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((localhost,port))
s.listen(1)
conn,addr = s.accept()
print('The connection is built!  Connection address:', addr)


i = 0
itvl = 0.01
  
while not joy.Back():
    #Xbox
    xbox_data=[]
    xbox_data.append(i)
    connect_flag = "Yes" if joy.connected() else "No"
    xbox_data.append(connect_flag)
    
    xbox_data.append(fmtFloat(joy.leftX()))  
    xbox_data.append(fmtFloat(joy.leftY()))
    xbox_data.append(fmtFloat(joy.rightX()))
    xbox_data.append(fmtFloat(joy.rightY()))
    #for debugging
    print ('HOST','time:',xbox_data[0],'connection:',xbox_data[1],'Left X/Y:',xbox_data[2],'/',xbox_data[3],'Right X/Y:',xbox_data[4],'/',xbox_data[5])
    
    data = pickle.dumps(xbox_data)
    if not data:
        break
    conn.send(data)
    time.sleep(itvl)
    i = round(i+itvl,2)
    

conn.close()




# xboxq = [fmtFloat(joy.leftX()), fmtFloat(joy.leftY())]
# data=pickle.dumps(xboxq)
# s.send(data)