import pygame as p
p.init()

win=p.display.set_mode((500,500))
p.display.set_caption("First Game")

x,y,width,height=50,50,40,60
vel=5

isJump=False
j_count=10

run=True
while run:
    p.time.delay(50)
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            break
    keys=p.key.get_pressed()
    if keys[p.K_LEFT] and x>vel:
        x-=vel
    if keys[p.K_RIGHT] and x<500-width-vel:
        x+= vel
    if not(isJump):
        if keys[p.K_UP] and y>vel:
            y-=vel
        if keys[p.K_DOWN] and y<500-height-vel:
            y+=vel
        if keys[p.K_SPACE]:
            isJump=True
    else:
        if j_count>= -10:
            neg=1
            if j_count <0:
                neg=-1
            y-=(j_count ** 2)* 0.5 * neg
            j_count-=1
        else:
            isJump=False
            j_count=10
    win.fill((0,0,0))
    p.draw.rect(win,(0,0,200),(x,y,width,height))
    p.display.update()
p.quit()