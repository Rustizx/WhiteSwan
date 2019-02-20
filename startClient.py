from urllib.request import urlopen
import time
import os, sys
from socket import AF_INET, socket, SOCK_STREAM
import uuid
from lib.info.info import *
import ctypes

from plugins.pyMusic import *

class Client:
    """ Client for WhiteSwan """
    def __init__(self, portNumber = 33000, size = 1024):
        self.classname = "Client"
        self.website = 'http://whiteswan.blayone.com/'

        self.serveripURL = self.website + 'server.txt'
        self.serverVerURL = self.website + 'currentVersion.txt'
        """ Sets up definitions """
        self.classname = '-- ClientCommunications --: '
        self.ip = self.getIP()
        self.port = portNumber
        self.size = size
        self.info = WhiteSwanInfo()
        print("{0} client setup to ip {1}, via port {2}".format(self.classname, self.ip, self.port))

    def setupSocket(self):
        """ Starts Socket """
        self.mySocket = socket(AF_INET, SOCK_STREAM)
        self.mySocket.connect((self.ip,self.port))

        # Debug Print
        #print("{0} socket created".format(self.classname))

    def receiveMessage(self):
        """ Handles receiving of messages """
        while True:
            try:
                message = self.mySocket.recv(self.size).decode("utf8")
                return message
            except OSError:
                break

    def sendMessage(self, message):
        """ Sends a Message to the Server """
        self.mySocket.send(bytes(message, "utf8"))

        # Debug Print
        #print("{0} sent a message ('{1}') to ip {2}, via port {3}".format(self.classname, message, self.ip, self.port))

    def exit(self):
        """ Quits console """
        #sys.exit()
        self.sendMessage("{quit}")

    def setCred(self):
        if('name' in self.info.clientInfo and 'id' in self.info.clientInfo):
            print(self.classname + "Name does exist")
            self.name = self.info.clientInfo["name"]
            self.id = self.info.clientInfo["id"]
        else:
            print(self.classname + "Name and/or ID does NOT exist creating new one")
            self.id = str(uuid.uuid4())
            self.name = "computer" + self.id[0] + self.id[1] + self.id[2] + self.id[4]
            newinfo = {"name": self.name, "id": self.id}
            self.info.update("client", newinfo)
        self.sendMessage(self.name)
        self.sendMessage(self.id)
        self.number = self.receiveMessage()

    def changeName(self, name):
        self.name = name
        newinfo = {"name": name}
        self.info.update("client", newinfo)
        self.exit()
        os.execl(sys.executable, sys.executable, *sys.argv)
        sys.exit()

    def getIP(self):
        ip_response = urlopen(self.serveripURL)
        ip = ip_response.read().decode('utf8')
        return ip

    def checkLatestVersion(self):
        ver_response = urlopen(self.serverVerURL)
        ver = ver_response.read().decode('utf8')
        return ver

client = Client()
client.setupSocket()
client.setCred()

pyMusic = pyMusicClass()

while True:
    incomingMessage = client.receiveMessage()
    mess = incomingMessage.split(" ", maxsplit=3) # 0 is where (ex: "clients"), 1 is who (ex: "1"), 2 is the command (ex: "install"), 3 is the arguments (ex: "pyMusic")
    print(mess)
    if(mess[0] == "command"):
        if(mess[1] == client.number):

            if(mess[2] == "displayMessage"):
                ctypes.windll.user32.MessageBoxW(0, mess[3], "Important Message", 1)
                client.sendMessage(client.name + " displayed " + mess[3] + " on the screen")
                print(mess[2] + " was called")

            elif(mess[2] == "changeName"):
                client.changeName(mess[3])

            elif(mess[2] == "pyMusic"):
                pyMusic.run(mess[3]) # volume, song, play

            elif(mess[2] == "checkVersion"):
                client.sendMessage(self.info.clientInfo["version"])

            elif(mess[2] == "update"):
                version = client.info.clientInfo["version"]
                lastest = client.checkLatestVersion()
                if(version != lastest):
                    client.sendMessage(client.name + " update needed")
                elif(version == lastest):
                    client.sendMessage(client.name + " client already up to date")

            elif(mess[2] == "quit"):
                break

            else:
                client.sendMessage(client.name + " command not found")
                print(mess[2] + " Command Not found")
        else:
            print("Not This Computer")
    else:
        print("Not a Command")

client.exit()
sys.exit()
