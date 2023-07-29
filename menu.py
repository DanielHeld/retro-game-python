import pygame

from globals import Globals


class MainMenu:

    def __init__(self, screen):
        self.screen = screen
        self.cursor = 0
        self.offset = 150

    def runMainMenu(self):
        menupoints = 3
        if Globals.GAME_STATE == Globals.MAIN_MENU_ACTIVE_GAME:
            # continue
            menupoints = 4
        # menu input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # close game window
                Globals.GAME_STATE = Globals.PLAYING
                Globals.RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.cursor == 0:
                        # play
                        Globals.GAME_STATE = Globals.NEW_GAME
                    if self.cursor == 1:
                        # options
                        Globals.GAME_STATE = Globals.OPTION_MENU
                    if self.cursor == 2:
                        # quit game
                        Globals.GAME_STATE = Globals.PLAYING
                        Globals.RUNNING = False
                    if self.cursor == 3:
                        # continue
                        Globals.GAME_STATE = Globals.PLAYING

                if event.key == pygame.K_UP:
                    self.cursor = (self.cursor - 1) % menupoints
                if event.key == pygame.K_DOWN:
                    self.cursor = (self.cursor + 1) % menupoints
        self.drawMenu()
        self.drawCursor()

    def drawMenu(self):
        self.screen.fill("white")
        myFont = pygame.font.SysFont('Arial', 100)
        textSurface = myFont.render("Retro Game", False, "red")
        self.screen.blit(textSurface, (Globals.SCREEN_WIDTH/2 - textSurface.get_width()/2, 30))

        myFont = pygame.font.SysFont('Comic', 70)

        if Globals.GAME_STATE == Globals.MAIN_MENU_ACTIVE_GAME:
            textSurface = myFont.render("continue", False, "blue")
            self.screen.blit(textSurface, (Globals.SCREEN_WIDTH / 2 - textSurface.get_width() / 2, 200))

        textSurface = myFont.render("start", False, "black")
        self.screen.blit(textSurface, (Globals.SCREEN_WIDTH / 2 - textSurface.get_width() / 2, 280))

        textSurface = myFont.render("controls", False, "black")
        self.screen.blit(textSurface, (Globals.SCREEN_WIDTH / 2 - textSurface.get_width() / 2, 360))

        textSurface = myFont.render("quit", False, "black")
        self.screen.blit(textSurface, (Globals.SCREEN_WIDTH / 2 - textSurface.get_width() / 2, 440))

    def drawCursor(self):
        y = 0
        if self.cursor == 0:
            y = 280
        if self.cursor == 1:
            y = 360
        if self.cursor == 2:
            y = 440
        if self.cursor == 3:
            y = 200
        myFont = pygame.font.SysFont('Comic', 70)
        textSurface = myFont.render("x", False, "darkgrey")
        self.screen.blit(textSurface, (Globals.SCREEN_WIDTH/2 - self.offset, y))



class OptionsMenu:

    def __init__(self, screen):
        self.screen = screen

    def runOptionsMenu(self):
        # menu input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # close game window
                Globals.GAME_STATE = Globals.PLAYING
                Globals.RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Globals.GAME_STATE = Globals.MAIN_MENU

        self.drawMenu()


    def drawMenu(self):
        self.screen.fill("white")
        myFont = pygame.font.SysFont('Arial', 100)
        textSurface = myFont.render("Controls", False, "red")
        self.screen.blit(textSurface, (Globals.SCREEN_WIDTH/2 - textSurface.get_width()/2, 30))

        textY = 200
        textList = [ "KEY_LEFT",
                     "KEY_RIGHT",
                     "KEY_DOWN",
                     "SPACEBAR",
                     "p",
                     "ESCAPE",
                     ]
        myFont = pygame.font.SysFont('Comic', 60)
        for textLine in textList:
            textSurface = myFont.render(textLine, False, "blue")
            self.screen.blit(textSurface, (Globals.SCREEN_WIDTH / 2 - 300, textY))
            textY += 60

        textY = 200
        textList = ["move left",
                    "move right",
                    "speed up",
                    "turn block",
                    "pause game",
                    "go to menu",
                    ]
        myFont = pygame.font.SysFont('Comic', 50)
        for textLine in textList:
            textSurface = myFont.render(textLine, False, "black")
            self.screen.blit(textSurface, (Globals.SCREEN_WIDTH / 2 , textY))
            textY += 60

        textSurface = myFont.render("press ESCAPE to go back", False, "grey")
        self.screen.blit(textSurface, (Globals.SCREEN_WIDTH / 2 - textSurface.get_width()/2, 600))

