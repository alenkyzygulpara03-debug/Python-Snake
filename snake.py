import pygame
import random

pygame.init()

# Терезе өлшемдері
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Түстер
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Жылдамдық
clock = pygame.time.Clock()

# Жыланның бастапқы позициясы
snake = [(300, 200), (290, 200), (280, 200)]
direction = "RIGHT"

# Тамақ
food = (
    random.randrange(0, WIDTH, 10),
    random.randrange(0, HEIGHT, 10)
)

score = 0
running = True

# === ОСЫ ЖЕРДЕН БАСТАП ЖАҢА КОДТЫ ҚОСАСЫЗ ===
# Басты ойын циклі
while running:
    # 1. Оқиғаларды тексеру (мысалы, терезені жабу немесе батырмаларды басу)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # 2. Жыланның қозғалысы
    head_x, head_y = snake[0]
    if direction == "RIGHT":
        head_x += 10
    elif direction == "LEFT":
        head_x -= 10
    elif direction == "UP":
        head_y -= 10
    elif direction == "DOWN":
        head_y += 10
        
    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    # Тамақты жегенін тексеру
    # Жылан мен тамақтың өлшемдері сәйкес келуі үшін жуықтау
    if abs(head_x - food[0]) < 10 and abs(head_y - food[1]) < 10:
        score += 1
        food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
    else:
        snake.pop() # Егер тамақ жемесе, құйрығын қысқарту (қозғалыс эффектісі)

    # 3. Қабырғаға немесе өзіне соғылуын тексеру (Ойынның бітуі)
    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or 
        new_head in snake[1:]):
        running = False

    # 4. Экранды суреттеу
    screen.fill(BLACK) # Экранды тазалау
    
    # Тамақты салу
    pygame.draw.rect(screen, RED, (food[0], food[1], 10, 10))
    
    # Жыланды салу
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))

    pygame.display.flip() # Экранды жаңарту
    clock.tick(15) # Ойын жылдамдығы (FPS)

pygame.quit()
