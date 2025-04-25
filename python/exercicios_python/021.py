# Escreva um programa que abra e toque um mp3
import pygame
pygame.init()
pygame.mixer.music.load ('021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
