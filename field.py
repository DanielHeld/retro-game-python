import pygame

from pygame import mixer
from globals import Globals


class Field:

    def __init__(self):
        self.score = 0
        self.field = []
        self.initField()

    def initField(self):
        for x in range(Globals.COLUMNS):
            list1 = []
            for y in range(Globals.ROWS):
                list1.append("grey")
            self.field.append(list1)

    def drawField(self, screen):
        for x in range(Globals.COLUMNS):
            for y in range(Globals.ROWS):
                pygame.draw.rect(screen, self.field[x][y], (
                    x * Globals.FIELD_SIZE + Globals.GAME_LEFT, y * Globals.FIELD_SIZE + Globals.GAME_TOP,
                    Globals.FIELD_SIZE, Globals.FIELD_SIZE))
        # draw score
        myfont = pygame.font.SysFont('Arial', 30)
        textsurface = myfont.render("Score: " + str(self.score), False, (0, 0, 0))
        screen.blit(textsurface, (Globals.GAME_LEFT + Globals.GAME_WIDTH + 50, 0))

    def addBlockToField(self, givenBlock):
        for element in givenBlock.block:
            self.field[element[0]][element[1]] = givenBlock.color

    def checkFullRowInField(self):
        for y in range(Globals.ROWS):
            if self.checkRow(y):
                print("row is full" + str(y))
                self.deleteRow(y)
                fullRowSound = mixer.Sound("fullrow.mp3")
                fullRowSound.play()

    def deleteRow(self, y):
        for x in range(Globals.COLUMNS):
            del self.field[x][y]
        for x in range(Globals.COLUMNS):
            self.field[x].insert(0, "grey")

    def checkRow(self, y):
        for x in range(Globals.COLUMNS):
            if self.field[x][y] == "grey":
                return False
        self.score += 10
        return True
