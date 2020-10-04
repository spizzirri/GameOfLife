import time
import pygame
import numpy as np

pygame.init()

width, height = 600, 600

screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25

screen.fill(bg)

nxC, nyC = 25, 25

DIMCW = width / nxC
DIMCH = height / nyC

gameState = np.zeros((nxC, nyC))

#Automata en movimiento
"""
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1
"""

# Control de la ejecucion
pauseExect = False
running = True

while running:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    # Registramos eventos de teclado y raton

    ev = pygame.event.get()

    for event in ev:

        if event.type == pygame.QUIT:
            running = False

        # Si se presiona una tecla pone en pausa
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        # Se obtiene la posicion del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sum(pygame.mouse.get_pressed()) > 0:
                posX, posY = pygame.mouse.get_pos()
                celX, celY = int(np.floor(posX / DIMCW)), int(np.floor(posY / DIMCH))

                newGameState[celX, celY] = not gameState[celX, celY]

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

                # Calculamos el numero de vecinos cercanos
                n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
                        gameState[(x)   % nxC, (y-1) % nyC] + \
                        gameState[(x+1) % nxC, (y-1) % nyC] + \
                        gameState[(x-1) % nxC, (y)   % nyC] + \
                        gameState[(x+1) % nxC, (y)   % nyC] + \
                        gameState[(x-1) % nxC, (y+1) % nyC] + \
                        gameState[(x)   % nxC, (y+1) % nyC] + \
                        gameState[(x+1) % nxC, (y+1) % nyC]

                #Regla1: Una celula muerta con exactamente 3 vecinas vivas, "revive"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                #Regla2: Una celula viva con menos 2 o mas de 3 vecinas vivas, "muere"
                if gameState[x, y] == 1 and ( n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # Creamos el poligono de cada celda a dibujar
            poly = [
                ((x)   * DIMCW, y * DIMCH),
                ((x+1) * DIMCW, y * DIMCH),
                ((x+1) * DIMCW, (y+1) * DIMCH),
                ((x)   * DIMCW, (y+1) * DIMCH)
            ]

            if pauseExect:
                pygame.display.set_caption('En pause')
                colorOfLines = 255, 0, 0
            else:
                pygame.display.set_caption('El juego de la vida')
                colorOfLines = 128, 128, 128

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, colorOfLines, poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()

pygame.quit()
