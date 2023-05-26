from ClaseInscripcion import *
from ClaseTallerCapacitacion import *
from ClasePersona import *
import csv

class ManejadorInscripcion(object):
	def __init__(self):
		self.__lista = []

	def AgregarInscripcion(self,inscripcion):
		self.__lista.append(inscripcion)

	def Consulta_Por_Dni(self,dni):
		i = 0
		band = False
		while (i < len(self.__lista)) and (band != True):
			persona = self.__lista[i].getPersona()
			if persona.getDNI() == dni:
				taller = self.__lista[i].getTaller()
				print ("Nombre del taller: {}, monto que adeuda: {}".format(taller.getNombre(),taller.getMonto()))
				band = True
			else:
				i += 1

		if i == len(self.__lista):
			print("DNI no encontrado!")

	def RegistrarPago(self,dni):
		i = 0
		band = False
		while (i < len(self.__lista)) and (band != True):
			persona = self.__lista[i].getPersona()
			if persona.getDNI() == dni:
				taller = self.__lista[i].getTaller()
				taller.setMonto(0)
				self.__lista[i].setPago(True)
				print("Pago registrado!")
				band = True
			else:
				i += 1

		if i == len(self.__lista):
			print("DNI no encontrado!")


	def GeneraArchivo(self):
		for i in range(len(self.__lista)):
			persona = self.__lista[i].getPersona()
			taller = self.__lista[i].getTaller()
			cadena = [str(persona.getDNI()),str(taller.getId_Taller()),str(self.__lista[i].getFecha()),str(self.__lista[i].getPago())]

			archivo = 'datos.csv'

			with open(archivo, 'w', newline='') as archivo:
				escritor_csv = csv.writer(archivo)
				escritor_csv.writerow(['DNI', 'Id', 'Fecha', 'Pago'])
				escritor_csv.writerow(cadena)

		print("Archivo CSV creado exitosamente.")

    	