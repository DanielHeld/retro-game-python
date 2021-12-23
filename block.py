import copy

import pygame
from pygame import mixer

from globals import Globals


class Block:

    def __init__(self, typOfBlock):
        self.dropSound = mixer.Sound("drop.mp3")
        self.speedX = 0
        self.roundCounter = 0
        # vertical speed
        self.fallInRound = 2
        self.landed = False
        self.block = []
        if typOfBlock == 0:
            self.block = copy.deepcopy(Globals.L_BLOCK)
            self.color = "red"
        elif typOfBlock == 1:
            self.block = copy.deepcopy(Globals.L2_BLOCK)
            self.color = "blue"
        elif typOfBlock == 2:
            self.block = copy.deepcopy(Globals.O_BLOCK)
            self.color = "green"
        elif typOfBlock == 3:
            self.block = copy.deepcopy(Globals.Z_BLOCK)
            self.color = "orange"
        elif typOfBlock == 4:
            self.block = copy.deepcopy(Globals.S_BLOCK)
            self.color = "yellow"
        elif typOfBlock == 5:
            self.block = copy.deepcopy(Globals.I_BLOCK)
            self.color = "purple"
        elif typOfBlock == 6:
            self.block = copy.deepcopy(Globals.T_BLOCK)
            self.color = "brown"

    def drawBlock(self, screen):
        for element in self.block:
            self.drawBlockElement(element[0], element[1], screen)

    def drawBlockElement(self, x, y, screen):
        newX = Globals.GAME_LEFT + x * Globals.FIELD_SIZE
        newY = Globals.GAME_TOP + y * Globals.FIELD_SIZE
        pygame.draw.rect(screen, self.color, (newX, newY, Globals.FIELD_SIZE, Globals.FIELD_SIZE))

    def updateBlock(self, field):
        if self.checkCollisionBottom() or self.checkCollisionField(field):
            self.landed = True
        else:
            # fall but not after every round
            if self.fallInRound <= self.roundCounter:
                for element in self.block:
                    element[1] += 1
                self.roundCounter = 0
            else:
                self.roundCounter += 1

            # move in x directon
            if not self.checkCollisionSide():
                # moving to right if space
                if self.speedX > 0 and not self.checkCollisionFieldRight(field):
                    for element in self.block:
                        element[0] += self.speedX
                # moving to left if space
                if self.speedX < 0 and not self.checkCollisionFieldLeft(field):
                    for element in self.block:
                        element[0] += self.speedX

    def checkCollisionBottom(self):
        for element in self.block:
            if element[1] >= Globals.ROWS - 1:
                self.dropSound.play()
                return True
        return False

    def checkCollisionSide(self):
        for element in self.block:
            # left wall
            if element[0] <= 0 and self.speedX < 0:
                return True
            # right wall
            if element[0] >= Globals.COLUMNS - 1 and self.speedX > 0:
                return True
        return False

    def checkCollisionField(self, field):
        for element in self.block:
            if field.field[element[0]][element[1] + 1] != "grey":
                self.dropSound.play()
                return True
        return False

    def checkCollisionFieldLeft(self, field):
        for element in self.block:
            if field.field[element[0] - 1][element[1]] != "grey":
                return True
        return False

    def checkCollisionFieldRight(self, field):
        for element in self.block:
            if field.field[element[0] + 1][element[1]] != "grey":
                return True
        return False

    def checkRotation(self, block, field):
        for element in block:
            if element[0] < 0 or element[0] >= Globals.COLUMNS:
                return True
            if field.field[element[0]][element[1]] != "grey":
                return True
        return False

    def rotateBlock(self, field):
        if self.color == "green":
            return
        newBlock = []
        for e in self.block:
            newBlock.append([e[0] - self.block[0][0], e[1] - self.block[0][1]])
        print(newBlock)

        for element in newBlock:
            newX = 0
            newY = 0
            if element[0] == 0 and element[1] == 1:
                newX = -1
                newY = 0
            elif element[0] == 0 and element[1] == -1:
                newX = 1
                newY = 0
            elif element[0] == 1 and element[1] == 0:
                newX = 0
                newY = 1
            elif element[0] == -1 and element[1] == 0:
                newX = 0
                newY = -1

            elif element[0] == -1 and element[1] == -1:
                newX = 1
                newY = -1
            elif element[0] == -1 and element[1] == 1:
                newX = -1
                newY = -1
            elif element[0] == 1 and element[1] == -1:
                newX = 1
                newY = 1
            elif element[0] == 1 and element[1] == 1:
                newX = -1
                newY = 1

            # only for I_BLOCK
            elif element[0] == 2:
                newX = 0
                newY = 2
            elif element[1] == 2:
                newX = 2
                newY = 0

            element[0] = self.block[0][0] + newX
            element[1] = self.block[0][1] + newY
        # only turn if possible
        if not self.checkRotation(newBlock, field):
            self.block = copy.deepcopy(newBlock)
