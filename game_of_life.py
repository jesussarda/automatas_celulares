import sys, pygame
from utils.conway_lib import Conway


# =================================================================================

size = WIDTH, HEIGHT = 1000, 564

BUTTON = 64

LABEL1_POS = 100
LABEL2_POS = 750
LABEL3_POS = 850

BPLAY_POS = 400 + 4
BPAUSE_POS = 400 + 68
BCLEAR_POS = 400 + 132

FIELD = HEIGHT - BUTTON
BUTTON_POS = FIELD+15

FONT_SIZE = 30

BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREY = (92,92,92)

# =================================================================================

def mouse_click(world: Conway, mouse_x: int, mouse_y: int) -> None:
    x = int(mouse_x / 10 )
    y = int(mouse_y / 10 )

    if world.read(x,y) == world.LIVE:
        world.write(x,y, world.DEAD)
    else:
        world.write(x,y, world.LIVE)

# =================================================================================

def main():

    print('Init...')

    pygame.init()
    pygame.font.init()

    world = Conway()    # reglas de transición 23/3 por defecto
#    world = Conway('23/36')
#    world = Conway('4/2')
#    world = Conway('51/346')

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('JUEGO DE LA VIDA DE CONWAY')

    play = pygame.image.load('images/play.png')
    playrect = play.get_rect()
    playrect = playrect.move(BPLAY_POS, BUTTON_POS)

    pause = pygame.image.load('images/pause.png')
    pauserect = play.get_rect()
    pauserect = pauserect.move(BPAUSE_POS,  BUTTON_POS)

    clear = pygame.image.load('images/clear.png')
    clearrect = play.get_rect()
    clearrect = clearrect.move(BCLEAR_POS,  BUTTON_POS)

    myfont = pygame.font.SysFont('Lucida Console', FONT_SIZE)

    running = False

    loop = True
    while loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if y <= FIELD:
                    mouse_click(world,x,y)
                else:
                    if playrect.collidepoint(x, y):
                        running = True
                    if pauserect.collidepoint(x, y):
                        running = False
                    if clearrect.collidepoint(x, y):
                        world.reset()

        # ------------------------------------------------------

        if running:
            world.update()

        screen.fill(BLACK)
        world.draw(screen)

        screen.blit(play, playrect)
        screen.blit(pause, pauserect)
        screen.blit(clear, clearrect)

        textsurface = myfont.render('Corriendo' if running else 'pausa', True, WHITE)
        screen.blit(textsurface, (LABEL1_POS,  BUTTON_POS))

        textsurface = myfont.render(str(world.iterations), True, WHITE)
        screen.blit(textsurface, (LABEL2_POS,  BUTTON_POS))

        textsurface = myfont.render(str(world.livecells), True, WHITE)
        screen.blit(textsurface, (LABEL3_POS,  BUTTON_POS))

        pygame.display.flip()

    print('End...')
    pygame.quit()

# =================================================================================
#            M A I N
# =================================================================================

if __name__ == "__main__":
    main()