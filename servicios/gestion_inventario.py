from modelos.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("Error: El ID ya existe.")
            return False
        self.productos.append(producto)
        print("Producto añadido con éxito.")
        return True

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                print(f" Producto {id_producto} eliminado.")
                return True
        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_producto:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                print("Producto actualizado.")
                return True
        print(" Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre_parcial):
        resultados = [p for p in self.productos if nombre_parcial.lower() in p.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)