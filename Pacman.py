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

level = matriz

#fuente
def get_font(size): #obtener la fuente de letra
    return pygame.font.SysFont("Impact", size)


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



#ventana principal
ancho = 1280
largo = 720
ventana = pygame.display.set_mode([ancho, largo]) #ventana
pygame.display.set_caption("Pac-Man") # Título
fondo= pygame.image.load("fondo_negro.png")

def jugar():
    pygame.display.set_caption("Juego") #ventana del juego

    while True:

        jugar_mouse_pos = pygame.mouse.get_pos()

        ventana.fill(negro)

        jugar_text= get_font(45).render("Pantalla de juego", True, negro)
        jugar_rect = jugar_text.get_rect(center= (640, 260))
        ventana.blit(jugar_text, jugar_rect)

        jugar_back = Button(imagen=None, pos=(640, 460), text_input= "Volver", font= get_font(75), color_base= blanco, hovering_color= amarillo)

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

        ayuda_text= get_font(45).render("Pantalla de ayuda", True, blanco)
        ayuda_rect = ayuda_text.get_rect(center= (640, 260))
        ventana.blit(ayuda_text, ayuda_rect)

        ayuda_back = Button(imagen=None, pos=(640, 460), text_input= "Volver", font= get_font(75), color_base= negro, hovering_color= amarillo)

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

def menu_principal(): #ventana del menú principal
    pygame.display.set_caption("Menú")

    while True:
        ventana.blit(fondo, (0,0)) #poner el fondo

        menu_mouse_pos = pygame.mouse.get_pos() #obtener la posición del mouse

        #poner texto
        menu_text = get_font(100).render("Menú Principal", True, amarillo)
        menu_rect= menu_text.get_rect(center= (640, 100))

#botones
        boton_jugar = Button(imagen=None, pos=(640,250), text_input= "Jugar", font=get_font(75), color_base= blanco, hovering_color = amarillo)
        boton_ayuda = Button(imagen=None, pos=(640, 350), text_input="Ayuda", font=get_font(75), color_base=blanco, hovering_color = amarillo)

        ventana.blit(menu_text, menu_rect)

        for button in [boton_jugar, boton_ayuda]:
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


        pygame.display.update()

menu_principal()


#CLASE JUEGO

#Atributos: Número de juego, tablero (matriz 40x36,
# 0: espaco vacío, 1: puntos, 2: cápsula de poder,3: frutas
# 4: pared horizontal, 5: pared vertical, 6: puerta fantasmas
# nivel (1 y 2), score

#métodos: iniciar juego

