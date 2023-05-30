#Faça um programa em pyton que e reproduza o áudio de um arquivo mp3 
import pygame

pygame.mixer.init()

pygame.init()

pygame.mixer.music.load('D:/tocar_mp3/musica.mp3')

pygame.mixer.music.play(loops=0,start=0.0)

pygame.event.wait()
input('Vamos lá')

