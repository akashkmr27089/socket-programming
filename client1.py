import socket
import sys
import threading

def func1():
    try:
        while(1):
            print(" Enter the Opitions :: (1 or 2)")
            d = int(input())
            if(d == 1):
                print("Sending")
                g = input(" Enter Your Message ")
                if(g == str(0)):
                    continue
                s1.send(g.encode('utf-8'))
                s1.recv(1024)
            elif(d == 2):
                print("Recieving")
                try:
                    print(s1.recv(1024))
                except KeyboardInterrupt:
                    func1()
    except KeyboardInterrupt:
        sys.exit()

s1 = socket.socket()
s1.connect(('',int(sys.argv[1])))
s1.send(input("Enter Your name ").encode('utf-8'))
print(s1.recv(1024))
t1 = threading.Thread(target=func1)
t1.start()
t1.join()
