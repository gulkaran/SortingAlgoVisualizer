import pygame
import random

pygame.font.init()
# Window Size / Settings / Title / Icon
WIDTH = 900
HEIGHT = 650
win_size = (WIDTH, HEIGHT)
window = pygame.display.set_mode(win_size)
icon = pygame.image.load("img/neural.png")
pygame.display.set_icon(icon)

pygame.display.set_caption('Sorting Algorithm Visualization')

# variable run - while loop to keep python window open
run = True
click = False

# colour settings
array_colour = [(0, 147, 22)]*151
colour_ind = 0
colour = [(255, 255, 255), (255, 0, 0),
          (0, 148, 255), (0, 147, 22)]
font = pygame.font.SysFont("Cambria", 18)
font2 = pygame.font.SysFont("Cambria", 15)
font3 = pygame.font.SysFont("Cambria", 60)
font4 = pygame.font.SysFont("Cambria", 25)

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
    pygame.time.delay(3)


def window_update2():
    window.fill((0, 0, 0))
    draw2()
    pygame.display.update()
    pygame.time.delay(3)

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
        window_update2()
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
        window_update2()
        array_colour[x] = colour[0]
        temp.append(array[x])
        x += 1
    while y <= y2:
        array_colour[y] = colour[1]
        window_update2()
        array_colour[y] = colour[0]
        temp.append(array[y])
        y += 1
    z = 0
    for x in range(x1, y2 + 1):
        pygame.event.pump()
        array[x] = temp[z]
        z += 1
        array_colour[x] = colour[2]
        window_update2()
        if y2-x1 == len(array)-2:
            array_colour[x] = colour[3]
        else:
            array_colour[x] = colour[0]

# quick sort algo


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
def draw():  # quick sort
    text = font.render("Press 'W' To Start Sorting",
                       1, (255, 255, 255))
    window.blit(text, (20, 20))

    text2 = font.render("Press 'Q' To Generate New Array",
                        1, (255, 255, 255))
    window.blit(text2, (20, 40))
    text3 = font3.render("Quick Sort",
                         1, (255, 255, 255))
    window.blit(text3, (600, 10))
    text4 = font.render("Press 'ESCAPE' To Go Back",
                        1, (255, 255, 255))
    window.blit(text4, (20, 60))
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


def draw2():
    text = font.render("Press 'W' To Start Sorting",
                       1, (255, 255, 255))
    window.blit(text, (20, 20))

    text2 = font.render("Press 'Q' To Generate New Array",
                        1, (255, 255, 255))
    window.blit(text2, (20, 40))
    text3 = font3.render("Merge Sort",
                         1, (255, 255, 255))
    window.blit(text3, (575, 10))
    text4 = font.render("Press 'ESCAPE' To Go Back",
                        1, (255, 255, 255))
    window.blit(text4, (20, 60))
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


def mergeoption():
    running = True
    while running:  # arrays
        # background
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    generate_array()
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    mergesort(array, 1, len(array) - 1)
        draw2()
        pygame.display.update()


def quicksortoption():
    runnin = True
    while runnin:  # arrays
        # background
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnin = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    generate_array()
                elif event.key == pygame.K_ESCAPE:
                    runnin = False
                if event.key == pygame.K_w:
                    sort(array, 1, len(array) - 1)
        draw()
        pygame.display.update()


def mainmenu():
    x = True
    while x:  # arrays
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        hover_colour = (56, 56, 56)
        button1 = pygame.Rect(260, 350, 400, 75)
        button2 = pygame.Rect(260, 450, 400, 75)
        button3 = pygame.Rect(263, 353, 394, 69)
        button4 = pygame.Rect(263, 453, 394, 69)
        pygame.draw.rect(window, "white", button1)
        pygame.draw.rect(window, "white", button2)
        pygame.draw.rect(window, "black", button3)
        pygame.draw.rect(window, "black", button4)

        if button1.collidepoint((mx, my)):
            if click:
                quicksortoption()
            else:
                pygame.draw.rect(window, hover_colour, button3)
        elif button2.collidepoint((mx, my)):
            if click:
                mergeoption()
            else:
                pygame.draw.rect(window, hover_colour, button4)

        title = font3.render("Sorting Algorithm Visualizer", 1, "white")
        window.blit(title, (60, 200))

        credits = font.render("Created By: Gulkaran Singh", 1, "white")
        window.blit(credits, (347, 290))

        button_text = font4.render("Quick Sort", 1, "white")
        window.blit(button_text, (392, 372))

        button_text2 = font4.render("Merge Sort", 1, "white")
        window.blit(button_text2, (390, 472))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    generate_array()
                if event.key == pygame.K_w:
                    mergesort(array, 1, len(array) - 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


mainmenu()
pygame.quit()
