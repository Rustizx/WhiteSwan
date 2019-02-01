#!/usr/bin/env python3
""" Client for Computer Communication """
import sys
from socket import socket, AF_INET, SOCK_DGRAM

class ClientCommunications():
	def __init__(self, serverIP, portNumber = 5000, size = 1024):
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
		
		# Debug Print
		print("{0} socket created".format(self.classname))
		
		
	def sendMessage(self, message):
		""" Sends a Message to the Server """
		self.mySocket.sendto(bytes(message, "utf8"), (self.ip, self.port))
		
		# Debug Print
		print("{0} sent a message ('{1}') to ip {2}, via port {3}".format(self.classname, message, self.ip, self.port))
		
	def exitConsole(self):
		""" Quits console """
		sys.exit()



""" If ran alone, run test script """		
clientconnection = ClientCommunications('192.168.1.108', 5000)
clientconnection.sendMessage("Hello World")
clientconnection.exitConsole()