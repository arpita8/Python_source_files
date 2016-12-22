import pygame, sys, random, time
#"sound for the game"
pygame.mixer.init()
pygame.mixer.music.load("game3.mp3")
pygame.mixer.music.play(-1)
splat = pygame.mixer.Sound("boom.mp3")




"""hit = pygame.mixer.Sound("boom.mp3")"""
rocket_images = ["ship.jpg"]

class RocketClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.image.load("ship.jpg")
        self.rect=self.image.get_rect()
        self.rect.center=[320,100]
        self.angle=0

    def turn(self, direction):
        self.angle=self.angle+direction
        if self.angle < -7: self.angle = -7
        if self.angle > 7: self.angle = 7
        center=self.rect.center
        self.image=pygame.image.load(rocket_images[0])
        self.rect.center=center
        speed=[self.angle, 6]
        #speed=[self.angle, 16 -  abs(self.angle)*2]
        
        return speed
    
    def move(self,speed):
        self.rect.centerx=self.rect.centerx+speed[0]
        if self.rect.centerx<20: self.rect.centerx=20
        if self.rect.centerx>1620: self.rect.centerx=620

class StuffClass(pygame.sprite.Sprite):
    def __init__(self,image_file, location, type,num=1):
        pygame.sprite.Sprite.__init__(self)
        self.image_file=image_file
        self.image =pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.center=location
        self.type=type
        self.passed=False
        self.num = num
    def update(self):
        global speed
        if self.type != "laser": self.rect.centery -= speed[1]
        if self.rect.centery<-32:
            self.kill()
        if self.type == "laser":
            self.rect.centery -= speed[1]*self.num+1
        if self.type == "glaser":
            self.rect.centery += speed[1]*self.num+1*3
            #glaser[self.num].rect.centery = self.rect.centery
            glaser.rect.centery = self.rect.centery
            
            
        

def create_map(starNum,rockNum,enemyNum,gLaser=0,loc=[]):
    global obstacles
    locations=[]

    #gl spawnner
    if gLaser != 0:
##        if not (loc in locations):
##            locations.append(loc)
##            img="lazer.jpg"
##            for laser in range(gLaser):
##                obstacle=StuffClass(img,loc,"glaser",laser)
##                obstacles.add(obstacle)
##                glaser[laser].rect.center=loc
    
        if not (loc in locations):
            locations.append(loc)
            img="lazer.jpg"
            obstacle=StuffClass(img,loc,"glaser")
            obstacles.add(obstacle)
            glaser.rect.center=loc

    
    #Star spawnner
    for i in range(starNum):
        row=random.randint(0,9)
        col=random.randint(0,9)
        location=[col*164+32,row*164+32+1640]
        if not (location in locations):
            locations.append(location)
            img="images.png"
            obstacle=StuffClass(img,location,"star")
            obstacles.add(obstacle)

    #r s
    for i in range(rockNum):
        row=random.randint(0,9)
        col=random.randint(0,9)
        location=[col*164+32,row*164+32+1640]
        if not (location in locations):
            locations.append(location)
            img="latest-1.png"
            obstacle=StuffClass(img,location,"rock")
            obstacles.add(obstacle)

    #e s
    for i in range(enemyNum):
        row=random.randint(0,9)
        col=random.randint(0,9)
        location=[col*164+32,row*164+32+1640]
        if not (location in locations):
            locations.append(location)
            img="enemy.png"
            obstacle=StuffClass(img,location,"enemy")
            obstacles.add(obstacle)
            img="lazer.jpg"
            for laser in range(5):
                obstacle=StuffClass(img,location,"laser",laser)
                obstacles.add(obstacle)

           
def animate(bg=""):
    if bg == "":
        screen.fill([255,255,255])
    else:
        img = pygame.image.load(bg)
        screen.blit(img, (0, 0))
    obstacles.draw(screen)
    screen.blit(rocket.image,rocket.rect)
    screen.blit(score_text,[10,10])
    pygame.display.flip()

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([1640,1640])
pygame.time.delay(1000)
clock=pygame.time.Clock()

rocket=RocketClass()
speed=[0,6]
obstacles=pygame.sprite.Group()
global glaser
#glaser = [RocketClass()]*5
glaser = RocketClass()
map_position=0
lives=10
points=0

starNum=7
rockNum=3
enemyNum=1

create_map(starNum,rockNum,enemyNum)
font=pygame.font.Font(None,50)

