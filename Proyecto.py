class Gestion_de_Tareas:
    def __init__(self, Tareas = None, Tareas_Completadas = None):
        self.Tareas = []
        self.Tareas_Completadas = []


    def Agregar_Tareas(self):
        while True:

           Tarea_Recientes = input("Ingrese el nombre de la tarea:").lower()
           self.Tareas.append(Tarea_Recientes)
        

           opcion = input("Deseas Agregar otra tarea s/n:").lower()

           if opcion == "n":
                  print("\n")
                  print("\n")
                  break


    

    def Marcar_TareasCompletadas(self):
        print("Tareas disponibles:", self.Tareas)
        tarea_completada = input("Ingrese el nombre de la tarea completada: ").lower()

        # Verifica si la tarea está en la lista de tareas disponibles
        if tarea_completada in self.Tareas:
            self.Tareas_Completadas.append(tarea_completada)
            self.Tareas.remove(tarea_completada)  # Opcional: Elimina la tarea de las tareas disponibles
            print(f"Tarea '{tarea_completada}' marcada como completada.")
        else:
            print(f"La tarea '{tarea_completada}' no está en las tareas disponibles.")

        Agregar = input("¿Deseas agregar otra tarea completada? (s/n): ").lower()
        if Agregar == "n":
            print("\n")
            print("\n")
        
     


            

        

    def Eliminar_Tareas(self):
        print("Tareas disponibles", self.Tareas)

        Eliminar = input("Que tarea deseas eliminar: ").lower()
        for Eliminar  in self.Tareas:
            self.Tareas.remove(Eliminar)
            print("Tarea eliminada con exito",)
            print("\n")

            Eliminar2 = input("Deseas eliminar otra tarea s/n:").lower()
            if Eliminar2 == "n":
                print("\n")
                print("\n")
                break
     

    def Listar_Tareas(self):
        while True:
           Listado = int(input("1.- Tareas disponibles \n2.- Tareas Completadas \n 3.- Salir \n  opcion :"))
        
           if Listado == 1:
            print("Tareas disponibles:", self.Tareas)
            print("\n")
        
           elif Listado == 2:
            if self.Tareas_Completadas:
                print("Tareas Completadas:", self.Tareas_Completadas)
            else:
                print("No hay tareas completadas aún.")
            print("\n")
        
           elif Listado == 3:
            print("\nSaliendo...\n")
            break
        
           else:
            print("Opción no disponible. Por favor, elija una opción válida.")
        


            
        
        
        
 
#Interfaz de usuario -------------

p1 = Gestion_de_Tareas(Tareas  = [], Tareas_Completadas = [])

print("Bievenidos al interfaz de Gestion de Tareas")
while True:
   opcion1 =  int(input((" Lista de opciones  \n1.- Agregar Tareas \n2.- Marcar Tareas Completadas \n3.- Eliminar Tareas \n4.- Listar Tareas \n5.- Salir \n Opcion:")))
   if opcion1 == 1:
       p1.Agregar_Tareas()
       print("\n")
          
       
   elif opcion1 == 2:
       p1.Marcar_TareasCompletadas()
       print("\n")
           
   elif opcion1 == 3:
       p1.Eliminar_Tareas()
       print("\n")
          
   elif opcion1 == 4:
       p1.Listar_Tareas()
       print("\n")
           
   elif opcion1 == 5:
       print("\n")
           
       break
  
       

