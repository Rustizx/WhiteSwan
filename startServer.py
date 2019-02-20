#!/usr/bin/env python3
""" Start WhiteSwan Server """
from lib.run_scripts.run import *
from lib.info.info import *
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class Server:
    """Server for multithreaded (asynchronous) chat application."""

    def __init__(self, port=33000):
        """Set class variables."""
        self.classname = "-- CommunicationServer --:"

        self.clients = {}
        self.addresses = {}

        self.computerNUMBERtoNAME = {}
        for x in range(100):
            self.computerNUMBERtoNAME.update({x: "name"})
        #self.computerNUMBERtoNAME = {0: "name", 1: "name", 2: "name", 3: "name", 4: "name", 5: "name", 6: "name", 7: "name", 8: "name", 9: "name"}
        self.computerNAMEtoID = {}
        self.computerIDtoNAME = {}
        #self.computerNAMEtoID = {"name0": "id", "name1": "id","name2": "id", "name3": "id", "name4": "id", "name5": "id", "name6": "id", "name7": "id", "name8": "id", "name9": "id"}
        #self.computerIDtoNAME = {"id0": "name", "id1": "name","id2": "name", "id3": "name", "id4": "name", "id5": "name", "id6": "name", "id7": "name", "id8": "name", "id9": "name"} # 10 Computers Can Connect

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
            Thread(target=self.handle_client, args=(
                self.client, self.client_address,)).start()

    def handle_client(self, client, addr):
        """Handle a single client connection."""
        name = client.recv(self.BUFSIZ).decode("utf8")
        id = client.recv(self.BUFSIZ).decode("utf8")
        number = self.registerComputer(id, name)
        client.send(bytes(str(number), "utf8"))
        msg = "%s has joined the chat!" % name
        self.broadcast(bytes(msg, "utf8"))
        self.clients[client] = name

        while True:
            msg = client.recv(self.BUFSIZ)
            if msg == bytes("getAllComputers()", "utf8"):
                self.getCompNumber(name)
            elif msg != bytes("{quit}", "utf8"):
                self.broadcast(msg)
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
                self.unregisterComputer(number, id, name)
                del self.clients[client]
                self.broadcast(bytes("%s has left the chat." % name, "utf8"))
                break

    def registerComputer(self, id, name):
        self.computerNAMEtoID[name] = id
        self.computerIDtoNAME[id] = name
        for x in range(100):
            if(self.computerNUMBERtoNAME[x] == "name"):
                self.computerNUMBERtoNAME[x] = name
                print(name + " " + id + "is registered as computer " + str(x))
                return x
        # elif(self.computerNUMBERtoNAME[1] == "name"):
        #     self.computerNUMBERtoNAME[1] = name
        #     print(name + " " + id + "is registered as computer 1")
        #     return 1
        # elif(self.computerNUMBERtoNAME[2] == "name"):
        #     self.computerNUMBERtoNAME[2] = name
        #     print(name + " " + id + "is registered as computer 2")
        #     return 2
        # elif(self.computerNUMBERtoNAME[3] == "name"):
        #     self.computerNUMBERtoNAME[3] = name
        #     print(name + " " + id + "is registered as computer 3")
        #     return 3
        # elif(self.computerNUMBERtoNAME[4] == "name"):
        #     self.computerNUMBERtoNAME[4] = name
        #     print(name + " " + id + "is registered as computer 4")
        #     return 4
        # elif(self.computerNUMBERtoNAME[5] == "name"):
        #     self.computerNUMBERtoNAME[5] = name
        #     print(name + " " + id + "is registered as computer 5")
        #     return 5
        # elif(self.computerNUMBERtoNAME[6] == "name"):
        #     self.computerNUMBERtoNAME[6] = name
        #     print(name + " " + id + "is registered as computer 6")
        #     return 6
        # elif(self.computerNUMBERtoNAME[7] == "name"):
        #     self.computerNUMBERtoNAME[7] = name
        #     print(name + " " + id + "is registered as computer 7")
        #     return 7
        # elif(self.computerNUMBERtoNAME[8] == "name"):
        #     self.computerNUMBERtoNAME[8] = name
        #     print(name + " " + id + "is registered as computer 8")
        #     return 8
        # elif(self.computerNUMBERtoNAME[9] == "name"):
        #     self.computerNUMBERtoNAME[9] = name
        #     print(name + " " + id + "is registered as computer 9")
        #     return 9

    def unregisterComputer(self, number, id, name):
        del self.computerNAMEtoID[name]
        del self.computerIDtoNAME[id]
        self.computerNUMBERtoNAME[number] = "name"

    def getCompNumber(self, name):
        print(name + " called getCompNumber")
        comp = ' '.join('{0} {1},'.format(key, val) for key, val in sorted(self.computerNUMBERtoNAME.items()))
        self.broadcast(bytes(comp, "utf8"))

    def broadcast(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the clients."""
        for sock in self.clients:
            sock.send(bytes(prefix, "utf8") + msg)

if __name__ == '__main__':
    server = Server(33000)
    server.startServer()
