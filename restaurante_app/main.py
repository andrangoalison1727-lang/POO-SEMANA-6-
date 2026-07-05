from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante
# 1. Mostrar menu
def mostrar_menu():
    print("\n=== MENÚ DEL RESTAURANTE ===")
    print("1. Agregar platillo")
    print("2. Agregar bebida")
    print("3. Mostrar productos")
    print("4. Salir")

# 2. Registrar platillo
def registrar_platillo(restaurante):
    print("\n=== REGISTRAR PLATILLO ===")
    nombre = input("Ingrese el nombre del platillo: ")
    precio = float(input("Ingrese el precio del platillo: "))   
    tiempo_preparacion = int(input("Ingrese el tiempo de preparación (en minutos): "))

    nuevo_platillo = Platillo(nombre, precio, True, tiempo_preparacion)
    restaurante.agregar_producto(nuevo_platillo)
    print(f"Platillo '{nombre}' registrado exitosamente.")

# 3. Registrar bebida
def registrar_bebida(restaurante):
    print("\n=== REGISTRAR BEBIDA ===")
    nombre = input("Ingrese el nombre de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))
    sabor = input("Ingrese el sabor de la bebida: ")

    nueva_bebida = Bebida(nombre, precio, True, sabor)
    restaurante.agregar_producto(nueva_bebida)
    print(f"Bebida '{nombre}' registrada exitosamente.")
    
def main():
    restaurante = Restaurante("Mi Restaurante")
# 4. Crear platillo 
    producto1 = Platillo("Fideos Wonton", 8.99, True, 15)
    producto2 = Platillo("Mousse de Chocolate", 6.99, True, 10)
    

# 5. Crear bebida
    producto3 = Bebida("Agua Mineral", 1.99, True, "Sin sabor")
    producto4 = Bebida("Vino Tinto Italiano", 9.99, True, "Sabor a vino tinto")

# 6. Agregar productos al restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)
    

# 7. Mostrar menu y opciones
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
    
        if opcion == "1":   
            registrar_platillo(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)       
        elif opcion == "3":
            restaurante.mostrar_productos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# 8. Ejecutar el programa
if __name__ == "__main__":
    main()