import math
import turtle

def Tinh_Chu_Vi(chieudai :float, chieurong: float) -> float:
    chuvi = (chieudai + chieurong)/2
    return chuvi

def Tinh_Dien_tich(chieudai :float, chieurong: float) -> float:
    dientich = chieudai * chieurong
    return dientich

def hinhtron(r:float):
    turtle.circle(r)
    turtle.done()
    
    
def chuvi_hinhtron(r:float,goc:float)->float:
    chuvi= 2 * math.pi * r
    chuvigoc=chuvi*goc/360
    return chuvigoc
def tinhdientich(r:float,goc:float)->float:
    dientich=math.pi * r * r
    return dientich
               