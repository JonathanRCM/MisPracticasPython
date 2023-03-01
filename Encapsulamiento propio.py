class Cliente:
	def __init__(self):
		self.__cuenta=12345

	def __processAccount(self):
		print("Listo tu numero de cuenta")

	def getAccountNumber(self):
		return self.__cuenta

c = Cliente()
print(c._Cliente__cuenta)
c._Cliente__processAccount()

