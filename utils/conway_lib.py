import pygame
import sys

# ===============================================================================================

class Conway:
    """

    """

    WIDTH = 100     # ancho de l celda
    HEIGHT = 50     # alto de la celda

    LIVE = 1        # estado de la celda viva
    DEAD = 0        # estado de la celda muerta

    __world = []    # espacio priincipal
    __next = []     # espacio de respaldo

    __born = []     # lista de números de celdas vecinas activas a una celda activa
    __alive = []    # lista de números de celdas vecinas activas para que una celda se mantanga activa

    # --------------------------------------------------------------------------------------

    def __init__(self, pattern: str = "23/3"):
        """
            Constructor
            A partir del patrón en <patterns> se obtienen las reglas de transición. Se obtiene la regla de la cantidad
            de celdas vecinss para determinar que la celda actual debe activarse o vivir, o debe desactivarse o morir.
            Ejemplo: 23/3 indica que
                regla 1:    el número  23 del patrón  determina el nº de celdas vecinas para continuar activa (2 o 3,
                            morir por escaces o sobrepoblacion, si la celda estaba activa)
                regla 2:    el numero 3 del patron determina el nº de celdas vecinas activas para activarse (3, vivir,
                            reproducirse, si l celda no estaba activa)
        :param pattern: Patrón  con función de transición
        """

        self.reset()
        self.__alive = [int(v) for v in pattern.split("/")[0]]  # n° de vecinos para mantener la celda inactiva
        self.__born = [int(v) for v in pattern.split("/")[1]]   # n° de vecinos para mantener la celda activa

    # --------------------------------------------------------------------------------------

    def reset(self):
        """
            Reinicaliza el autómata eliminando todas las celdas activas del espcio y reiniciando el n° de
            iteraciones
        :return:
        """
        self.__iterations = 0
        self.__world = [0] * (self.WIDTH * self.HEIGHT) # Crea una lista de ceros con width*lenght elementos
        self.__next = [0] * (self.WIDTH * self.HEIGHT)  # Crea una lista de ceros con width*lenght elementos

    # --------------------------------------------------------------------------------------

    @property
    def iterations(self) -> int:
        """
        Devuuelve el n° de iteraciones procesadas
        :return:
        """

        return self.__iterations

    # --------------------------------------------------------------------------------------

    @property
    def livecells(self) -> int:
        """
        Devuelve el n° de celdas activas presentes
        :return:
        """

        return self.__world.count(self.LIVE)

    # --------------------------------------------------------------------------------------

    def read(self, x: int, y: int) -> int:
        """
        Devuelve el estado de una celda dadas sus coordenadas en ekl espacio con fronteras
        reflectoras

        :param x:   Coordenda X en el espacio
        :param y:   Coordenda Y en el espacio
        :return:    Estado de la celda: INACTIVA = 0 (self.DEAD), ACTIVA = 1 (self.LIVE)
        """
        if x >= self.WIDTH:
            x -= self.WIDTH
        elif x < 0:
            x += self.WIDTH

        if y >= self.HEIGHT:
            y -= self.HEIGHT
        elif y < 0:
            y += self.HEIGHT

#        idx = y * self.WIDTH + x
#        print(idx)
        return self.__world[y * self.WIDTH + x]

    # --------------------------------------------------------------------------------------

    def write(self, x: int, y: int, value: int)-> None:
        """

        :param x:
        :param y:
        :param value:
        :return:
        """

        self.__world[ y * self.WIDTH + x] = value

    # --------------------------------------------------------------------------------------

    def update(self) -> None:
        """
        ACtualiza el estado del autómata celular ejecutando una iteración
        :return:
        """

        self.__iterations += 1

        # recorre todas las celdas  del espacio

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                near = [self.read(x - 1, y - 1) ,       # se obtiene el etado de todas las celdas vecianas
                        self.read(x ,    y - 1) ,
                        self.read(x + 1, y - 1) ,
                        self.read(x - 1, y) ,
                        self.read(x + 1, y) ,
                        self.read(x - 1, y + 1) ,
                        self.read(x,     y + 1) ,
                        self.read(x + 1, y + 1) ]
                alive_count =  near.count(self.LIVE)    # obtiene el numero de celdas activas vecinas

                current = self.read(x, y)               # obtiene la celda actual

                if current == self.LIVE:                # si la celda actual esta activa
                    if alive_count not in self.__alive: # regla 1: si  el n° de celdas vecinas no está entre el patron
                        current = self.DEAD             # la celda se desactiva (muere por escaces o por sobreploblacion)
                else:
                    if alive_count  in self.__born:     # regla 2: si el n° de celdas vecinas es el numero necesario
                        current = self.LIVE             # la celda se activa (se reproduce)

                self.__next[y * self.WIDTH + x] = current

        for i in range(self.WIDTH*self.HEIGHT):
            self.__world[i] = self.__next[i]            # el estado anteriores de todas las celdas pasan a se las actuales

    # --------------------------------------------------------------------------------------

    def draw(self, context: pygame.Surface) -> None:
        """
        Funcion de proyección del espacio en el estado de las celdas del autómata celular

        :param context: contexto gráfico de la pantalla
        :return:
        """

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                current = self.read(x, y)
                if current == self.LIVE:
                    pygame.draw.rect(surface= context, color= (255,255,255), rect = [x*10, y*10, 10, 10])
                else:
                    pygame.draw.lines(surface= context, color= (64,64,64), closed = True, points = (
                        (x * 10, y * 10),
                        ((x + 1) * 10, y * 10),
                        ((x + 1) * 10, (y + 1) * 10 ),
                        (x * 10, (y + 1) * 10)), width = 1)
