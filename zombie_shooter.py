from ast import walk
from sre_constants import JUMP
import pygame, random
pygame.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

CHARACTER_WIDTH, CHARACTER_HEIGHT = 100, 145
VEL = 5
RED = (255, 0, 0)
MAX_BULLETS = 5
BULLET_VEL = 7
black = (0, 0, 0)
LOST_FONT = pygame.font.SysFont('comicsans', 100)

background = pygame.transform.scale(pygame.image.load('fotos/background.png'), (1000, 1100))

laserbeam = pygame.transform.scale(pygame.image.load('fotos/laserbeam.png'), (20, 7))

rocket_image = [pygame.image.load('fotos/rocket.png'),
pygame.transform.rotate(pygame.image.load('fotos/rocket.png'),180),
pygame.transform.rotate(pygame.image.load('fotos/rocket.png'),270),
pygame.transform.rotate(pygame.image.load('fotos/rocket.png'),90)]

grass = pygame.image.load('fotos/grass.png')
grass_floor = pygame.transform.scale(pygame.image.load('fotos/grass_floor.png'), (WIDTH, 100))

character_standard_image_R = pygame.transform.scale(pygame.image.load('fotos/character_R.png'), (CHARACTER_WIDTH, 145))
character_standard_image_L = pygame.transform.scale(pygame.image.load('fotos/character_L.png'), (CHARACTER_WIDTH, 145))

character_animations_left = [pygame.transform.scale(pygame.image.load('fotos/CL1.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL2.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL3.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL4.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL5.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL6.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL7.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL8.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CL9.png'), (CHARACTER_WIDTH, 145))]

character_animations_right = [pygame.transform.scale(pygame.image.load('fotos/CR1.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR2.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR3.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR4.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR5.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR6.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR7.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR8.png'), (CHARACTER_WIDTH, 145)),
pygame.transform.scale(pygame.image.load('fotos/CR9.png'), (CHARACTER_WIDTH, 145))]

enemy_width, enemy_height = 170, 125
walkcount_enemy = 0
walkCount = 0
VEL_enemy = 2
health = 100
health_enemy = 100

walkLeft = [
pygame.transform.scale(pygame.image.load('fotos/Enemy/L1E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L2E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L3E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L4E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L5E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L6E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L7E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L8E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/L9E.png'), (enemy_width, enemy_height))
]
walkRight = [
pygame.transform.scale(pygame.image.load('fotos/Enemy/R1E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R2E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R3E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R4E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R5E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R6E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R7E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R8E.png'), (enemy_width, enemy_height)),
pygame.transform.scale(pygame.image.load('fotos/Enemy/R9E.png'), (enemy_width, enemy_height))
]



