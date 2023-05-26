from ClaseTallerCapacitacion import *
import csv

class ManejadorTaller(object):
	def __init__(self):
		self.__lista = []

	def CargaTalleres(self):
		archivo = open('Talleres.csv',encoding='utf8')
		reader = csv.reader(archivo,delimiter=',')
		for fila in reader:
			taller = TallerCapacitacion(int(fila[0]),fila[1],int(fila[2]),float(fila[3]))
			self.__lista.append(taller)

	def Muestra(self):
		for i in range(len(self.__lista)):
			print(self.__lista[i])

	def Inscribir(self,fecha,codigo,persona):
		i = 0
		band = False
		retorno = None
		while (i < len(self.__lista)) and (band != True):
			if codigo == self.__lista[i].getId_Taller():
				retorno = self.__lista[i].InscribirPersonas(fecha,persona)
				print("Persona inscripta!")
				band = True
			else:
				i += 1
		if i == len(self.__lista):
			print("Codigo no encontrado!")

		return retorno

	def Consultar_Por_Codigo(self,codigo):
		i = 0
		band = False
		while (i < len(self.__lista)) and (band != True):
			if self.__lista[i].getId_Taller() == codigo:
				self.__lista[i].Mostrar_Datos_Inscriptos()
				band = True
			else:
				i += 1

		if i == len(self.__lista):
			print("Codigo no encontrado!")