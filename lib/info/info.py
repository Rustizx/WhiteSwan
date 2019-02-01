#!/usr/bin/env python3
""" Get Infomation for WhiteSwan """
import os
import json

class WhiteSwanInfo():
	def __init__(self):
		""" Sets up definitions """
		self.classname = "-- Info --:"
		self.libraryPath = 'lib\\info'
		
		self.jsonFiles = {"allModules": "allModules.json", "clientInfo": "clientInfo.json"}
		
		self.rawAllModulesWrite = None
		self.rawClientWrite = None
		self.rawAllModulesRead = None
		self.rawClientRead = None
		
		# Get Path
		self.path = "{0}\\".format(('{0}'.format(str(os.getcwd()))).split(self.libraryPath, 1)[0])
		
		with open((self.path + self.jsonFiles["allModules"])) as self.rawAllModulesRead:
			self.allModules = json.load(self.rawAllModulesRead)
			
		with open((self.path + self.jsonFiles["clientInfo"])) as self.rawClientRead:
			self.clientInfo = json.load(self.rawClientRead)
			
	def updateFiles(self, file = "both", add = {"hello": "world"}):
		""" Updates The JSON Files """
		
		if(file == "allModules"):
			if(add != {"hello": "world"}):
				self.allModules.update(add)
			
			with open((self.path + self.jsonFiles["allModules"])) as self.rawAllModulesWrite:
				json.dump(self.allModules, self.rawAllModulesWrite)
			
		elif(file == "client"):
			if(add != {"hello": "world"}):
				self.clientInfo.update(add)
				
			with open((self.path + self.jsonFiles["clientInfo"]), 'w') as self.rawClientWrite:
				json.dump(self.clientInfo, self.rawClientWrite)
		
		elif(file == "both"):
			with open((self.path + self.jsonFiles["clientInfo"]), 'w') as self.rawClientWrite:
				json.dump(self.clientInfo, self.rawClientWrite)
			with open((self.path + self.jsonFiles["allModules"])) as self.rawAllModulesWrite:
				json.dump(self.allModules, self.rawAllModulesWrite)
		
		
	def printAll(self):
		""" Debug Print All Info """
		
		print("{0} WhiteSwan Path is {1}".format(self.classname, self.path))
		print("{0} All Modules '{1}'".format(self.classname, self.allModules))
		print("{0} Client Info '{1}'".format(self.classname, self.clientInfo))
		