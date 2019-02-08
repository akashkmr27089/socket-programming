import threading
import socket

def reciver(b):
    print(" Accepted the data from :")
    print(" Waiting for the Messages ")
    try:
        while True:
            data = str(b.recv(1024))
            data = data.strip("b''")
            print(data)
    except KeyboarError:
        exit(0)

def sender(b):
    print(" Accepted the data from :")
    try:
        while True:
            b.send(input(" Your Querry :").encode('utf-8'))
    except KeyboarError:
        exit(0)


if __name__ == "__main__":
    a = socket.socket()
    a2 = socket.socket()
    port = 12312 #Reciver
    port2 = 12441 #Sender
    a.bind(("",port))
    a.listen(12)
    print(" Sender Port Number {} \n Reciver Port Number {}:".format(port2, port))
    b,addr = a.accept()
    print(" Connection Accepted from for Reciver \n", b )
    print("\n")

    a2.bind(("",port2))
    a2.listen(12)
    print(" Port Number :", port2)
    b2,addr2 = a2.accept()
    print(" Connection Accepted from for Sender \n", b2 )
    print("\n")

    # creating thread
    t1 = threading.Thread(target=sender, args=(b2,))
    t2 = threading.Thread(target=reciver, args=(b,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
