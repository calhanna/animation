# animation
An animation class for python arcade. Includes demo with bouncing and colour changing squares 

Usage:

Unpack animation.py into the folder with your main game file

from animation import Animation

Animation(frames, dt)

animation_demo.py must be run in the same direc as animation.py

To repeat a frame, give '_n' as the frame after with n = number of repetitions

Class Arguments:
        -   frames: array containing executable strings. 
        -   dt: how many ticks per frame

Note: First frame cannot have '_' as it's first character, as this signifies a repeat
