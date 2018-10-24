import pygame

'''Faça um programa que seja capaz de tocar um mp3'''

pygame.init()
pygame.mixer.music.load('oi.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''É necessário instalar o pacote do pygame, não é o foco do curso neste momento
como dito pelo prof Gustavo Guanabara no desafio.'''

'''É necessário que o arquivo de áudio esteja no mesmo projeto que vocẽ está fazendo o programa, 
na mesma pasta. Não estou commitando o .mp3 porque a música fica a sua escolha.'''