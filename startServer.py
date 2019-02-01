#!/usr/bin/env python3
""" Start WhiteSwan Server """
from lib.chat_connection.server import *
from lib.run_scripts.run import *
from lib.info.info import *

info = WhiteSwanInfo()
ps = PowerShell()

#ps.run('power_scripts\\firewallPortBypass-server.ps1')

server = CommunicationServer(33000)
server.startServer()
