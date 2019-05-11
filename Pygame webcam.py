import pygame as pg
import pygame.camera as pgc

pg.init()
pgc.init()

window = pg.display.set_mode((640,480),0)
camlist = pgc.list_cameras()
webcam = pgc.Camera(camlist[0],(640,480))
webcam.start()

while True:
    frame = webcam.get_image()
    frame = pg.transform.scale(frame,(640,480))
    window.blit(frame,(0,0))
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            webcam.stop()
            pg.quit()