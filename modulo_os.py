#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:04:47 2021

@author: Army-R

Source: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion7/archivos.html  
"""
# Métodos del modulo os para manipular archivos
import os

# Crear nueva carpeta
os.mkdir("modulo_os")

# Listar el contenido de una carpeta
os.listdir("./")

# Mostrar el actual directorio de trabajo
os.getcwd()

# Mostrar el tamaño del archivo en bytes del archivo pasado en parámetro
os.path.getsize("modulo_os")

# ¿Es un archivo el parámetro pasado?
os.path.isfile("modulo_os")

# ¿Es una carpeta el parámetro pasado?
os.path.isdir("modulo_os")

# Cambiar directorio/carpeta
os.chdir("modulo_os")
os.getcwd()
os.listdir("./")
os.chdir("../")
os.getcwd()

# Renombrar un archivo
os.rename("modulo_os", "modulo_os_renombrado")
os.listdir("./")

# Eliminar un archivo
os.chdir("modulo_os_renombrado")
archivo = open(os.getcwd()+'/texto.txt', 'w')
archivo.write("Hola mundo")
archivo.close()
os.getcwd()
os.listdir("./")
os.remove(os.getcwd()+"/texto.txt")
os.listdir("./")

# Eliminar una carpeta
os.rmdir("modulo_os_renombrado")
os.chdir("modulo_os_renombrado")
# Lanza una excepción OSError cuando inetnta acceder al directorio que previamente se elimino.
