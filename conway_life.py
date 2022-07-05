import pygame
import numpy as np
import time

# --------------------------------------------------------------
# Parámentros

width, height = 600, 600
nxC, nyC =      60, 60

# colores

BG =            15, 15, 15
GRID =          40, 40, 40
CELL =          255, 0, 0

pygame.init()

screen  = pygame.display.set_mode((height, width))
screen.fill(BG)

# ---------------------------------------------------------------
# Tamaño de nuestra matriz

gameState = np.zeros((nxC,  nyC))

# Dimensiones de cada celda individual

dimCW = width / nxC
dimCH = height / nyC

""" ==============================================================
    Existen agrupaciones interesantes de células con un compartamiento 
    bien identificado y que podemos distribuir por nuestra matriz. 
    Cada una de estas estructuras tienen caractísticas conocidas y 
    bien clasificadas como:    
    
    - Caja 2×2:     una estructura invariable en el tiempo (vidas estáticas)
    - Línea 3×1:    una estructura que rota en 45º en cada iteración (osciladores)
    - El corredor:  una estructura de 5 celdas vivas que se desplaza en diagonal
                    por la matriz (naves espaciales).
    - La serpiente, la rana … y mil formas que puedes probar

    A continuación incluimos algunos de estos elementos en
    nuestra matriz
"""

# Oscilador.

gameState[38, 20] = 1
gameState[39, 20] = 1
gameState[40, 20] = 1

# Runner 1

gameState[10,5] = 1
gameState[12,5] = 1
gameState[11,6] = 1
gameState[12,6] = 1
gameState[11,7] = 1

#Runner 2

gameState[5,10] = 1
gameState[5,12] = 1
gameState[6,11] = 1
gameState[6,12] = 1
gameState[7,11] = 1

#Box 1

gameState[18,15] = 1
gameState[17,16] = 1
gameState[17,15] = 1
gameState[18,16] = 1

#Serpent 1

gameState[30,20] = 1
gameState[31,20] = 1
gameState[32,20] = 1
gameState[32,19] = 1
gameState[33,19] = 1
gameState[34,19] = 1

pauseExect = False

""" ======================================================================  
        Bucle de ejecución
    ====================================================================== 
"""

while True:

    # Copiamos la matriz del estado anterior
    # para representar la matriz en el nuevo estado

    newGameState = np.copy(gameState)

    # Ralentizamos la ejecución a 100 milisegundos

    time.sleep(0.1)

    # Limpiamos la pantalla

    screen.fill(BG)

    # Registramos eventos de teclado y ratón.

    ev = pygame.event.get()

    # Cada vez que identificamos un evento lo procesamos

    for event in ev:
        if event.type == pygame.QUIT:               # Salgo de pygame
            pygame.quit()

        elif event.type == pygame.KEYDOWN:          # Detectamos si se presiona una tecla para pausar el proceso
            pauseExect = not pauseExect

        elif sum(pygame.mouse.get_pressed()) > 0:   # Detectamos si se presiona el ratón para crear una celda viva
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

    """ ================================================================
        A continuación recorremos todas las celdas de la matriz, en
        el eje Y y en el eje X, para contabilizar cuantos vecinos
        vivos tiene cada celda.
    """

    for y in range(0, nxC):
        for x in range (0, nyC):

            if not pauseExect:

                # Calculamos el número de vecinos cercanos. Nota: el uso del operador mod (%) resuelve el
                # problema de os bordes en el espacio de celdas

                n_neigh =   gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x)     % nxC, (y - 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x - 1) % nxC, (y)      % nyC] + \
                            gameState[(x + 1) % nxC, (y)      % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
                            gameState[(x)     % nxC, (y + 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1)  % nyC]

                # Regla #1 : Una celda muerta con exactamente 3 vecinas vivas, "revive".

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla #2 : Una celda viva con menos de 2 o 3 vecinas vivas, "muere".

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

                """
                    Tras conocer el número de vecinos vivos de cada celda procedemos
                     a aplicar las dos reglas mencionadas, y pintamos el resultado 
                     según el resultado se «Viva» o «Muerta».
                """

            # Calculamos el polígono que forma la celda. nota: Las dimensiones de una celda son dimCH y dimCW

            poly = [(  x * dimCW,         y * dimCH ),
                    ( (x + 1) * dimCW,    y * dimCH),
                    ( (x + 1) * dimCW,   (y + 1) * dimCH),
                    (  x * dimCW,        (y + 1) * dimCH)]

            # Si la celda está "muerta" pintamos un recuadro con borde gris

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, GRID, poly, 1)

            # Si la celda está "viva" pintamos un recuadro relleno de color

            else:
                pygame.draw.polygon(screen, CELL, poly, 0)

    # Actualizamos el estado del juego.

    gameState = np.copy(newGameState)

    # Mostramos el resultado

    pygame.display.flip()