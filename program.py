#Librerias 

import pyodbc
# Detalles de la conexión a la base de datos 
server = 'Natanael\\SQLEXPRESS'  
database = 'GestionInventario'

# Crear la cadena de conexión para autenticación de Windows
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

# Conectarse a la base de datos
conn = pyodbc.connect(conn_str)
print("Conexión exitosa a la base de datos.")

# Crear un cursor para ejecutar las consultas
cursor = conn.cursor()
#-----------------------------------------------------------------------------------------------------------------------------------------------
class Gestion_Libreria:
    def __init__(self, Lista = None):
        if Lista is None:
            self.Lista = [] 
        else: 
            self.Lista = Lista
    
    def Añadir_Libro(self):

        while True:
         libro = { 
            "Título": input("Ingrese el título del libro: ").strip(), 
            "Autor": input("Ingrese el autor del libro: ").strip(), 
            "Género": input("Ingrese el género del libro: ").strip(),
            "Año de Publicacion": input("Ingrese el año de publicación: ").strip(), 
            "Precio ": input("Ingrese el precio del libro:").strip(),
            "Cantidad disponible de libros " : input("Cantidad de libros:").strip() }
         
         print("Libro Agregado")  # Confirmación
         self.Lista.append(libro)

         

         

          # Guardamos el nombre del libro
         I = input("¿Deseas realizar otra acción? (s/n): ".lower())
         if I != "s":
          break  
    def Mostrar_Libros(self):
        print(self.Lista)

    def Moficar_Libro(self):
        print(self.Lista)
        titulo_libro = input("\nIngresa el título del libro que deseas modificar: ").strip()  # Eliminar espacios
        libro_seleccionado = next((libro for libro in self.Lista if libro["Titulo"].lower() == titulo_libro.lower()), None)
        if libro_seleccionado:
            print(f"\nHas seleccionado: {libro_seleccionado}")
            campo = input("¿Qué campo deseas modificar? (Titulo, Autor, Genero, Año de Publicacion, Precio, Cantidad disponible): ").strip()
            
            if campo in libro_seleccionado:
                nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                # Convertir el valor según el campo
                if campo in ["Precio"]:
                    nuevo_valor = float(nuevo_valor)
                elif campo in ["Cantidad disponible"]:
                    nuevo_valor = int(nuevo_valor)
                libro_seleccionado[campo] = nuevo_valor
                print("Libro modificado exitosamente.")
            else:
                print("Campo inválido.")
        else:
            print("No se encontró un libro con ese título.")

    
        
#-------------------------------------------------------------------------------------------------------------------------------


# Intancias de las clases "
p1 = Gestion_Libreria(Lista=[{"Titulo": "Ted 2"  , "Autor" : "Natanael Cano" , "Genero" : "Comedia", "Año de Publicacion " : 2004 , "Precio" : 233.33 , "Cantidad disponible" : 23 } ])

# Interfaz del usuario 
while True:  
    print("Bienvenido a la Gestión de Librería")

    # Menu de opciones 
    x = int(input("Opciones Disponibles  \n 1- Gestión de Libros \n 2.- Gestión de Clientes \n 3.- Realizar Ventas \n 4.- Reportes \n Opción a Ingresar: "))
    
    if x == 1:
        print("Bienvenido a Gestión de Libros: \n ¿Qué opción deseas hacer?")
        print("1.-Añadir de Libros\n2.-Mostrar libros\n3.-Modificar libro")
        
        opcion = int(input("Selecciona una opción: " ))
        
        if opcion == 1:
            p1.Añadir_Libro()  # Llamamos al método para añadir libro
        elif opcion == 2:
            p1.Mostrar_Libros()
        elif opcion == 3:
            p1.Moficar_Libro()
    
    elif x == 2:
        print("Gestión de Clientes (Aún no implementado)")
    elif x == 3:
        print("Realizar Ventas (Aún no implementado)")
    elif x == 4:
        print("Reportes (Aún no implementado)")
    else:
        print("Opción no válida.")

    continuar = input("¿Deseas realizar otra acción? (s/n): ").lower()
    if continuar != 's':
        break  
 