level = 1

   
running=True
#while running:
while lives > 0:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed=rocket.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = rocket.turn(1)
            elif event.key == pygame.K_SPACE:
                create_map(0,0,0,5,rocket.rect.center)

    rocket.move(speed)
            
    map_position += speed[1]
    
    #map_position += 2
    if map_position>=640:
        create_map(starNum,rockNum,enemyNum)
        map_position=0
               
    

    #for i in range(5):
        #shoot = pygame.sprite.spritecollide(glaser[i], obstacles, False)
    shoot = pygame.sprite.spritecollide(glaser, obstacles, False)
    for k in range(len(shoot)):
        if shoot[k].type == "glaser" or shoot[k].type == "star": continue
        elif shoot[k].type == "rock" or shoot[k].type == "enemy" or shoot[k].type == "laser":
            shoot[k].kill()
            animate()
            obstacles.update()
        '''
        if shoot:
            if shoot[k].type == "glaser": continue
            elif shoot[0].type== "rock" and not shoot[0].passed:
                print("SHOOT!!!",shoot[0].type)
                rocket.image=pygame.image.load("explosion3.png")
                shoot[0].kill()
                animate()
                print("HIT ROCK!!!")
            elif shoot[0].type== "laser" and not shoot[0].passed:
                print("SHOOT!!!",shoot[0].type)
                rocket.image=pygame.image.load("explosion3.png")
                shoot[0].kill()
                animate()
                
                print("HIT LASER!!!")
            elif shoot[0].type== "enemy" and not shoot[0].passed:
                print("SHOOT!!!",shoot[0].type)
                rocket.image=pygame.image.load("explosion3.png")
                shoot[0].kill()
                animate()
                print("HIT ENEMY!!!")
            obstacles.update()
            '''

    hit=pygame.sprite.spritecollide(rocket, obstacles, False)
    
        
    
    if hit:
        if hit[0].type== "rock" and not hit[0].passed:
            lives=lives-1
            rocket.image=pygame.image.load("explosion3.png")
            animate()
            pygame.time.delay(1000)
            rocket.image=pygame.image.load("ship.jpg")
            rocket.angle=0
            speed=[0,6]
            hit[0].passed=True
            splat.play()
            pygame.time.delay(1000)
        
        elif hit[0].type=="star"and not hit[0].passed:
            points+=10
            hit[0].kill()
        elif hit[0].type== "enemy" and not hit[0].passed:
            lives=lives-1
            rocket.image=pygame.image.load("explosion3.png")
            hit[0].kill()
            animate()
            pygame.time.delay(1000)
            rocket.image=pygame.image.load("ship.jpg")
            rocket.angle=0
            speed=[0,6]
            hit[0].passed=True
         
            
        elif hit[0].type== "laser" and not hit[0].passed:
            lives=lives-1
            rocket.image=pygame.image.load("explosion3.png")
            animate()
            pygame.time.delay(1000)
            rocket.image=pygame.image.load("ship.jpg")
            rocket.angle=0
            speed=[0,6]
            hit[0].passed=True    
 
    obstacles.update()
    score_text=font.render("Score: "+str(points)+"  Lives: "+str(lives)+"   LV"+str(level),1,(0,0,0))
    animate()
    
    #if pygame.sprite.spritecollide(rocket, obstacles, False):
     #   hit.play()
    

    #Code for level 2 start

    if points >= 100 and points < 200:
        if level==1:
            lives+=1
        level=2
        starNum=5
        rockNum=5
        enemyNum=2

    #lv3
    if points >= 200 and points < 300:
        if level==2:
            lives+=1 
        level=3
        starNum=5
        rockNum=6
        enemyNum=2          

        


    if points >= 300 and points < 400:
        if level==3:
            lives+=1 
        level=4
        starNum=5
        rockNum=7
        enemyNum=2
        
    if points >= 400 and points < 500:
        if level==4:
            lives+=1 
        level=5
        starNum=5
        rockNum=8
        enemyNum=3

    if points >= 500 and points < 600:
        if level==5:
            lives+=3 
        level=6
        starNum=50
        rockNum=9
        enemyNum=4

    if points >= 600 and points < 999:
        if level==6:
            lives+=1000000000000000000000000000000000000000000000000 
        level="BONUS"
        starNum=99
        rockNum=0

    if points == 1000:
        score_text=font.render("you win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",1,(0,0,0))
        for o in obstacles:
            o.kill()
        animate("planet.jpg")
        
        time.sleep(10)
        pygame.quit()


score_text=font.render("suny boy!",1,(0,0,0))
pygame.init()

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
