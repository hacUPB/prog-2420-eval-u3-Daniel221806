[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre: Daniel Alexander Colmenares Rolón
ID: 000542675
---
# Gestor de Flota de Aerolínea

Este proyecto tiene como objetivo principal desarrollar una herramienta que permita gestionar de manera eficiente una flota de aeronaves. La aplicación se encargará de almacenar información relevante sobre cada modelo de aeronave, como su capacidad de pasajeros, consumo de combustible, carga máxima y cantidad de aeronaves disponibles. Además, ofrecerá al usuario funcionalidades para consultar y analizar diversos aspectos de la flota, como la capacidad total de transporte, el consumo de combustible total y las ganancias potenciales.

La importancia de este proyecto radica en la necesidad de las compañías aéreas de optimizar la gestión de sus flotas. Al contar con una herramienta como esta, las empresas podrán:

1. Tomar decisiones más informadas: Al tener acceso a datos precisos y actualizados sobre su flota, las empresas podrán planificar rutas, asignar aeronaves y realizar mantenimientos de manera más eficiente.
2. Reducir costos: Optimizando el uso de los recursos, como el combustible y la mano de obra.
3. Mejorar la seguridad: Asegurando que las aeronaves estén en óptimas condiciones para operar.
4. Incrementar los ingresos: Maximizando la capacidad de carga y la ocupación de las aeronaves.

*Funcionalidades principales:*

1. Ingreso de datos: Permitir al usuario ingresar información sobre los diferentes modelos de aeronaves, incluyendo capacidad de pasajeros, consumo de combustible, carga máxima y cantidad de aeronaves disponibles.
2. Consulta de información: Facilitar al usuario la consulta de información específica sobre un modelo de aeronave o sobre la flota en general.
3. Cálculos: Realizar cálculos como la capacidad total de pasajeros, el consumo de combustible total, la carga máxima total y la ganancia potencial de la flota.
4. Informes: Generar informes personalizados con los resultados de las consultas y cálculos realizados.

*Casos de uso:*

1. Planificación de vuelos: Determinar la aeronave más adecuada para una ruta en función de la capacidad de pasajeros, carga y alcance.
2. Análisis de costos: Calcular los costos operativos de la flota y evaluar la rentabilidad de diferentes rutas.
3. Toma de decisiones de inversión: Evaluar la necesidad de adquirir nuevas aeronaves o modernizar las existentes.

# Pseudocódigo

## *Gestión de flota de aeronaves*
```
*Definir cantidad_de_modelos*
*Definir n = 1*
*Definir modelo_iteracion = {}*
*Definir modelo_iter*
*Definir modelos = {}*
*Definir pasajeros_iteracion*
*Definir combustible_iteracion*
*Definir carga_iteracion*
*Definir mantenimiento_iteracion*
*Definir modelo1*
*Definir lista_de_modelos = []*
*Definir cantidad_iteracion*
*Definir m = 1*
*Definir matricula_iteracion*
*Definir flota = {}*
*Definir opcion*
*Definir modelo1_iteracion*
*Definir opcion1*
*Definir avion*
*Definir l = 0*
*Definir pasajeros_totales = 0*
*Definir pasajeros_parciales*
*Definir combustible_total = 0*
*Definir r = 0*
*Definir combustible_parcial*
*Definir b = 0*
*Definir carga_total = 0*
*Definir carga_parcial*
*Definir c = 0*
*Definir valor*
*Definir ganancia_total = 0*
*Definir ganancia_parcial*

Imprimir "Por favor, ingrese la cantidad de modelos de aeronaves"
Leer cantidad_de_modelos

Mientras *cantidad_de_modelos* > 0
    *cantidad_de_modelos* = *cantidad_de_modelos* - 1
    Imprimir "Ingrese el nombre del modelo #" *n*
    Leer *modelo_iteracion*
    *modelo_iter* = *modelo_iteracion*
    Agregar *modelo_iteracion* a *lista_de_modelos*
    Imprimir "Indique la cantidad de pasajeros máxima para este modelo"
    Leer *pasajeros_iteracion*
    Agregar *pasajeros_iteracion* a *modelo_iteracion* en la clave *Pasajeros*
    Imprimir "Indique la cantidad de combustible mínima para este modelo"
    Leer *combustible iteración*
    Agregar *combustible_iteracion* a *modelo_iteracion* en la clave *Combustible*
    Imprimir "Indique la cantidad de carga paga máxima para este modelo"
    Leer *carga_iteracion*
    Agregar *carga_iteracion* a *modelo_iteracion* en la clave *Carga*
    Agregar *modelo_iteracion* a *modelos* en la clave *modelo_iter*
    n = n + 1

Para *modelo1* en *lista_de_modelos*
    Imprimir "Indique la cantidad total de aeronaves para el modelo" *modelo1*
    Leer *cantidad_iteracion*
    Mientras *cantidad_iteracion* > 0
        *cantidad_iteracion* = *cantidad_iteracion* - 1
        Imprimir "Ingrese el número de matrícula para la aeronave #" *m* " de este modelo"
        Leer *matricula_iteracion*
        Agregar a *flota* la clave *matricula_iteracion* con el valor *modelos* en la posición *modelo1*

Imprimir "Muy bien, ya tenemos inventariada nuestra flota, ahora vamos a gestionarla. Por favor, selecciona un número del siguiente menú: 1. Cantidad máxima de pasajeros que pueden ser transportados. 2. Cantidad mínima de combustible para utilizar toda la flota. 3. Máxima cantidad de carga paga que puede ser transportada. 4. Dinero promedio generado con la flota."

Leer *opcion*

Si *opcion* = 1
    Imprimir "Excelente! Conozcamos cuántos pasajeros podemos transportar. Contamos con los siguientes modelos:"
    Para *modelo1_iteracion* en *modelos*
        Imprimir *modelo1_iteracion*
    Imprimir "Escriba el nombre del modelo que desea consultar. Si desea conocer la cantidad total de pasajeros que se pueden transpotar, escriba "Total""
    Leer *opcion1*
    Si *opcion1* en *modelos*
        Para *avion* en *flota*
            Si *flota* en *avion* = *opcion1*
                *l* = *l* + 1
            *pasajeros_totales* = *l* x *modelos* en la clave *opcion1* en la clave *Pasajeros*
        Imprimir "Para este modelo podemos transportar en total " *pasajeros_totales* " pasajeros."
    Si *opcion1* = "Total"
        Para *modelo1* en *lista_de_modelos*
            Para *avion* en *flota*
                Si *flota* en *avion* = *modelo1*
                    *l* = *l* + 1
            *pasajeros_parciales* = *l* x *modelos* en la clave *opcion1* en la clave *Pasajeros*
            *pasajeros_totales* = *pasajeros_totales* + *pasajeros_parciales*
        Imprimir "Podemos transportar con toda nuestra flota " *pasajeros_totales* " pasajeros."
Si no
    Si *opcion* = 2
        Imprimir "Excelente! Conozcamos cuánto es el combustible mínimo con el que podemos volar. Contamos con los siguientes modelos:"
        Para *modelo1_iteracion* en *modelos*
            Imprimir *modelo1_iteracion*
        Imprimir "Escriba el nombre del modelo que desea consultar. Si desea conocer la cantidad mínima de combustible con el que puede volar toda la flota, escriba "Total""
        Leer *opcion1*
        Si *opcion1* en *modelos*
            Para *avion* en *flota*
                Si *flota* en *avion* = *opcion1*
                    *r* = *r* + 1
                *combustible_total* = *r* x *modelos* en la clave *opcion1* en la clave *Combustible*
            Imprimir "Para volar todos nuestros aviones de este modelo necesitamos mínimo " *combustible_total* " galones de combustible"
        Si *opcion1* = "Total"
            Para *modelo1* en *lista_de_modelos*
                Para *avion* en *flota*
                    Si *flota* en *avion* = *modelo1*
                        *r* = *r* + 1
                *combustible_parcial* = *r* x *modelos* en la clave *opcion1* en la clave *Combustible*
                *combustible_total* = *combustible_total* + *combustible_parcial*
            Imprimir "Podemos volar toda nuestra flota con mínimo" *combustible_total* " galones de combustible."
Si no
    Si *opcion* = 3
        Imprimir "Excelente! Conozcamos cuánto es la carga paga máxima que podemos transportar. Contamos con los siguientes modelos:"
        Para *modelo1_iteracion* en *modelos*
            Imprimir *modelo1_iteracion*
        Imprimir "Escriba el nombre del modelo que desea consultar. Si desea conocer la cantidad de carga paga máxima que puede transportar toda la flota, escriba "Total""
        Leer *opcion1*
        Si *opcion1* en *modelos*
            Para *avion* en *flota*
                Si *flota* en *avion* = *opcion1*
                    *b* = *b* + 1
                *carga_total* = *b* x *modelos* en la clave *opcion1* en la clave *Carga*
            Imprimir "Con este modelo podemos transportar máximo " *carga_total* " toneladas de carga paga"
        Si *opcion1* = "Total"
            Para *modelo1* en *lista_de_modelos*
                Para *avion* en *flota*
                    Si *flota* en *avion* = *modelo1*
                        *b* = *b* + 1
                *carga_parcial* = *b* x *modelos* en la clave *opcion1* en la clave *Carga*
                *carga_total* = *carga_total* + *carga_parcial*
            Imprimir "Toda nuestra flota puede transportar máximo" *carga_total* " toneladas de carga paga."
Si no
    Si *opcion* = 4
        Imprimir "Excelente! Conozcamos cuánto es la ganancia promedio que podemos generar. Contamos con los siguientes modelos:"
        Para *modelo1_iteracion* en *modelos*
            Imprimir *modelo1_iteracion*
        Imprimir "Escriba el nombre del modelo que desea consultar. Si desea conocer el promedio de ganancias que genera toda la flota, escriba "Total""
        Leer *opcion1*
        Si *opcion1* en *modelos*
            Para *avion* en *flota*
                Si *flota* en *avion* = *opcion1*
                    *c* = *c* + 1
                Imprimir "¿Cuánto es el valor promedio del billete para este modelo?"
                Leer *valor*
                *ganancia_total* = *c* x *modelos* en la clave *opcion1* en la clave *Pasajeros* x *valor*
            Imprimir "Con este modelo podemos ganar en promedio " *ganancia_total*
        Si *opcion1* = "Total"
            Para *modelo1* en *lista_de_modelos*
                Imprimir "¿Cuánto es el valor promedio del billete para este modelo?"
                Leer *valor*
                Para *avion* en *flota*
                    Si *flota* en *avion* = *modelo1*
                        *c* = *c* + 1
                *ganancia_parcial* = *c* x *modelos* en la clave *opcion1* en la clave *Carga* x *valor*
                *ganancia_total* = *ganancia_total* + *ganancia_parcial*
            Imprimir "Toda nuestra flota genera en promedio una ganacia de " *ganacia_total*