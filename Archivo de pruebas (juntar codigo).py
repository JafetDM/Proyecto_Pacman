#Proyecto Pacman

import pygame, sys, math
from Matriz import matriz
import random

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
ancho = 1280
largo = 720
ventana = pygame.display.set_mode([ancho, largo]) #ventana
superficie = pygame.Surface((ancho, largo), pygame.SRCALPHA)
pygame.display.set_caption("Pac-Man") # Título
fondo= pygame.image.load("fondo_negro.png")
tiempo = pygame.time.Clock()
fps = 60
pause = False

#imagenes
jose_foto = pygame.image.load("jose_foto.jpg")
jafet_foto = pygame.image.load("jafet_foto.png")

#IMAGENES PARA EL JUEGO

imagenes_jugador_principal = []
for i in range(1, 3):  # Toma dos imagenes, se reeedimensionan y esto crea la ilusion de movimiento en mi personaje
    imagenes_jugador_principal.append(pygame.transform.scale(pygame.image.load(
        f"C:\\Users\\emora\\OneDrive - Estudiantes ITCR\\Documentos\\GitHub\\Proyecto_Pacman\\pacman_imagenes\\{i}.jpg"),
                                            (10, 10)))

rojo_img = pygame.transform.scale(pygame.image.load("rojo.jpg"),(20, 20))

rosa_img = pygame.transform.scale(pygame.image.load("rosa.jpg"), (20,20))

azul_img = pygame.transform.scale(pygame.image.load("azul.jpg"), (20,20))

naranja_img = pygame.transform.scale(pygame.image.load("naranja.jpg"), (20,20))

mi_fuente = pygame.font.SysFont("Pacifico", 36)
font = pygame.font.Font('freesansbold.ttf', 20)


pos_x = 200 #Posiciones donde va a inicar pacman
pos_y = 180
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

#fuente
def get_font(size): #obtener la fuente de letra
    return pygame.font.SysFont("Impact", size)

def mostrar_texto(ventana, fuente, texto, color,  x, y):
    superficie = fuente.render(texto, True, color)
    rectangulo = superficie.get_rect(center=(x, y))
    ventana.blit(superficie, rectangulo)

#variable donde almacenar puntajes
puntajes=[]

#  MANEJO DE ARCHIVOS DE TEXTO

#función para ordenar números
def ordenar(numeros):
    n = len(numeros)

#Uso del método burbuja para el ordenamiento

    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if numeros[j] < numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    return numeros

# Lee los números desde el archivo de texto
with open("puntajes_pacman.txt", "r") as archivo:
    lineas = archivo.readlines()

# Convierte las cadenas de texto a números y los almacena en una lista
numeros = [int(linea.strip()) for linea in lineas]

# Ordena la lista de mayor a menor
ordenar(numeros)

# Escribe los números ordenados de nuevo en el archivo
with open("puntajes_pacman.txt", "w") as archivo:
    for numero in numeros:
        archivo.write(f"{numero}\n") #reescribe el archivo
        puntajes.append(numero) #añade los numeros a la lista a mostrar en el hall of fame

    contenido_actualizado = str(puntajes)

#clase boton para la interfaz
class Button():
    #iniciar atributos
    def __init__(self, imagen, pos, text_input, font, color_base, hovering_color):
        self.imagen = imagen
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.color_base, self.hovering_color = color_base, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.color_base)
        if self.imagen is None:
            self.imagen = self.text
        self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    #metodo para actualizar el boton y ponerlo en la ventana
    def update(self, ventana):
        if self.imagen is not None:
            ventana.blit(self.imagen, self.rect)
        ventana.blit(self.text, self.text_rect)

    #metodo para determinar si lo estamos clickeando
    def checkForInput(self, posicion):
        if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range (self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, posicion):
        if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.color_base)

