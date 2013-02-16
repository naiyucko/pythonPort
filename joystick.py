from units import Units
class JoyStick:
	def __init__(self):
		self.converter = Units()
	def moveUp(self, amount):
		return "PR ,{0}".format(self.converter.El_to_encoder(amount,False),)
	def moveDown(self, amount):
		return "PR ,{0}".format(-1*self.converter.El_to_encoder(amount,False),)
	
	def moveRight(self, amount):
		return "PR {0},".format(self.converter.Az_to_encoder(amount,False),)
		
	def moveLeft(self, amount):
		return "PR {0},".format(-1*self.converter.Az_to_encoder(amount,False),)
	def moveAbs(self, Az, El):
		return "PA {0},{1}".format(self.converter.Az_to_encoder(Az), self.converter.El_to_encoder(El))
	def calibrate(self, wanted_Az, wanted_El, current_Az, current_El):
		self.converter.setOffset(wanted_Az, wanted_El, current_Az, current_El)

if __name__=="__main__":
	p = JoyStick()
	p.calibrate(0,0,10,10)
	print p.moveUp(-10)