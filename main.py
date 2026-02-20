from modelos.producto import Producto
from servicios.gestion_inventario import Inventario

def menu():
    # El inventario se carga automáticamente al instanciar la clase
    mi_inventario = Inventario()
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN ---")
        print("1. Añadir producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Listar Inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID único: "))
                nombre = input("Nombre: ")
                cant = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                mi_inventario.añadir_producto(Producto(id_p, nombre, cant, precio))
            except ValueError:
                print("Error: Los campos ID, Cantidad y Precio deben ser numéricos.")

        elif opcion == "2":
            try:
                id_p = int(input("Ingrese ID del producto a eliminar: "))
                mi_inventario.eliminar_producto(id_p)
            except ValueError:
                print("Error: El ID debe ser un número.")

        elif opcion == "3":
            try:
                id_p = int(input("Ingrese ID del producto: "))
                cant = input("Nueva cantidad (vacío para omitir): ")
                prec = input("Nuevo precio (vacío para omitir): ")
                
                n_cant = int(cant) if cant else None
                n_prec = float(prec) if prec else None
                mi_inventario.actualizar_producto(id_p, n_cant, n_prec)
            except ValueError:
                print("Error: Los valores de actualización deben ser numéricos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "5":
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()