# -----------------------------------Clase Juego---------------------------
class Juego():
    # Atributos: 1) Número de juego,
    # 2) tablero (matriz 40x36) sus valores son
    # 0: pared horizontal, 1: puntos, 2: cápsula de poder,3: frutas, 4: espacio vacío, 5: puerta fantasma, 6: pared vertical
    # 3) nivel (1 y 2)
    # 4) score

    def __init__(self, num_juego, nivel):
        self.num_juego = num_juego #consecutivo del juego, cada que termina se actualiza
        self.tablero = matriz #será una matriz 40x36, se actualiza en tiempo real. Proviene de Matriz.py
        self.nivel = nivel #de 1 a 2, inicia en 1
        self.score = 0 #inicia en 0, esquema de puntos definido por alimento (puntos y fruta) y fantasmas comidos

    # Métodos: iniciar juego, get_xx necesarios
    def iniciar(self):
        num1 = (largo-25) // 36
        num2 = (ancho - 560) // 40
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if self.tablero[i][j] == 0:
                    pygame.draw.rect(ventana, azul, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), 18,
                                                     20))  # dibuja el rectangulo, (posición x, posición y, largo, ancho)
                if self.tablero[i][j] == 1:
                    pygame.draw.circle(ventana, blanco, (j * num2 + (num2), i * num1 + (num1)),
                                       1)  # dibuja círculos, (coordenadas del centro del círculo, radio
                if self.tablero[i][j] == 2 and not pacman.get_destellos():
                    pygame.draw.circle(ventana, blanco, (j * num2 + (num2), i * num1 + (num1)), 5)
                if self.tablero[i][j] == 3:
                    pygame.draw.circle(ventana, rojo, (j * num2 + (num2), i * num1 + (num1)), 4)

                if self.tablero[i][j] == 5: #dibuja una linea que sirve como la puerta para los fantasmas, posicion inicial y final y width
                    pygame.draw.line(ventana, blanco, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                     (j * num2 + (0.5 * num2) + 18, i * num1 + (0.5 * num1)), 4)
    def get_score(self): #retorna score
        return (self.score)

    def get_matriz(self): #retorna la matriz
        return self.tablero

#instancias de juego
niv1 = Juego(1, 1)
niv2 = Juego(1, 2)

#-------------------------------Clase Pacman-----------------

