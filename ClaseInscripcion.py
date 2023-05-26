from ClasePersona import *
from ClaseTallerCapacitacion import *

class Inscripcion(object):
	__persona = object
	__taller = object
	def __init__(self,fecha_inscripcion,pago,persona,taller):
		self.__fecha_inscripcion = fecha_inscripcion
		self.__pago = pago
		self.__persona = persona
		self.__taller = taller

	def getFecha(self):
		return self.__fecha_inscripcion

	def getPago(self):
		return self.__pago

	def getPersona(self):
		return self.__persona

	def getTaller(self):
		return self.__taller

	def setPago(self,pago):
		self.__pago = pago