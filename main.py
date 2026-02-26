from modelos.producto import Producto
from servicios.gestion_inventario import Inventario

def menu():
    # El inventario se carga automáticamente al instanciar la clase 
    mi_inventario = Inventario()
    
    while True:
        print("\n" + "═"*35)
        print("  ✨ SISTEMA DE GESTIÓN LIBRERIA ✨ ")
        print("═"*35)
        print("1. ➕ Añadir producto")
        print("2. 🗑️ Eliminar Producto")
        print("3. 🔄 Actualizar Producto")
        print("4. 🔍 Buscar Producto por Nombre")
        print("5. 📋 Listar Inventario Completo")
        print("6. 🚪 Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("🆔 ID único: "))
                nombre = input("🏷️ Nombre: ")
                cant = int(input("🔢 Cantidad: "))
                precio = float(input("💰 Precio: "))
                # Se mantiene el uso de la lista interna del objeto 
                mi_inventario.añadir_producto(Producto(id_p, nombre, cant, precio))
            except ValueError:
                print("❌ Error: ID, Cantidad y Precio deben ser numéricos.")

        elif opcion == "2":
            try:
                id_p = int(input("🗑️ Ingrese ID del producto a eliminar: "))
                mi_inventario.eliminar_producto(id_p)
            except ValueError:
                print("❌ Error: El ID debe ser un número.")

        elif opcion == "3":
            try:
                id_p = int(input("📝 Ingrese ID del producto: "))
                cant = input("🔢 Nueva cantidad (vacío para omitir): ")
                prec = input("💰 Nuevo precio (vacío para omitir): ")
                
                n_cant = int(cant) if cant else None
                n_prec = float(prec) if prec else None
                mi_inventario.actualizar_producto(id_p, n_cant, n_prec)
            except ValueError:
                print("❌ Error: Los valores de actualización deben ser numéricos.")

        elif opcion == "4":
            # Cambio solicitado: Búsqueda por nombre con emoji de lupa 
            nombre = input("🔍 Ingrese el nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            if resultados:
                print(f"\n✅ Coincidencias encontradas para '{nombre}':")
                for r in resultados: 
                    # Se asume que el objeto Producto tiene un método de impresión
                    print(f"🔎 {r}") 
            else:
                print("❌ No se encontraron coincidencias.")

        elif opcion == "5":
            print("\n📦 --- INVENTARIO ACTUAL ---")
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            print("🚪 Cerrando sistema... ¡Hasta luego!")
            break
        else:
            print("🚫 Opción no válida.")

if __name__ == "__main__":
    menu()