class Pacman():

    # Atributos
    # Estado: indica si PacMan está vivo o muerto.
    # Posición x: fila de la matriz en que se encuentra PacMan.
    # Posición y: columna de la matriz en que se encuentra PacMan.
    # Velocidad: indicador de velocidad de PacMan (1 Normal, 2 Rápido)
    # Dirección: indica hacia donde mira pacman
    def __init__(self):
        self.estado = True
        self.pos_x= ((1280-560) //40) *30
        self.pos_y= (((720-25) //36) *31)
        self.pacman_velocidad= 1
        self.direccion = 0
        self.contador = 0
        self.destellos = False
        self.giros_p = [False, False, False, False]
        self.direccion_commando = 0
        self.num1 = ((largo - 20) // 36)
        self.num2 = (ancho - 560) // 40
        self.rect = pygame.Rect((self.pos_x)-10, (self.pos_y)-10, 10, 10)
        self.giros = [False, False, False, False]
        self.row = self.rect.centery // self.num1
        self.col = self.rect.centerx // self.num2
        global pause

    def direccion_personaje(self):
        # Dirección a la que debe mirar mi personaje principal
        # 0 = derecha, 1 = izquierda, 2= arriba, 3= abajo
        if self.direccion == 0:
            ventana.blit(imagenes_jugador_principal[self.contador // 10], (self.pos_x, self.pos_y))
        if self.direccion == 1:
            ventana.blit(pygame.transform.flip(imagenes_jugador_principal[self.contador // 10], True, False),
                                   (self.pos_x, self.pos_y))
        if self.direccion == 2:
            ventana.blit(pygame.transform.rotate(imagenes_jugador_principal[self.contador // 10], 90),
                                   (self.pos_x, self.pos_y))
        if self.direccion == 3:
            ventana.blit(pygame.transform.rotate(imagenes_jugador_principal[self.contador // 10], 270),
                                   (self.pos_x, self.pos_y))

    def revisar_posicion(self):
        self.giros = [False, False, False, False]

        if 0 <= self.row < len(niv1.get_matriz()) and 0 <= self.col < len(niv1.get_matriz()[self.row]):
            # Verificar giros basados en las casillas adyacentes
            if niv1.get_matriz()[self.row][self.col] != 0:
                self.giros[0] = True  # Puede moverse a la derecha
            if niv1.get_matriz()[self.row][self.col - 1] != 0:
                self.giros[1] = True  # Puede moverse a la izquierda
            if niv1.get_matriz()[self.row - 1][self.col] != 0:
                self.giros[2] = True  # Puede moverse hacia arriba
            if niv1.get_matriz()[self.row + 1][self.col] != 0:
                self.giros[3] = True  # Puede moverse hacia abajo

        return self.giros

    def obtener_pos(self):
        nueva_pos_x = self.rect.x
        nueva_pos_y = self.rect.y

        if self.direccion == 0 and self.giros_p[0]:
            nueva_pos_x += self.pacman_velocidad
        elif self.direccion == 1 and self.giros_p[1]:
            nueva_pos_x -= self.pacman_velocidad
        if self.direccion == 2 and self.giros_p[2]:
            nueva_pos_y -= self.pacman_velocidad
        elif self.direccion == 3 and self.giros_p[3]:
            nueva_pos_y += self.pacman_velocidad

        # Verificar si la nueva posición colisiona con las paredes
        rect_futuro = pygame.Rect(nueva_pos_x, nueva_pos_y, 10, 10)
        if not self.colisiona_pared(rect_futuro):
            self.rect.x = nueva_pos_x
            self.rect.y = nueva_pos_y

        return self.rect.x, self.rect.y

    def colisiona_pared(self, rect_futuro):
        for i in range(len(niv1.get_matriz())):
            for j in range(len(niv1.get_matriz()[i])):
                if niv1.get_matriz()[i][j] == 0:
                    pared = pygame.Rect(j * self.num2, i * self.num1, self.num2, self.num1)
                    if rect_futuro.colliderect(pared):
                        return True
        return False

    def get_destellos(self):
        return self.destellos

    def get_estado(self):
        return self.estado

    def revisar_puntos(self):
        score1= niv1.get_score()

        if 0 <= self.row < len(niv1.get_matriz()) and 0 <= self.col < len(niv1.get_matriz()[self.row]):
            if niv1.get_matriz()[self.row][self.col] == 2:
                niv1.get_matriz()[self.row][self.col] = 4
                score1 += 10
            elif niv1.get_matriz()[self.row][self.col] == 3:
                niv1.get_matriz()[self.row][self.col] = 4

        return score1

    # Para que la ventana del juego se mantenga abierta
    def mover_pacman(self):
        global pause
        while self.estado:  # Aquí se aplica el loop para mantener la ventana abierta a ciertos fps
            tiempo.tick(fps)
            if pause:
                menu_pausa()

            ventana.fill(negro)
            niv1.iniciar()
            pacman.revisar_puntos()

            if self.contador < 19:  # Esto es simplemente para aplicar la ilusion del movimiento de la boca de pacman, utilizando el contador
                self.contador += 1
                if self.contador > 3:
                    self.destellos = False
            else:
                self.contador = 0
                self.destellos = True  # Esto hara que la bolita grande titile o destelle 3 veces por 1 segundo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.estado = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if pause:
                            pause = False
                        else:
                            pause = True
                    # Esto es para que el personaje PACMAN cambie de dirección respecto a las teclas
                    if not pause:
                        if event.key == pygame.K_RIGHT:
                            self.direccion_commando = 0
                        if event.key == pygame.K_LEFT:
                            self.direccion_commando = 1
                        if event.key == pygame.K_UP:
                            self.direccion_commando = 2
                        if event.key == pygame.K_DOWN:
                            self.direccion_commando = 3

            # Mover pacman después de verificar las colisiones
            if not pause and (0 < self.pos_x <720) and (0 < self.pos_y <695):
                self.pos_x, self.pos_y = pacman.obtener_pos()
                self.giros_p = pacman.revisar_posicion()

            for i in range(4):
                if self.direccion_commando == i and self.giros_p[i]:
                    self.direccion = i
            #self.pos_x, self.pos_y =
            #self.giros_p =
            pacman.direccion_personaje()
            # Esto me permite mostrar una y otra vez en la pantalla de juego lo creado en el loop y támbien las interacciones en la misma.
            pygame.display.flip()
        pygame.quit()

#instancia de pacman:

pacman= Pacman()

# ----------------------------------Clase Fantasma -----------------------------------------

class Ghost():  # Estas son las caracteristicas que comparten los fantasmas;
    # x_coord y y_coord son las coordenadas de los fantasmas, objetivo es a quien buscan, img sus imagenes
    # direcc su direccion, box es para saber si se encuentran en la parte de la caja, id es para identificar a cada fantasma por separado
    def __init__(self, x_coord, y_coord, objetivo, velocidad, img, direcc, muerto, box, id, x_pos, y_pos, max_pasos):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 10  # Para ajustar el centro de la imagen
        self.center_y = self.y_pos + 10
        self.objetivo = objetivo
        self.velocidad = velocidad
        self.img = img
        self.direccion = direcc
        self.muerto = muerto
        self.in_box = box
        self.id = id
        self.rect = self.dibuja()  # Hitbox de los fantasmas para revisar en colisiones
        self.turns = [False, False, False, False]
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.max_pasos = max_pasos
        self.contador_pasos = 0
        self.direccion_actual = random.choice([0, 1, 2, 3])

    def dibuja(self):  # Condiciones de los estados de los fantasmas
        # Fantasmas en su estado normal
        if (not powerup and not self.muerto) or (come_fantasmas[self.id] and powerup and not self.muerto):
            ventana.blit(self.img, (self.x_pos, self.y_pos))
        # Fantasmas en estado asustado sino esta muertos
        elif powerup and not self.muerto and not come_fantasmas[self.id]:
            ventana.blit(asustado_img, (self.x_pos, self.y_pos))
        # Fantasmas muertos
        else:
            ventana.blit(muerto_img, (self.x_pos, self.y_pos))
        fantasma_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (
        36, 36))  # hitbox para colisiones con los fantasmas, es un simple rectangulo para verificar las colisiones
        return fantasma_rect

    def revisar_colisiones(self, x_coord, y_coord):
        # Verificar si la posición siguiente está dentro de los límites de la matriz
        if 0 <= x_coord < len(niv1.get_matriz()[0]) and 0 <= y_coord < len(niv1.get_matriz()):
            # Verificar si el próximo movimiento es permitido (casillas diferentes de 0)
            if niv1.get_matriz()[y_coord][x_coord] != 0:
                return True
        return False

    def move_naranja(self):
        global naranja_direccion

        if self.contador_pasos < 20:
            # Mover en la dirección actual
            self.contador_pasos += 1
            nueva_x, nueva_y = self.x_pos, self.y_pos

            if self.direccion_actual == 0:  # Mover hacia arriba
                nueva_y -= 1
            elif self.direccion_actual == 1:  # Mover hacia abajo
                nueva_y += 1
            elif self.direccion_actual == 2:  # Mover hacia la izquierda
                nueva_x -= 1
            elif self.direccion_actual == 3:  # Mover hacia la derecha
                nueva_x += 1

            # Verificar si las nuevas coordenadas son válidas (no colisionan con obstáculos)
            if not self.revisar_colisiones(nueva_x, nueva_y):
                self.x_pos, self.y_pos = nueva_x, nueva_y
        else:
            # Cambiar de dirección después de 20 pasos
            self.contador_pasos = 0
            posibles_direcciones = [0, 1, 2, 3]
            posibles_direcciones.remove(self.direccion_actual)
            nueva_direccion = random.choice(posibles_direcciones)

            # Calcular las nuevas coordenadas según la nueva dirección
            nueva_x, nueva_y = self.x_pos, self.y_pos

            if nueva_direccion == 0:  # Mover hacia arriba
                nueva_y -= 1
            elif nueva_direccion == 1:  # Mover hacia abajo
                nueva_y += 1
            elif nueva_direccion == 2:  # Mover hacia la izquierda
                nueva_x -= 1
            elif nueva_direccion == 3:  # Mover hacia la derecha
                nueva_x += 1

            # Verificar si las nuevas coordenadas son válidas (no colisionan con obstáculos)
            if not self.revisar_colisiones(nueva_x, nueva_y):
                self.x_pos, self.y_pos = nueva_x, nueva_y
                self.direccion_actual = nueva_direccion

        return self.x_pos, self.y_pos

    # def move_rojo(self):

    # def move_azul(self):

    # def move_rosa(self):


def draw_misc():
    global gana_juego
    score_text = font.render(f'Puntaje: {score}', True, 'white')  # Texto de puntaje
    ventana.blit(score_text, (10, 920))
    if powerup:  # Dibuja el indicador de la potencia si está activo
        pygame.draw.circle(ventana, 'blue', (140, 930), 15)
    for i in range(lives):  # Dibuja los íconos de vidas
        ventana.blit(pygame.transform.scale(imagenes_jugador_principal[0], (30, 30)), (650 + i * 40, 915))
    if game_over:  # Dibuja la pantalla de Game Over si es necesario
        pygame.draw.rect(ventana, 'white', [50, 200, 800, 300], 0, 10)
        pygame.draw.rect(ventana, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('Fin del juego! Barra espaciadora para reiniciar!', True, 'red')
        ventana.blit(gameover_text, (100, 300))

    if gana_juego:  # Dibuja la pantalla de Victoria si es necesario
        pygame.draw.rect(ventana, 'white', [50, 200, 800, 300], 0, 10)
        pygame.draw.rect(ventana, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('Ganaste! Barra espaciadora para reiniciar!', True, 'green')
        ventana.blit(gameover_text, (100, 300))


    center_x = pos_x + 10
    center_y = pos_y + 10

    if powerup:
        fantasmas_velocidad = [1, 1, 1, 1]  # Velocidades de los fantasmas durante el poder especial
    else:
        fantasmas_velocidad = [2, 2, 2, 2]  # Velocidades normales de los fantasmas.
    if come_fantasmas[0]:
        fantasmas_velocidad[0] = 2  # Velocidad del fantasma rojo cuando es comido.
    if come_fantasmas[1]:
        fantasmas_velocidad[1] = 2  # Velocidad del fantasma azul cuando es comido.
    if come_fantasmas[2]:
        fantasmas_velocidad[2] = 2  # Velocidad del fantasma rosa cuando es comido.
    if come_fantasmas[3]:
        fantasmas_velocidad[3] = 2  # Velocidad del fantasma naranja cuando es comido.
    if rojo_muerto:
        fantasmas_velocidad[0] = 4  # Velocidad del fantasma rojo cuando está muerto.
    if azul_muerto:
        fantasmas_velocidad[1] = 4  # Velocidad del fantasma azul cuando está muerto.
    if rosa_muerto:
        fantasmas_velocidad[2] = 4  # Velocidad del fantasma rosa cuando está muerto.
    if naranja_muerto:
        fantasmas_velocidad[3] = 4  # Velocidad del fantasma naranja cuando está muerto.

    gana_juego = True  # Ciclo for para ganar
    for i in range(len(niv1.get_matriz())):
        if 1 in niv1.get_matriz()[i] or 2 in niv1.get_matriz()[i]:
            gana_juego = False


# INSTANCIAS FANTASMAS


rojo = Ghost(rojo_x, rojo_y, targets[0], fantasmas_velocidad[0], rojo_img, rojo_direccion, rojo_muerto,
                 blinky_box, 0)

azul = Ghost(azul_x, azul_y, targets[1], fantasmas_velocidad[1], azul_img, azul_direccion, azul_muerto,
                 inky_box, 1)

rosita = Ghost(rosa_x, rosa_y, targets[2], fantasmas_velocidad[2], rosa_img, rosa_direccion, rosa_muerto,
                 pinky_box, 2)

naranja = Ghost(naranja_x, naranja_y, targets[3], fantasmas_velocidad[3], naranja_img, naranja_direccion,
                    naranja_muerto,
                    clyde_box, 3)


# ......................... VENTANAS -------------

def jugar():
    pygame.display.set_caption("Juego") #ventana del juego

    #poner música
    pygame.mixer.init()
    pygame.mixer.music.load("01. Game Start.mp3")
    pygame.mixer.music.play()

    while True:

        ventana.fill(negro)
        niv1.iniciar()
        pacman.mover_pacman()
        # Inicializa a los fantasmas con sus respectivas posiciones, velocidades y estados.

        rojo.dibuja()

        azul.dibuja()

        rosita.dibuja()

        naranja.dibuja()
        mostrar_texto(ventana, get_font(45), str(niv1.get_score()), blanco, 1000, 110)

        jugar_text= get_font(45).render("Puntaje", True, rosado)
        jugar_rect = jugar_text.get_rect(center= (1000, 50))
        ventana.blit(jugar_text, jugar_rect)


        pygame.display.update()

def ayuda():
    pygame.display.set_caption("Ayuda") #ventana del juego

    while True:

        ayuda_mouse_pos = pygame.mouse.get_pos()

        ventana.fill(negro)
#titulo
        ayuda_text= get_font(75).render("Pantalla de ayuda", True, amarillo)
        ayuda_rect = ayuda_text.get_rect(center= (640, 100))
        ventana.blit(ayuda_text, ayuda_rect)

        # info del juego
        info_juego_text = get_font(50).render("Historia del juego:", True, blanco)
        info_juego_rect = info_juego_text.get_rect(center=(640, 200))
        ventana.blit(info_juego_text, info_juego_rect)

        info_juego_text1 = get_font(25).render(
            "PacMan es un videojuego arcade creado por el diseñador de videojuegos Toru Iwatani de la empresa Namco",
            True, blanco)
        info_juego_rect1 = info_juego_text1.get_rect(center=(640, 250))
        ventana.blit(info_juego_text1, info_juego_rect1)

        info_juego_text2 = get_font(25).render(
            "distribuido por Midway Gams al mercado estadounidense a principios de los años 1980",
            True, blanco)
        info_juego_rect2 = info_juego_text2.get_rect(center=(640, 300))
        ventana.blit(info_juego_text2, info_juego_rect2)

        # info controles
        info_controles_text = get_font(50).render(
            "Como jugar:",
            True, blanco)
        info_controles_rect = info_controles_text.get_rect(center=(640, 400))
        ventana.blit(info_controles_text, info_controles_rect)

        info_controles_text1 = get_font(25).render(
            "W: arriba, A: izquierda, S: abajo, D: derecha",
            True, blanco)
        info_controles_rect1 = info_controles_text1.get_rect(center=(640, 450))
        ventana.blit(info_controles_text1, info_controles_rect1)

        info_controles_text2 = get_font(25).render(
            "¡Para ganar cómete todo el alimento (puntos blancos) antes de que te coman a ti!",
            True, blanco)
        info_controles_rect2 = info_controles_text2.get_rect(center=(640, 500))
        ventana.blit(info_controles_text2, info_controles_rect2)

        ayuda_back = Button(imagen=None, pos=(640, 600), text_input= "Volver", font= get_font(75), color_base= blanco, hovering_color= amarillo)

        ayuda_back.changeColor(ayuda_mouse_pos)
        ayuda_back.update(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ayuda_back.checkForInput(ayuda_mouse_pos):
                    menu_principal()

        pygame.display.update()

def acerca_de():
    pygame.display.set_caption("Acerca de") #ventana del juego

    while True:

        acerca_mouse_pos = pygame.mouse.get_pos() #obtener posición mouse

        ventana.fill(negro) #cubrir ventana de negro

#fotos programadores
        ventana.blit(jose_foto, (300, 350))
        ventana.blit(jafet_foto, (775, 350))

# título
        acerca_text = get_font(75).render("Acerca de", True, amarillo)
        acerca_rect = acerca_text.get_rect(center=(640, 100))
        ventana.blit(acerca_text, acerca_rect)

#info jafet
        jafet_text = get_font(30).render("Programador: Jafet Díaz Morales, ID: 1 1929 0996, carnet: 2023053249", True,blanco)
        jafet_rect = jafet_text.get_rect(center=(640, 200))
        ventana.blit(jafet_text, jafet_rect)

# info jose
        jose_text = get_font(30).render("Programador: Jose Luis Vargas, ID: 2 0868 0247, carnet: 2023058736", True,
                                         blanco)
        jose_rect = jose_text.get_rect(center=(640, 250))
        ventana.blit(jose_text, jose_rect)

        # info general
        general_text = get_font(30).render("ITCR, Introducción a la programación, CE, 2023, "
                                         "Profesor: Jeff Schidt Peralta, Costa Rica, Python 3.11", True, blanco)
        general_rect = general_text.get_rect(center=(640, 300))
        ventana.blit(general_text, general_rect)

        ayuda_back = Button(imagen=None, pos=(640, 600), text_input= "Volver", font= get_font(75), color_base= blanco, hovering_color= amarillo)

        ayuda_back.changeColor(acerca_mouse_pos)
        ayuda_back.update(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ayuda_back.checkForInput(acerca_mouse_pos):
                    menu_principal()

        pygame.display.update()

def salon():
    pygame.display.set_caption("Salón de la fama") #ventana del juego

    while True:

        salon_mouse_pos = pygame.mouse.get_pos() #obtener posición mouse

        ventana.fill(negro) #cubrir ventana de negro


# título
        salon_text = get_font(75).render("Salón de la Fama", True, amarillo)
        salon_rect = salon_text.get_rect(center=(640, 100))
        ventana.blit(salon_text, salon_rect)

#putnajes
        puntajes_text = get_font(25).render(str(contenido_actualizado), True, amarillo)
        puntajes_rect = puntajes_text.get_rect(center=(640, 300))
        ventana.blit(puntajes_text, puntajes_rect)


#botón para volver
        salon_back = Button(imagen=None, pos=(640, 600), text_input= "Volver", font= get_font(75), color_base= blanco, hovering_color= amarillo)

        salon_back.changeColor(salon_mouse_pos)
        salon_back.update(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if salon_back.checkForInput(salon_mouse_pos):
                    menu_principal()

        pygame.display.update()

def menu_principal(): #ventana del menú principal
    pygame.display.set_caption("Menú")
    pygame.mixer.music.stop()
    global pausa

    while True:
        ventana.blit(fondo, (0,0)) #poner el fondo

        menu_mouse_pos = pygame.mouse.get_pos() #obtener la posición del mouse

        #poner texto
        menu_text = get_font(100).render("PacMan", True, amarillo)
        menu_rect= menu_text.get_rect(center= (640, 100))

#botones
        boton_jugar = Button(imagen=None, pos=(640,250), text_input= "Jugar", font=get_font(75), color_base= blanco, hovering_color = amarillo)
        boton_ayuda = Button(imagen=None, pos=(640, 350), text_input="Ayuda", font=get_font(75), color_base=blanco, hovering_color = amarillo)
        boton_acerca= Button(imagen=None, pos=(640, 450), text_input="Acerca de", font=get_font(75), color_base=blanco,
                             hovering_color=amarillo)
        boton_salon = Button(imagen=None, pos=(640, 550), text_input="Salón de la Fama", font=get_font(75), color_base=blanco,
                              hovering_color=amarillo)

        ventana.blit(menu_text, menu_rect)

        for button in [boton_jugar, boton_ayuda, boton_acerca, boton_salon]:
            button.changeColor(menu_mouse_pos)
            button.update(ventana)



        for event in pygame.event.get(): #registrar eventos en ventana
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() #salirnos de la ventana
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.checkForInput(menu_mouse_pos):
                        jugar()
                        pausa = False
                    if boton_ayuda.checkForInput(menu_mouse_pos):
                        ayuda()
                    if boton_acerca.checkForInput(menu_mouse_pos):
                        acerca_de()
                    if boton_salon.checkForInput(menu_mouse_pos):
                        salon()


        pygame.display.update()

def menu_pausa():
    global pause

    while pause:

        jugar_mouse_pos = pygame.mouse.get_pos()

        pygame.draw.rect(superficie, (128, 128, 128, 150), [0, 0, ancho, largo])
        pygame.draw.rect(superficie, "dark gray", [650, 150, 600, 50], 0,20)


        jugar_back = Button(imagen=None, pos=(1000, 460), text_input="Volver", font=get_font(75), color_base=blanco,
                            hovering_color=amarillo)

        jugar_back.changeColor(jugar_mouse_pos)
        jugar_back.update(superficie)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jugar_back.checkForInput(jugar_mouse_pos):
                    menu_principal()
                    pause = False


        superficie.blit(get_font(25).render("Juego Pausado: ESC para continuar", True, negro), (670, 160))


        if pacman.get_estado() == True:
            superficie.blit(get_font(25).render("Pacman está vivo", True, negro), (670, 230))

        else:
            superficie.blit(get_font(25).render("Pacman está muerto", True, negro), (670, 230))

        mostrar_matriz(niv1.get_matriz())

        superficie.blit(get_font(25).render("Fantasmas están vivos: ", True, negro), (920, 230))
        ventana.blit(superficie, (0,0))
        pygame.display.update()
        pygame.display.flip()





def mostrar_matriz(matriz):
    global pause
    if pause:
    # Configuración de la ventana
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                texto = get_font(10).render(str(valor), True, negro)
                x = j * 15  # Ajusta este valor según el ancho deseado de las celdas
                y = i * 15  # Ajusta este valor según el largo deseado de las celdas
                superficie.blit(texto, (x, y))

menu_principal()


