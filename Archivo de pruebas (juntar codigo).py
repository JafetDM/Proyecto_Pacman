import pygame


pygame.init()  # configuración básica de la pantalla de juego
ancho = 1280
alto = 720
puntaje = 0
pantalla_de_juego = pygame.display.set_mode([ancho, alto])  # establece la pantalla de juego
tiempo = pygame.time.Clock()
fps = 60

level = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

imagenes_jugador_principal = []
for i in range(1, 3):  # Toma dos imagenes, se reeedimensionan y esto crea la ilusion de movimiento en mi personaje
    imagenes_jugador_principal.append(pygame.transform.scale(pygame.image.load(
        f"C:\\Users\\emora\\OneDrive - Estudiantes ITCR\\Documentos\\GitHub\\Proyecto_Pacman\\pacman_imagenes\\{i}.jpg"),
                                            (20, 20)))

rojo_img = pygame.transform.scale(pygame.image.load("rojo.jpg"),(20, 20))

rosa_img = pygame.transform.scale(pygame.image.load("rosa.jpg"), (20,20))

azul_img = pygame.transform.scale(pygame.image.load("azul.jpg"), (20,20))

naranja_img = pygame.transform.scale(pygame.image.load("naranja.jpg"), (20,20))

mi_fuente = pygame.font.SysFont("Pacifico", 36)


def dibuja_puntaje():
    puntaje_texto = mi_fuente.render(f'Puntaje: {puntaje}', True, "white")
    pantalla_de_juego.blit(puntaje_texto, (50, 600))


def revisar_puntos():
    global puntaje
    num1 = (alto - 50) // 31
    num2 = ancho // 30

    row = centroy // num1
    col = centrox // num2

    if 0 <= row < len(level) and 0 <= col < len(level[row]):
        if level[row][col] == 2:
            level[row][col] = 4
            puntaje += 10
        elif level[row][col] == 3:
            level[row][col] = 4

    return puntaje


