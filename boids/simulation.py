import pygame
from pygame.locals import *
import random
from boid import Boid
from functions import (
    fly_towards_center,
    avoid_others,
    match_velocity,
    limit_speed,
    keep_within_bounds,
)


def run_simulation(
    num_boids=100,
    visual_range=75,
    coherence=0.01,
    max_speed=5,
    turning_speed=1,
    margin_between_boids=20,
    width=800,
    height=600,
):
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    boids = [
        Boid(
            x=random.uniform(0, width),
            y=random.uniform(0, height),
            dx=random.uniform(-max_speed, max_speed),
            dy=random.uniform(-max_speed, max_speed),
        )
        for _ in range(num_boids)
    ]

    gameOn = True
    while gameOn:
        screen.fill((255, 255, 255))  # Fill the screen with white background

        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Backspace key has been pressed set
                # running to false to exit the main loop
                if event.key == K_BACKSPACE:
                    gameOn = False

            elif event.type == QUIT:
                gameOn = False

        for boid in boids:
            fly_towards_center(
                boids, boid, visual_range=visual_range, coherence=coherence
            )
            avoid_others(boids, boid)
            match_velocity(boids, boid, visual_range=visual_range)
            limit_speed(boid, max_speed=max_speed)
            keep_within_bounds(
                boid,
                width=width,
                height=height,
                margin_between_boids=margin_between_boids,
                turning_speed=turning_speed,
            )
            boid.update()

        for boid in boids:
            boid.draw(screen)

        pygame.display.flip()


import cProfile

cProfile.run("run_simulation()")