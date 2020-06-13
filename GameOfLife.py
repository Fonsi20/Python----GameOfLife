import pygame
import numpy as np
import time
import os

pygame.init()

current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'images') # The image folder path

#Creación de pantalla
width, height = 800,800
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption('GameOfLife')
icon = pygame.image.load(os.path.join(image_path, 'image.png'))
pygame.display.set_icon(icon)

#Pintamos el fondo de nuestra pantalla
bg = 24,30,32
screen.fill(bg)

#Número de celdas
nxC, nyC = 50,50

#Dimensiones de la celda
dimCW = width / nxC
dimCH = height / nyC

#Estados de las celdas. Vivas  = 1, Muertas = 0
gameState = np.zeros((nxC,nyC))

#Automata Palo
gameState[5,3]=1
gameState[5,4]=1
gameState[5,5]=1

#Automata Movil
gameState[21,21]=1
gameState[22,22]=1
gameState[22,23]=1
gameState[21,23]=1
gameState[20,23]=1

#Control del estado de ejecución
pauseExect = False

#Bucle de ejecución
while True:

    newGameState = np.copy(gameState)

    #Reseteamos pantalla y ponemos un retardo de 0.1s
    screen.fill(bg)
    time.sleep(0.1)

    #Registramos eventos teclado y ratón
    ev = pygame.event.get()
    for event in ev:
        #Detectamos si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Detectamos si se presiona un botón
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick)>0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX,celY] = not mouseClick[2]

    for y in range(0,nxC):
        for x in range (0,nyC):

            if not pauseExect:
                #Calculamos el número de vecinos cercanos
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x) % nxC,     (y - 1) % nyC] +\
                          gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x - 1) % nxC, (y) % nyC] + \
                          gameState[(x + 1) % nxC, (y) % nyC] + \
                          gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                          gameState[(x) % nxC,     (y + 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y + 1) % nyC]

                #Rule #1 : Una célula con exactamente 3 vecinas vivas, "revive"
                if gameState[x,y,] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1

                #Rule #2 : Una célula viva con menso de 2 o mmás de 3 vecinas vivas, "muere"
                if gameState[x,y,] == 1 and (n_neigh <2 or n_neigh > 3):
                    newGameState[x,y] = 0

            #Creamos polígono de cada celda a dibujar
            poly=[(int((x)   * dimCW),  int(y    * dimCH)),
                  (int((x+1) * dimCW),  int(y    * dimCH)),
                  (int((x+1) * dimCW), int((y+1) * dimCH)),
                  (int((x)   * dimCW), int((y+1) * dimCH))]

            if newGameState[x,y] == 0:
                 pygame.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                pygame.draw.polygon(screen, (58,161,191), poly, 0)

    #Actualizamos le estado del juego
    gameState = np.copy(newGameState)

    #Actualizamos la pantalla
    pygame.display.flip()