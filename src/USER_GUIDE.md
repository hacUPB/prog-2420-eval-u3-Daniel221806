# Guía de uso para el programa Gestor de Flota de Aerolínea

## Instrucciones de Instalación y Ejecución

### Requisitos:

- **Python**: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde https://www.python.org/.

- **Editor de código**: Se recomienda usar Visual Studio Code.

### Pasos:

- **Clonar el repositorio**: Utiliza el siguiente comando en tu terminal:

*git clone https://github.com/hacUPB/prog-2420-eval-u3-Daniel221806.git*


**Abrir el proyecto**: Abre el directorio clonado en tu editor de código.

**Ejecutar el programa**: Abre el archivo *main.py* y ejecútalo desde tu editor de código o desde la terminal.

## Uso del Programa

### Ejecución

Al ejecutar el programa, el sistema te solicitará que proporciones datos específicos acerca de cada tipo de avión que tienes en tu flota (modelos) y de cada avión individual (flota).

**Modelos de aeronaves**: Aquí deberás indicar las características de cada tipo de avión, como el número máximo de pasajeros, la cantidad de combustible necesaria y la capacidad de carga.
**Flota**: En esta sección, deberás registrar cada avión individual, especificando a qué modelo pertenece y otras características relevantes como el número de matrícula.

### Menú

A continuación se te presentará un menú con las siguientes opciones:

**Cantidad máxima de pasajeros que pueden ser transportados**: Calcula la capacidad total de pasajeros de un modelo específico o de toda la flota.
**Cantidad mínima de combustible para utilizar toda la flota**: Calcula la cantidad mínima de combustible necesaria para operar todos los aviones de un modelo específico o de toda la flota.
**Máxima cantidad de carga paga que puede ser transportada**: Calcula la capacidad máxima de carga de un modelo específico o de toda la flota.
**Dinero promedio generado con la flota**: Calcula la ganancia promedio generada por un modelo específico o por toda la flota, considerando el precio promedio del billete.
**Salir**: Termina la ejecución del programa.

## Interacción con el programa:

El programa te guiará a través de una serie de preguntas para ingresar los datos necesarios. Asegúrate de proporcionar respuestas válidas (números enteros positivos para cantidades, nombres de modelos, etc.).

## Ejemplos
### Ejemplo 1: 
**Calcular la capacidad total de pasajeros**

1. Ejecuta el programa.
2. Ingresa la información solicitada sobre los modelos y la flota.
3. Selecciona la opción "1. Cantidad máxima de pasajeros que pueden ser transportados".
4. Ingresa el nombre del modelo o "Total" para obtener la capacidad total de la flota.

### Ejemplo 2:
**Calcular la ganancia promedio**

1. Ejecuta el programa.
2. Ingresa la información solicitada sobre los modelos y la flota.
3. Selecciona la opción "4. Dinero promedio generado con la flota".
4. Ingresa el nombre del modelo o "Total".
5. Ingresa el valor promedio del billete para cada modelo cuando se te solicite.

## Observaciones

- **Limpieza de pantalla**: Después de cada respuesta, la terminal se limpiará para una mejor visualización.

- **Validación de datos**: El programa realiza algunas validaciones básicas para asegurar que los datos ingresados sean válidos (por ejemplo, que la cantidad de pasajeros sea un número positivo).