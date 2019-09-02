import pygame
import neat
import time
import os
import random
from classes.bird import Bird
from classes.pipe import Pipe
from classes.base import Base
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
STAT_FONT = pygame.font.SysFont("gigi", 50)

def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0)) #blit means draw EX. win.draw()

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    base.draw(win)
    bird.draw(win)
    pygame.display.update()


def main(genomes, config):
    BASE_POINT = 700

    bird = Bird(230,350)
    base = Base(BASE_POINT)
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


        if bird.y + bird.img.get_height() >= BASE_POINT:
            pass

        base.move()
        draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()

main()

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    winner = population.run(main, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__) # get the current directory
    config_path = os.path.join(local_dir, "neat-config.txt")
    run(config_path)