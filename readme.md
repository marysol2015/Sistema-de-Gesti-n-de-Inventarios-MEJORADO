El sistema funciona con  una arquitectura modular basada en  la Programación Orientada a Objetos (POO):

Modelo de Datos (Producto): Utiliza encapsulamiento para proteger los datos (ID, nombre, stock, precio) mediante atributos privados y decoradores @property.

Lógica de Negocio (Inventario): Gestiona de objetos en memoria. Implementa algoritmos de validación (para evitar IDs duplicados), filtrado dinámico (búsquedas parciales) y manipución de estados (actualización y borrado).

Interfaz de Usuario: Un bucle while en consola actúa como controlador, capturando las entradas del usuario y coordinando las llamadas a los servicios del inventario.