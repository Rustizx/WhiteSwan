#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class CommunicationsServer:
	def __init__(self, port = 33000):
		self.clients = {}
		self.addresses = {}

		self.HOST = ''
		self.PORT = port
		self.BUFSIZ = 1024
		self.ADDR = (self.HOST, self.PORT)
		
	def startSocket(self):
		self.SERVER = socket(AF_INET, SOCK_STREAM)
		self.SERVER.bind(self.ADDR)
	
	def startServer(self):
		self.startSocket()
		self.SERVER.listen(5)
		print("Waiting for connection...")
		self.ACCEPT_THREAD = Thread(target=self.accept_incoming_connections)
		self.ACCEPT_THREAD.start()
		self.ACCEPT_THREAD.join()
		self.SERVER.close()
	
	def accept_incoming_connections(self):
		"""Sets up handling for incoming clients."""
		while True:
			self.client, self.client_address = self.SERVER.accept()
			print("%s:%s has connected." % self.client_address)
			self.client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
			self.addresses[self.client] = self.client_address
			Thread(target=self.handle_client, args=(self.client, self.client_address,)).start()


	def handle_client(self, client, addr):  # Takes client socket as argument.
		"""Handles a single client connection."""

		self.name = client.recv(self.BUFSIZ).decode("utf8")
		self.welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % self.name
		client.send(bytes(self.welcome, "utf8"))
		print(str(addr) + " renamed to " + self.name)
		self.msg = "%s has joined the chat!" % self.name
		self.broadcast(bytes(self.msg, "utf8"))
		self.clients[client] = self.name
		print(str(self.clients))

		while True:
			self.msg = self.client.recv(self.BUFSIZ)
			if self.msg != bytes("{quit}", "utf8"):
				self.broadcast(self.msg, self.name+": ")
			else:
				self.client.send(bytes("{quit}", "utf8"))
				self.client.close()
				del self.clients[self.client]
				self.broadcast(bytes("%s has left the chat." % self.name, "utf8"))
				print("%s has left the chat." % self.name)
				break


	def broadcast(self, msg, prefix=""):  # prefix is for name identification.
		"""Broadcasts a message to all the clients."""

		for sock in self.clients:
			sock.send(bytes(prefix, "utf8")+msg)




server = CommunicationsServer(33000)
server.startServer()



