import pygame
import math

pygame.init() #configuración básica de la pantalla de juego
global alto, ancho
ancho = 1280
alto = 720

pantalla_de_juego = pygame.display.set_mode([ancho, alto])#establece la pantalla de juego y su dimensiones basado en ancho y alto
timepo = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0],
[0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0],
[0, 4, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, 0],
[0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
[0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
color = 'blue'
PI = math.pi
imagenes_jugador_principal = []
for i in range(1, 3):#Toma dos imagenes, se reeedimensionan y esto crea la ilusion de movimiento en mi personaje
    imagenes_jugador_principal.append(pygame.transform.scale(pygame.image.load(f"C:\\Users\\equid\\Documents\\Phyton\\Proyecto Pacman\\imagenes_jugador_principal\\{i}.jpg"), (20, 20)))
rojo_img = pygame.transform.scale(pygame.image.load(f"C:\\Users\\equid\Documents\\Phyton\\Proyecto Pacman\\Fantasmas Img\\rojo.jpg"), (20, 20))
rosa_img = pygame.transform.scale(pygame.image.load(f"C:\\Users\\equid\Documents\\Phyton\\Proyecto Pacman\\Fantasmas Img\\rosa.jpg"), (20, 20))
azul_img = pygame.transform.scale(pygame.image.load(f"C:\\Users\\equid\Documents\\Phyton\\Proyecto Pacman\\Fantasmas Img\\azul.jpg"), (20, 20))
naranja_img = pygame.transform.scale(pygame.image.load(f"C:\\Users\\equid\Documents\\Phyton\\Proyecto Pacman\\Fantasmas Img\\naranja.jpg"), (20, 20))
asustado_img = pygame.transform.scale(pygame.image.load(f"C:\\Users\\equid\\Documents\\Phyton\\Proyecto Pacman\\Fantasmas Img\\asustado.jpg"), (20, 20))
muerto_img = pygame.transform.scale(pygame.image.load(f"C:\\Users\\equid\\Documents\\Phyton\\Proyecto Pacman\\Fantasmas Img\\muerto.jpg"), (20, 20))
pos_x = 200 #Posiciones donde va a inicar pacman
pos_y = 180
direccion = 0
#Posiciones de los fantasmas
rojo_x = 900
rojo_y = 350
rojo_direccion = 0
azul_x = 800
azul_y = 350
azul_direccion = 2
rosa_x = 850
rosa_y = 350
rosa_direccion = 2
naranja_x = 700
naranja_y = 350
naranja_direccion = 2
contador = 0
destellos = False
turns_allowed = [False, False, False, False]
direccion_command = 0
jugador_velocidad = 2
score = 0
powerup = False
power_contador = 0
come_fantasmas = [False, False, False, False]
targets = [(pos_x, pos_y), (pos_x, pos_y), (pos_x, pos_y), (pos_x, pos_y)]
rojo_muerto = False
azul_muerto = False
naranja_muerto = False
rosa_muerto = False
blinky_box = False
inky_box = False
clyde_box = False
pinky_box = False
moving = False
fantasmas_velocidad = [2, 2, 2, 2]
startup_counter = 0
lives = 3
game_over = False
gana_juego = False


class Ghost:# Estas son las caracteristicas que comparten los fantasmas;
    #x_coord y y_coord son las coordenadas de los fantasmas, objetivo es a quien buscan, img sus imagenes
    #direcc su direccion, box es para saber si se encuentran en la parte de la caja, id es para identificar a cada fantasma por separado
    def __init__(self, x_coord, y_coord, objetivo, velocidad, img, direcc, muerto, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 10 # Para ajustar el centro de la imagen
        self.center_y = self.y_pos + 10
        self.objetivo = objetivo
        self.velocidad = velocidad
        self.img = img
        self.direccion = direcc
        self.muerto = muerto
        self.in_box = box
        self.id = id
        self.rect = self.dibuja() #Hitbox de los fantasmas para revisar en colisiones
        self.turns = [False,False,False,False]

    def dibuja(self):#Condiciones de los estados de los fantasmas
        #Fantasmas en su estado normal
        if (not powerup and not self.muerto) or (come_fantasmas[self.id] and powerup and not self.muerto):
            pantalla_de_juego.blit(self.img, (self.x_pos, self.y_pos))
        #Fantasmas en estado asustado sino esta muertos    
        elif powerup and not self.muerto and not come_fantasmas[self.id]:
            pantalla_de_juego.blit(asustado_img, (self.x_pos, self.y_pos))
        #Fantasmas muertos    
        else:
            pantalla_de_juego.blit(muerto_img, (self.x_pos, self.y_pos))
        fantasma_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))#hitbox para colisiones con los fantasmas, es un simple rectangulo para verificar las colisiones
        return fantasma_rect

    def colisiones(self, x_coord, y_coord):
        # Verificar si la posición siguiente está dentro de los límites de la matriz
        if 0 <= x_coord < len(level[0]) and 0 <= y_coord < len(level):
            # Verificar si el próximo movimiento es permitido (1, 2, 3 o 4)
            if level[y_coord][x_coord] in [1, 2, 3, 4]:
                return True
        return False

    def revisar_colisiones(self):
        

        # Calcular las posiciones siguientes según la dirección del fantasma
        x_coord = int(self.center_x / 15)  # Ajusta según tus necesidades
        y_coord = int(self.center_y / 15)  # Ajusta según tus necesidades

        # Verificar colisiones en las posiciones siguientes
        if self.direccion == 0 and self.colisiones(x_coord + 1, y_coord):
            self.turns[0] = True
        if self.direccion == 1 and self.colisiones(x_coord - 1, y_coord):
            self.turns[1] = True
        if self.direccion == 2 and self.colisiones(x_coord, y_coord + 1):
            self.turns[2] = True
        if self.direccion == 3 and self.colisiones(x_coord, y_coord - 1):
            self.turns[3] = True
    def move_naranja(self):
        # Calcular las posiciones siguientes según la dirección del fantasma
        x_coord = int(self.center_x / 40)  # Ajustar según el ancho de la ventana
        y_coord = int(self.center_y / 40)  # Ajustar según el alto de la ventana

        # Verificar colisiones en las posiciones siguientes
        self.revisar_colisiones()

        # Lógica de movimiento
        if self.direccion == 0 and self.turns[0]:
            self.x_pos += self.velocidad
        elif self.direccion == 1 and self.turns[1]:
            self.x_pos -= self.velocidad
        elif self.direccion == 2 and self.turns[2]:
            self.y_pos += self.velocidad
        elif self.direccion == 3 and self.turns[3]:
            self.y_pos -= self.velocidad

        # Verificar límites de la ventana
        if self.x_pos < -30:
            self.x_pos = 1280
        elif self.x_pos > 1280:
            self.x_pos = -30  # Ajustar según el ancho de la ventana

        return self.x_pos, self.y_pos, self.direccion
        
        

    def move_rojo(self):
        
        if self.direccion == 0:
            if self.objetivo[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.velocidad
            elif not self.turns[0]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
            elif self.turns[0]:
                self.x_pos += self.velocidad
        elif self.direccion == 1:
            if self.objetivo[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.velocidad
            elif not self.turns[1]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
            elif self.turns[1]:
                self.x_pos -= self.velocidad
        elif self.direccion == 2:
            if self.objetivo[1] < self.y_pos and self.turns[2]:
                self.direccion = 2
                self.y_pos -= self.velocidad
            elif not self.turns[2]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
            elif self.turns[2]:
                self.y_pos -= self.velocidad
        elif self.direccion == 3:
            if self.objetivo[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.velocidad
            elif not self.turns[3]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
            elif self.turns[3]:
                self.y_pos += self.velocidad
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direccion

    def move_azul(self):
        
        if self.direccion == 0:
            if self.objetivo[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.velocidad
            elif not self.turns[0]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
            elif self.turns[0]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                if self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                else:
                    self.x_pos += self.velocidad
        elif self.direccion == 1:
            if self.objetivo[1] > self.y_pos and self.turns[3]:
                self.direccion = 3
            elif self.objetivo[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.velocidad
            elif not self.turns[1]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
            elif self.turns[1]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                if self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                else:
                    self.x_pos -= self.velocidad
        elif self.direccion == 2:
            if self.objetivo[1] < self.y_pos and self.turns[2]:
                self.direccion = 2
                self.y_pos -= self.velocidad
            elif not self.turns[2]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
            elif self.turns[2]:
                self.y_pos -= self.velocidad
        elif self.direccion == 3:
            if self.objetivo[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.velocidad
            elif not self.turns[3]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
            elif self.turns[3]:
                self.y_pos += self.velocidad
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direccion

    def move_rosa(self):
        # r, l, u, d
        # inky is going to turn left or right whenever advantageous, but only up or down on collision
        if self.direccion == 0:
            if self.objetivo[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.velocidad
            elif not self.turns[0]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
            elif self.turns[0]:
                self.x_pos += self.velocidad
        elif self.direccion == 1:
            if self.objetivo[1] > self.y_pos and self.turns[3]:
                self.direccion = 3
            elif self.objetivo[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.velocidad
            elif not self.turns[1]:
                if self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
            elif self.turns[1]:
                self.x_pos -= self.velocidad
        elif self.direccion == 2:
            if self.objetivo[0] < self.x_pos and self.turns[1]:
                self.direccion = 1
                self.x_pos -= self.velocidad
            elif self.objetivo[1] < self.y_pos and self.turns[2]:
                self.direccion = 2
                self.y_pos -= self.velocidad
            elif not self.turns[2]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.objetivo[1] > self.y_pos and self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.turns[3]:
                    self.direccion = 3
                    self.y_pos += self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
            elif self.turns[2]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                else:
                    self.y_pos -= self.velocidad
        elif self.direccion == 3:
            if self.objetivo[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.velocidad
            elif not self.turns[3]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.objetivo[1] < self.y_pos and self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[2]:
                    self.direccion = 2
                    self.y_pos -= self.velocidad
                elif self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                elif self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
            elif self.turns[3]:
                if self.objetivo[0] > self.x_pos and self.turns[0]:
                    self.direccion = 0
                    self.x_pos += self.velocidad
                elif self.objetivo[0] < self.x_pos and self.turns[1]:
                    self.direccion = 1
                    self.x_pos -= self.velocidad
                else:
                    self.y_pos += self.velocidad
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direccion


def draw_misc():
    score_text = font.render(f'Puntaje: {score}', True, 'white')#Texto de puntaje
    pantalla_de_juego.blit(score_text, (10, 920))
    if powerup: # Dibuja el indicador de la potencia si está activo
        pygame.draw.circle(pantalla_de_juego, 'blue', (140, 930), 15)
    for i in range(lives):# Dibuja los íconos de vidas
        pantalla_de_juego.blit(pygame.transform.scale(imagenes_jugador_principal[0], (30, 30)), (650 + i * 40, 915))
    if game_over: # Dibuja la pantalla de Game Over si es necesario
        pygame.draw.rect(pantalla_de_juego, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(pantalla_de_juego, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('Fin del juego! Barra espaciadora para reiniciar!', True, 'red')
        pantalla_de_juego.blit(gameover_text, (100, 300))
    if gana_juego: # Dibuja la pantalla de Victoria si es necesario
        pygame.draw.rect(pantalla_de_juego, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(pantalla_de_juego, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('Ganaste! Barra espaciadora para reiniciar!', True, 'green')
        pantalla_de_juego.blit(gameover_text, (100, 300))


def revisar_collisions(scor, power, power_contador, come_fantasmas):
    # Calcular las dimensiones de las celdas en la matriz del nivel
    num1 = (alto - 50) // 32
    num2 = ancho // 30
    # Verificar si la posición de Pacman está dentro de los límites laterales
    if 0 < pos_x < 1280:
        # Verificar si Pacman ha alcanzado un punto blanco (valor 1) en la matriz del nivel
        if level[center_y // num1][center_x // num2] == 1:
            # Actualizar la posición en la matriz del nivel a un valor diferente (por ejemplo, 4) para indicar que el punto ha sido comido
            level[center_y // num1][center_x // num2] = 4
            # Incrementar la puntuación
            scor += 10
        if level[center_y // num1][center_x // num2] == 2:# Verificar si Pacman ha alcanzado una cápsula de poder (valor 2) en la matriz del nivel
            level[center_y // num1][center_x // num2] = 4  # Actualizar la posición en la matriz del nivel a un valor diferente (por ejemplo, 4) para indicar que la cápsula ha sido comido
            # Incrementar la puntuación
            scor += 50
             # Activar el poder temporal de comer fantasmas
            power = True
            # Reiniciar el contador del poder
            power_contador = 0
            # Restablecer el estado de los fantasmas comidos
            come_fantasmas = [False, False, False, False]
    return scor, power, power_contador, come_fantasmas # Devolver los valores actualizados


def dibujar_mapa():
    num1 = ((alto - 50) // 32)
    num2 = (ancho // 30)
    for i in range (len(level)): # Es para interactuar con cada fila de la matriz
        for j in range (len(level[i])):
            if level[i][j] == 1:
                #En esta parte se dibuja en la matriz los puntos blancos que come pacman definiendo color, posicion y tamaño
                pygame.draw.circle(pantalla_de_juego, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 0:
                # Esto dibuja un rectangulo azul en el valor 0, definido por los limites num1 y num2 
                pygame.draw.rect(pantalla_de_juego, 'blue', pygame.Rect(j * num2, i * num1, num2, num1))    
            if level[i][j] == 2 and not destellos:
                #En esta parte se dibuja en la matriz los puntos blancos que le dan velocidad (capsulas de poder)
                pygame.draw.circle(pantalla_de_juego, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 5)
            if level[i][j] == 3:
                #En esta parte se dibuja en la matriz las frutas 
                pygame.draw.circle(pantalla_de_juego, 'red', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 5)
            if level[i][j] == 4:
                #En esta parte se dibuja en la matriz las frutas 
                pygame.draw.circle(pantalla_de_juego, 'black', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 5)


def dibuja_jugador():
    #Movimiento de mi personaje principal
    # 0 = derecha, 1 = izquierda, 2= arriba, 3= abajo
    if direccion == 0:
        pantalla_de_juego.blit(imagenes_jugador_principal[contador // 10], (pos_x, pos_y))
    elif direccion == 1:
        pantalla_de_juego.blit(pygame.transform.flip(imagenes_jugador_principal[contador // 10], True, False), (pos_x, pos_y))
    elif direccion == 2:
        pantalla_de_juego.blit(pygame.transform.rotate(imagenes_jugador_principal[contador // 10], 90), (pos_x, pos_y))
    elif direccion == 3:
        pantalla_de_juego.blit(pygame.transform.rotate(imagenes_jugador_principal[contador // 10], 270), (pos_x, pos_y))


def revisar_posiciones(centrox, centroy):
    giros = [False, False, False, False]
    num1 = (alto - 50) // 32
    num2 = (ancho // 30)
    row = centroy // num1
    col = centrox // num2
    

    if 0 <= row < len(level) and 0 <= col < len(level[row]):
        # Verificar giros basados en las casillas adyacentes
        if level[row][col] != 0:
            giros[0] = True  # Puede moverse a la derecha
        if level[row][col - 1] != 0:
            giros[1] = True  # Puede moverse a la izquierda
        if level[row - 1][col] != 0:
            giros[2] = True  # Puede moverse hacia arriba
        if level[row + 1][col] != 0:
            giros[3] = True  # Puede moverse hacia abajo

    return giros



def move_player(play_x, play_y):
# Mover al jugador en la dirección actual si la siguiente casilla en esa dirección está permitida
    if direccion == 0 and turns_allowed[0]:
        play_x += jugador_velocidad
    elif direccion == 1 and turns_allowed[1]:
        play_x -= jugador_velocidad
    if direccion == 2 and turns_allowed[2]:
        play_y -= jugador_velocidad
    elif direccion == 3 and turns_allowed[3]:
        play_y += jugador_velocidad
        # Devolver las nuevas coordenadas del jugador
    return play_x, play_y





run = True
while run:
    timepo.tick(fps) # Controla la velocidad del bucle principal del juego.
    if contador < 19: # Controla la animación de destellos del jugador
        contador += 1
        if contador > 3:
            destellos = False
    else:
        contador = 0
        destellos = True
    if powerup and power_contador < 600: # Controla la duración del poder especial(come fantasmas) y su reinicio
        power_contador += 1
    elif powerup and power_contador >= 600:
        power_contador = 0
        powerup = False
        come_fantasmas = [False, False, False, False]
    if startup_counter < 180 and not game_over and not gana_juego: # Controla el inicio del juego y la animación inicial
        moving = False
        startup_counter += 1
    else:
        moving = True

    pantalla_de_juego.fill('black') # Llena la pantalla con un color negro.
    dibujar_mapa() # Dibuja el mapa del juego.
    center_x = pos_x + 10
    center_y = pos_y + 10
    if powerup:
        fantasmas_velocidad = [1, 1, 1, 1] # Velocidades de los fantasmas durante el poder especial
    else:
        fantasmas_velocidad = [2, 2, 2, 2] # Velocidades normales de los fantasmas.
    if come_fantasmas[0]:
        fantasmas_velocidad[0] = 2 # Velocidad del fantasma rojo cuando es comido.
    if come_fantasmas[1]:
        fantasmas_velocidad[1] = 2 # Velocidad del fantasma azul cuando es comido.
    if come_fantasmas[2]:
        fantasmas_velocidad[2] = 2 # Velocidad del fantasma rosa cuando es comido.
    if come_fantasmas[3]:
        fantasmas_velocidad[3] = 2 # Velocidad del fantasma naranja cuando es comido.
    if rojo_muerto:
        fantasmas_velocidad[0] = 4 # Velocidad del fantasma rojo cuando está muerto.
    if azul_muerto:
        fantasmas_velocidad[1] = 4 # Velocidad del fantasma azul cuando está muerto.
    if rosa_muerto:
        fantasmas_velocidad[2] = 4 # Velocidad del fantasma rosa cuando está muerto.
    if naranja_muerto:
        fantasmas_velocidad[3] = 4 # Velocidad del fantasma naranja cuando está muerto.

    gana_juego = True # Ciclo for para ganar
    for i in range(len(level)):
        if 1 in level[i] or 2 in level[i]:
            gana_juego = False
    # Dibuja el círculo del jugador en pantalla, este se utiliza para simplifacr aspectos como las colisiones
    player_circle = pygame.draw.circle(pantalla_de_juego, 'black', (center_x, center_y), 10, 1)
    dibuja_jugador() # Dibuja al jugador en pantalla.
    #Inicializa a los fantasmas con sus respectivas posiciones, velocidades y estados.
    rojo = Ghost(rojo_x, rojo_y, targets[0], fantasmas_velocidad[0], rojo_img, rojo_direccion, rojo_muerto,
                   blinky_box, 0)
    azul = Ghost(azul_x, azul_y, targets[1], fantasmas_velocidad[1], azul_img, azul_direccion, azul_muerto,
                 inky_box, 1)
    rosa = Ghost(rosa_x, rosa_y, targets[2], fantasmas_velocidad[2], rosa_img, rosa_direccion, rosa_muerto,
                  pinky_box, 2)
    naranja = Ghost(naranja_x, naranja_y, targets[3], fantasmas_velocidad[3], naranja_img, naranja_direccion, naranja_muerto,
                  clyde_box, 3)
    draw_misc() #Dbuja funcion de los cuadros emergentes y el puntaje, esta se define arriba en el código
    #targets = get_targets(rojo_x, rojo_y, azul_x, azul_y, rosa_x, rosa_y, naranja_x, naranja_y)

    turns_allowed = revisar_posiciones(center_x, center_y)
    if moving:# Verifica las direcciones permitidas para el jugador basándose en la posición central del jugador.
        pos_x, pos_y = move_player(pos_x, pos_y)
        if not rojo_muerto and not rojo.in_box:
            rojo_x, rojo_y, rojo_direccion = rojo.move_rojo()
        else:
            rojo_x, rojo_y, rojo_direccion = rojo.move_naranja()
        if not rosa_muerto and not rosa.in_box:
            rosa_x, rosa_y, rosa_direccion = rosa.move_rosa()
        else:
            pinky_x, pinky_y, pinky_direction = rosa.move_naranja()
        if not azul_muerto and not azul.in_box:
            azul_x, azul_y, azul_direccion = azul.move_azul()
        else:
            azul_x, azul_y, azul_direccion = azul.move_naranja()
        naranja_x, naranja_y, naranja_direccion = naranja.move_naranja()
    #Verifica colisiones del jugador y actualiza el puntaje, el estado de la "powerup" y el estado de los fantasmas comidos.    
    score, powerup, power_contador, come_fantasmas = revisar_collisions(score, powerup, power_contador, come_fantasmas)
    if not powerup:# Verifica colisiones del jugador con fantasmas y actualiza el estado del juego y puntaje en consecuencia.
        if (player_circle.colliderect(rojo.rect) and not rojo.muerto) or \
                (player_circle.colliderect(azul.rect) and not azul.muerto) or \
                (player_circle.colliderect(rosa.rect) and not rosa.muerto) or \
                (player_circle.colliderect(naranja.rect) and not naranja.muerto):
            if lives > 0: # Reduce el número de vidas y reinicia la posición del jugador y fantasmas.
                lives -= 1
                startup_counter = 0
                powerup = False
                power_contador = 0
                pos_x = 200 # Reinicia la posición del jugador y los fantasmas
                pos_y = 180
                direccion = 0
                direccion_command = 0
                rojo_x = 900
                rojo_y = 350
                rojo_direccion = 0
                azul_x = 800
                azul_y = 350
                azul_direccion = 2
                rosa_x = 850
                rosa_y = 350
                rosa_direccion = 2
                naranja_x = 700
                naranja_y = 350
                naranja_direccion = 2
                come_fantasmas = [False, False, False, False]
                rojo_muerto = False
                azul_muerto = False
                naranja_muerto = False
                rosa_muerto = False
            else:# Si no hay vidas restantes, marca el juego como terminado.
                game_over = True
                moving = False
                startup_counter = 0
    if powerup and player_circle.colliderect(rojo.rect) and come_fantasmas[0] and not rojo.muerto:# Verifica si el jugador tiene un powerup activo, ha colisionado con un fantasma rojo y el rojo no está muerto.
        if lives > 0: # Verifica si hay vidas restantes para el jugador.
            powerup = False # Desactiva el powerup, reduce el contador, y disminuye las vidas.
            power_contador = 0
            lives -= 1 
            startup_counter = 0
            pos_x = 200 # Reinicia la posición del jugador y los fantasmas.
            pos_y = 180
            direccion = 0
            direccion_command = 0
            rojo_x = 900
            rojo_y = 350
            rojo_direccion = 0
            azul_x = 800
            azul_y = 350
            azul_direccion = 2
            rosa_x = 850
            rosa_y = 350
            rosa_direccion = 2
            naranja_x = 700
            naranja_y = 350
            naranja_direccion = 2
            come_fantasmas = [False, False, False, False]# Reinicia el estado de los fantasmas.
            rojo_muerto = False
            azul_muerto = False
            naranja_muerto = False
            rosa_muerto = False
        else:
            game_over = True # Si no hay vidas restantes, marca el juego como terminado.
            moving = False
            startup_counter = 0
    if powerup and player_circle.colliderect(azul.rect) and come_fantasmas[1] and not azul.muerto:# Verifica si el jugador tiene un powerup activo, ha colisionado con un fantasma azul y el azul no está muerto.
        if lives > 0:
            powerup = False# Desactiva el powerup, reduce el contador, y disminuye las vidas.
            power_contador = 0
            lives -= 1
            startup_counter = 0 # Reinicia la posición del jugador y los fantasmas.
            pos_x = 200
            pos_y = 180
            direccion = 0
            direccion_command = 0
            rojo_x = 900
            rojo_y = 350
            rojo_direccion = 0
            azul_x = 800
            azul_y = 350
            azul_direccion = 2
            rosa_x = 850
            rosa_y = 350
            rosa_direccion = 2
            naranja_x = 700
            naranja_y = 350
            naranja_direccion = 2
            come_fantasmas = [False, False, False, False]# Reinicia el estado de los fantasmas.
            rojo_muerto = False
            azul_muerto = False
            naranja_muerto = False
            rosa_muerto = False
        else:# Si no hay vidas restantes, marca el juego como terminado.
            game_over = True
            moving = False
            startup_counter = 0
    if powerup and player_circle.colliderect(rosa.rect) and come_fantasmas[2] and not rosa.muerto:# Verifica si el jugador tiene un powerup activo, ha colisionado con un fantasma rosa y el rosa no está muerto.
        if lives > 0:# Verifica si hay vidas restantes para el jugador.
            powerup = False # Desactiva el powerup, reduce el contador, y disminuye las vidas.
            power_contador = 0
            lives -= 1
            startup_counter = 0
            pos_x = 200# Reinicia la posición del jugador y los fantasmas
            pos_y = 180
            direccion = 0
            direccion_command = 0
            rojo_x = 900
            rojo_y = 350
            rojo_direccion = 0
            azul_x = 800
            azul_y = 350
            azul_direccion = 2
            rosa_x = 850
            rosa_y = 350
            rosa_direccion = 2
            naranja_x = 800
            naranja_y = 350
            naranja_direccion = 2
            come_fantasmas = [False, False, False, False]# Reinicia el estado de los fantasmas.
            rojo_muerto = False
            azul_muerto = False
            naranja_muerto = False
            rosa_muerto = False
        else:# Si no hay vidas restantes, marca el juego como terminado.
            game_over = True
            moving = False
            startup_counter = 0
    if powerup and player_circle.colliderect(naranja.rect) and come_fantasmas[3] and not naranja.muerto:# Verifica si el jugador tiene un powerup activo, ha colisionado con un fantasma naranja y el naranja no está muerto.
        if lives > 0:
            powerup = False# Desactiva el powerup, reduce el contador, y disminuye las vidas.
            power_contador = 0
            lives -= 1
            startup_counter = 0
            pos_x = 200 # Reinicia la posición del jugador y los fantasmas.
            pos_y = 180
            direccion = 0
            direccion_command = 0
            rojo_x = 900
            rojo_y = 350
            rojo_direccion = 0
            azul_x = 800
            azul_y = 350
            azul_direccion = 2
            rosa_x = 850
            rosa_y = 350
            rosa_direccion = 2
            naranja_x = 700
            naranja_y = 350
            naranja_direccion = 2
            come_fantasmas = [False, False, False, False]# Reinicia el estado de los fantasmas.
            rojo_muerto = False
            azul_muerto = False
            naranja_muerto = False
            rosa_muerto = False
        else:# Si no hay vidas restantes, marca el juego como terminado.
            game_over = True
            moving = False
            startup_counter = 0
    if powerup and player_circle.colliderect(rojo.rect) and not rojo.muerto and not come_fantasmas[0]:# Verifica si el jugador tiene un powerup activo y ha colisionado con un fantasma rojo que aún no ha sido comido.
        rojo_muerto = True # Marca al fantasma rojo como muerto y comido, actualiza el puntaje según el número total de fantasmas comidos.
        come_fantasmas[0] = True
        score += (2 ** come_fantasmas.count(True)) * 100
    if powerup and player_circle.colliderect(azul.rect) and not azul.muerto and not come_fantasmas[1]:# Lo mismo pero para el fantasma azul
        azul_muerto = True
        come_fantasmas[1] = True
        score += (2 ** come_fantasmas.count(True)) * 100
    if powerup and player_circle.colliderect(rosa.rect) and not rosa.muerto and not come_fantasmas[2]:# Lo mismo pero para el fantasma rosa
        rosa_muerto = True
        come_fantasmas[2] = True
        score += (2 ** come_fantasmas.count(True)) * 100
    if powerup and player_circle.colliderect(naranja.rect) and not naranja.muerto and not come_fantasmas[3]:# Lo mismo pero para el fantasma naranja
        naranja_muerto = True
        come_fantasmas[3] = True
        score += (2 ** come_fantasmas.count(True)) * 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # Verifica si se ha cerrado la ventana
            run = False
        if event.type == pygame.KEYDOWN: # Verifica teclas presionadas
            if event.key == pygame.K_RIGHT:# Cambia la dirección del jugador basado en la tecla presionada
                direccion_command = 0
            if event.key == pygame.K_LEFT:
                direccion_command = 1
            if event.key == pygame.K_UP:
                direccion_command = 2
            if event.key == pygame.K_DOWN:
                direccion_command = 3
            if event.key == pygame.K_SPACE and (game_over or gana_juego):# Si se presiona la tecla espaciadora y el juego ha terminado (ya sea por pérdida o victoria), reinicia el juego.
                powerup = False # Reinicia las variables del juego
                power_contador = 0
                lives -= 1
                startup_counter = 0
                pos_x = 200
                pos_y = 180
                direccion = 0
                direccion_command = 0
                rojo_x = 900
                rojo_y = 350
                rojo_direccion = 0
                azul_x = 800
                azul_y = 350
                azul_direccion = 2
                rosa_x = 850
                rosa_y = 350
                rosa_direccion = 2
                naranja_x = 700
                naranja_y = 350
                naranja_direccion = 2
                come_fantasmas = [False, False, False, False]
                rojo_muerto = False
                azul_muerto = False
                naranja_muerto = False
                rosa_muerto = False
                score = 0
                lives = 3
                game_over = False
                gana_juego = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direccion_command == 0:
                direccion_command = direccion
            if event.key == pygame.K_LEFT and direccion_command == 1:
                direccion_command = direccion
            if event.key == pygame.K_UP and direccion_command == 2:
                direccion_command = direccion
            if event.key == pygame.K_DOWN and direccion_command == 3:
                direccion_command = direccion

    if direccion_command == 0 and turns_allowed[0]:# Verifica y actualiza la dirección del jugador basado en la dirección solicitada y si la dirección solicitada es permitida.
        direccion = 0
    if direccion_command == 1 and turns_allowed[1]:
        direccion = 1
    if direccion_command == 2 and turns_allowed[2]:
        direccion = 2
    if direccion_command == 3 and turns_allowed[3]:
        direccion = 3

    if rojo.in_box and rojo_muerto:# Verifica y ajusta el estado de los fantasmas después de salir de la caja de inicio.
        rojo_muerto = False
    if azul.in_box and azul_muerto:
        azul_muerto = False
    if rosa.in_box and rosa_muerto:
        rosa_muerto = False
    if naranja.in_box and naranja_muerto:
        naranja_muerto= False
    
    pygame.display.flip()
pygame.quit()
