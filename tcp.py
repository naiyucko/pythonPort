from telnetlib import *
import time

class Tcp:

	def __init__(self, ip):
		self.tn = Telnet(ip)
		#Changes the MSB of the data sent in because the smart terminal Galil SDK changes it to a trash value for god knows why
		self.sendRead("CW 2;")
		#Forces Galil to read unsolicited messages from current port
		self.sendRead("CF I;")
	def sendRead(self, data):
	#Garuntees that every send command gets a responce
		self.tn.write(data)
		time.sleep(.1)
		a = self.tn.read_eager()
		time.sleep(.1);
		a = a.replace("\r\n:","")
		return a
	def close(self):
		self.tn.close()
	def __del__(self):
		self.close()
		

if __name__ == "__main__":
	a= ""
	s = Tcp("192.168.1.241")
	s.sendRead("MO;")
	s.sendRead("TP;")
	s.sendRead("SH;")
	print s.sendRead("TPA;")
	

	
	#s.close()
	
	
