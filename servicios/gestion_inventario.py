from modelos.producto import Producto
import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        # Carga automática al iniciar
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Reconstruye la lista de productos desde el archivo de texto."""
        if not os.path.exists(self.archivo):
            return 

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_p, nombre, cant, precio = datos
                        # Se crean objetos Producto a partir de los datos guardados
                        nuevo_p = Producto(int(id_p), nombre, int(cant), float(precio))
                        self.productos.append(nuevo_p)
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda la lista actual de productos en el archivo físico."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    # Accedemos a los datos mediante los @property definidos
                    f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")
            return True
        except Exception as e:
            print(f"Error crítico al escribir en archivo: {e}")
            return False

    def añadir_producto(self, producto):
        """Añade producto a memoria y actualiza el archivo inmediatamente."""
        if any(p.id == producto.id for p in self.productos):
            print("Error: El ID ya existe.")
            return False
        
        self.productos.append(producto)
        if self.guardar_en_archivo():
            print("Producto guardado exitosamente en el archivo.")
            return True
        return False

    def mostrar_inventario(self):
        """Lista los productos que están cargados en la memoria del sistema."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- PRODUCTOS EN EXISTENCIA ---")
            for p in self.productos:
                print(p)

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print(f"Producto {id_producto} eliminado.")
                return True
        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_producto:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return True
        print("Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre_parcial):
        return [p for p in self.productos if nombre_parcial.lower() in p.nombre.lower()]