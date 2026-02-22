"""
Clase Inventario mejorada
Incluye almacenamiento en archivo y manejo de excepciones.
"""

from producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # ==============================
    # Cargar productos desde archivo
    # ==============================
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_p, nombre, cantidad, precio = datos
                        producto = Producto(id_p, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
            print("✔ Inventario cargado correctamente.")
        except FileNotFoundError:
            print("⚠ Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()
        except PermissionError:
            print("❌ Error de permisos al acceder al archivo.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    # ==============================
    # Guardar en archivo
    # ==============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")
            print("💾 Cambios guardados en archivo.")
        except PermissionError:
            print("❌ No se pudo escribir en el archivo (Permiso denegado).")
        except Exception as e:
            print(f"❌ Error al guardar: {e}")

    # ==============================
    # Agregar producto
    # ==============================
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto agregado correctamente.")

    # ==============================
    # Eliminar producto
    # ==============================
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("🗑 Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    # ==============================
    # Actualizar producto
    # ==============================
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("✏ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    # ==============================
    # Buscar producto
    # ==============================
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron coincidencias.")

    # ==============================
    # Mostrar todos
    # ==============================
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        print("\n=== INVENTARIO ===")
        for p in self.productos:
            print(p)
