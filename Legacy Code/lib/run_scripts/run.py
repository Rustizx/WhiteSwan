#!/usr/bin/env python3
""" Run PowerShell Scripts with Python """
import sys, os
import subprocess
import importlib.machinery

class PowerShell():
	def __init__(self):
		""" Sets up definitions """
		self.classname = "-- PowerShell --:"
		
		self.libraryPath = 'lib\\run_scripts'
		self.libraryInfoPath = 'lib\\info\\info.py'
		self.loader = importlib.machinery.SourceFileLoader('report', ("{0}\\{1}".format(('{0}'.format(str(os.getcwd())).split(self.libraryPath, 1)[0]), self.libraryInfoPath)))
		infoScript = self.loader.load_module('report')
		
		self.info = infoScript.WhiteSwanInfo()
		
		self.testscript = self.info.path + "lib\\run_scripts\\test.ps1"
		self.runCMD = self.info.path + "lib\\run_scripts\\executePowerShell.cmd"
		self.powershellEXE = "powershell.exe"
		
	def run(self, path = "lib\\run_scripts\\test.ps1", usWhiteSwanPath = True):
		""" Run a Powershell Script with Choosen Path """
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		#si.wShowWindow = subprocess.SW_HIDE # default
		filePath = self.info.path + path
		print(self.classname + " the script that is about to run is " + filePath)
		if(usWhiteSwanPath == True):
			subprocess.call('{0} {1}'.format(self.powershellEXE, filePath), startupinfo=si)
		elif(usWhiteSwanPath == False):
			subprocess.call('{0} {1}'.format(self.powershellEXE, path), startupinfo=si)
		# Debug Print
		print("{0} just ran {1}".format(self.classname, path))
		
	def runTest(self):
		""" Run the Test PowerShell Script """
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		subprocess.call('{0} {1}'.format(self.powershellEXE, self.testscript), startupinfo=si)
		
		# Debug Print
		print("{0} just ran test script".format(self.classname))
		
		