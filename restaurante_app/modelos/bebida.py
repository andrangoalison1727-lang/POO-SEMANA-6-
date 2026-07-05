from modelos.producto import Producto

# 1. Clase Bebida que hereda de Producto
class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, disponible: bool = True, sabor: str = "" ):
        super().__init__(nombre, precio, disponible)
        self.sabor = sabor

# 2. Mostrar información de la bebida

    def mostrar_informacion(self) -> str:
        return (
            f"\n=== BEBIDA ===\n"
            f"{super().mostrar_informacion()}\n"
            f"Sabor: {self.sabor}"
        )