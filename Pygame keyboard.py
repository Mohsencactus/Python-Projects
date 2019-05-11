import pygame as pg

pg.init()
pg.display.set_mode((100,100),0)

while True:
    for event in pg.event.get():

        if event.type == pg.KEYDOWN:
            # key W pressed
            if event.key == pg.K_w:
                print("Go forward")
            # key S pressed
            if event.key == pg.K_s:
                print("Go back")
            # key Q pressed
            if event.key == pg.K_q:
                pg.quit()
        elif event.type == pg.KEYUP:
                print("Stop")