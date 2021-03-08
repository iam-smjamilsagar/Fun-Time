# already installed pygame in the terminal
# to use pygame need to import pygame
import pygame
from time import sleep
# here we need to initialize pygame
pygame.init()
# setup window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('soft.mp3')
pygame.mixer.music.play()
image = pygame.image.load('pic.jpg')
window.blit(image, (0, 0))
pygame.display.update()
# it will take 20 seconds to show the display
sleep(20)
pygame.mixer.music.load('gsound.mp3')
pygame.mixer.music.play()
image = pygame.image.load('ghost.jpg')
window.blit(image, (0, 0))
pygame.display.update()
sleep(5)
