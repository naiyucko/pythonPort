import unittest
from joystick import JoyStick
from units import Units

class JoyStickTests(unittest.TestCase):
	

	def testUpAdds10(self):
		p = JoyStick()
		self.failUnless(p.moveUp(10)=="PR ,1110")
	def testDownAdds10(self):
		p = JoyStick()
		self.failUnless(p.moveDown(10)=="PR ,-1110")
	def testLeftAdds10(self):
		p = JoyStick()
		self.failUnless(p.moveLeft(10)=="PR -28440,")
	def testRightAdds10(self):
		p = JoyStick()
		self.failUnless(p.moveRight(10)=="PR 28440,")
	def testAbs(self):
		p = JoyStick()
		self.failUnless(p.moveAbs(10,10)=="PA 28440,1110")
		
class UnitsTest(unittest.TestCase):
	
	def testAzEncToDeg(self):
		p = Units()
		self.failUnless(p.encoder_to_Az(10)==28440)
	def testElEncToDeg(self):
		p = Units()
		self.failUnless(p.encoder_to_El(10)==1110)
	

def main():
	unittest.main()

if __name__ == '__main__':
	main()