# **Estudio y Análisis de Programas con Automatas Celulares**

 # Vida Artificial


## Juego de la vida de John Horton Conway

En 1970, John Horton Conway dio a conocer el autómata celular que probablemente sea el más conocido: el Juego de la vida (Life), publicado por Martin Gardner en su columna Mathematical Games en la revista Scientific American.2​ Life ocupa una cuadrícula (lattice bidimensional) donde se coloca al inicio un patrón de células "vivas" o "muertas". La vecindad para cada célula son ocho: los vecinos formados por la vecindad de Von Neumann y las cuatro células de las dos diagonales (esta vecindad se conoce como vecindad de Moore). De manera repetida, se aplican simultáneamente sobre todas las células de la cuadrícula las siguientes 3 reglas:

- **Nacimiento:** se reemplaza una célula muerta por una viva si dicha célula tiene exactamente 3 vecinos vivos.
- **Muerte:** se reemplaza una célula viva por una muerta si dicha célula no tiene más de 1 vecino vivo (muerte por aislamiento) o si tiene más de 3 vecinos vivos (muerte por sobrepoblación).
- **Supervivencia:** una célula viva permanecerá en ese estado si tiene 2 o 3 vecinos vivos.

Una de las características más importantes de Life es su capacidad de realizar cómputo universal, es decir, que con una distribución inicial apropiada de células vivas y muertas, Life se puede convertir en una computadora de propósito general (máquina de Turing).

## Vida de Stephen Wolfram

Stephen Wolfram ha realizado numerosas investigaciones sobre el comportamiento cualitativo de los A.C. Con base en su trabajo sobre AC unidimensionales, con dos o tres estados, sobre configuraciones periódicas que se presentan en el A.C., observó sus evoluciones para configuraciones iniciales aleatorias. Así, dada una regla, el A.C. exhibe diferentes comportamientos para diferentes condiciones iniciales.

De esta manera, Wolfram clasificó el comportamiento cualitativo de los A.C. unidimensionales. De acuerdo con esto, un AC pertenece a una de las siguientes clases:

-  **Clase I.**
        La evolución lleva a una configuración estable y homogénea, es decir, todas las células terminan por llegar al mismo valor.

-  **Clase II.**
        La evolución lleva a un conjunto de estructuras simples que son estables o periódicas.

-  **Clase III.**
        La evolución lleva a un patrón caótico.

- **Clase IV.** 
        La evolución lleva a estructuras aisladas que muestran un comportamiento complejo (es decir, ni completamente caótico, ni completamente ordenado, sino en la línea entre uno y otro, este suele ser el tipo de comportamiento más interesante que un sistema dinámico puede presentar).
        
_(De Wikipedia)_