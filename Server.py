import socket
from _thread import *
import sys

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(1)
print("Waiting for connection, Server Started")


def trapped_client(conn):

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(trapped_client, (conn,))