def dibujar_mapa():
    num1 = ((alto - 50) // 32)
    num2 = ((ancho // 30))
    for i in range(len(level)):  # Es para interactuar con cada fila de la matriz
        for j in range(len(level[i])):
            if level[i][j] == 1:
                # En esta parte se dibuja en la matriz los puntos blancos que come pacman definiendo color, posicion y tamaño
                pygame.draw.circle(pantalla_de_juego, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 0:
                # Esto dibuja un rectangulo azul en el valor 0, definido por los limites num1 y num2
                pygame.draw.rect(pantalla_de_juego, 'blue', pygame.Rect(j * num2, i * num1, num2, num1))
            if level[i][j] == 2 and not destellos:
                # En esta parte se dibuja en la matriz los puntos blancos que le dan velocidad (capsulas de poder)
                pygame.draw.circle(pantalla_de_juego, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 5)
            if level[i][j] == 3:
                # En esta parte se dibuja en la matriz las frutas
                pygame.draw.circle(pantalla_de_juego, 'red', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 5)
            if level[i][j] == 4:
                # En esta parte se dibuja en la matriz las frutas
                pygame.draw.circle(pantalla_de_juego, 'black', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 5)




class Pacman():

    # Atributos
    # Estado: indica si PacMan está vivo o muerto.
    # Posición x: fila de la matriz en que se encuentra PacMan.
    # Posición y: columna de la matriz en que se encuentra PacMan.
    # Velocidad: indicador de velocidad de PacMan (1 Normal, 2 Rápido)
    # Dircción: indica hacia donde mira pacman
    def __init__(self):
        self.estado = True
        self.pos_x=200
        self.pos_y=200
        self.pacman_velocidad= 2
        self.direccion = 0
        self.contador = 0
        self.destellos = False
        self.giros_p = [False, False, False, False]
        self.direccion_commando = 0
        self.centrox = self.pos_x + 11  # (ancho de la imagen dividido por 2)
        self.centroy = self.pos_y + 11  # (alto de la imagen dividido por 2)
        self.giros = [False, False, False, False]
        self.num1 = (alto - 50) // 32
        self.num2 = ancho // 30
        self.row = self.centroy // self.num1
        self.col = self.centrox // self.num2

    def direccion_personaje(self):
        # Dirección a la que debe mirar mi personaje principal
        # 0 = derecha, 1 = izquierda, 2= arriba, 3= abajo
        if self.direccion == 0:
            pantalla_de_juego.blit(imagenes_jugador_principal[self.contador // 10], (self.pos_x, self.pos_y))
        if self.direccion == 1:
            pantalla_de_juego.blit(pygame.transform.flip(imagenes_jugador_principal[self.contador // 10], True, False),
                                   (self.pos_x, self.pos_y))
        if self.direccion == 2:
            pantalla_de_juego.blit(pygame.transform.rotate(imagenes_jugador_principal[self.contador // 10], 90),
                                   (self.pos_x, self.pos_y))
        if self.direccion == 3:
            pantalla_de_juego.blit(pygame.transform.rotate(imagenes_jugador_principal[self.contador // 10], 270),
                                   (self.pos_x, self.pos_y))

    def revisar_posicion(self):

        if 0 <= self.row < len(level) and 0 <= self.col < len(level[self.row]):
            # Verificar giros basados en las casillas adyacentes
            if level[self.row][self.col] != 0:
                self.giros[0] = True  # Puede moverse a la derecha
            if level[self.row][self.col - 1] != 0:
                self.giros[1] = True  # Puede moverse a la izquierda
            if level[self.row - 1][self.col] != 0:
                self.giros[2] = True  # Puede moverse hacia arriba
            if level[self.row + 1][self.col] != 0:
                self.giros[3] = True  # Puede moverse hacia abajo

        return self.giros

    def obtener_pos(self):
        if self.direccion == 0 and self.giros_p[0]:
            self.pos_x += self.pacman_velocidad
        elif self.direccion == 1 and self.giros_p[1]:
            self.pos_x -= self.pacman_velocidad
        if self.direccion == 2 and self.giros_p[2]:
            self.pos_y -= self.pacman_velocidad
        elif self.direccion == 3 and self.giros_p[3]:
            self.pos_y += self.pacman_velocidad

        return self.pos_x, self.pos_y

    # Para que la ventana del juego se mantenga abierta
    def mover_pacman(self):

        while self.estado == True:  # Aquí se aplica el loop para mantener la ventana abierta a ciertos fps
            tiempo.tick(fps)
            pantalla_de_juego.fill("black")
            dibujar_mapa()
            dibuja_puntaje()

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
                    # Esto es para que el personaje PACMAN cambie de posicion respecto a las teclas
                    if event.key == pygame.K_RIGHT:
                        self.direccion_commando = 0
                    if event.key == pygame.K_LEFT:
                        self.direccion_commando = 1
                    if event.key == pygame.K_UP:
                        self.direccion_commando = 2
                    if event.key == pygame.K_DOWN:
                        self.direccion_commando = 3

            # Mover pacman después de verificar las colisiones
                self.pos_x, self.pos_y = pacman.obtener_pos()
                self.centrox = self.pos_x + 10
                self.centroy = self.pos_y + 10
                self.giros_p = pacman.revisar_posicion()

                for i in range(4):
                    if self.direccion_commando == i and self.giros_p[i]:
                        self.direccion = i

                if self.pos_x > 900:  # para teletransportar a pacman de un lado del borde a otro
                    self.pos_x = -47
                elif self.pos_x < -58:
                    self.pos_x = 897

            pacman.direccion_personaje()
            # Esto me permite mostrar una y otra vez en la pantalla de juego lo creado en el loop y támbien las interacciones en la misma.
            pygame.display.flip()

        pygame.QUIT()



    #instancias:

pacman= Pacman()
pacman.mover_pacman()



#Métodos
#Mover izquierda
#Mover derecha
#Mover arriba
#Mover abajo
#Comer alimento
#Comer cápsula

