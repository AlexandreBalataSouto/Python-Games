#Space invaders in Python 3

import turtle
import winsound
import math
import random

#Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space invaders by Balata")
window.bgpic("space_invaders_background.gif")
window.setup(width=700, height=500)
window.tracer(0)

#Register the shapes
window.register_shape("invader.gif")
window.register_shape("player.gif")


#Score
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.goto(-340,226)
score_string = "Score: %s" %score
score_pen.write(score_string, False, align = "left", font=("Arial",14,"normal"))
score_pen.hideturtle()

#Player
player = turtle.Turtle()
player.color("green")
player.shape("player.gif")
player.penup()
player.speed(0)
player.goto(0, -200)
player.setheading(90)

player_speed = 20

#Player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bullet_speed = 1

#Bullet state
bullet_state = True

#Choose a number of enemies
number_of_enemies = 5
#List of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

#Enemy
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(-100,200)
    enemy.goto(x,y)

enemy_speed = 0.05

#Funcions
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -300:
        x = -300
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 300:
        x = 300
    player.setx(x)

def shoot():
    #Declare bulletstate as a global if it needs changed
    global bullet_state

    if bullet_state == True:
        bullet_state = False
        #Move the bullet
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x,y)
        bullet.showturtle()
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

def isHit(turtle01, turtle02): #Distance between two objects c = SQUARE(a^2 + b^2)  pythagorean theorem
    distance = math.sqrt(math.pow(turtle01.xcor() - turtle02.xcor(),2) + math.pow(turtle01.ycor() - turtle02.ycor(),2))

    if distance < 15: #15 is a random number but it suit well
        return True
    else:
        return False


#Keyboard bindings
window.listen()
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(shoot, "space")

#Main loop
while True:
    window.update()

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
        #Move enemy back and down
        if  x < -300:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 10
                e.sety(y)
            #Change enemy direction  
            enemy_speed *= -1 
        elif x > 300:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 10
                e.sety(y)
            #Change enemy direction
            enemy_speed *= -1
        #Check collision between bullet and enemy
        if isHit(bullet,enemy):
            bullet.hideturtle()
            bullet_state = True
            bullet.goto(0, -400)

            x = random.randint(-300, 300)
            y = random.randint(-100,200)
            enemy.goto(x,y)

            #Update score
            score += 10
            score_string = "Score: %s" %score
            score_pen.clear()
            score_pen.write(score_string, False, align = "left", font=("Arial",14,"normal"))
        
        #Check collision between player and enemy
        if isHit(player, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
        
    #Move the bullet
    y = bullet.ycor()
    y += bullet_speed
    bullet.sety(y)
    #Check if bullet has gone to the top
    if y > 250:
        bullet_state = True
        bullet.hideturtle()
    
    

   
window.mainloop()