#!/usr/bin/env python3
""" Server for Computer Communication """
import sys
import time
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM


class ServerCommunications():
	def __init__(self, portNumber=33000, size=1024):
		"""Sets up definitions"""
		self.classname = "-- ServerCommunications --:"
		self.hostName = gethostbyname('0.0.0.0')
		self.port = portNumber
		self.size = size

		self.message = ''

		# Debug Print
		print("{0} server definitions set to Host {1}, Port {2}".format(self.classname, self.hostName, self.port))

		self.setupSocket()

	def setupSocket(self):
		""" Starts Socket """
		self.mySocket = socket( AF_INET, SOCK_DGRAM )
		self.mySocket.bind( (self.hostName, self.port) )

		# Debug Print
		print("{0} socket created".format(self.classname))


	def getMessage(self):
		""" Sends a Message to the Server """
		(self.data, self.addr) = self.mySocket.recvfrom(self.size)

		self.message = self.data.decode("utf8")

		# Debug Print
		print("{0} got a message '{1}' from ip {2}".format(self.classname, self.message, self.addr))

		return self.message, self.addr

	def exitConsole(self):
		""" Quits console """
		sys.exit()



""" If ran alone, run test script """
serverconnection = ServerCommunications(33000)
(mes, ad) = serverconnection.getMessage()
print(mes, ad)
time.sleep(5)
serverconnection.exitConsole()
