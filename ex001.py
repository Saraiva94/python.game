import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
b_m = pygame.mixer.music.load('BoxCat Games - Battle.mp3')
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound('coin.wav')
crash_sound.set_volume(2)

largura = 640 
altura = 480

x_snake = int(largura / 2)
y_snake = int(altura / 2)

x_apple = randint(40, 600)
y_apple = randint(50, 430)

fonte = pygame.font.SysFont('times new roman', 20, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
relogio = pygame.time.Clock()
lista_body_snake = []

def add_snake(lista_body_snake):
    for XeY in lista_body_snake:
        pygame.draw.circle(tela, (40,255,40), (XeY[0], XeY[1]), 20 )

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x_snake = x_snake - 20
    if pygame.key.get_pressed()[K_s]:
        y_snake = y_snake + 20
    if pygame.key.get_pressed()[K_d]:
        x_snake = x_snake + 20
    if pygame.key.get_pressed()[K_w]:
        y_snake = y_snake - 20

    snake = pygame.draw.circle(tela, (40,255,40), (x_snake,y_snake), 20)

    apple = pygame.draw.rect(tela, (255, 50, 50), (x_apple,y_apple ,30,30))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        pontos += 1
        crash_sound.play()
        print('Crash')

    lista_head_snake = []
    lista_head_snake.append(x_snake)
    lista_head_snake.append(y_snake)


    lista_body_snake.append(lista_head_snake)

    add_snake(lista_body_snake)

    tela.blit(texto_formatado,(280,15))

    pygame.display.update()



    '''
    if event.type == KEYDOWN:
        if event.key == K_a:
            x = x - 20
        if event.key == K_d:
            x = x + 20
        if event.key == K_w:
            y = y - 20
        if event.key == K_s:
            y = y + 20
    '''