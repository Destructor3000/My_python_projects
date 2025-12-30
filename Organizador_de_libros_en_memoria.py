Generos = set()

Bibloteca = []

Libro = {"Titulo":"",
         "Autor":"",
         "Genero":""}

while True:

    print("1. Añadir libro",
      "2. Ver libros",
      "3. Total de libros",
      "4. Ver géneros",
      "5. Salir")
    
    Funcion = input()
    if Funcion == "1":
        Libro["Titulo"] = input("Nombre: ")
        Libro["Autor"] = input("Autor: ")
        Libro["Genero"] = input("Genero: ")

        Bibloteca.append(Libro.copy())

        Generos.add(Libro["Genero"])

        Funcion = input()

    elif Funcion == "2":
        print(Generos)
        Funcion = input()

    elif Funcion == "3":
        print(len(Bibloteca))
        Funcion = input()


    elif Funcion == "4":
        print(Bibloteca)
        Funcion = input()

    elif Funcion == "5":
        print("Saliendo del programa.....")
        break

    else:
        print("opcion no valida")













