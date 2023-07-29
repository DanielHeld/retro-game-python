import pygame
import random
import time

from pygame import mixer
from block import Block
from field import Field
from globals import Globals
from menu import MainMenu, OptionsMenu

pygame.init()
screen = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))

mainMenu = MainMenu(screen)
optionsMenu = OptionsMenu(screen)

mixer.music.load("media/tetrismusic.mp3")
mixer.music.play(-1)

field = Field()
block1 = Block(random.randint(0, 6))

lastTime = time.time()


def runGame (block1):
    # game input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Globals.RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Globals.GAME_STATE = Globals.MAIN_MENU_ACTIVE_GAME

            if event.key == pygame.K_p:
                if Globals.GAME_STATE == Globals.PAUSED:
                    Globals.GAME_STATE = Globals.PLAYING
                else:
                    Globals.GAME_STATE = Globals.PAUSED
            if event.key == pygame.K_LEFT:
                block1.speedX = -1
            if event.key == pygame.K_RIGHT:
                block1.speedX = 1
            if event.key == pygame.K_DOWN:
                block1.fallInRound = 0
            if event.key == pygame.K_SPACE and Globals.GAME_STATE != Globals.PAUSED:
                block1.rotateBlock(field)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                block1.speedX = 0
            if event.key == pygame.K_RIGHT:
                block1.speedX = 0
            if event.key == pygame.K_DOWN:
                block1.fallInRound = 3
    # update
    if Globals.GAME_STATE == Globals.PLAYING:
        field.checkFullRowInField()
        block1.updateBlock(field)
        if block1.landed:
            field.addBlockToField(block1)
            block1 = Block(random.randint(0, 6))  # random.randint(0, 6)
            if block1.checkCollisionField(field):
                Globals.GAME_STATE = Globals.GAME_OVER
                gameOverSound = mixer.Sound("media/gameover.wav")
                gameOverSound.play()
                pygame.display.update()

    # render
    drawBackground()
    field.drawField(screen)
    block1.drawBlock(screen)
    drawGrid()
    if Globals.GAME_STATE == Globals.GAME_OVER:
        myfont = pygame.font.SysFont('Arial', 100)
        textsurface = myfont.render("GAME OVER", False, "red")
        screen.blit(textsurface, (100, 300))
    return block1


def drawBackground():
    screen.fill("white")
    pygame.draw.rect(screen, "black", (Globals.GAME_LEFT - 5, Globals.GAME_TOP - 5, Globals.GAME_WIDTH + 10, Globals.GAME_HEIGHT + 10))
    pygame.draw.rect(screen, "white", (Globals.GAME_LEFT, Globals.GAME_TOP, Globals.GAME_WIDTH, Globals.GAME_HEIGHT))


def drawGrid():
    for i in range(Globals.COLUMNS):
        vector1 = (Globals.GAME_LEFT + i * Globals.FIELD_SIZE, Globals.GAME_TOP)
        vector2 = (Globals.GAME_LEFT + i * Globals.FIELD_SIZE, Globals.GAME_TOP + Globals.GAME_HEIGHT)
        pygame.draw.line(screen, "black", vector1, vector2)
    for i in range(Globals.ROWS):
        vector1 = (Globals.GAME_LEFT, Globals.GAME_TOP + i * Globals.FIELD_SIZE)
        vector2 = (Globals.GAME_LEFT + Globals.GAME_WIDTH, Globals.GAME_TOP + i * Globals.FIELD_SIZE)
        pygame.draw.line(screen, "black", vector1, vector2)


drawBackground()
drawGrid()
running = True
while Globals.RUNNING:
    # 80ms per loop
    dt = time.time() - lastTime
    # dt in milisecs as int
    dt = int(dt * 1000)
    pygame.time.wait(80 - dt)
    lastTime = time.time()

    # menu
    if Globals.GAME_STATE == Globals.NEW_GAME:
        block1 = Block(random.randint(0, 6))
        field = Field()
        Globals.GAME_STATE = Globals.PLAYING
    if Globals.GAME_STATE == Globals.MAIN_MENU or Globals.GAME_STATE == Globals.MAIN_MENU_ACTIVE_GAME:
        mainMenu.runMainMenu()
    elif Globals.GAME_STATE == Globals.OPTION_MENU:
        optionsMenu.runOptionsMenu()
    else:
        block1 = runGame(block1)
    pygame.display.update()


