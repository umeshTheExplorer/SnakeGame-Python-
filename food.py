from turtle import Turtle
import random



class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('yellow')
        self.speed('fastest')
        self.refresh()

    

    def refresh(self):
        random_x =  random.randint(-285, 285)
        random_y =  random.randint(-285, 285)
        self.goto(random_x,random_y)




    
