#Proyecto Pacman

import pygame, sys

pygame.init() #Iniciar pygame

#colores
negro= (0, 0, 0) #fondo
blanco = (255, 255, 255) #bolitas, texto
azul = (0, 0, 255)
rojo = (255, 0, 0)
amarillo = (255, 255, 0)
celeste = (135, 206, 235)
rosado =(255, 182, 193)
naranja= (255, 128, 0)


#ventana principal
ancho = 800
largo = 600
ventana = pygame.display.set_mode([ancho, largo])
game_over = False

#Bucle para la ventana

while not game_over:
    for event in pygame.event.get(): #registrar eventos en ventana
        if event.type == pygame.QUIT:
            sys.exit() #salirnos de la ventana

    ventana.fill(negro)


#CLASE JUEGO

#Atributos: Número de juego, tablero (matriz 40x36,
# 0: espaco vacío, 1: puntos, 2: cápsula de poder,3: frutas
# 4: pared horizontal, 5: pared vertical, 6: puerta fantasmas
# nivel (1 y 2), score

#métodos: iniciar juego

class juego(object):
    def __init__(self):
        pass

matriz_1= [
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]