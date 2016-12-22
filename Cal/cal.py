import pygame, sys, random, time, os

rocket_images = ["ship.jpg"]


class RocketClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.getcwd(),"ship.jpg"))
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -9: self.angle = -9
        if self.angle > 9: self.angle = 9
        center = self.rect.center
        self.image = pygame.image.load(rocket_images[0])
        self.rect.center = center
        speed = [self.angle, 9 - abs(self.angle) * 2]

        return speed

    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 1620: self.rect.centerx = 620


class StuffClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type, num=1):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False
        self.num = num

    def update(self):
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery < -32:
            self.kill()
        if self.type == "laser":
            self.rect.centery -= speed[0] * self.num + 1


def create_map(starNum, rockNum, enemyNum):
    global obstacles
    locations = []
    # Star spawnner
    for i in range(starNum):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 164 + 32, row * 164 + 32 + 1640]
        if not (location in locations):
            locations.append(location)
            img = "images.png"
            obstacle = StuffClass(img, location, "star")
            obstacles.add(obstacle)

    # r s
    for i in range(rockNum):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 164 + 32, row * 164 + 32 + 1640]
        if not (location in locations):
            locations.append(location)
            img = "latest-1.png"
            obstacle = StuffClass(img, location, "rock")
            obstacles.add(obstacle)

    # e s
    for i in range(enemyNum):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 164 + 32, row * 164 + 32 + 1640]
        if not (location in locations):
            locations.append(location)
            img = "enemy.png"
            obstacle = StuffClass(img, location, "enemy")
            obstacles.add(obstacle)
            img = "lazer.jpg"
            for laser in range(10):
                obstacle = StuffClass(img, location, "laser", laser)
                obstacles.add(obstacle)


def animate():
    screen.fill([255, 255, 255])
    obstacles.draw(screen)
    screen.blit(rocket.image, rocket.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode([1640, 1640])
clock = pygame.time.Clock()
rocket = RocketClass()
speed = [0, 6]
obstacles = pygame.sprite.Group()
map_position = 0
lives = 2
points = 0

starNum = 7
rockNum = 3
enemyNum = 1

create_map(starNum, rockNum, enemyNum)
font = pygame.font.Font(None, 50)

level = 1

running = True
# while running:
while lives > 0:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = rocket.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = rocket.turn(1)
        rocket.move(speed)

    map_position += speed[1]
    #   map_position+=8
    if map_position >= 640:
        create_map(starNum, rockNum, enemyNum)
        map_position = 0

    hit = pygame.sprite.spritecollide(rocket, obstacles, False)

    if hit:
        if hit[0].type == "rock" and not hit[0].passed:
            lives = lives - 1
            rocket.image = pygame.image.load("explosion3.png")
            animate()
            pygame.time.delay(1000)
            rocket.image = pygame.image.load("ship.jpg")
            rocket.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "star" and not hit[0].passed:
            points += 10
            hit[0].kill()
        elif hit[0].type == "enemy" and not hit[0].passed:
            lives = lives - 1
            rocket.image = pygame.image.load("explosion3.png")
            hit[0].kill()
            animate()
            pygame.time.delay(1000)
            rocket.image = pygame.image.load("ship.jpg")
            rocket.angle = 0
            speed = [0, 6]
            hit[0].passed = True


        elif hit[0].type == "laser" and not hit[0].passed:
            lives = lives - 1
            rocket.image = pygame.image.load("explosion3.png")
            hit[0].kill()
            animate()
            pygame.time.delay(1000)
            rocket.image = pygame.image.load("ship.jpg")
            rocket.angle = 0
            speed = [0, 6]
            hit[0].passed = True

    obstacles.update()
    score_text = font.render("Score: " + str(points) + "  Lives: " + str(lives) + "   LV" + str(level), 1, (0, 0, 0))
    animate()

    # Code for level 2 start

    if points >= 100 and points < 200:
        if level == 1:
            lives += 2
        level = 2
        starNum = 5
        rockNum = 5
        enemyNum = 2

    # lv3
    if points >= 200 and points < 300:
        if level == 2:
            lives += 2
        level = 3
        starNum = 5
        rockNum = 6
        enemyNum = 2

    if points >= 300 and points < 400:
        if level == 3:
            lives += 2
        level = 4
        starNum = 5
        rockNum = 7
        enemyNum = 2

    if points >= 400 and points < 500:
        if level == 4:
            lives += 2
        level = 5
        starNum = 5
        rockNum = 8
        enemyNum = 3

    if points >= 500 and points < 600:
        if level == 5:
            lives += 2
        level = 6
        starNum = 50
        rockNum = 9
        enemyNum = 4

    if points >= 600 and points < 999:
        if level == 6:
            lives += 2
        level = "BONUS"
        starNum = 99
        rockNum = 0

score_text = font.render("suny boy!", 1, (0, 0, 0))

animate()
time.sleep(5)
pygame.quit()


'''

Level 1:    obstacles- more stars less rocks
            100 points to level up

Level 2:    obstacles- even stars and rocks
            200 points to level up

Level 3:    obstacles- more rocks than stars
            300 points to win

message box in between each level to signal level change
message box at end to signal you've won or lost.
Option to play again or quit.


Machine gun lasers!!!!

create good lazers-var: goodLazers
crate ob of type gl
add ob to goodLazers

ob going downwards at twice speed of enemy lasers
instead of hit var use kill var and have a condition of impact
with goodLazer and obstacles. :-)
 . .
  |
[___]


'''