def draw(character, LEFT, RIGHT, JUMP, LEFT_JUMP, RIGHT_JUMP, start, bullets_left, bullets_right, floor1, floor3, floor, floor2, floor4, floor5, healthbar,
 healthbar_health, healthbar_enemy, healthbar_health_enemy, enemies,enemy):
    WIN.blit(background, (0, 0))

    WIN.blit(grass_floor, (floor.x, floor.y))
    WIN.blit(grass, (floor1.x, floor1.y))
    WIN.blit(grass, (floor2.x, floor2.y))
    WIN.blit(grass, (floor3.x, floor3.y))
    WIN.blit(grass, (floor4.x, floor4.y))
    WIN.blit(grass, (floor5.x, floor5.y))

    global walkcount_enemy, walkCount, health

    if len(enemies) > 0:

        for enemy in enemies:
            if walkcount_enemy + 1 >=11:
                walkcount_enemy = 0

            if enemy.colliderect(floor3):
                WIN.blit(walkRight[walkcount_enemy//3], (enemy.x-50, enemy.y))
                enemy.x += VEL_enemy
                walkcount_enemy += 1
            elif (character.x - enemy.x < 20) and not(enemy.colliderect(character)):
                WIN.blit(walkLeft[walkcount_enemy//3], (enemy.x-50, enemy.y))
                if enemy.colliderect(floor) or enemy.colliderect(floor1) or enemy.colliderect(floor2) or enemy.colliderect(floor3) or enemy.colliderect(floor4) or enemy.colliderect(floor5):
                    enemy.x -= VEL_enemy
                    walkcount_enemy += 1
                else:
                    enemy.y += 10
                    walkcount_enemy += 1
            elif (character.x - enemy.x > -20) and not(enemy.colliderect(character)):
                WIN.blit(walkRight[walkcount_enemy//3], (enemy.x, enemy.y))
                if enemy.colliderect(floor) or enemy.colliderect(floor1) or enemy.colliderect(floor2) or enemy.colliderect(floor3) or enemy.colliderect(floor4) or enemy.colliderect(floor5):
                    enemy.x += VEL_enemy
                    walkcount_enemy += 1
                else:
                    enemy.y += 10
                    walkcount_enemy += 1
            elif enemy.colliderect(character) and (character.x - enemy.x < 20):
                health -= 5
                WIN.blit(walkLeft[0], (enemy.x-50, enemy.y))
            elif enemy.colliderect(character) and (character.x - enemy.x > -20):
                health -= 5
                WIN.blit(walkRight[6], (enemy.x, enemy.y))
            if health_enemy > 0:
                pygame.draw.rect(WIN, black, healthbar_enemy)
                pygame.draw.rect(WIN, RED, healthbar_health_enemy)

    pygame.draw.rect(WIN, black, healthbar)
    pygame.draw.rect(WIN, RED, healthbar_health)

    if walkCount + 1 >=9:
        walkCount = 0

    if LEFT:
        WIN.blit(character_animations_left[walkCount//3], (character.x, character.y))
        walkCount += 1
    elif RIGHT:
        WIN.blit(character_animations_right[walkCount//3], (character.x, character.y))
        walkCount += 1
    elif JUMP:
        if LEFT_JUMP:
            WIN.blit(character_standard_image_L, (character.x, character.y))
            LEFT_JUMP = False
        elif RIGHT_JUMP:
            WIN.blit(character_standard_image_R, (character.x, character.y))
            RIGHT_JUMP = False
        else:
            WIN.blit(character_standard_image_L, (character.x, character.y))
    else:
        if LEFT_JUMP:
            WIN.blit(character_standard_image_L, (character.x, character.y))
            LEFT_JUMP = False
        elif RIGHT_JUMP:
            WIN.blit(character_standard_image_R, (character.x, character.y))
            RIGHT_JUMP = False
    if start:
        WIN.blit(character_standard_image_L, (character.x, character.y))

    for bullet in bullets_left:
        WIN.blit(laserbeam, (bullet.x, bullet.y))
    for bullet in bullets_right:
        WIN.blit(laserbeam, (bullet.x, bullet.y))

    pygame.display.update()

def handle_bullets(bullets_left, bullets_right, enemies, enemy):
    global health_enemy
    for bullet in bullets_left:
        if not(bullet.colliderect(enemy)):
            bullet.x -= BULLET_VEL
        elif len(enemies) == 0:
            bullet.x -= BULLET_VEL
        if bullet.x < 0:
            bullets_left.remove(bullet)
        if bullet.colliderect(enemy) and len(enemies) > 0:
            if health_enemy > 0:
                health_enemy -= 10
                bullets_left.remove(bullet)
            elif health_enemy == 0 and len(enemies) > 0:
                enemies.remove(enemy)
            else:
                bullets_left.remove(bullet)

    for bullet in bullets_right:
        if not(bullet.colliderect(enemy)):
            bullet.x += BULLET_VEL
        elif len(enemies) == 0:
            bullet.x += BULLET_VEL
        if bullet.x > WIDTH:
            bullets_right.remove(bullet)
        if bullet.colliderect(enemy) and len(enemies) > 0:
            if health_enemy > 0:
                health_enemy -= 10
                bullets_right.remove(bullet)
            elif health_enemy == 0 and len(enemies) > 0:
                enemies.remove(enemy)
            else:
                bullets_right.remove(bullet)

def lose():
    draw_text = LOST_FONT.render('You lost', 1, black)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def rocket_fire(rockets, enemy, enemies):
    global health_enemy
    for rocket in rockets:
        if not (rocket.colliderect(enemy)) and enemy.y - rocket.y <= 10:
            rocket.y -= 10
            WIN.blit(rocket_image[0], (rocket.x, rocket.y))
        elif not (rocket.colliderect(enemy)) and enemy.y - rocket.y >= 20:
            rocket.y += 10
            WIN.blit(rocket_image[1], (rocket.x, rocket.y))
        elif not (rocket.colliderect(enemy)) and enemy.x - rocket.x > 0:
            rocket.x += 10
            WIN.blit(rocket_image[2], (rocket.x, rocket.y))
        elif not (rocket.colliderect(enemy)) and enemy.x - rocket.x < 0:
            rocket.x -= 10
            WIN.blit(rocket_image[3], (rocket.x, rocket.y))
        elif rocket.colliderect(enemy):
            health_enemy -= 100
            rockets.remove(rocket)
            enemies.remove(enemy)
        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    LEFT = False
    RIGHT = False
    JUMP = False
    jumpCount = 10
    LEFT_JUMP = False
    RIGHT_JUMP = False
    start = True
    bullets_left = []
    bullets_right = []
    enemies = []

    character = pygame.Rect(WIDTH/2-CHARACTER_WIDTH//2, 820, CHARACTER_WIDTH, 125) 
    floor = pygame.Rect(0, HEIGHT - 60, WIDTH, 100)
    floor1 = pygame.Rect(WIDTH - 300, 760, 300, 20)
    floor2 = pygame.Rect(0, 760, 300, 20)
    floor3 = pygame.Rect(WIDTH/2 - 150, 560, 300, 20)
    floor4 = pygame.Rect(WIDTH - 300, 360, 300, 20)
    floor5 = pygame.Rect(0, 360, 300, 20)

    x_coord = [100,900]
    y_coord = [830, 650, 249]
        
    enemy = pygame.Rect(random.choice(x_coord), random.choice(y_coord), enemy_width - 50, enemy_height)

    enemies.append(enemy)

    rockets = []
    rocket = pygame.Rect(character.x + CHARACTER_WIDTH/2, character.y - CHARACTER_HEIGHT, 35, 100)

    while run:
        clock.tick(27) 

        if len(enemies) == 0:
            enemy = pygame.Rect(random.choice(x_coord), random.choice(y_coord), enemy_width, enemy_height)
            global health_enemy
            health_enemy = 100
            enemies.append(enemy)

        healthbar = pygame.Rect(character.x, character.y - 30, 104, 15)
        healthbar_health = pygame.Rect(character.x + 2, character.y - 28, health, 11)
        healthbar_enemy = pygame.Rect(enemy.x + 10, enemy.y - 30, 104, 15)
        if health_enemy > 0:
            healthbar_health_enemy = pygame.Rect(enemy.x + 12, enemy.y - 28, health_enemy, 11)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and len(bullets_left)  < MAX_BULLETS and len(bullets_right) < MAX_BULLETS:
                    if LEFT_JUMP:
                        bullet = pygame.Rect(character.x, character.y + 7 + CHARACTER_HEIGHT / 2, 20, 7)
                        bullets_left.append(bullet)
                    elif RIGHT_JUMP:
                        bullet = pygame.Rect(character.x + 100, character.y + 7 + CHARACTER_HEIGHT / 2, 20, 7)
                        bullets_right.append(bullet)
                elif event.button == 3 and len(rockets) < 1:
                    rocket = pygame.Rect(character.x + CHARACTER_WIDTH/2, character.y - CHARACTER_HEIGHT + 120, 35, 100)
                    rockets.append(rocket)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and character.x + VEL >= 0:
            character.x -= VEL
            LEFT = True
            RIGHT = False
            LEFT_JUMP = True
            RIGHT_JUMP = False
            start = False
        if keys[pygame.K_d] and character.x + VEL <= WIDTH-CHARACTER_WIDTH:
            character.x += VEL
            LEFT = False
            RIGHT = True
            LEFT_JUMP = False
            RIGHT_JUMP = True
            start = False
        if keys[pygame.K_SPACE]:
            JUMP = True
            LEFT = False
            RIGHT = False
            start = False
        if JUMP:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    if not(character.colliderect(floor1)) and not(character.colliderect(floor3)) and not(character.colliderect(floor)) and not(character.colliderect(floor2)) and not(character.colliderect(floor4)) and not(character.colliderect(floor5)):
                        neg = -1
                    elif character.colliderect(floor1) or character.colliderect(floor3) or character.colliderect(floor) or character.colliderect(floor2) or character.colliderect(floor4) or character.colliderect(floor5):
                        neg = 0
                character.y -= (jumpCount ** 2) * 0.7 * neg
                jumpCount -= 1
            else:
                JUMP = False
                jumpCount = 10
                if character.colliderect(floor1) or character.colliderect(floor2):
                    character.y = 640
                if character.colliderect(floor3):
                    character.y = 439
                if character.colliderect(floor):
                    character.y = 820
                if character.colliderect(floor4) or character.colliderect(floor5):
                    character.y = 239
        
        if not(character.colliderect(floor1)) and  not(character.colliderect(floor3)) and not(character.colliderect(floor)) and not(character.colliderect(floor2)) and not(character.colliderect(floor4)) and not(character.colliderect(floor5)):
            character.y += 10

        handle_bullets(bullets_left,bullets_right, enemies, enemy)
        draw(character, LEFT, RIGHT, JUMP, LEFT_JUMP, RIGHT_JUMP, start, bullets_left, bullets_right, floor1, floor3, floor, floor2, floor4, floor5,
         healthbar,healthbar_health, healthbar_enemy, healthbar_health_enemy, enemies, enemy)
        rocket_fire(rockets, enemy, enemies)

        LEFT = False
        RIGHT = False

        if health <= 0:
            lose()
            break

if __name__ == '__main__':
    main()
    