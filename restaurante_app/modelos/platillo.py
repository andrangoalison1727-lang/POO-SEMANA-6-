from modelos.producto import Producto
# 1. Clase Platillo que hereda de Producto
class Platillo(Producto): 
    def __init__(self, nombre: str, precio: float, disponible: bool = True, tiempo_preparacion: int = 0):
        super().__init__(nombre, precio, disponible)
        self.tiempo_preparacion = tiempo_preparacion

# 2. Mostrar información del platillo
    def mostrar_informacion(self) -> str:
        return (
    f"\n=== PLATILLO ===\n"
    f"{super().mostrar_informacion()}\n"
    f"Tiempo de preparación: {self.tiempo_preparacion} minutos"
    )