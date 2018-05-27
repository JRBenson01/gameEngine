import pygame, sys
from pygame.locals import *
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 125, 0)
yellow = (255, 255, 0)
spring_green = (125, 255, 0)
green = (0, 255, 0)
turquoise = (0, 255, 125)
cyan = (0, 255, 255)
ocean = (0, 125, 255)
blue = (0, 0, 255)
violet = (125, 0, 255)
magenta = (255, 0, 255)
dull_magenta = (125, 0, 125)
raspberry = (255, 0, 125)

class game_Window(object):
    def __init__(self):
        self.height = 100
        self.width = 100
        self.display = pygame.display.set_mode((self.width, self.height))
        self.caption = ""
        self.frameCount = 0
        self.clock = pygame.time.Clock()
        self.fps = 0

    def display(self):
        return self.display

    def set_res(self, width, height):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))

    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(caption)

    def set_background(self, image):
        self.background = pygame.image.load(image)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def gameExit(self):
        print("exiting game")
        pygame.quit()
        sys.exit()

    def frameUpdate(self):
        self.clock.tick()
        self.fps = self.clock.get_fps() 
        #print ("FPS: ", self.fps)
        self.display.blit(self.background, (0, 0))
        start_button.display()
        collider.display()
        player.display()
        pygame.display.update()
        
        

class game_Action(object):
    def __init__(self):
        self.exit = False

    def gameLoop(self):
        while self.exit == False:
            gameWindow.frameUpdate()
            player.collision(collider)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    print("Space key Pressed")
                    collider.set_pos(200, 100)
                if event.type == QUIT:
                    gameWindow.gameExit()

class game_Input(object):
    def __init__(self):
        self.blank = 0


class button(object):
    def __init__(self, text):
        self.text = text
        self.normal_color = dull_magenta
        self.trigger_color = magenta
        self.click_color = violet
        self.font_size = 22
        self.font = pygame.font.Font("freesansbold.ttf", self.font_size)
        self.width = 100
        self.height = 100
        self.xPos = gameWindow.width/2
        self.yPos = gameWindow.height/2

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def set_font_size(self, size):
        self.font_size = size

    def set_normal_color(self, color):
        self.normal_color = color

    def set_trigger_color(self, color):
        self.trigger_color = color

    def set_click_color(self, color):
        self.click_color = color

    def set_text(self, text):
        self.text = text

    def set_pos(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def display(self):
        #print ("Displaying", text, "button")
        disp_specs = ((self.xPos - (self.width/2)), (self.yPos - (self.height/2)), self.width, self.height)
        #print (position)
        textSurface = self.font.render(self.text, True, black)
        textBox = textSurface.get_rect()
        textBox.center = (self.xPos, self.yPos)
        pygame.draw.rect(gameWindow.display, self.normal_color, (disp_specs))
        gameWindow.display.blit(textSurface, textBox)


class gamePiece(object):
    def __init__(self):
        self.gravity = False
        self.collidable = False
        self.position = (0, 0)
        self.length = 100
        self.height = 100
        self.hb_length = 100
        self.hb_height = 100
        self.triggered = False
        self.use_image = False
        self.sprite = ""

    def set_pos(self, x, y):
        self.position = (x, y)

    def set_hitbox(self, length, height):
        self.hb_length = length
        self.hb_height = height

    def set_hb(self, length, height):
        self.hb_length = length
        self.hb_height = height

    def set_sprite(self, image):
        self.use_image = True
        self.sprite = ""
        self.sprite = pygame.transform.scale(self.sprite, (self.length, self.height))
        #self.background = pygame.transform.scale(self.background, (self.width, self.height))
        
    def set_size(self, length, height):
        self.length = length
        self.height = height
        if self.use_image:
            self.sprite = pygame.transform.scale(self.sprite, (self.length, self.height))

    def get_hb(self):
        xPos = self.position[0]
        yPos = self.position[1]
        xMin = xPos - self.hb_length/2
        xMax = xPos + self.hb_length/2
        yMin = yPos - self.hb_height/2
        yMax = yPos + self.hb_height/2
        return (xMin, xMax, yMin, yMax)

    def get_triggered(self):
        return self.triggered

    def collision(self, collider):
        xPos = self.position[0]
        yPos = self.position[1]
        xMin = xPos - self.hb_length/2
        xMax = xPos + self.hb_length/2
        yMin = yPos - self.hb_height/2
        yMax = yPos + self.hb_height/2
        collider_hb = collider.get_hb()
        col_xMin = collider_hb[0]
        col_xMax = collider_hb[1]
        col_yMin = collider_hb[2]
        col_yMax = collider_hb[3]
        dim_hb = (xMin, xMax, yMin, yMax)
        #print (dim_hb)
        #print (collider_hb)
        if (xMin <= collider_hb[0] and xMax >= collider_hb[1] and yMin <= collider_hb[2] and yMax >= collider_hb[3]):
            self.triggered = True
            print ("Collision detected")

        elif (xMin <= collider_hb[1] and xMax >= collider_hb[0] and yMin <= collider_hb[3] and yMax >= collider_hb[2]):
            self.triggered = True
            print ("Collision detected")

    def display(self):
        #print ("Displaying gamePiece")
        xPos = self.position[0]
        yPos = self.position[1]
        xMin = xPos - self.length/2
        yMin = yPos - self.height/2
        if self.use_image:
            gameWindow.display.blit(self.sprite, (xMin, yMin))
        else:
            disp_specs = ((xPos - (self.length/2)), (yPos - (self.height/2)), self.length, self.height)
            pygame.draw.rect(gameWindow.display, black, (disp_specs))

gameWindow = game_Window()
gameAction = game_Action()

gameWindow.set_res(500, 500)
gameWindow.set_caption("Hello World")
gameWindow.set_background("map_use.png")

start_button = button("Start")

player = gamePiece()
player.set_pos(100, 100)

collider = gamePiece()
collider.set_pos(300, 100)

gameAction.gameLoop()
