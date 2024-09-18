Tarea 1


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Autor: Miranda Merino Irigoyen Jorge Missael#
#Fecha: 06/09/2024#
#Descripciòn: Este codigo compara tres de los metodos de Monte Carlo#
#generando una muestra de la variable aleatoria con distribuciòn g(x)#
#1.Monte Carlo crudo#
#2.Acierto y error#
#3.Muestreo de importancia#

#Librerias#

from random import random
import matplotlib.pyplot as plt
from math import cos, pi
from statistics import mean, variance
import numpy as np
import pandas as pd
from tabulate import tabulate

#Primero definiremos la funciòn de distribuciòn de probabilidad#
#Funciòn que usaremos para comparar la eficiencia de los metodos#
def g(x):
    return np.cos(pi*x/2)

#Resultado análitico e la integral#
I_exacta=0.6366197723675813
print("El resultado exacto de la integral es:", I_exacta)


#######    Monte Carlo Crudo    ########
#Esta funciòn realizará el metodo de monte carlo crudo#
#a=Valor inferior del intervalo#
#b=valor superior del intervalo#
#n=nùmero de puntos#
def monte_carlo_crudo(a,b,n):

    #primero vamos a crear una secuencia de nùmeros aleatorios#
    u=np.random.uniform(a,b,n)
    #calculamos nuestras observaciones Xi#
    x=a+u*(b-a)
    #Calculamos g(x)#
    g_x=g(x)

    #Calculamos la media muestral#
    m=(b-a)*np.mean(g_x)
    var_crudo=variance(g_x)
    return m,var_crudo

#Ahora podemos estimar el valor de la integral#
Integral_estim_mcc,var_crudo=monte_carlo_crudo(0,1,1000)
#print("La estimaciòn de la integral por monte carlo crudo:", Integral_estim_mcc)

error_mccrudo=abs(Integral_estim_mcc-I_exacta)
#print("El error del metodo de monte carlo crudo:", error_mccrudo)

#######    Monte Carlo de acierto y error    ########
#Esta funciòn realizarà el metodo de monte carlo de acierto y error#
#a=Valor inferior del intervalo#
#b=Valor superior del intervalo#
#n=nùmero de puntos#
def monte_carlo_acierto(a,b,n):
    # Generamos nuestros puntos aleatorios (Xi,Yi)#
    x_puntos=np.random.uniform(a,b,n)

    # Calculamos el valor máximo de g(x) en todo el intervalo
    y_max = np.max([g(x) for x in np.linspace(a, b, 1000)])  # Buscamos el valor máximo en el intervalo

    y_puntos=np.random.uniform(0,y_max,n)

    # Ahora contamos los puntos que caen debajo de la curva g(x)#
    abajo_curva=y_puntos<g(x_puntos)
    aux_num=np.sum(abajo_curva)
    var_aye=variance(y_puntos)

    # Estimamos el area bajo la curva#
    area_curv=(b-a)*y_max
    I=(aux_num / n) * area_curv
    return I,var_aye

#Ahora estimamos el valor de la integral usando este metodo de acierto y error#
Integral_estim_mcaye,var_aye=monte_carlo_acierto(0,1,10000)
#print("El valor de la integral usando el metodo de acierto y error es:", Integral_estim_mcaye)

error_mcaye=abs(Integral_estim_mcaye-I_exacta)
#print("El error del metodo de monte acierto y error:", error_mcaye)

#######    Monte Carlo de muestro de importancia   ########
# Vamos a usar una distribución uniforme [0, 1] como q(x), y modificamos el cálculo
def q(x):
    return 1  # q(x) = 1 en [0, 1] ya que estamos usando una distribución uniforme

def gen_q(n):
    return np.random.uniform(0, 1, n)

def monte_carlo_importancia(a, b, n):
    # Generamos muestras de una distribución uniforme [0, 1]
    x_muestras = gen_q(n)

    # Evaluamos g(x) / q(x) en cada una de las muestras
    g_q = g(x_muestras) / q(x_muestras)

    # Calculamos la media ponderada
    estimacion = np.mean(g_q) * (b - a)

    var_mci=variance(g_q)

    return estimacion,var_mci

# Estimamos el valor de la integral usando muestreo de importancia
Integral_estim_mci,var_mci = monte_carlo_importancia(0, 1, 10000)
#print("El valor de la integral usando el metodo de muestreo de importancia es:", Integral_estim_mci)

error_mci=abs(Integral_estim_mci-I_exacta)
#print("El error del metodo de monte carlo por muestro de importancia:", error_mci)


#Ahora pongamos esta información en una tabla#
resultados = {
    'Método': ['Monte Carlo Crudo', 'Monte Carlo Acierto y Error', 'Monte Carlo Muestreo de Importancia'],
    'Estimación': [Integral_estim_mcc, Integral_estim_mcaye, Integral_estim_mci],
    'Error': [error_mccrudo, error_mcaye, error_mci],
    'Varianza':[var_crudo, var_aye, var_mci]
}

# Crea un DataFrame con los resultados
df_resultados = pd.DataFrame(resultados)

# Muestra la tabla con bordes en la consola usando tabulate
print(tabulate(df_resultados, headers='keys', tablefmt='grid'))


# In[ ]:




