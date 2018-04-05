

##Rusty Clayton
##4/5/2018
##Snake Game

import turtle
import time
import random



def main():
    wn=turtle.Screen()

    boundary=turtle.Turtle()
    boundary.ht()
    boundary.up()
    boundary.goto(-70,70)
    boundary.down()
    for i in range(4):
        boundary.forward(140)
        boundary.right(90)

    apple=turtle.Turtle()
    apple.ht()
    apple.up()
    apple.color("red")
    apple.shape("circle")




    snake=turtle.Turtle()
    snake2=turtle.Turtle()
    snake3=turtle.Turtle()
    snake4=turtle.Turtle()
    snake5=turtle.Turtle()
    snake6=turtle.Turtle()
    snake7=turtle.Turtle()
    snake8=turtle.Turtle()
    snake9=turtle.Turtle()
    snake10=turtle.Turtle()
    snake11=turtle.Turtle()
    snake12=turtle.Turtle()
    snake13=turtle.Turtle()
    snake14=turtle.Turtle()
    snake15=turtle.Turtle()
    snake16=turtle.Turtle()
    snake17=turtle.Turtle()
    snake18=turtle.Turtle()
    snake19=turtle.Turtle()

    snake.up()
    snake2.up()
    snake3.up()
    snake4.up()
    snake5.up()
    snake6.up()
    snake7.up()
    snake8.up()
    snake9.up()
    snake10.up()
    snake11.up()
    snake12.up()
    snake13.up()
    snake14.up()
    snake15.up()
    snake16.up()
    snake17.up()
    snake18.up()
    snake19.up()

    snake2.ht()
    snake3.ht()
    snake4.ht()
    snake5.ht()
    snake6.ht()
    snake7.ht()
    snake8.ht()
    snake9.ht()
    snake10.ht()
    snake11.ht()
    snake12.ht()
    snake13.ht()
    snake14.ht()
    snake15.ht()
    snake16.ht()
    snake17.ht()
    snake18.ht()
    snake19.ht()



    snake.shape("square")
    snake2.shape("square")
    snake3.shape("square")
    snake4.shape("square")
    snake5.shape("square")
    snake6.shape("square")
    snake7.shape("square")
    snake8.shape("square")
    snake9.shape("square")
    snake10.shape("square")
    snake11.shape("square")
    snake12.shape("square")
    snake13.shape("square")
    snake14.shape("square")
    snake15.shape("square")
    snake16.shape("square")
    snake17.shape("square")
    snake18.shape("square")
    snake19.shape("square")

    snake.speed(0)

    bad_coordinatesX=[]
    bad_coordinatesY=[]
    counter=[]

    def input1():
        new_apple()
        snake.forward(20)
        wn.onkey(turn_left,"Left")
        wn.onkey(turn_right,"Right")
        wn.listen()
        no_key_pressed=0
        while no_key_pressed==0:
            time.sleep(.01)
            forward()
            check()

    def new_apple():
        apple.ht()
        apple.goto(random.randrange(-60,60,20),random.randrange(-60,60,20))
        apple.st()
        

    def turn_left():
        snake.left(90)
        time.sleep(.01)
    def turn_right():
        snake.right(90)
        time.sleep(.01)
        
    def forward():
        follow()
        snake.forward(20)
        
        
        
        
    def follow():
        
        if len(counter)>=1:
            bad_coordinatesX.append(snake2.xcor())
            bad_coordinatesY.append(snake2.ycor())
        if len(counter)>=2:
            bad_coordinatesX.append(snake3.xcor())
            bad_coordinatesY.append(snake3.ycor())
        if len(counter)>=3:
            bad_coordinatesX.append(snake4.xcor())
            bad_coordinatesY.append(snake4.ycor())
        if len(counter)>=4:
            bad_coordinatesX.append(snake5.xcor())
            bad_coordinatesY.append(snake5.ycor())
        if len(counter)>=5:
            bad_coordinatesX.append(snake6.xcor())
            bad_coordinatesY.append(snake6.ycor())
        if len(counter)>=6:
            bad_coordinatesX.append(snake7.xcor())
            bad_coordinatesY.append(snake7.ycor())
        if len(counter)>=7:
            bad_coordinatesX.append(snake8.xcor())
            bad_coordinatesY.append(snake8.ycor())
        if len(counter)>=8:
            bad_coordinatesX.append(snake9.xcor())
            bad_coordinatesY.append(snake9.ycor())
        if len(counter)>=9:
            bad_coordinatesX.append(snake10.xcor())
            bad_coordinatesY.append(snake10.ycor())
        if len(counter)>=10:
            bad_coordinatesX.append(snake11.xcor())
            bad_coordinatesY.append(snake11.ycor())
        if len(counter)>=11:
            bad_coordinatesX.append(snake12.xcor())
            bad_coordinatesY.append(snake12.ycor())
        if len(counter)>=12:
            bad_coordinatesX.append(snake13.xcor())
            bad_coordinatesY.append(snake13.ycor())
        if len(counter)>=13:
            bad_coordinatesX.append(snake14.xcor())
            bad_coordinatesY.append(snake14.ycor())
        if len(counter)>=14:
            bad_coordinatesX.append(snake15.xcor())
            bad_coordinatesY.append(snake15.ycor())
        if len(counter)>=15:
            bad_coordinatesX.append(snake16.xcor())
            bad_coordinatesY.append(snake16.ycor())
        if len(counter)>=16:
            bad_coordinatesX.append(snake17.xcor())
            bad_coordinatesY.append(snake17.ycor())
        if len(counter)>=17:
            bad_coordinatesX.append(snake18.xcor())
            bad_coordinatesY.append(snake18.ycor())
        if len(counter)>=18:
            bad_coordinatesX.append(snake19.xcor())
            bad_coordinatesY.append(snake19.ycor())


        snake19.goto(snake18.xcor(),snake18.ycor())
        snake18.goto(snake17.xcor(),snake17.ycor())
        snake17.goto(snake16.xcor(),snake16.ycor())
        snake16.goto(snake15.xcor(),snake15.ycor())
        snake15.goto(snake14.xcor(),snake14.ycor())
        snake14.goto(snake13.xcor(),snake13.ycor())
        snake13.goto(snake12.xcor(),snake12.ycor())
        snake12.goto(snake11.xcor(),snake11.ycor())
        snake11.goto(snake10.xcor(),snake10.ycor())
        snake10.goto(snake9.xcor(),snake9.ycor())
        snake9.goto(snake8.xcor(),snake8.ycor())
        snake8.goto(snake7.xcor(),snake7.ycor())
        snake7.goto(snake6.xcor(),snake6.ycor())    
        snake6.goto(snake5.xcor(),snake5.ycor())
        snake5.goto(snake4.xcor(),snake4.ycor())
        snake4.goto(snake3.xcor(),snake3.ycor())
        snake3.goto(snake2.xcor(),snake2.ycor())
        snake2.goto(snake.xcor(),snake.ycor())

        
        
    def check():
        for coords in range(len(bad_coordinatesX)):
            bad_x_coord=bad_coordinatesX[coords]
            bad_y_coord=bad_coordinatesY[coords]
            if bad_x_coord+10>=snake.xcor() and bad_x_coord-10<=snake.xcor():
                if bad_y_coord+10>=snake.ycor() and bad_y_coord-10<=snake.ycor():
                    game_over()

        if snake.xcor()>70 or snake.xcor()<-70 or snake.ycor()>70 or snake.ycor()<-70:
            game_over()
        
        if snake.xcor()>=apple.xcor()-10 and snake.xcor()<=apple.xcor()+10 and snake.ycor()>=apple.ycor()-10 and snake.ycor()<=apple.ycor()+10:
            counter.append(1)
            new_apple()
            if len(counter)==1:
                snake2.st()
                snake2.color(random.random(),random.random(),random.random())
            if len(counter)==2:
                snake3.st()
                snake3.color(random.random(),random.random(),random.random())
            if len(counter)==3:
                snake4.st()
                snake4.color(random.random(),random.random(),random.random())
            if len(counter)==4:
                snake5.st()
                snake5.color(random.random(),random.random(),random.random())
            if len(counter)==5:
                snake6.st()
                snake6.color(random.random(),random.random(),random.random())
            if len(counter)==6:
                snake7.st()
                snake7.color(random.random(),random.random(),random.random())
            if len(counter)==7:
                snake8.st()
                snake8.color(random.random(),random.random(),random.random())
            if len(counter)==8:
                snake9.st()
                snake9.color(random.random(),random.random(),random.random())
            if len(counter)==9:
                snake10.st()
                snake10.color(random.random(),random.random(),random.random())
            if len(counter)==10:
                snake11.st()
                snake11.color(random.random(),random.random(),random.random())
            if len(counter)==11:
                snake12.st()
                snake12.color(random.random(),random.random(),random.random())
            if len(counter)==12:
                snake13.st()
                snake13.color(random.random(),random.random(),random.random())
            if len(counter)==13:
                snake14.st()
                snake14.color(random.random(),random.random(),random.random())
            if len(counter)==14:
                snake15.st()
                snake15.color(random.random(),random.random(),random.random())
            if len(counter)==15:
                snake16.st()
                snake16.color(random.random(),random.random(),random.random())
            if len(counter)==16:
                snake17.st()
                snake17.color(random.random(),random.random(),random.random())
            if len(counter)==17:
                snake18.st()
                snake18.color(random.random(),random.random(),random.random())
            if len(counter)==18:
                snake19.st()
                snake19.color(random.random(),random.random(),random.random())
        for i in range(len(bad_coordinatesX)):
            bad_coordinatesX.pop()
            bad_coordinatesY.pop()
    
        
    def game_over():
        try:
            game_over_message="Game over, your score was "+str(len(counter))+" would you like to try again?Y/N"
            restart=wn.textinput(" ",game_over_message)
            if restart.upper()=="Y":
                wn.clear()
                main()
                
            else:
                turtle.bye()
                
        except AttributeError:
            turtle.bye()
    input1()
main()
