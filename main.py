from ClassLista import listaVehiculos
from ClassVehiculoNuevo import Vehiculo_Nuevo
from  ClassVehiculoUsado import Vehiculo_usado
def menu():
    print('1. Insertar un vehículo en la colección en una posición determinada.')
    print('2. Agregar un vehículo a la colección.')
    print('3. Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.')
    print('4. Modificar el precio base, y luego mostrar el precio de venta.')
    print('5. Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.')
    print('6. Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.')
    print('7. Almacenar los objetos de la colección Lista en el archivo')
    print('8. Salir')
def crear_vehiculo():
    print("1. Vehiculo Nuevo")
    print("2. Vehiculo Usado")
    tipo = input("¿Es un vehículo nuevo o usado? (nuevo/usado): ")
    modelo = input("Ingrese el modelo del vehículo: ")
    cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
    color = input("Ingrese el color del vehículo: ")
    precio_base = float(input("Ingrese el precio base del vehículo: "))
    if tipo == 1:
        marca = input('Ingrese marca: ')
        version = input('¿Es un vehiculo full/base?: ')
        vehiculo_n = Vehiculo_Nuevo(modelo, cantidad_puertas, color, precio_base, marca, version)
        retorna = vehiculo_n
    elif tipo == 2:
        marca = input('Ingrese marca: ')
        Patente = input('Ingrese patente: ')
        ani = input('ingrese año: ')
        kilometraje = input('Ingrese Kilometraje: ')
        vehiculo_u = Vehiculo_usado(modelo, cantidad_puertas, color, precio_base, marca, Patente, ani, kilometraje)
        retorna = vehiculo_u
    else:
        print('Opcion Invalida.')
        retorna = None
    return retorna

if __name__ == '__main__':
    lista = listaVehiculos()
    lista.leerJSONArchivo()
    opcion = None

    while opcion != 0:
        menu()
        opcion = int(input('\n Ingrese una opción: '))

        if opcion == 1:
            vehiculo = crear_vehiculo()
            posicion = int(input("Ingrese la posición: "))
            lista.insertar_vehiculo(vehiculo, posicion)  # Insertar un vehiculo en la coleccion en una posicion determinada

        elif opcion == 2:
            vehiculo2 = crear_vehiculo()
            lista.agregar_vehiculo(vehiculo2)  # Se agrega un vehiculo a la coleccion
        elif opcion == 3:
            posicion = int(input('Ingrese posicion para mostrar tipo de objeto: '))
            lista.mostrar_tipo_vehiculo(posicion)
        elif opcion == 4:
            patente = str(input('Ingrese patente del vehiculo usado: '))
            lista.modificacion(patente)
        elif opcion == 5:
            lista.vehiculo_economico()
        elif opcion == 6:
            lista.vehiculo_venta()
        elif opcion == 7:
            lista.AlmacenarEnArchivo()
        elif opcion == 8:
            print('Saliendo...')
            break
        else:
            if opcion >= 9:
                opcion = int(input('\n Ingrese una opción: '))

