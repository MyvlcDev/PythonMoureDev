def miAgenda():

    print("\n")
    print("Elija una de las siguientes opciones: ")
    print("\n")
    print("1. Insertar contacto") 
    print("2. Actualizar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Mostrar contactos")
    print("6. Salir\n")


    opcion = input("Selecciona una opción: ")

    #delcaro mi diccionario llamado Contacto

    contacto= {}
    control = True

    contacto={

        "nombre":"     ",
        "telefono":" "

    }

    match opcion:

        case "1":
            ## insertar:

            nombre = input("Intoduce el nombre:")
            telf= input("Intoduce el telefono:  ")
            print(len(telf))
            if nombre and len(telf)> 0 and len(telf)<=11:

                contacto["nombre"]=telf
                print("ok")

            else:
                print("Debes de introducion un número de telefono valido menor a 12 digitos")

            
            
        case "2":
            ## Actualizar:
            pass

        case "3":
            ## Eliminar:

            pass
        case "4":
            ## Buscar:
            
            pass
        case "5":
            ## Mostrar:
            print("Salir")

        case "6":
            ##Salir:
            print("Salir")
            exit

            
        case "_":
            ##Otra opcion

            print("Salir")
            exit
            
            
miAgenda()