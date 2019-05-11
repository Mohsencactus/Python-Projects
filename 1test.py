'''
import pygame as pg

pg.init()
pg.display.set_mode()

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_0:
                print("Hey, you pressed the key, '0'!")
            if event.key == pg.K_1:
                print("Doing whatever")
            if event.key == pg.K_q:
                pg.quit()


import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys

camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([1280,720])

try:
    while True:

        ret, frame = camera.read()
		
        screen.fill([0,0,0])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        pygame.display.update()

        for event in pygame.event.get():
			if event.type == KEYDOWN:
				sys.exit(0)
except KeyboardInterrupt,SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()


import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640,480),0)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0],(640,480))
cam.start()

while True:
    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1,(640,480))
    screen.blit(image1,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
'''
