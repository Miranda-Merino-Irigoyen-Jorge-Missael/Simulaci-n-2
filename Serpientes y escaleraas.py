#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Autor: Miranda Merino Irigoyen Jorge Missael#
#Fecha: 17/09/2024#
#Descripción: Este programa simula el juego de serpientes y escaleras#
#y devuelve el número promedio de veces que se necesita tirar el dado#
#para terminar el juego#

#Librerias#
from random import random

# Función que simula tirar un dado
def tirar_dado():
    x = random()
    if x <= 1/6:
        return 1
    elif x <= 2/6:
        return 2
    elif x <= 3/6:
        return 3
    elif x <= 4/6:
        return 4
    elif x <= 5/6:
        return 5
    else:
        return 6

# Número de simulaciones
simulaciones = 10000
total_tiradas = 0

# Simulamos el juego para cada partida
for i in range(simulaciones):
    casilla = 0  # Reiniciar la casilla al inicio del juego
    tiradas = 0  # Contador de tiradas para cada partida
    
    # Mientras el jugador no haya llegado o pasado de la casilla 20
    while casilla < 20:
        dado = tirar_dado()
        tiradas += 1  # Aumentar el contador de tiradas
        
        # Avanzar las casillas correspondientes según el dado
        casilla += dado
    
    # Sumar el número de tiradas de esta partida al total
    total_tiradas += tiradas

# Calcular el promedio de tiradas por partida
promedio_tiradas = total_tiradas / simulaciones

print(f"Promedio de tiradas: {promedio_tiradas}")

