#!/usr/bin/env python3
"""Script for Client to execute commands"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys

class WhiteSwanClient():
    def __init__(self, serverIP, portNumber = 33000, size = 1024):
        """ Sets up definitions """
        self.classname = "-- ClientCommunications --: "
        self.ip = serverIP
        self.port = portNumber
        self.size = size
        self.BUFSIZ = 1024

        # Debug Print
        print("{0} client setup to ip {1}, via port {2}".format(self.classname, self.ip, self.port))

        self.setupSocket()

    def setupSocket(self):
        """ Starts Socket """
        self.mySocket = socket(AF_INET, SOCK_STREAM)
        self.mySocket.connect((self.ip,self.port))

    def receiveMessage(self):
        """ Handles receiving of messages """
        while True:
            try:
                message = self.mySocket.recv(self.BUFSIZ).decode("utf8")
                return message
            except OSError:
                break

    def sendMessage(self, message):
        """ Sends a Message to the Server """
        self.mySocket.send(bytes(message, "utf8"))

        # Debug Print
        #print("{0} sent a message ('{1}') to ip {2}, via port {3}".format(self.classname, message, self.ip, self.port))

    def exitConsole(self):
        """ Quits console """
        sys.exit()



""" If ran alone, run test script """
if __name__ == '__main__':
    clientconnection = WhiteSwanClient('38.109.217.102', 33000)
    clientconnection.sendMessage(input("Name?"))
    clientconnection.sendMessage(input("Type?"))
    id = clientconnection.receiveMessage()
    print(id)
    while True:
        print(clientconnection.receiveMessage())
