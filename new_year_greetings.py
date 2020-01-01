# -*- coding: utf-8 -*-
"""
new_year_greetings.py

Copyright (c) 2020 @RR_Inyo
Released under the MIT license.
https://opensource.org/licenses/mit-license.php
"""

# Preparations
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NFRAMES = 60
RADIUS = 1.0
RESOLUTION = 200
LIMIT = 4
LINE_WIDTH = 4
ALPHA = 0.6
AMPLITUDE = 0.15
SEPARATION = 1.5
NWAVES = 10
NMOD = 5
AMPMOD_OFFSET = 1.7
TEXT_HEIGHT = 3
TEXT_SIZE = 35
TEXT_ALPHA = 0.9
TEXT_FRAME = 10
INTERVAL = 250
REPEAT_DELAY = 2500

# Figure and Axes configuration
fig, ax = plt.subplots(figsize = (9, 9))

# Plotting function
def update(i):

    ## Clearing the Axes for the new frame
    ax.cla()
    ax.set_xlim(-LIMIT, LIMIT)
    ax.set_ylim(-LIMIT, LIMIT)
    ax.grid()
    
    ## Data and plotting: Sun
    height = 3 * i / NFRAMES - 1.6
    if height > -RADIUS and height < RADIUS:
        phi = np.arcsin(height / RADIUS)
        theta = np.arange(-phi, np.pi + phi, np.pi / RESOLUTION)
        xs = RADIUS * np.cos(theta)
        ys = RADIUS * np.sin(theta) + height
        ax.plot(xs, ys, color = 'orangered', lw = LINE_WIDTH, alpha = ALPHA)
        ax.fill(xs, ys, color = 'lightcoral', lw = LINE_WIDTH, alpha = ALPHA)
    elif height >= RADIUS:
        theta = np.arange(-np.pi / 2, 3 * np.pi / 2, np.pi / RESOLUTION)
        xs = RADIUS * np.cos(theta)
        ys = RADIUS * np.sin(theta) + height
        ax.plot(xs, ys, color = 'orangered', lw = LINE_WIDTH, alpha = ALPHA)
        ax.fill(xs, ys, color = 'lightcoral', lw = LINE_WIDTH, alpha = ALPHA)

    ## Data: Waves
    delta = 2 * np.pi * i / NFRAMES
    ampmod = AMPMOD_OFFSET + np.cos(NMOD * 2 * np.pi * i / NFRAMES)
    xw = np.arange(-LIMIT, LIMIT, LIMIT / RESOLUTION)
    yw1 = -AMPLITUDE * ampmod * np.abs(np.sin(xw / LIMIT * NWAVES + delta))
    yw2 = -AMPLITUDE * ampmod * np.abs(np.sin(xw / LIMIT * NWAVES - delta - np.deg2rad(120))) - SEPARATION
    yw3 = -AMPLITUDE * ampmod * np.abs(np.sin(xw / LIMIT * NWAVES + delta + np.deg2rad(120))) - 2 * SEPARATION

    ## Plotting: Waves
    ax.plot(xw, yw1, color = 'mediumblue', lw = LINE_WIDTH, alpha = ALPHA)
    ax.fill_between(xw, yw1, -LIMIT, color = 'royalblue', lw = LINE_WIDTH, alpha = ALPHA / 2)
    ax.plot(xw, yw2, color = 'mediumblue', lw = LINE_WIDTH, alpha = ALPHA)
    ax.plot(xw, yw3, color = 'mediumblue', lw = LINE_WIDTH, alpha = ALPHA)
    
    ## Graph title
    ax.set_title('New Year Greetings')

    ## Text
    if i > NFRAMES - TEXT_FRAME:
        ax.text(0, TEXT_HEIGHT, 'Happy New Year!', color = 'blueviolet', alpha = TEXT_ALPHA, \
                size = TEXT_SIZE, horizontalalignment = 'center', fontweight = 'bold')
        ax.text(LIMIT - 0.2, -LIMIT + 0.2, r'$\copyright$ 2020 @RR_Inyo', color = 'darkcyan', alpha = TEXT_ALPHA, \
                size = TEXT_SIZE * 0.5, horizontalalignment = 'right', fontweight = 'bold')

# Creating and saving the animation
ani = animation.FuncAnimation(fig, update, frames = NFRAMES, interval = INTERVAL, repeat_delay = REPEAT_DELAY)
ani.save('output.gif', writer = 'imagemagick')
