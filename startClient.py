from urllib.request import urlopen
import time
import os


class Client:
    """ Client for WhiteSwan """
    def __init__(self):
        self.classname = "Client"
        self.website = 'http://whiteswan.blayone.com/'

        self.serveripURL = self.website + 'server.txt'
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

    def command(self, command):
        
    def getIP(self):
        ip_response = urlopen(self.serveripURL)
        ip = ip_response.read().decode('utf8')
        return ip
