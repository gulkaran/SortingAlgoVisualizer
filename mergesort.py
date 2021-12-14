import pygame
import random

pygame.font.init()
# Window Size / Settings / Title / Icon
WIDTH = 900
HEIGHT = 650
win_size = (WIDTH, HEIGHT)
window = pygame.display.set_mode(win_size)
icon = pygame.image.load("img/ascending-sort.png")
pygame.display.set_icon(icon)

pygame.display.set_caption('Quick Sorting Visualization')

# variable run - while loop to keep python window open
run = True

# colour settings
array_colour = [(0, 147, 22)]*151
colour_ind = 0
colour = [(255, 255, 255), (255, 0, 0),
          (0, 148, 255), (0, 147, 22)]
font = pygame.font.SysFont("Cambria", 17)
font2 = pygame.font.SysFont("Cambria", 15)

array = [0]*151

# generating array function
def generate_array():
    for i in range(1, 151):
        array_colour[i] = colour[0]
        array[i] = random.randrange(1, 100)
generate_array()

# updates on window
def window_update():
    window.fill((0, 0, 0))
    draw()
    pygame.display.update()
    pygame.time.delay(0)

# merge sort algo
def mergesort(array, L, R):
    middle = (L + R)//2
    if L < R:
        mergesort(array, L, middle)
        mergesort(array, middle + 1, R)
        merge(array, L, middle,
            middle + 1, R)
def merge(array, x1, y1, x2, y2):
    x = x1
    y = x2
    temp = []
    pygame.event.pump()
    while x <= y1 and y <= y2:
        array_colour[x] = colour[1]
        array_colour[y] = colour[1]
        window_update()
        array_colour[x] = colour[0]
        array_colour[y] = colour[0]
        if array[x] > array[y]:
                temp.append(array[x])
                x += 1
        else:
                temp.append(array[y])
                y += 1
    while x <= y1:
        array_colour[x] = colour[1]
        window_update()
        array_colour[x] = colour[0]
        temp.append(array[x])
        x += 1
    while y <= y2:
        array_colour[y] = colour[1]
        window_update()
        array_colour[y] = colour[0]
        temp.append(array[y])
        y += 1
    z = 0
    for x in range(x1, y2 + 1):
        pygame.event.pump()
        array[x] = temp[z]
        z += 1
        array_colour[x] = colour[2]
        window_update()
        if y2-x1 == len(array)-2:
            array_colour[x] = colour[3]
        else:
            array_colour[x] = colour[0]




# draw function
def draw():
    text = font.render("Press 'W' To Start Sorting",
                       1, (255, 255, 255))
    window.blit(text, (20, 20))

    text2 = font.render("Press 'Q' To Generate New Array",
                       1, (255, 255, 255))
    window.blit(text2, (20, 40))
    text3 = font2.render("Algorithm Used: Merge Sort",
                       1, (255, 255, 255))
    window.blit(text3, (20, 60))

    object_width = (WIDTH - 150) // 150
    boundary_array = 900 / 150
    boundary_group = 550 / 100
    pygame.draw.line(window, (0, 0, 0),
                     (0, 95), (900, 95), 6)

    for i in range(1, 150):
        pygame.draw.line(window,
                         array_colour[i], (boundary_array * i - 3, 1000),
                         (boundary_array * i - 3,
                          array[i] * boundary_group - -100),
                         object_width)


while run:
    # background
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                generate_array()
            if event.key == pygame.K_w:
                mergesort(array, 1, len(array) - 1)
    draw()
    pygame.display.update()
pygame.quit()






