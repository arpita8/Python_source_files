
import random, easygui
#pygame.init()
''''pygame.mixer.init()'''
secret=random.randint(-100,900)
secret2=random.randint(-100,900)
guess2=0
tries2=0
guess=0
tries=0
'''song=pygame.mixer.music.load("01 Stupid Man.mp3")
pygame.mixer.music.play(-1)
easygui.msgbox()'''
easygui.msgbox ("""I'm batman and i like math so to go into my house
you have 8 tries to guess a number from -100 to 900""")

while guess != secret and tries <8 and tries2<8 and guess2!= secret2:
    guess=easygui.integerbox("what yey guess ",lowerbound=-9999, upperbound=1234567890)
    guess2=easygui.integerbox("what yey guess 2",lowerbound=-9999, upperbound=1234567890)
    guess = input("what yey guess? ")
    guess2 = input("what yey guess 2? ")
    
    

    if guess < secret:
        easygui.msgbox(str(guess)+"to low wirdo")
        print guess,"to low wirdo"
        
    elif guess> secret:
        easygui.msgbox(str(guess)+ "to high crazy guy")
        #print guess,"to high crazy guy"
    if guess2< secret2:
        easygui.msgbox(str(guess2)+"to low wirdo")
        #print guess2,"to low wirdo"
    elif guess2> secret2:
        easygui.msgbox(str(guess2)+ "to high crazy guy")
        #print guess2,"to high crazy guy"
    tries2=tries2+1
    tries=tries+1
if guess==secret or guess2==secret2:
    #print "yey got it man"
    easygui.msgbox("yey got it man")
else:       
    easygui.msgbox("""i win i'm going to party to celebrate (bad grammar)
    the secret number was"""+str(secret) +",secret2 "+str(secret2))
    #print """i win i'm going to party to celebrate (bad grammar)
    #the secret number was"""+str(secret) +",secret2 "+str(secret2)

    












     





    
