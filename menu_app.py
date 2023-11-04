# Función para agregar una compra a la lista de compras
def agregar_compra(compras):
    precio = float(input("Ingrese el precio del producto: "))
    compras.append(precio)
    print("Compra agregada correctamente.")


# Función para mostrar las compras registradas
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Compras registradas:")
        for i, (precio) in enumerate(compras, start=1):
            print(f"{i}. Precio: ${precio:.2f}")


# Función para mostrar el total gastado
def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")


# Función principal del programa
def main():
    compras = []

    while True:
        print("\nMenú de Compras")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()



