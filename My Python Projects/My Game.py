import turtle
import math

game_choice = True
game_start = False
main_loop = True
weapon = True

if game_choice == True:
    game_start = True
    #Starting the game
    print("Starting the game")
    print("Loading Game.")
    print("Loading Game..")
    print("Loading Game...")
    print("Game Loaded")



while game_start == True:

    #The Screen
    bs = turtle.Screen()
    bs.bgcolor("black")
    bs.title("Game")

    #The Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()
    break

#Create the player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
print("Player Has Spawned")

playerspeed = 15

#Create the monster
monster = turtle.Turtle()
monster.color("red")
monster.shape("square")
monster.penup()
monster.setposition(0, 250)
monster.shapesize(4, 4)
monster.setheading(270)
print("Monster Has Spawned")
print("We All are in danger now")

monsterspeed = 5

#Create player weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move the Player
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



#Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


while main_loop == True:

    #Move the monster
    x = monster.xcor()
    x += monsterspeed
    monster.setx(x)

    #Move the monster back
    if monster.xcor() > 280:
        y = monster.ycor()
        y -= 45
        monster.sety(y)
        #Change monster direction
        monsterspeed *= -1

    if monster.xcor() < -280:
        y = monster.ycor()
        y -= 45
        monster.sety(y)

        #Change monster direction
        monsterspeed *= -1

    #Check for a collision between the bullet and the monster
    if isCollision(bullet, monster):
        #Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        print("You Won")
        break
    #Check for a collision between the player and the monster
    if isCollision(player, monster):
        player.hideturtle()
        monster.hideturtle()
        print("Game Over")
        print("You Lose")
        break    

        #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


    
    



