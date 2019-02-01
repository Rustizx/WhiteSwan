"""
from lib.info.info import *

info = WhiteSwanInfo()

add_module = {"modules": {"pyMicOn":{"verson": "0.01"}}}

info.updateFiles("client", add_module)

"""

from run_scripts.run import *

ps = PowerShell()

ps.run("lib\\run_scripts\\test.ps1")
