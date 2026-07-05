class Producto: 
    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        self.__precio = precio
        self.disponible = disponible

# 1. Obtener y establecer el precio del producto

    def obtener_precio(self) -> float:
        return self.__precio
    
    def establecer_precio(self, nuevo_precio: float):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = nuevo_precio
    
# 2. Métodos para la disponibilidad del producto
    def esta_disponible(self) -> bool:
        return self.disponible    
    
    def cambiar_disponibilidad(self, disponible: bool):
        self.disponible = disponible  

    def mostrar_informacion(self) -> str:
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre}\nPrecio: ${self.__precio:.2f}\nDisponibilidad: {disponibilidad}"      
    