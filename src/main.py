def main():

    from os import system

    # Definición de todas las funciones necesarias para el código

    def calcular_capacidad_pasajeros(modelos, flota):
        print("Excelente! Conozcamos cuántos pasajeros podemos transportar. Contamos con los siguientes modelos:")
        for modelo in modelos:
            print(modelo)
        opcion = input("Escriba el nombre del modelo que desea consultar tal como lo escribió al inicio del programa. Si desea conocer la cantidad total de pasajeros que se pueden transportar, escriba \"Total\": ")
        system("cls")
        if opcion in modelos:
            # Calcular capacidad para un modelo específico
            pasajeros_totales = 0
            for avion in flota:
                if flota[avion] == opcion:
                    pasajeros_totales += modelos[opcion]["Pasajeros"]
            print(f"Para este modelo podemos transportar en total {pasajeros_totales} pasajeros.")
        elif opcion == "Total" or opcion == "total":
            # Calcular capacidad total de la flota
            pasajeros_totales = 0
            for modelo in modelos:
                for avion in flota:
                    if flota[avion] == modelo:
                        pasajeros_totales += modelos[modelo]["Pasajeros"]
            print(f"Podemos transportar con toda nuestra flota {pasajeros_totales} pasajeros.")
        else:
            print("Modelo no encontrado.")


    def calcular_combustible_minimo(modelos, flota):
        print("Excelente! Conozcamos cuánto es el combustible mínimo con el que podemos volar. Contamos con los siguientes modelos:")
        for modelo in modelos:
            print(modelo)
        opcion = input("Escriba el nombre del modelo que desea consultar tal como lo escribió al inicio del programa. Si desea conocer la cantidad mínima de combustible con el que puede volar toda la flota, escriba \"Total\": ")
        system("cls")
        if opcion in modelos:
            # Calcular combustible para un modelo específico
            combustible_total = 0
            for avion in flota:
                if flota[avion] == opcion:
                    combustible_total += modelos[opcion]["Combustible"]
            print(f"Para volar todos nuestros aviones de este modelo necesitamos mínimo {combustible_total} galones de combustible.")
        elif opcion == "Total" or opcion == "total":
            # Calcular combustible total para toda la flota
            combustible_total = 0
            for modelo in modelos:
                for avion in flota:
                    if flota[avion] == modelo:
                        combustible_total += modelos[modelo]["Combustible"]
            print(f"Podemos volar toda nuestra flota con mínimo {combustible_total} galones de combustible.")
        else:
            print("Modelo no encontrado.")

    
    def calcular_carga_maxima(modelos, flota):
        print("Excelente! Conozcamos cuánto es la carga paga máxima que podemos transportar. Contamos con los siguientes modelos:")
        for modelo in modelos:
            print(modelo)
        opcion = input("Escriba el nombre del modelo que desea consultar tal como lo escribió al inicio del programa. Si desea conocer la cantidad de carga paga máxima que puede transportar toda la flota, escriba \"Total\": ")
        system("cls")
        if opcion in modelos:
            # Calcular carga para un modelo específico
            carga_total = 0
            for avion in flota:
                if flota[avion] == opcion:
                    carga_total += modelos[opcion]["Carga"]
            print(f"Con este modelo podemos transportar máximo {carga_total} toneladas de carga paga.")
        elif opcion == "Total" or opcion == "total":
            # Calcular carga total para toda la flota
            carga_total = 0
            for modelo in modelos:
                for avion in flota:
                    if flota[avion] == modelo:
                        carga_total += modelos[modelo]["Carga"]
            print(f"Toda nuestra flota puede transportar máximo {carga_total} toneladas de carga paga.")
        else:
            print("Modelo no encontrado.")


    def calcular_ganancia_promedio(modelos, flota):
        print("Excelente! Conozcamos cuánto es la ganancia promedio que podemos generar. Contamos con los siguientes modelos:")
        for modelo in modelos:
            print(modelo)
        opcion = input("Escriba el nombre del modelo que desea consultar tal como lo escribió al inicio del programa. Si desea conocer el promedio de ganancias que genera toda la flota, escriba \"Total\": ")
        system("cls")
        if opcion in modelos:
            # Calcular ganancia para un modelo específico
            ganancia_total = 0
            valor_billete = float(input(f"¿Cuánto es el valor promedio del billete para el modelo {opcion}? "))
            system("cls")
            for avion in flota:
                if flota[avion] == opcion:
                    ganancia_total += modelos[opcion]["Pasajeros"] * valor_billete
            print(f"Con este modelo podemos ganar en promedio {ganancia_total}")
        elif opcion == "Total" or opcion == "total":
            # Calcular ganancia total para toda la flota
            ganancia_total = 0
            for modelo in modelos:
                valor_billete = float(input(f"¿Cuánto es el valor promedio del billete para el modelo {modelo}? "))
                system("cls")
                for avion in flota:
                    if flota[avion] == modelo:
                        ganancia_total += modelos[modelo]["Pasajeros"] * valor_billete
            print(f"Toda nuestra flota genera en promedio una ganancia de {ganancia_total}")
        else:
            print("Modelo no encontrado.")

    # CÓDIGO

    modelos = {}
    flota = {}

    # Ingreso de información de los modelos
    while True:
        try:
            cantidad_modelos = int(input("Por favor, ingrese la cantidad de modelos de aeronaves: "))
            system("cls")
            if cantidad_modelos > 0:
                break
            else:
                print("La cantidad de modelos debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    for n in range(1, cantidad_modelos+1):
        modelo_iter = {}
        modelo_iteracion = input(f"Ingrese el nombre del modelo #{n}: ")
        system("cls")
        while True:
            try:
                pasajeros = int(input("Indique la cantidad de pasajeros máxima para este modelo: "))
                system("cls")
                if pasajeros > 0:
                    break
                else:
                    print("La cantidad de pasajeros debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        modelo_iter["Pasajeros"] = pasajeros

        while True:
            try:
                combustible = int(input("Indique la cantidad de combustible mínima para este modelo: "))
                system("cls")
                if combustible >= 0:
                    break
                else:
                    print("La cantidad de combustible debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        modelo_iter["Combustible"] = combustible

        while True:
            try:
                carga = int(input("Indique la cantidad de carga paga máxima para este modelo: "))
                system("cls")
                if carga >= 0:
                    break
                else:
                    print("La cantidad de carga debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        modelo_iter["Carga"] = carga

        modelos[modelo_iteracion] = modelo_iter

    # Ingreso de información de las aeronaves
    for modelo1 in modelos:
        while True:
            try:
                cantidad_iteracion = int(input(f"Indique la cantidad total de aeronaves para el modelo {modelo1}: "))
                system("cls")
                if cantidad_iteracion >= 0:
                    break
                else:
                    print("La cantidad de aeronaves debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        for m in range(1, cantidad_iteracion+1):
            matricula_iteracion = input(f"Ingrese el número de matrícula para la aeronave #{m} de este modelo: ")
            system("cls")
            flota[matricula_iteracion] = modelo1

    # Menú de opciones
    while True:
        opcion = int(input("Por favor, selecciona un número del siguiente menú:\n"
                           "1. Cantidad máxima de pasajeros que pueden ser transportados.\n"
                           "2. Cantidad mínima de combustible para utilizar toda la flota.\n"
                           "3. Máxima cantidad de carga paga que puede ser transportada.\n"
                           "4. Dinero promedio generado con la flota.\n"
                           "5. Salir\n"))
        system("cls")

        if opcion == 1:
            # Calcular cantidad máxima de pasajeros
            calcular_capacidad_pasajeros(modelos, flota)
        elif opcion == 2:
            # Calcular cantidad mínima de combustible
            calcular_combustible_minimo(modelos, flota)
        elif opcion == 3:
            # Calcular máxima cantidad de carga
            calcular_carga_maxima(modelos, flota)
        elif opcion == 4:
            # Calcular ganancias promedio
            calcular_ganancia_promedio(modelos, flota)
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()