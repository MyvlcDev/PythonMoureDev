
###
## arreglar el mostrar para que muestre bien los datos
###
print("Agenda")

agenda={}


class Agenda:

    def __init__(self):
        
        self.contacto=[]    
    
    def registrar_contacto(self):

        nombre = input ("Introduce el nombre: ").strip
        self.contacto.append(nombre)
        apellido = input ("Introduce el apellido: ").strip  
        self.contacto.append(apellido)
        telefono = input ("Introduce el Telefon: ").strip
        self.contacto.append(telefono)
    
    def mostrar_contacto(self):
        print("Mostrando los contactos")
        for elements in self.contacto:
            print (str(elements))
    
    def eliminar_contacto(self):
        
        name = input("Introduce el nombre del contacto a a eliminar: ")
       
        if name in self.contacto:
            del self.contacto[name]
        else:
            print(f"El contacto {name} no existe.")
    
    def buscar_contacto(self):

        name = input("Introduce el nombre del contacto a buscar: ")

        if name in agenda:
            print(
                f"El número de teléfono de {name} es {agenda[name]}.")
        else:
            print(f"El contacto {name} no existe.")



agenda = Agenda()



while True:
    
    print("\n")
    print("Elija una de las siguientes opciones: ")
    print("\n")
    print("1. Insertar contacto") 
    print("2. Actualizar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Mostrar contactos")
    print("6. Salir")

    option = input("\nSelecciona una opción: ")

    match option:

        case "1":
            agenda.registrar_contacto()
        case "2":
            pass
        case "3":
            agenda.eliminar_contacto()
        case "4":
            agenda.buscar_contacto()
        case "5":
            agenda.mostrar_contacto()
        case "6":
            print("Saliendo del simulador...")
            break
        case _:
            print("Opción invalida, selecciones una opción correcta....")
            
        