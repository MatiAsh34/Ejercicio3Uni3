from ManejadorPersona import *
from ClasePersona import *
from ManejadorTaller import *
from ManejadorPersona import *
from ManejadorInscripcion import *
import datetime

if __name__ == '__main__':
	opcion = None
	while opcion != '0':
		print("\n1- Cargar los datos de los talleres")
		print("2- Inscribir una persona en un taller")
		print("3- Consultar inscripción")
		print("4- Consultar inscriptos")
		print("5- Registrar pago")
		print("6- Guardar inscripciones")
		print("0- Salir")
		opcion = input("\nIngrese opcion: ")

		if opcion == '1':
			Manejador_Taller = ManejadorTaller()
			Manejador_Taller.CargaTalleres()
			Manejador_Persona = ManejadorPersona()
			Manejador_Inscripcion = ManejadorInscripcion()

		elif opcion == '2':
			fecha = datetime.datetime.now()
			fecha_actual = fecha.strftime('%Y/%m/%d')
			Manejador_Taller.Muestra()
			codigo = int(input("Ingrese codigo de taller: "))

			nombre = input("Ingrese nombre: ")
			direccion = input("Ingrese direccion: ")
			dni = input("Ingrese dni: ")
			persona = Persona(nombre,direccion,dni)
			Manejador_Persona.AgregaPersona(persona)

			retorno = Manejador_Taller.Inscribir(fecha_actual,codigo,persona)

			if retorno != None:
				Manejador_Inscripcion.AgregarInscripcion(retorno)

		elif opcion == '3':
			dni = input("Ingrese dni: ")
			Manejador_Inscripcion.Consulta_Por_Dni(dni)

		elif opcion == '4':
			codigo = int(input("Ingrese codigo de taller: "))
			Manejador_Taller.Consultar_Por_Codigo(codigo)

		elif opcion == '5':
			dni = input("Ingrese dni: ")
			Manejador_Inscripcion.RegistrarPago(dni)

		elif opcion == '6':
			Manejador_Inscripcion.GeneraArchivo()

		elif opcion == '0':
			print ("Saliendo...")