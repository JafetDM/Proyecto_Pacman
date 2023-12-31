#Proyecto Pacman

import pygame, sys
from Matriz import matriz

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
pygame.display.set_caption("Pac-Man") # Título
fondo= pygame.image.load("fondo_negro.png")

#imagenes
jose_foto = pygame.image.load("jose_foto.jpg")
jafet_foto = pygame.image.load("jafet_foto.png")

#fuente
def get_font(size): #obtener la fuente de letra
    return pygame.font.SysFont("Impact", size)

def mostrar_texto(ventana, fuente, texto, color,  x, y):
    superficie = fuente.render(texto, True, color)
    rectangulo = superficie.get_rect(center=(x, y))
    ventana.blit(superficie, rectangulo)

#variable donde almacenar puntajes
puntajes=[]

#MANEJO DE ARCHIVOS DE TEXTO

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

#clase Juego
class Juego():
    # Atributos: 1) Número de juego,
    # 2) tablero (matriz 40x36) sus valores son
    # 0: pared horizontal, 1: puntos, 2: cápsula de poder,3: frutas, 4: espacio vacío, 5: puerta fantasma, 6: pared vertical
    # 3) nivel (1 y 2)
    # 4) score

    #métodos: iniciar juego
    def __init__(self, num_juego, nivel):
        self.num_juego = num_juego #consecutivo del juego, cada que termina se actualiza
        self.tablero = matriz #será una matriz 40x36, se actualiza en tiempo real. Proviene de Matriz.py
        self.nivel = nivel #de 1 a 2, inicia en 1
        self.score = 0 #inicia en 0, esquema de puntos definido por alimento (puntos y fruta) y fantasmas comidos

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
                if self.tablero[i][j] == 2:
                    pygame.draw.circle(ventana, blanco, (j * num2 + (num2), i * num1 + (num1)), 5)
                if self.tablero[i][j] == 3:
                    pygame.draw.circle(ventana, rojo, (j * num2 + (num2), i * num1 + (num1)), 4)

                if self.tablero[i][j] == 5: #dibuja una linea que sirve como la puerta para los fantasmas, posicion inicial y final y width
                    pygame.draw.line(ventana, blanco, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)),
                                     (j * num2 + (0.5 * num2) + 18, i * num1 + (0.5 * num1)), 4)
    def get_score(self): #retorna score
        return (self.score)

# instancias de juego
niv1 = Juego(1, 1)
niv2 = Juego(1, 2)

def jugar():
    pygame.display.set_caption("Juego") #ventana del juego

    #poner música
    pygame.mixer.init()
    pygame.mixer.music.load("01. Game Start.mp3")
    pygame.mixer.music.play()

    while True:

        jugar_mouse_pos = pygame.mouse.get_pos()

        ventana.fill(negro)
        niv1.iniciar()
        score1= niv1.get_score()
        mostrar_texto(ventana, get_font(45), str(score1), blanco, 1000, 110)


        jugar_text= get_font(45).render("Puntaje", True, rosado)
        jugar_rect = jugar_text.get_rect(center= (1000, 50))
        ventana.blit(jugar_text, jugar_rect)

        jugar_back = Button(imagen=None, pos=(1000, 460), text_input= "Volver", font= get_font(75), color_base= blanco, hovering_color= amarillo)

        jugar_back.changeColor(jugar_mouse_pos)
        jugar_back.update(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jugar_back.checkForInput(jugar_mouse_pos):
                    menu_principal()

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
                    if boton_ayuda.checkForInput(menu_mouse_pos):
                        ayuda()
                    if boton_acerca.checkForInput(menu_mouse_pos):
                        acerca_de()
                    if boton_salon.checkForInput(menu_mouse_pos):
                        salon()


        pygame.display.update()

menu_principal()



