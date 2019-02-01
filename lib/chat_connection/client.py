#!/usr/bin/env python3
"""Script for Client to execute commands"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys

class CommunicationClient():
	def __init__(self, serverIP, portNumber = 33000, size = 1024):
		""" Sets up definitions """
		self.classname = "-- ClientCommunications --:"
		self.ip = serverIP
		self.port = portNumber
		self.size = size

		# Debug Print
		print("{0} client setup to ip {1}, via port {2}".format(self.classname, self.ip, self.port))

		self.setupSocket()

	def setupSocket(self):
		""" Starts Socket """
		self.mySocket = socket( AF_INET, SOCK_DGRAM )
        self.mySocket.connect(self.ip,self.port)

		# Debug Print
		#print("{0} socket created".format(self.classname))

    def receiveMessage(self):
		""" Handles receiving of messages """
		while True:
            try:
                message = client_socket.recv(BUFSIZ).decode("utf8")
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
    clientconnection = ClientCommunications('192.168.1.108', 33000)
    name = input("Whats your name?")
    clientconnection.sendMessage(name)
    computernumber = receiveMessage()
    clientconnection.sendMessage(input())
    while True:
        clientconnection.receiveMessage()
