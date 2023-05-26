from ClasePersona import *
from ClaseInscripcion import *
from ManejadorInscripcion import *

class TallerCapacitacion(object):
	__lista_inscripciones = list
	def __init__(self,id_taller,nombre,vacantes,monto_inscripcion):
		self.__id_taller = id_taller
		self.__nombre = nombre
		self.__vacantes = vacantes
		self.__monto_inscripcion = monto_inscripcion
		self.__lista_inscripciones = []
		
	def InscribirPersonas(self,fecha,persona):
		inscripcion = Inscripcion(fecha,False,persona,self)
		self.__lista_inscripciones.append(inscripcion)
		self.__vacantes -= 1
		return inscripcion

	def Mostrar_Datos_Inscriptos(self):
		for i in range(len(self.__lista_inscripciones)):
			persona = self.__lista_inscripciones[i].getPersona()
			print("Nombre {}, direccion {}, dni {}".format(persona.getNombre(),persona.getDireccion(),persona.getDNI()))

	def getId_Taller(self):
		return self.__id_taller

	def getNombre(self):
		return self.__nombre

	def getMonto(self):
		return self.__monto_inscripcion

	def getVacantes(self):
		return self.__vacantes

	def setMonto(self,monto):
		self.__monto_inscripcion = monto

	def __str__(self):
		return "%d - %s" % (self.__id_taller,self.__nombre)
