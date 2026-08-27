import turtle
import time
import random 
import sys


# The screen 

main_screen = turtle.Screen()
main_screen.title("Snake Game!")
main_screen.setup(width=  700 , height= 700 )
main_screen.tracer(0)
main_screen.bgcolor(.1 , .6  , .2)


# The snake

snake = turtle.Turtle()
snake.shape("square")
snake.color("darkblue")
snake.speed(0)
snake.shapesize(stretch_len= 1.5 , stretch_wid= 1.5)
snake.penup()
snake.goto(-100 ,0)
snake.direction= "Stop"

# The Edges 
# Up
edge_u = turtle.Turtle()
edge_u.shape("square")
edge_u.speed(0)
edge_u.penup()
edge_u.color("darkgreen")
edge_u.shapesize(stretch_len= 40 , stretch_wid= 4.27)
edge_u.goto(0 , 330)
edge_u.stamp()
edge_u.hideturtle()

# Down
edge_d = turtle.Turtle()
edge_d.shape("square")
edge_d.speed(0)
edge_d.penup()
edge_d.color("darkgreen")
edge_d.shapesize(stretch_len= 40 , stretch_wid= 1.5)
edge_d.goto(0 , -330)

# Right
edge_r = turtle.Turtle()
edge_r.shape("square")
edge_r.speed(0)
edge_r.penup()
edge_r.color("darkgreen")
edge_r.shapesize(stretch_len= 2.5 , stretch_wid= 34)
edge_r.goto(330 , 0)

# Left
edge_l = turtle.Turtle()
edge_l.shape("square")
edge_l.speed(0)
edge_l.penup()
edge_l.color("darkgreen")
edge_l.shapesize(stretch_len= 3.4 , stretch_wid= 34)
edge_l.goto(-330 , 0)

# Appel
apple= turtle.Turtle()
apple.shape("circle")
apple.speed(0)
apple.color("red")
apple.shapesize(stretch_len = 1.5 ,stretch_wid= 1.5 )
apple.penup()
apple.goto(100 , 0)
# Score 
score_n = 0 
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.goto(0 , 300)
score.write(f"Score : {score_n}", align = "center" , font =("Courier" , 25 , "bold") )
score.hideturtle()



tail = []

one_dir = True 
# Moves 

# Up
def go_up () :
    global one_dir 
    if snake.direction != "down" and one_dir == True:
        snake.direction = "up"
        one_dir = False
        


# Down
def go_down () :
    global one_dir 
    if snake.direction != "up" and one_dir == True:
        snake.direction = "down"
        one_dir = False
        


# Right
def go_right () :
    global one_dir 
    if snake.direction != "left"and one_dir == True:
        snake.direction = "right"
        one_dir = False
        

# Left
def go_left () :
    global one_dir 
    if snake.direction != "right"and one_dir == True:
        snake.direction = "left"
        one_dir = False
        


# keybord listener

main_screen.listen ()

main_screen.onkeypress(go_up , "Up")
main_screen.onkeypress(go_down , "Down")
main_screen.onkeypress(go_right , "Right")
main_screen.onkeypress(go_left , "Left")

new_tail1 = turtle.Turtle()
new_tail1.speed(0)
new_tail1.penup()
new_tail1.shape("square")
new_tail1.color("blue")

new_tail1.shapesize(stretch_len=1.5 , stretch_wid= 1.5)
tail.append(new_tail1)
new_tail1.goto(-130, 0)



while True :

    
    main_screen.update()
    time.sleep(.2)

    x= snake.xcor()
    y= snake.ycor()
    # keep moving
    if snake.direction == "up" :
        snake.sety(snake.ycor() + 30)

    if snake.direction == "down" :
        snake.sety(snake.ycor() - 30)
    
    if snake.direction == "right" :
        snake.setx(snake.xcor() + 30)

    if snake.direction == "left" :
        snake.setx(snake.xcor() - 30)

    one_dir=True

    # The Edges

    # Up 
    if snake.ycor() > 290 :
        snake.sety(snake.ycor())
        break; 

    # Down 
    if snake.ycor() < -317 :
        snake.sety(snake.ycor())
        break; 

    # Right 
    if snake.xcor() > 317 :
        snake.setx(snake.xcor())
        break; 

    # Left  
    if snake.xcor() < -308 :
        snake.setx(snake.xcor())
        break; 

    # Eating Apples
    if snake.distance(apple) < 25 :
         
         while  True :
             x_apple = random.randint(-280 , 280)
             y_apple = random.randint(-300 , 270)
             collision = False
             for segment in tail:
                 if segment.distance(x_apple , y_apple) < 30:
                     collision = True
                     break
         
                     
             if   collision == False :
                 break

         apple.goto(x_apple ,y_apple)
         score.clear()
         score_n+=1
         score.write(f"Score : {score_n}", align = "center" , font =("Courier" , 25 , "bold") )
         # Tail new and add
         new_tail = turtle.Turtle()
         new_tail.speed(0)
         new_tail.penup()
         new_tail.shape("square")
         new_tail.color("blue")
         new_tail.shapesize(stretch_len=1.5 , stretch_wid= 1.5)
         tail.append(new_tail)
    if len(tail) ==1 and snake.direction != "Stop" : 
       tail[0].goto(x , y)
    # tail move 
    for index in range (len(tail) -1 , 0 , -1 ) :
        tail[index].goto(tail[index-1].xcor() , tail[index-1].ycor())
        if index == 1 :
           tail[0].goto(x , y)
    for index in range (len(tail) -1 , 1 , -1) :
        if snake.distance(tail[index]) < 30 : 
            sys.exit()
            


        


    

  
         




