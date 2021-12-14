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
    pygame.time.delay(5)

# quicksort algo
def sort(array, L, R):
    if L < R:
        div = divide(array, L, R)
        sort(array, L, div - 1)
        window_update()
        for i in range(0, div + 1):
            array_colour[i] = colour[3]
        sort(array, div + 1, R)

# dividing the array
def divide(array, low, high):
    pygame.event.pump()
    pivot = array[high]
    array_colour[high] = colour[2]
    x = low - 1
    for y in range(low, high):
        array_colour[y] = colour[1]
        window_update()
        array_colour[high] = colour[2]
        array_colour[y] = colour[0]
        array_colour[x] = colour[0]
        if array[y] > pivot:
            x += 1
            array_colour[x] = colour[1]
            array[x], array[y] = array[y], array[x]
    window_update()
    array_colour[x] = colour[0]
    array_colour[high] = colour[0]
    array[x + 1], array[high] = array[high], array[x + 1]

    return (x + 1)

# draw function
def draw():
    text = font.render("Press 'W' To Start Sorting",
                       1, (255, 255, 255))
    window.blit(text, (20, 20))

    text2 = font.render("Press 'Q' To Generate New Array",
                       1, (255, 255, 255))
    window.blit(text2, (20, 40))
    text3 = font2.render("Algorithm Used: Quick Sort",
                       1, (255, 255, 255))
    window.blit(text3, (20, 60))

    object_width = (WIDTH - 150) // 150
    boundary_array = 900 / 150
    boundary_group = 550 / 100
    pygame.draw.line(window, (0, 0, 0),
                     (0, 95), (900, 95), 6)

    for x in range(1, 150):
        pygame.draw.line(window,
                         array_colour[x], (boundary_array * x - 3, 1000),
                         (boundary_array * x - 3,
                          array[x] * boundary_group - -100),
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
                sort(array, 1, len(array) - 1)
    draw()
    pygame.display.update()
pygame.quit()






