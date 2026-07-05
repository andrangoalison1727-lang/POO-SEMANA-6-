class Restaurante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []
# 1. Agregar productos del restaurante
    def agregar_producto(self, producto):
        self.productos.append(producto)
        return f"Producto '{producto.nombre}' agregado al restaurante."

# 2. Mostrar productos del restaurante
    
    def mostrar_productos(self):
        print(f"\n=== PRODUCTOS DEL RESTAURANTE '{self.nombre}' ===")
        for producto in self.productos:
            print(producto.mostrar_informacion())