#3.4
import turtle
t=turtle
t.speed(0)
def drawChessBoard(sx, ex, sy, ey):
    c1='black'
    c2='white'
    '''
    drawLineOfSquares(sx, ex,(((ey-sy)*(0/8))+sy),(((ey-sy)*(1/8))+sy), c1, c2)
    drawLineOfSquares(sx, ex,(((ey-sy)*(1/8))+sy),(((ey-sy)*(2/8))+sy), c2, c1)
    drawLineOfSquares(sx, ex,(((ey-sy)*(2/8))+sy),(((ey-sy)*(3/8))+sy), c1, c2)
    drawLineOfSquares(sx, ex,(((ey-sy)*(3/8))+sy),(((ey-sy)*(4/8))+sy), c2, c1)
    drawLineOfSquares(sx, ex,(((ey-sy)*(4/8))+sy),(((ey-sy)*(5/8))+sy), c1, c2)
    drawLineOfSquares(sx, ex,(((ey-sy)*(5/8))+sy),(((ey-sy)*(6/8))+sy), c2, c1)
    drawLineOfSquares(sx, ex,(((ey-sy)*(6/8))+sy),(((ey-sy)*(7/8))+sy), c1, c2)
    drawLineOfSquares(sx, ex,(((ey-sy)*(7/8))+sy),(((ey-sy)*(8/8))+sy), c2, c1)
    '''

    for i in range(8):
        if i%2 == 0:
            drawLineOfSquares(sx, ex,(((ey-sy)*(i/8))+sy),(((ey-sy)*((i+1)/8))+sy), c1, c2)
        else:
            drawLineOfSquares(sx, ex,(((ey-sy)*(i/8))+sy),(((ey-sy)*((i+1)/8))+sy), c2, c1)
            







def drawRect(startx, endx, starty, endy, color):
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.color(color)
    t.pencolor("black")
    t.pensize(5)
    t.begin_fill()
    dx=endx-startx
    dy=endy-starty
    t.seth(0)
    t.fd(dx)
    t.lt(90)
    t.fd(dy)
    t.lt(90)
    t.fd(dx)
    t.lt(90)
    t.fd(dy)
    t.lt(90)
    t.end_fill()

    

#drawSquare(-50,150,-50,100,'Green')
#drawSquare(0,100,0,100,'Green')



def drawLineOfSquares(sx, ex, sy, ey, c1, c2):
    '''
    drawRect(sx,(((ex-sx)*(1/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(1/8))+sx),(((ex-sx)*(2/8))+sx),sy,ey,c2)
    drawRect((((ex-sx)*(2/8))+sx),(((ex-sx)*(3/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(3/8))+sx),(((ex-sx)*(4/8))+sx),sy,ey,c2)
    drawRect((((ex-sx)*(4/8))+sx),(((ex-sx)*(5/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(5/8))+sx),(((ex-sx)*(6/8))+sx),sy,ey,c2)
    drawRect((((ex-sx)*(6/8))+sx),(((ex-sx)*(7/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(7/8))+sx),(((ex-sx)*(8/8))+sx),sy,ey,c2)

    
    drawRect((((ex-sx)*(0/8))+sx),(((ex-sx)*(1/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(1/8))+sx),(((ex-sx)*(2/8))+sx),sy,ey,c2)
    drawRect((((ex-sx)*(2/8))+sx),(((ex-sx)*(3/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(3/8))+sx),(((ex-sx)*(4/8))+sx),sy,ey,c2)
    drawRect((((ex-sx)*(4/8))+sx),(((ex-sx)*(5/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(5/8))+sx),(((ex-sx)*(6/8))+sx),sy,ey,c2)
    drawRect((((ex-sx)*(6/8))+sx),(((ex-sx)*(7/8))+sx),sy,ey,c1)
    drawRect((((ex-sx)*(7/8))+sx),(((ex-sx)*(8/8))+sx),sy,ey,c2)
    '''
    for i in range(8):
        if i%2==0:
            drawRect((((ex-sx)*(i/8))+sx),(((ex-sx)*((i+1)/8))+sx),sy,ey,c2)
        else:
            drawRect((((ex-sx)*(i/8))+sx),(((ex-sx)*((i+1)/8))+sx),sy,ey,c1)



turtle.tracer(0,0)
drawChessBoard(210,30,30,210)
drawChessBoard(-30,-210,30,210)
turtle.update()
#drawLineOfSquares(0,100,0,100,'black','blue')   
