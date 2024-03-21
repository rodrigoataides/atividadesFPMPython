# configurações iniciais

import pygame
import random

pygame.init()

pygame.display.set_caption("Jogo Snake Python")

largura, altura = 600, 400

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

# cores RGB

preta = (0, 0, 0)

branca = (255, 255, 255)

vermelha = (255, 0, 0)

verde = (0, 255, 0)

# parametros da cobrinha

tamanho_quadrado = 20

velocidade_jogo = 10

def gerar_comida():

    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):

    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):

    for pixel in pixels:

        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):

    fonte = pygame.font.SysFont("Helvetica", 35)

    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)

    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):

    if tecla == pygame.K_DOWN:

        velocidade_x = 0

        velocidade_y = tamanho_quadrado

    elif tecla == pygame.K_UP:

        velocidade_x = 0

        velocidade_y = -tamanho_quadrado

    elif tecla == pygame.K_RIGHT:

        velocidade_x = tamanho_quadrado

        velocidade_y = 0

    elif tecla == pygame.K_LEFT:

        velocidade_x = -tamanho_quadrado

        velocidade_y = 0

    return velocidade_x, velocidade_y

def rodar_jogo():

    fim_jogo = False

    x = largura / 2

    y = altura / 2

    velocidade_x = 0

    velocidade_y = 0

    tamanho_cobra = 1

    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:

        tela.fill(preta)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                fim_jogo = True

            elif evento.type == pygame.KEYDOWN:

                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar_comida

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posicao da cobra

        if x < 0 or x >= largura or y < 0 or y >= altura:

            fim_jogo = True

        x += velocidade_x

        y += velocidade_y

        # desenhar_cobra

        pixels.append([x, y])

        if len(pixels) > tamanho_cobra:

            del pixels[0]

        # se a cobrinha bateu no proprio corpo

        for pixel in pixels[:-1]:

            if pixel == [x, y]:

                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        # desenhar_pontos

        desenhar_pontuacao(tamanho_cobra - 1)

        # atualizacao da tela

        pygame.display.update()

        # criar uma nova comida

        if x == comida_x and y == comida_y:

            tamanho_cobra += 1

            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

rodar_jogo()