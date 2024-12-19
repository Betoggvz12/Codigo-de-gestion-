productos = [
    {"nombre": "Laptop", "precio": 15000, "cantidad": 10},
    {"nombre": "Mouse", "precio": 300, "cantidad": 50},
    {"nombre": "Teclado", "precio": 800, "cantidad": 30}
]

def Agregar_Producto():
    while True:
        Producto_Nuevo = {
            "nombre" : input("Ingrese el  nombre del producto:"),
            "precio" : float(input("Ingrese el precio del producto")),
            "cantidad": int(input("Ingrese la cantidad de productos"))
        }
        print("Producto agregado exitosamente ")
        productos.append(Producto_Nuevo)
        opcion = input("¿Deseas realizar otra acción? (s/n): ".lower())
        if opcion !="s":
           break
def Mostrar_Producto():
    print("Linea de productos")
    print(productos)

def Modificar_Producto():
    for produ in productos:
        print(produ["nombre"])

    nombre_producto = input("Nombre del libro a modificar:")
    
    producto = next((p for p in productos if p["nombre"].lower() == nombre_producto.lower()), None)

    if producto:
        campo = input("¿Qué deseas modificar? (nombre/precio/cantidad): ").lower()
        if campo in producto:
            nuevo_valor = input(f"Ingrese el nuevo {campo}: ")
            producto[campo] = int(nuevo_valor) if campo == "cantidad" else float(nuevo_valor) if campo == "precio" else nuevo_valor
            print(f"{campo.capitalize()} del producto actualizado correctamente.")
        else:
            print("Campo no válido.")
    else:
        print("Producto no encontrado.")

    
            
        

    


while True:
     x = int(input(("Que opcion deseas ingresar:\n 1.- Ingresar producto nuevo \n 2.- Mostrar linea de productos \n 3.- Modificar Producto \n Opcion a Ingresar: ")))
     if x == 1:
         Agregar_Producto()
     elif x == 2:
        Mostrar_Producto()
     elif x == 3:
         Modificar_Producto()
     else:
        print("Opción no válida.")

     r = input("¿Deseas realizar otra acción? (s/n): ".lower())
     if r !="s":
           break






    
        
    