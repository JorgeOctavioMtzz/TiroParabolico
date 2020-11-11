import math
# import package and making objects 
import turtle 
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
sc=turtle.Screen()
trtl=turtle.Turtle()
sc.screensize(canvwidth=800, canvheight=800)
trtl.speed(100)
trtl.penup()
trtl.pensize(1)
trtl.shapesize(5,5,5)
trtl.goto(-300,-300)
s=-300
d=-300
trtl.pendown()
sc.bgcolor("blue")
trtl.pencolor("white")
for i in range(0,600,10):
  trtl.forward(600)
  trtl.penup()
  d+=10
  trtl.setpos(-300,d)
  trtl.pendown()
  i+=10
trtl.penup()
trtl.goto(-320,0)
trtl.pensize(4)
trtl.pendown()
trtl.forward(640)
trtl.stamp()
trtl.pensize(1)
trtl.penup()
trtl.forward(20)
trtl.write("X",font=("Verdana", 12, "bold"))
trtl.goto(-300,300)
trtl.pendown()
trtl.forward(600)
trtl.penup()
trtl.goto(-300,-300)
trtl.pendown()
trtl.left(90)
for k in range(0,600,10):
  trtl.forward(600)
  trtl.penup()
  s+=10
  trtl.setpos(s, -300)
  trtl.pendown()
  i+=10
trtl.penup()
trtl.goto(300,-300)
trtl.pendown()
trtl.forward(600)
trtl.penup()
trtl.goto(0,-320)
trtl.pensize(5)
trtl.pendown()
trtl.forward(640)
trtl.pensize(1)
trtl.stamp()
trtl.penup()
trtl.forward(20)
trtl.write("y",font=("Verdana", 12, "bold"))
trtl.penup()
trtl.goto(0,0)
trtl.shapesize(2,2,2)
Vo1= sc.numinput("Velocidad Inicial", "¿Cuál es la velocidad incial?", 0)
Vo=Vo1
thet1a= sc.numinput("Angulo Inicial", "¿Cuál es el valor del angulo inicial en grados?", 0)
theta=(thet1a*(math.pi))/180
g = -9.81 #m/s2
t=0
op=0
Vox=(Vo*(math.cos(theta))) 
Voy=(Vo*(math.sin(theta)))
Dxt=((Vo**2)*(math.sin(2*theta)))/(9.81)
tf=(Dxt/Vox)
Vfy=(Voy)+((g)*(tf))
x=0
y=0
print("El componente X de la velocidad es ", "{0:.3f}".format(Vox), "m")
print("El componente Y de la velocidad es ", "{0:.3f}".format(Voy), "m")
print("El alcance horizontal es de ", "{0:.3f}".format(Dxt), "m/s")
print("La velocidad Final en y es de ", "{0:.3f}".format(Vfy), "m/s")
print("El tiempo total del recorrido es de ", "{0:.3f}".format(tf), "s")

trtl.pensize(3)
trtl.pencolor("black")
trtl.right(90)
trtl.pendown()
 
while op!=4:
  trtl.setheading(theta)
  y=Voy*t+(g*t**2)/2
  x=(Vox*t)
  Vy=Voy+(g*t)
  V=math.sqrt(((Vox)**2)+((Vy)**2))
  theta=math.asin(Vy/V)
  trtl.goto(x, y)
  if t >=  tf:
    x=Dxt
    y=0
    op=4
  else:
    t+=0.1
Conf= sc.textinput("¿Seguir?", "¿Desea Calcular un tiempo especifico Yes/No?")
if Conf=="Yes":
  Tiemp= sc.numinput("Tiempo Especifico", "¿En que valor del tiempo desea analizar el movimiento?")
  if Tiemp>tf:
    print("Error el Tiempo especificado es mayor que el tiempo total de la trayectoria")
  else:
    y=Voy*t+(g*t**2)/2
    x=(Vox*t)
    Vy=Voy+(g*t)
    Vx=Vox
    V=math.sqrt(((Vox)**2)+((Vy)**2))
    iy="El valor de la posición en y es de: ", y
    ix="El valor de la posición en x es de: ", x
    ivy="El valor del componente y de la velocidad es de: ", Vy
    ivx="El valor del componente x de la velocidad es de: ", Vx
    iv="El valor de la Velocidad es de : ", V
   # Impresion=[iy, ix, ivy, ivx, iv]
   # mb.showinfo("Valor en Tiempos especificos", "\n".join(''.join(el) for el in Impresion))
else:
  pass
turtle.Screen().exitonclick()  
