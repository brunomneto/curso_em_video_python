'''import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('acidjazz.mp3')
pygame.mixer.music.play(1, 0, 0)
pygame.event.wait()

from pygame import mixer
mixer.init()
mixer.music.load('acidjazz.mp3')
mixer.music.play()
input()'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('acidjazz.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
