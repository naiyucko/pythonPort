from __future__ import print_function
class Config:
	def __init__(self, fileName):
		self.configList = ""
		self.fileName = fileName
		self.d = dict()
		self.configure()
		
	def openConfig(self):
		fname = open(self.fileName, "r")
		self.configList = fname.readlines()
		fname.close()
	
	def configure(self):
		self.openConfig()
		for each in self.configList:
			temp=each.split()
			self.d[temp[0]] = temp[1]
		
	def get(self, attribute):
		return self.d[attribute]
	def update(self, attribute, value):
		self.d[attribute] = value
		fname = open(self.fileName, "w")
		for each in self.d.keys():
			print(each + " " + str(self.d[each]), file=fname)
		fname.close()
if __name__=="__main__":
	c = Config("config.txt")
	c.update("AzOffset",12)
	
	