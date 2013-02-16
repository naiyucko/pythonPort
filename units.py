from config import Config
class Units:
	def __init__(self):
		self.c = Config("config.txt")
		self.azOffset = self.c.get("AzOffset")
		self.elOffset = self.c.get("ElOffset")
	def Az_to_encoder(self, counts, abs=True):
		if abs:
			return (int(self.c.get("AzEncPerRev"))/360)*(counts+self.azOffset)
		else:
			return (int(self.c.get("AzEncPerRev"))/360)*(counts)
	def El_to_encoder(self, counts, abs=True):
		if abs:
			return (int(self.c.get("ElEncPerRev"))/360)*(counts+self.elOffset)
		else:
			return (int(self.c.get("ElEncPerRev"))/360)*(counts)
	def Encoder_to_az(self, counts):
		return (int(360/self.c.get("AzEncPerRev"))*(counts-self.azOffset))
	def Encoder_to_el(self, counts):
		return (int(360/self.c.get("ElEncPerRev"))*(counts-self.elOffset))
	def setOffset(self, wanted_Az, wanted_El, current_Az, current_El):
		self.azOffset = current_Az - wanted_Az
		self.elOffset = current_El - wanted_El
		self.c.update("AzOffset",self.azOffset)
		self.c.update("ElOffset",self.elOffset)