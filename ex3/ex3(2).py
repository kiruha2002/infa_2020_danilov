import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

cWhite = (255, 255, 255)
cRed = (255, 0, 0)
cGreen = (138, 170, 232)
cBlue = (166, 241, 160)
cBlack = (0, 0, 0)

cGrey = (255, 0, 255)
cPink = (192, 126, 187)
cIcecream = (150, 0, 0)

cHooman = (200, 200, 200)

def wline(xb, yb, xe, ye, color, width):
    line(screen, color, (xb, yb), (xe, ye), width)
def wrect (xLU, yLU, xRD, yRD, color, width):
    rect(screen, color, (xLU, yLU, xRD - xLU, yRD - yLU), width)
def wpolygon (xLU, yLU, xLD, yLD, xRD, yRD, xRU, yRU, color, width):
    polygon(screen, color, [(xLU,yLU), (xLD,yLD), (xRD,yRD), (xRU,yRU)], width)
def wcircle (x, y, R, color, width):
    circle(screen, color, (x, y), R, width)

wrect(0, 200, 400, 400, cBlue, 0) #фон
wrect(0, 0, 400, 200, cGreen, 0)

wline(140, 240, 140, 350, cBlack, 2) #ноги парня
wline(140, 350, 120, 350, cBlack, 2)
wline(160, 240, 160, 350, cBlack, 2)
wline(160, 350, 180, 350, cBlack, 2)
wline(200, 160, 200, 230, cBlack, 2) #руки парня
wline(100, 160, 80, 230, cBlack, 2)
wcircle(150, 240, 50, cGrey, 0) #тело парня
wcircle(150, 160, 50, cGrey, 0)
wcircle(150, 100, 30, cHooman, 0) #голова парня

wline(240, 240, 240, 350, cBlack, 2) #ноги девушки
wline(240, 350, 220, 360, cBlack, 2)
wline(260, 240, 260, 350, cBlack, 2)
wline(260, 350, 280, 360, cBlack, 2)
wline(240, 130, 200, 230, cBlack, 2) #руки девушки
wline(260, 130, 300, 230, cBlack, 2)
wpolygon(250, 100, 200, 300, 300, 300, 250, 100, cPink, 0) #тело девушки
wcircle(250, 100, 30, cHooman, 0) #голова девушки

wpolygon(85, 230, 65, 200, 75, 150, 85, 230, cIcecream, 0) #мороженое
wcircle(70, 190, 10, cRed, 0)

wline(290, 240, 320, 100, cWhite, 2) #шарик
wpolygon(320, 100, 300, 60, 340, 60, 320, 100, cRed, 0)
wcircle(310, 60, 10, cRed, 0)
wcircle(330, 60, 10, cRed, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
