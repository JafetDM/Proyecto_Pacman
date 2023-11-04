import pygame
import math

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

pos_x = 200  # Posiciones donde va a inicar pacman
pos_y = 200
direccion = 0
contador = 0
destellos = False
giros_p = [False, False, False, False]
direccion_commando = 0
pacman_velocidad = 2
centrox = pos_x + 11  # (ancho de la imagen dividido por 2)
centroy = pos_y + 11  # (alto de la imagen dividido por 2)
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


def personaje_principal():
    # Movimiento de mi personaje principal
    # 0 = derecha, 1 = izquierda, 2= arriba, 3= abajo
    if direccion == 0:
        pantalla_de_juego.blit(imagenes_jugador_principal[contador // 10], (pos_x, pos_y))
    if direccion == 1:
        pantalla_de_juego.blit(pygame.transform.flip(imagenes_jugador_principal[contador // 10], True, False),
                               (pos_x, pos_y))
    if direccion == 2:
        pantalla_de_juego.blit(pygame.transform.rotate(imagenes_jugador_principal[contador // 10], 90), (pos_x, pos_y))
    if direccion == 3:
        pantalla_de_juego.blit(pygame.transform.rotate(imagenes_jugador_principal[contador // 10], 270), (pos_x, pos_y))


def revisar_posicion(centrox, centroy):
    giros = [False, False, False, False]
    num1 = (alto - 50) // 32
    num2 = ancho // 30
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


def mover_pacman(pos_x, pos_y, direccion):
    # Esta es mi funcion en movimiento, se basa en la velocidad asginada por la variable pacman_velocidad,
    # me permite moverme segun el valor de la direccion de 0 a 3 el cual esta asociado con las teclas y tambien
    # me permite revisar si choca con pared para que el pacman se de vuelta

    if direccion == 0 and giros_p[0]:
        pos_x += pacman_velocidad
    elif direccion == 1 and giros_p[1]:
        pos_x -= pacman_velocidad
    if direccion == 2 and giros_p[2]:
        pos_y -= pacman_velocidad
    elif direccion == 3 and giros_p[3]:
        pos_y += pacman_velocidad

    return pos_x, pos_y


correr_juego = True
# Para que la ventana del juego se mantenga abierta
while correr_juego:  # Aquí se aplica el loop para mantener la ventana abierta a ciertos fps
    tiempo.tick(fps)
    pantalla_de_juego.fill("black")
    dibujar_mapa()
    revisar_puntos()
    puntaje = revisar_puntos()
    dibuja_puntaje()

    if contador < 19:  # Esto es simplemente para aplicar la ilusion del movimiento de la boca de pacman, utilizando el contador
        contador += 1
        if contador > 3:
            destellos = False
    else:
        contador = 0
        destellos = True  # Esto hara que la bolita grande titile o destelle 3 veces por 1 segundo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr_juego = False
        if event.type == pygame.KEYDOWN:
            # Esto es para que el personaje PACMAN cambie de posicion respecto a las teclas
            if event.key == pygame.K_RIGHT:
                direccion_commando = 0
            if event.key == pygame.K_LEFT:
                direccion_commando = 1
            if event.key == pygame.K_UP:
                direccion_commando = 2
            if event.key == pygame.K_DOWN:
                direccion_commando = 3

    # Mover pacman después de verificar las colisiones
    pos_x, pos_y = mover_pacman(pos_x, pos_y, direccion)
    centrox = pos_x + 10
    centroy = pos_y + 10
    giros_p = revisar_posicion(centrox, centroy)

    for i in range(4):
        if direccion_commando == i and giros_p[i]:
            direccion = i

    if pos_x > 900:  # para teletransportar a pacman de un lado del borde a otr
        pos_x = -47
    elif pos_x < -58:
        pos_x = 897

    personaje_principal()  # Para la decuada implementacion del movimiento del personaje
    pygame.display.flip()  # Esto me permite mostrar una y otra vez en la pantalla de juego lo creado en el loop y támbien las interacciones en la misma.
pygame.quit()  # Para cerrar la ventana de juego
