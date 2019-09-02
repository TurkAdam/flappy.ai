import pygame
import neat
import time
import os
import random
from classes.bird import Bird
from classes.pipe import Pipe
from classes.base import Base

WIN_WIDTH = 500
WIN_HEIGHT = 800

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_window(win, bird, pipes, base):
    win.blit(BG_IMG, (0,0)) #blit means draw EX. win.draw()

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    bird.draw(win)
    pygame.display.update()


def main():
    bird = Bird(230,350)
    base = Base(700)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bird.move()
        remove = []
        add_pipe = False
        for pipe in pipes:
            if pipe.collide(bird):
                pass 


            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(600)) #add new pipe


        for pipe in remove:
            pipes.remove(pipe)
        base.move()
    
        draw_window(win, bird, pipes, base)

    pygame.quit()
    quit()

main()