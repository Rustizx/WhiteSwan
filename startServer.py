#!/usr/bin/env python3
""" Start WhiteSwan Server """
from lib.run_scripts.run import *
from lib.info.info import *
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import random
import multiprocessing


class WhiteSwanServer:
    """Server for Whiteswan."""

    def __init__(self, port=33000):
        """Set class variables."""
        self.classname = "-- WhiteSwan --: "

        self.clients = {}

        self.HOST = ''
        self.PORT = port
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)

    def startSocket(self):
        """Start Socket for tcp communication."""
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.ADDR)

    def startServer(self):
        """Start server and activates handler for clients."""
        self.startSocket()
        self.SERVER.listen(5)
        print("Waiting for connection...")
        self.ACCEPT_THREAD = Thread(target=self.accept_incoming_connections)
        self.ACCEPT_THREAD.start()
        self.ACCEPT_THREAD.join()
        self.SERVER.close()

    def accept_incoming_connections(self):
        """Set up handling for incoming clients."""
        while True:
            self.client, self.client_address = self.SERVER.accept()
            print("%s:%s has connected." % self.client_address)

            number = ""
            while True:
                for x in range(6):
                    digit = random.randrange(0,9)
                    number = number + str(digit)
                if(int(number) in self.clients and len(number) == 6):
                    continue
                else:
                    id = int(number)
                    break

            try:
                Thread(target=self.handle_client, args=(self.client, self.client_address, id,)).start()
            except:
                self.broadcastAdmins("%s has left the chat." % self.clients[id]["name"], "utf8")
                print("%s has left the chat." % self.clients[id]["name"])
                del self.clients[id]

    def handle_client(self, client, addr, id):
        """Handle a single client connection."""
        try:
            name = client.recv(self.BUFSIZ).decode("utf8")
            type = client.recv(self.BUFSIZ).decode("utf8")
        except:
            return 1

        computerinfo = {
            "name": name,
            "type": type,
            "lastMessage": "",
            "sock": client
        }

        self.clients[id] = computerinfo

        if(self.clients[id]["type"] == "admin"):
            self.welcome = 'Welcome ' + str(name) + '! Your ID is ' + str(id)
            client.send(bytes(self.welcome, "utf8"))
            print("An Admin Joined")
            self.broadcastAdmins("Admin " + self.clients[id]["name"] + " joined at ID - " + str(id), self.classname)
        else:
            print("A Client Joined")
            self.broadcastAdmins("Client " + self.clients[id]["name"] + " joined at ID - " + str(id), self.classname)
            client.send(bytes(str(id), "utf8"))


        while True:
            # Get Message with 60 second timeout
            #p = multiprocessing.Process(target=self.getIncomming, args=(id,))
            #p.start()
            #p.join(timeout=60)
            #p.terminate()
            self.getIncomming(id)
            try:
                message = (self.clients[id]["lastMessage"]).split(".")
            except:
                break

            if(len(message[0]) == 6):
                try:
                    self.sendTo(str(message[1]), message[0])
                except:
                    print("Error - Tried to send message " + str(message[1]) + " to " + str(message[0]))

            if(message[0] == "admin"):
                broadcastAdmins(str(id) + " said " + str(message[1]))

            if(message[0] == "server"):
                if(message[1] == "getClients"):
                    self.clients[id]["sock"].send(bytes(str(self.clients), "utf8"))

                if(message[1] == "sendAll"):
                    print(str(id) + " said " + str(message[2]))
                    broadcast(str(id) + " said " + str(message[2]))

                if(message[1] == "{quit}"):
                    self.clients[id]["sock"].send(bytes("{quit}", "utf8"))
                    self.clients[id]["sock"].close()
                    self.broadcastAdmins("%s has left the chat." % self.clients[id]["name"], "utf8")
                    print("%s has left the chat." % self.clients[id]["name"])
                    del self.clients[id]
                    break

    def getIncomming(self, id):
        try:
            self.clients[id]["lastMessage"] = self.clients[id]["sock"].recv(self.BUFSIZ).decode("utf8")
        except:
            self.broadcastAdmins("%s has left the chat." % self.clients[id]["name"], "utf8")
            print("%s has left the chat." % self.clients[id]["name"])
            del self.clients[id]

    def sendTo(self, msg, id):  # prefix is for name identification.
        """Sends a message to an id."""
        keys = list(self.clients.keys())
        for x in keys:
            if(int(id) == x):
                sock = self.clients[x]["sock"]
                sock.send(bytes(msg, "utf8"))

    def broadcast(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the clients."""
        keys = list(self.clients.keys())
        for x in keys:
            sock = self.clients[x]["sock"]
            sock.send(bytes(prefix, "utf8") + bytes(msg, "utf8"))

    def broadcastAdmins(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the admins."""
        keys = list(self.clients.keys())
        for x in keys:
            if(self.clients[x]["type"] == "admin"):
                sock = self.clients[x]["sock"]
                sock.send(bytes(prefix, "utf8") + bytes(msg, "utf8"))

if __name__ == '__main__':
    server = WhiteSwanServer()
    server.startServer()
