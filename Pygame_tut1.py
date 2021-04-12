import pygame as p
p.init()

win=p.display.set_mode((500,500))
p.display.set_caption("First Game")

x,y,width,height=50,50,40,60
vel=10

run=True
while run:
    p.time.delay(100)
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            break
    keys=p.key.get_pressed()
    if keys[p.K_LEFT]:
        x-=vel
    if keys[p.K_RIGHT]:
        x+= vel
    if keys[p.K_UP]:
        y-=vel
    if keys[p.K_DOWN]:
        y+=vel
    win.fill((0,0,0))
    p.draw.rect(win,(0,0,200),(x,y,width,height))
    p.display.update()
p.quit()