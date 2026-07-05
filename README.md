# Restaurante App - Semana 6

## Nombre del estudiante
*Andrango Nieto Alison Dayana*

---

## Descripción del sistema
Este proyecto corresponde a una mejora del sistema *Restaurante App*, en el cual se aplican los principios de Programación Orientada a Objetos (POO): herencia, encapsulación y polimorfismo.

El sistema simula la gestión de productos de un restaurante, permitiendo registrar y mostrar información de platillos y bebidas.

---

## Estructura del proyecto
El proyecto está organizado de forma modular de la siguiente manera:

- **modelos/**
  - producto.py (clase padre)
  - platillo.py (clase hija)
  - bebida.py (clase hija)
  - __init__.py

- **servicios/**
  - restaurante.py (gestión de productos)
  - __init__.py

- main.py (punto de ejecución del programa)
- README.md (documentación del proyecto)

---

## Herencia
Se implementa herencia mediante la clase `Producto`, la cual actúa como clase padre.

Las clases `Platillo` y `Bebida` heredan de `Producto`, reutilizando atributos como nombre, precio y disponibilidad, y agregando atributos propios:

- Platillo: tiempo de preparación  
- Bebida: sabor  

---

## Encapsulación
Se aplica encapsulación al atributo `__precio`, el cual no puede ser accedido directamente desde fuera de la clase.

Para su manejo se utilizan los métodos:
- obtener_precio()
- establecer_precio()

Esto permite proteger la información y controlar su modificación.

---

## Polimorfismo
El polimorfismo se implementa mediante el método `mostrar_informacion()`, el cual es sobrescrito en las clases `Platillo` y `Bebida`.

Esto permite que cada tipo de producto muestre su información de forma diferente.

---

## Reflexión
La aplicación de los principios de Programación Orientada a Objetos permite estructurar el código de manera organizada, facilitando su mantenimiento y comprensión. La división en módulos mejora la identificación de errores y la escalabilidad del sistema. Además, el uso de herencia, encapsulación y polimorfismo permite reutilizar código y modelar de mejor forma situaciones del mundo real dentro de un sistema de software.