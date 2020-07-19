from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class CommunicationServer:
    """Server for multithreaded (asynchronous) chat application."""

    def __init__(self, port=33000):
        """Set class variables."""
        self.classname = "-- CommunicationServer --:"

        self.clients = {}
        self.admins = {}
        self.addresses = {}

        self.computer = {}
        self.computers = 0

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
            self.addresses[self.client] = self.client_address
            Thread(target=self.handle_client, args=(
                self.client, self.client_address,)).start()

    def handle_client(self, client, addr):
        """Handle a single client connection."""
        self.name = client.recv(self.BUFSIZ).decode("utf8")
        if(self.name == 'whiteswan'):
            self.welcome = 'Welcome %s!' % self.name
            client.send(bytes(self.welcome, "utf8"))
            self.msg = "callAllClients"
            self.broadcast(bytes(self.msg, "utf8"))
            self.admins[client] = self.name
            self.clients[client] = self.name
            print(str(self.admins))
            print(str(self.clients))

        else:
            self.clients[client] = self.name
            self.computers = self.computers + 1
            self.computer[str(self.computers)] = self.name

        print(str(addr) + " renamed to " + self.name)

        while True:
            self.msg = (self.client.recv(self.BUFSIZ)).decode("utf8")
            if (self.msg.charAt(0) == "a" and self.msg.charAt(1) == "d" and self.msg.charAt(2) == "."):   # If its from an admin
                newmsg = "{0}".format(('{0}'.format(self.msg)).split("ad.", 1)[1])
                self.broadcast(newmsg)
                print()

            elif(self.msg.charAt(0) == "c" and self.msg.charAt(1) == "l" and self.msg.charAt(2) == "."):
                newmsg = "{0}".format(('{0}'.format(self.msg)).split("cl.", 1)[1])
                self.broadcastAdmins(newmsg)

            if(self.msg == bytes("{quit}", "utf8")):
                self.client.send(bytes("{quit}", "utf8"))
                self.client.close()
                del self.clients[self.client]
                self.broadcastAdmins(bytes("%s has left the chat." %
                                     self.name, "utf8"))
                print("%s has left the chat." % self.name)
                break

    def broadcast(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the clients."""
        for sock in self.clients:
            sock.send(bytes(prefix, "utf8") + msg)

    def broadcastAdmins(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the clients."""
        for sock in self.admins:
            sock.send(bytes(prefix, "utf8") + msg)

if __name__ == '__main__':
    server = CommunicationsServer(33000)
    server.startServer()
