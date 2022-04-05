from visual import *
from visual.graph import *  #準備畫座標圖

#  1. 畫面設定
##1螢幕、地板、牆壁、木塊、彈簧
scene = display(width=1000, height=1000, background=(0.5,0.6,0.5))
bottom = box(length=3, height=0.01, width=1, material=materials.silver)
wall = box(length=0.01, height=0.5, width=1, material=materials.silver)
square = box(length=0.2, height=0.2, width=0.2, material=materials.wood) 
spring = helix(pos=(-bottom.length/2,0,0), radius=0.1, coils=15, thickness = 0.03) #彈簧
bottom.pos = (0,-square.height/2,0)
wall.pos = (-bottom.length/2,0.5/2-square.height/2,0)

#  2. 初始參數設定(單位SI制)
t = 0
dt = 0.001
m = 0.5     #木塊質量0.5 kg
k = 10.0    #彈簧的彈性性數 10 N/m
v0 = 2      #初速
square.vx = v0

#  3. (x-t)圖與(v-t)圖
gd1 = gdisplay(x=800, y=0, title='t v.s. x', xtitle='t (s)', ytitle='x (m)',
               ymax=0.4, ymin=-0.4, xmax=1.5)
tx = gcurve(gdisplay=gd1, color=color.yellow)
gd2 = gdisplay(x=800, y=350, title='t v.s. vx', xtitle='t (s)', ytitle='vx (m/s)',
               ymax=2, ymin=-2, xmax=1.5)
tvx = gcurve(gdisplay=gd2, color=color.yellow)
       
#  4. 運動部分
while square.vx >0:
    rate(1000)
    tx.plot( pos = (t, square.pos.x) )
    tvx.plot( pos = (t, square.vx) )
    t += dt
    square.a = -(k/m)*(square.pos.x - 0) #彈力公式F=-k*x，因此彈簧的加速度a =F/m = -(k / m) * 物體在+x的位移量
    square.vx += square.a*dt
    square.pos.x += square.vx*dt
    spring.length =square.pos.x-spring.pos.x-square.length/2 #改變彈簧的長度

while square.vx<0:
    rate(1000)
    tx.plot( pos = (t, square.pos.x) )
    tvx.plot( pos = (t, square.vx) )
    t += dt
    square.a = -(k/m)*(square.pos.x - 0) #彈力公式F=-k*x，因此彈簧的加速度a =F/m = -(k / m) * 物體在+x的位移量
    square.vx += square.a*dt
    square.pos.x += square.vx*dt
    spring.length =square.pos.x-spring.pos.x-square.length/2 #改變彈簧的長度

while square.pos.x<0:
    rate(1000)
    tx.plot( pos = (t, square.pos.x) )
    tvx.plot( pos = (t, square.vx) )
    t += dt
    square.a = -(k/m)*(square.pos.x - 0) #彈力公式F=-k*x，因此彈簧的加速度a =F/m = -(k / m) * 物體在+x的位移量
    square.vx += square.a*dt
    square.pos.x += square.vx*dt
    spring.length =square.pos.x-spring.pos.x-square.length/2 #改變彈簧的長度
print square.pos.x
print t
print square.vx
print square.a
##    spring.length = (square.pos.x-square.length/2)-spring.pos.x    #求出彈簧的長度



print square.pos.x
print t
print square.vx
print square.a

print square.pos.x
print t
print square.vx
print square.a

