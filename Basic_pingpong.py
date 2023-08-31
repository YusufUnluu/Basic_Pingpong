import turtle 
import time
import winsound

window = turtle.Screen()  # turtle kütüphanesi kullanarak ekran tanımladık 
window.title("BASIC PINPON ")
window.bgcolor("black")   
window.setup(width=800,height=600)
window.tracer(0) 
#Score 
score_a = 0
score_b = 0


#Paddle A   
paddle_a = turtle.Turtle() 
paddle_a .speed(0) 
paddle_a.shape("square")  
paddle_a.color("white")  
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # hareket ederken  bu kullanıldığında line çizmeye gerek yok
paddle_a.goto(-350,0)   # x,y kordinatı için  çubuğun  başlangıçta duracağı konum  

#Paddle B   
paddle_b = turtle.Turtle()
paddle_b .speed(0) 
paddle_b.shape("square")  
paddle_b.color("white")  
paddle_b.shapesize(stretch_wid=5,stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350,0)   

# ball
ball = turtle.Turtle()  
ball.speed(0)
ball.shape("square")  
ball.color("white")  
ball.shapesize(1,1)
ball.penup() 
ball.goto(0,0)   
ball.dx =2  # d  deltadan geliyor x  , x kordinatından  bizim yazdığımız değişken adı
ball.dy = 2

#pen
pen = turtle.Turtle()  
pen.speed(0)
pen.color("white")  
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center",font=("Courier",24,"normal"))

# Paddle Hareket
def paddle_a_up():
    y = paddle_a.ycor()
    if y >= 300:
        pass   
    else:# şu anki y kordinatını öğrenme  "ycor" turtle modülünden gelme 
        y+=20   # 20 piksel y kordinatına yukarı ekler 
    paddle_a.sety(y)    #  eski y kordinatını yeni y kordinatına ekliyor
    
def paddle_a_down():
    y = paddle_a.ycor()   
    if y <= -300:
        pass
    else:
         y-=20   
    paddle_a.sety(y)   
    
def paddle_b_up():
    y = paddle_b.ycor()  
    if y>=300:
        pass
    else:
        y+=20  
    paddle_b.sety(y)    
    
def paddle_b_down():
    y = paddle_b.ycor()  
    if y <= -300:
        pass
    else:
        y-=20   
    paddle_b.sety(y)   
 
  
#keyboard binding
window.listen()  #Input dinleme
window.onkeypress(paddle_a_up, "w") #klavyeden paddle_a_up fonksiyonunu çağırıyor, caps açıksa çalışmaz
window.onkeypress(paddle_a_down, "s") 
window.onkeypress(paddle_b_up, "Up") 
window.onkeypress(paddle_b_down, "Down")  


# Main Game

while True:
    time.sleep(1/100)
    window.update() # her loop bitişinde ekran yenileniyor .
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)  #topun şu anki konumu + dx den gelen 2 piksel ile yeni konuma taşıyor
    ball.sety(ball.ycor() + ball.dy) 
    
    # Border Checking
    # y kordinatı border check
    if ball.ycor() > 290:   # bu kısım y cordinatı aşşağı ve yukarıdan sekmesi için
        ball.sety(290)  # 290 pikselden yukarı çıkarsa geri 290 a çekiyor
        ball.dy *=-1    # ve giderek piksel aşşağı doğru kayıyor 
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor() < -290: 
        ball.sety(-290)  
        ball.dy *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    # x kordinatı border check 
    if ball.xcor() >  350:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
        
    if ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
            
   # Paddle and ball collisions
   
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
       