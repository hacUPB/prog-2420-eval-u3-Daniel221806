[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre: Daniel Alexander Colmenares Rolón
ID: 000542675
---
Pseudocódigo

# *Gestión de flota de aeronaves*

*Definir cantidad_de_modelos*
*Definir n = 1*
*Definir modelo_iteracion = {}*
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
*Definir iteracion*
*Definir l = 1*

Imprimir "Por favor, ingrese la cantidad de modelos de aeronaves"
Leer cantidad_de_modelos

Mientras *cantidad_de_modelos* > 0
    *cantidad_de_modelos* = *cantidad_de_modelos* - 1
    Imprimir "Ingrese el nombre del modelo #" *n*
    Leer *modelo_iteracion*
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
    Imprimir "Indique el tiempo máximo entre mantenimientos para este modelo"
    Leer *mantenimiento_iteracion*
    Agregar *mantenimiento_iteracion* a *modelo_iteracion* en la clave *Mantenimiento*
    Agregar *modelo_iteracion* a *modelos* en la clave *modelo_iteracion*
    n = n + 1

Para *modelo1* en *lista_de_modelos*
    Imprimir "Indique la cantidad total de aeronaves de este modelo"
    Leer *cantidad_iteracion*
    Mientras *cantidad_iteracion* > 0
        *cantidad_iteracion* = *cantidad_iteracion* - 1
        Imprimir "Ingrese el número de matrícula para la aeronave #" *m* " de este modelo"
        Leer *matricula_iteracion*
        Agregar a *flota* la clave *matricula_iteracion* con el valor *modelos* en la posición *modelo1*

Imprimir "Muy bien, ya tenemos inventariada nuestra flota, ahora vamos a gestionarla. Por favor, selecciona un número del siguiente menú: 1. Cantidad máxima de pasajeros que pueden ser transportados. 2. Cantidad mínima de combustible para utilizar toda la flota. 3. Próximo mantenimiento de una aeronave. 4. Dinero promedio generado con la flota."

Leer *opcion*

Si *opcion* = 1
    Imprimir "Excelente! Conozcamos cuántos pasajeros podemos transportar. Seleccione una de las opciones:"
    Para *iteracion* en *lista_de_modelos"
        Imprimir *l* ". Cantidad máxima de pasajeros en" *iteracion*
        *l* = *l* + 1
    