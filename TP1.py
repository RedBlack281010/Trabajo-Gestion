class Miembro: 
    def __init__ (self , dni: str , nombre: str ):
        #self.__dni =  dni
        self.setDni(dni)
        self.__nombre =  nombre
        self.libros_prestados : List[Libro] = []
    def agregarLibroPrestado(self , libro):
        self.libros_prestados.append(libro)
    def quitarLibroPrestado(self , libro):
        self.libros_prestados.remove(libro)
    def getDni(self ):
        return self.__dni
    def setDni(self , dni):
        if dni.isdigit() and len(dni ) < 6: 
            self.__dni =  dni
        
class Libro:
    def __init__ (self , titulo: str ,autor : str , isbn: str , ejemplar: int    ):
        self.titulo = titulo
        self.autor =  autor
        self.isbn =  isbn
        self.ejemplar =  ejemplar
        self.prestado_a =[]
    
    def prestar_libro(self , miembro : Miembro):
        if  self.estaDisponible():
            self.prestado_a.append(miembro)
    def estaDisponible(self ):
        if len(self.prestado_a)  <    self.ejemplar:
            return True
        else:
            return False
    
    def devolver_libro(self, miembro : Miembro):
        if  miembro in self.prestado_a :
            self.prestado_a.remove(miembro)

class Biblioteca:
    def __init__ (self ):
        self.libros : List[Libro] = []
        self.miembros : List[Miembro] = []
        
    def agregarLibro(self):
        titulo = input("Ingrese el titulo del libro: ") 
        autor = input("Ingrese el autor del libro: ") 
        isbn = input("Ingrese el isbn del libro: ") 
        libro = self.getLibro(isbn)
        if libro:
            agregarejemplar = int(input("Cuantos ejemplares desea agregar: ") )   
            libro.ejemplar += agregarejemplar
        else:
            agregarejemplar = int(input("Cuantos ejemplares desea agregar: ") )
            
            libro = Libro ( titulo , autor , isbn, agregarejemplar)
            self.libros.append(libro)

    def getLibro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro 
    
    def getMiembro (self, dni):
        for miembro in self.miembros:
            if miembro.getDni() == dni:
               return miembro
            
    def quitarLibro(self):
        isbn = input("Ingrese el isbn del libro a borrar: ")
        libroaBorrar = self.getLibro(isbn)
        self.libros.remove(libroaBorrar)
            
    def agregarMiembro(self):
        nombre = input("Ingrese el nombre del socio: ")
        dni = input("Ingrese el dni del socio: ")
        miembroobj = Miembro (dni, nombre)
        self.miembros.append(miembroobj)
        
    def quitarMiembro(self):
        dni = input("Ingrese el DNI de la persona borrar: ")
        personaaborrar = self.getMiembro(dni)
        if personaaborrar:
            self.miembros.remove(personaaborrar)
        else:
            print("La persona con el dni " +dni+ " no esta en la lista")
            
    def prestar_libro(self):
        dni = input("Ingrese el DNI de la persona a prestar: ")
        isbn = input("Ingrese el isbn del libro a prestar: ")
        libroaprestar = self.getLibro(isbn)
        if libroaprestar == None:
            print ("Libro no existe")
            return False  
        miembroaprestar = self.getMiembro(dni)
        if miembroaprestar == None:
            print ("Miembro no existe")
            return False
        if libroaprestar.estaDisponible():
            libroaprestar.prestar_libro(miembroaprestar)
            miembroaprestar.agregarLibroPrestado(libroaprestar)
     
    def devolver_libro(self):
        dni = input("Ingrese el DNI de la persona a prestar: ")
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        libroaDevolver = self.getLibro(isbn)
        miembro = self.getMiembro(dni)
        if libroaDevolver == None:
            print("El libro con ese ISBN no existe.")
            return False
        if miembro == None:
            print("El miembro con ese DNI no existe.")
            return False
        libroaDevolver.devolver_libro(miembro)
        miembro.quitarLibroPrestado(libroaDevolver)

    def mostrarLibros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return
        print("Lista de Libros")
        for libro in self.libros:
            disponibles = libro.ejemplar - len(libro.prestado_a)
            print(f"ISBN: {libro.isbn} \nTítulo: {libro.titulo} \nAutor: {libro.autor} \nCopias totales: {libro.ejemplar} \nDisponibles: {disponibles}")

    def mostrarMiembros(self):
        if not self.miembros:
            print("No hay miembros registrados.")
            return
        print("\nLista de Miembros")
        for miembro in self.miembros:
            nombre = miembro._Miembro__nombre
            try:
                print(f"Nombre: {nombre} \nDNI: {miembro.getDni()} \nLibros prestados: {len(miembro.libros_prestados)} \n")
            except AttributeError:
                print("Miembro con DNI no registrado correctamente \nLibros prestados: 0 \n")

    def mostrarLibrosPrestadosMiembro(self):
        dni = input("Ingrese el DNI del miembro a consultar: ")
        miembro = self.getMiembro(dni)
        if miembro is None:
            print("El miembro no existe o el DNI no es válido.")
            return
        nombre = miembro._Miembro__nombre
        print(f"\nLibros prestados a {nombre}:")
        if not miembro.libros_prestados:
            print("Este miembro no tiene libros prestados.")
            return
        for libro in miembro.libros_prestados:
            print(f"Título: {libro.titulo} \nISBN: {libro.isbn} \n")
    
######################################
            
    #miembro_1= Miembro("dasdsa", "juan")
    #miembro_1.__dni="sdsadasdas"
    #print(getDni())
 
def main():

    biblioteca_urquiza= Biblioteca()    
    while True:
        opcion= menu()
        if opcion == "10": 
            break
        elif opcion == "1":
            biblioteca_urquiza.agregarLibro()
        elif opcion == "2":
            biblioteca_urquiza.quitarLibro()
        elif opcion == "3":
            biblioteca_urquiza.agregarMiembro()
        elif opcion == "4":
            biblioteca_urquiza.quitarMiembro()
        elif opcion == "5":
            biblioteca_urquiza.prestar_libro()
        elif opcion == "6":
            biblioteca_urquiza.devolver_libro()
        elif opcion == "7":
            biblioteca_urquiza.mostrarLibros()
        elif opcion == "8":
            biblioteca_urquiza.mostrarMiembros()
        elif opcion == "9":
            biblioteca_urquiza.mostrarLibrosPrestadosMiembro()  
    print ("Programa Terminado")
    
def menu():
        print ("Sistema de Gestion de Bibioteca:")    
        print ("1-Agregar Libro:")    
        print ("2-Quitar Libro:")    
        print ("3-Agregar Miembro:")    
        print ("4-Borrar Miembro:")    
        print ("5-Prestar Libro:")    
        print ("6-Devolver Libro:")    
        print ("7-Mostrar Libros:")    
        print ("8-Mostrar Miembros:")    
        print ("9-Mostrar  Libro Prestados a Miembro:")    
        print ("10-Salir:")     
        return input("Seleccione una opcion: ")
  
########################
main()
