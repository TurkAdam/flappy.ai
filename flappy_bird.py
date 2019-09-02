import pygame
import neat
import time
import os
import random
from classes.bird import Bird
from classes.pipe import Pipe
from classes.base import Base

pygame.font.init()


GEN = 0
WIN_WIDTH = 500
WIN_HEIGHT = 800
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy.ai")
STAT_FONT = pygame.font.Font("font/Flappy-Bird.ttf", 40)


def draw_window(win, birds, pipes, base, score, gen):
    win.blit(BG_IMG, (0,0)) #blit means draw EX. win.draw()

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Gen: " + str(gen), 1, (255,255,255))
    win.blit(text, (10, 10))

    base.draw(win)

    for bird in birds:
        bird.draw(win)

    pygame.display.update()


def main(genomes, config):
    global GEN
    BASE_POINT = 700
    GEN += 1

    nets = []
    gens = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        gens.append(g)


    base = Base(BASE_POINT)
    pipes = [Pipe(600)]
    clock = pygame.time.Clock()
    score = 0
    
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()


        pipe_idx = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_idx = 1
        else:
            run = False
            break


        for i, bird in enumerate(birds):
            bird.move()
            gens[i].fitness += 0.1
            
            output = nets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipe_idx].height), abs(bird.y - pipes[pipe_idx].bottom)))

            if output[0] > 0.5:  # use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
                bird.jump()
        
        
        remove = []
        add_pipe = False
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    gens[i].fitness -= 1
                    birds.pop(i)
                    nets.pop(i)
                    gens.pop(i)
                
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1

            for g in gens:
                g.fitness += 5

            pipes.append(Pipe(600))

        for pipe in remove:
            pipes.remove(pipe)


        for i, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= BASE_POINT or bird.y < 0:
                birds.pop(i)
                nets.pop(i)
                gens.pop(i)

        base.move()
        draw_window(win, birds, pipes, base, score, GEN)

			


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