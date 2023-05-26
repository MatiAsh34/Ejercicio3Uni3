from ClasePersona import *

class ManejadorPersona():
	def __init__(self):
		self.__lista = []

	def AgregaPersona(self,persona):
		self.__lista.append(persona)

