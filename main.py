from modelos.producto import Producto
from servicios.gestion_inventario import Inventario

def menu():
    mi_inventario = Inventario()
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIOS ---")
        print("1. Añadir Producto")
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
                print(" Error: Ingrese valores numéricos válidos para ID, cantidad y precio.")

        elif opcion == "2":
            id_p = int(input("Ingrese ID del producto a eliminar: "))
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = int(input("Ingrese ID del producto: "))
            cant = input("Nueva cantidad (deje vacío para no cambiar): ")
            prec = input("Nuevo precio (deje vacío para no cambiar): ")
            
            nueva_cant = int(cant) if cant else None
            nuevo_prec = float(prec) if prec else None
            mi_inventario.actualizar_producto(id_p, nueva_cant, nuevo_prec)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            for r in resultados: print(r)

        elif opcion == "5":
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            print("Salir del sistema...")
            break
        else:
            print(" Opción no válida.")

if __name__ == "__main__":
    menu()