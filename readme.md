Cada operación de escritura (añadir, eliminar, actualizar) llama a guardar_en_archivo(), lo que garantiza que los datos no se pierdan si el programa se cierra inesperadamente.
El método cargar_desde_archivo verifica si el archivo existe usando os.path.exists y lo crea si es necesario, evitando errores en la primera ejecución.
Los productos no se borran al cerrar el programa porque se guardan en inventario.txt. 
El sistema valida que no repitas IDs y maneja errores si el archivo se daña o no tiene permisos. 
Implementación de emojis en el menú y búsqueda por nombre según requerimientos