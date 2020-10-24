import pygame

from pygame.draw import *

pygame.init()

FPS = 10
screen_width = 1300
screen_height = 800
body_width = 100
body_height = 200
head_radius = 40
horn_width = 40
horn_height = 80
heart_width = 80
heart_height = 80

BLACK = (0, 0, 0)
MAN_COLOR = (192, 126, 187)
WOMAN_COLOR = (255,0,255)
HEAD_COLOR = (200,200,200)
HORN_COLOR = (236, 128, 19)
ICE_BALL_COLORS = ((30, 30, 250), (255, 255, 255), (255, 42, 19), (100, 30, 30))
HEART_COLOR = (240, 19, 42)

screen = pygame.display.set_mode((screen_width, screen_height))


def draw_background(width, height):
    '''
        draw_background(width, height) -> void
        function draws background
        width, heighr -- width and height of it (better use screen_height and screen_width)
    '''
    rect(screen,(166, 241, 160),(0,0,width, height)) #sky
    rect(screen,(138, 170, 232),(0,0,width, 7 * height // 16))    #earth


def draw_person(width, height, radius, gender, hands_types, x, y):
    '''
        draw_person(width, height, radius, gender, hands_types, x, y) -> void
        function draws human
        width, height -- width and height of bodyes
        radius -- radius of head
        gender -- 0 - male, 1 - female
        hands_types -- (0,0) -> /0\; (1,0) -> ˅0\, (0,1) -> /0˅; (1,1) -> ˅0˅
        x, y -- coordinates of 'neck' - top point of body's shape
        top point -- (x, y - 1.9 * height), bottom point -- (x +- (0.35 + 0.125 * gender) * width, y + 2.5 width)
        right and left points -- (x +- 0.45 * height, y + 0.05 * height) - hands_type = 1
        right and left points -- (x +- 0.45 * height, y + 0.45 * height) - hands_type = 0
    '''
    body_left_corner_x = x - width // 2
    body_left_corner_y = y
    head_center_x = x
    head_center_y = y - 9 * radius // 10

    legs = ((0.15 + gender * 0.25, 1), (0.4 + gender * 0.25, 2), (0.7 + gender * 0.25, 2))
    hands = ((0, 0.05), (0.3, 0.25), (0.6, 0.45))
    
    for i in range(2):
        line(screen, BLACK, (x + int(0.5 * width * legs[i][0]), y + int(0.75 * height * legs[i][1])), #right leg
                             (x + int(0.5 * width * legs[i + 1][0]), y + int(0.75 * height * legs[i + 1][1])))
        
        line(screen, BLACK, (x - int(0.5 * width * legs[i][0]), y + int(0.75 * height * legs[i][1])), #left leg
                             (x - int(0.5 * width * legs[i + 1][0]), y + int(0.75 * height * legs[i + 1][1])))
        
        line( screen, BLACK, (x + int(height * hands[i][0]), y + int(height * hands[i][1])), #right hand
                              (x + int(height * hands[i + 1][0]), y + int((1 - 8 / 9 * (i and hands_types[0])) * height * hands[i + 1][1])))

        line( screen, BLACK, (x - int(height * hands[i][0]), y + int(height * hands[i][1])), #left hand
                              (x - int(height * hands[i + 1][0]), y + int((1 - 8 / 9 * (i and hands_types[1])) * height * hands[i + 1][1])))

     
    if not gender: #body, depends on gender
        ellipse(screen, MAN_COLOR, (body_left_corner_x, body_left_corner_y, width, height))
    else:
        polygon(screen, WOMAN_COLOR, ((body_left_corner_x, body_left_corner_y + height),
                                      (body_left_corner_x + width // 2, body_left_corner_y),
                                      (body_left_corner_x + width, body_left_corner_y + height)))

    circle(screen,HEAD_COLOR,(head_center_x, head_center_y),radius) #head


def draw_ice_cream(width, height, color0, color1, color2, color3, x, y):
    '''
        draw_ice_cream(width, height, color0, color1, color2, color3, x, y) -> void
        function draws ice cream
        width, height -- width and height of horn
        color0 -- color of horn
        color1, color2, color3 - colors of balls
        x, y - coordinates of bottom of horn
        top point (x + 0.35 * width, y - 2.2 * height)
        left and right points (x - 0.575 * width, y - height), (x + 0.8 * width, y - 1.2 * height)
    '''
    radius = 9 * width // 20
    polygon(screen, color0, ((x, y), (x - 3 * width // 8, y - height), (x + 5 * width // 8, y - 7 * height // 8), (x, y)))
    circle(screen, color1, (x - width // 8, y - height), radius)
    circle(screen, color2, (x + 3 * width // 5, y - 9 * height // 10), radius)
    circle(screen, color3, (x + 7 * width // 20, y - 12 * height // 10), radius)


def draw_heart(width, height, color, x, y):
    '''
        draw_heart(width, height, color, x, y) -> void
        function draws heart
        width, height -- width and height of 'horn' of heart
        color0 -- color of heart
        x, y - coordinates of bottom of heart
        top point (x + 0.25 * width, y - 1.26 * height)
        left and right points (x - 0.01 * width, y - height), (x + 0.51 * width, y - height)
    '''
    polygon(screen, HEART_COLOR, ((x, y), (x - width // 2, y - height), (x + width // 2, y - height), (x, y)))
    circle(screen, HEART_COLOR, (x + width // 4, y - height), 13 * width // 50)
    circle(screen, HEART_COLOR, (x - width // 4, y - height), 13 * width // 50)



draw_background(screen_width, screen_height)

draw_person(body_width, body_height, head_radius, 0,(0,0), 300, 400)
draw_person(body_width, body_height, head_radius, 1,(1,0), 540, 400)
draw_person(body_width, body_height, head_radius, 1,(0,1), 780, 400)
draw_person(body_width, body_height, head_radius, 0,(0,0), 1020, 400)

draw_ice_cream(horn_width, horn_height,HORN_COLOR,ICE_BALL_COLORS[1], ICE_BALL_COLORS[2], ICE_BALL_COLORS[3], 620, 320)
draw_ice_cream(horn_width, horn_height,HORN_COLOR,ICE_BALL_COLORS[1], ICE_BALL_COLORS[0], ICE_BALL_COLORS[3], 1140, 490)
draw_heart(heart_width, heart_height, HEART_COLOR, 160, 400)

aaline(screen, BLACK, (660, 410), (620, 320))
aaline(screen, BLACK, (180, 490), (160, 400))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
