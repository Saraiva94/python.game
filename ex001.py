import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
background_music = pygame.mixer.music.load('BoxCat Games - Battle.mp3')
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound('coin.wav')
crash_sound.set_volume(2)

largura = 640 
altura = 480

x_snake = int(largura / 2)
y_snake = int(altura / 2)

speed = 10
x_control = 20
y_control = 0

x_apple = randint(40, 600)
y_apple = randint(50, 430)

fonte = pygame.font.SysFont('times new roman', 20, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
relogio = pygame.time.Clock()
lista_body_snake = []
begin_body_snake = 5

def add_snake(lista_body_snake):
    for XeY in lista_body_snake:
        pygame.draw.circle(tela, (40,255,40), (XeY[0], XeY[1]), 20 )

def restart_game():
    global pontos, begin_body_snake, x_snake, y_snake, lista_body_snake, lista_head_snake, x_apple, y_apple, die
    pontos = 0
    begin_body_snake = 5
    x_snake = int(largura / 2)
    y_snake = int(altura / 2)
    lista_body_snake = []
    lista_head_snake = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    die = False

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0
            if event.key == K_d:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
            if event.key == K_w:
                if y_control == speed:
                    pass
                else:
                    y_control = -speed
                    x_control = 0
            if event.key == K_s:
                if y_control == -speed:
                    pass
                else:
                    y_control = speed
                    x_control = 0

    snake = pygame.draw.circle(tela, (40,255,40), (x_snake,y_snake), 20)

    apple = pygame.draw.rect(tela, (255, 50, 50), (x_apple,y_apple ,30,30))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        pontos += 1
        crash_sound.play()
        print('Crash')
        begin_body_snake = begin_body_snake + 1

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control

    lista_head_snake = []
    lista_head_snake.append(x_snake)
    lista_head_snake.append(y_snake)

    lista_body_snake.append(lista_head_snake)

    if lista_body_snake.count(lista_head_snake) > 1:
        fonte2 = pygame.font.SysFont('Arial', 22, True, False )
        mensagem = 'Game Over! Pressione [R] para reiniciar o game.'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_text = texto_formatado.get_rect()
        die = True
        while die:         
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()

            ret_text.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado, ret_text)
            pygame.display.update()

    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake < 0:
        y_snake = altura
    if y_snake > altura:
        y_snake = 0

    if len(lista_body_snake) > begin_body_snake:
        del lista_body_snake[0]

    add_snake(lista_body_snake)

    tela.blit(texto_formatado,(280,15))

    pygame.display.update()

