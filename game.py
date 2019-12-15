# coding: utf-8
import pygame
from random import randint
pygame.init() # FUNÇÂO INICIAl PYGAME
x = 400 # POSIÇÃO HORIZONTAL DO RATO (VALOR MAX 400, VALOR MIN 80)
y = 100 # POSIÇÃO VERTICAL DO RATO
pos_x = 300 # POSIÇÃO HORIZONTAL DO GATO
pos_y = 800 # POSIÇÃO VERTICAL DO RATO
pos_x_z = 100 # POSIÇÃO HORIZONTAL DO GATO 2
pos_y_z = 800 # POSIÇÂO VERTICAL DO GATO2
velocidade = 10 # VELOCIDADE DO MEU JOGADOR(RATO)
velocidade_outros = 7 # VELOCIDADE DO VILÃO(GATO)
fundo = pygame.image.load('pista.jpg')
rato = pygame.image.load('rato.jpg')
gato =  pygame.image.load('gato.jpg')
gato2 =  pygame.image.load('gato.jpg')
tempo_segundo = 0
timer = 0

font = pygame.font.SysFont('arial black', 30)
texto = font.render("TEMPO: ", True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pygame.display.set_mode((600,800)) # JANELA PRINCIPAL(MAIN)
pygame.display.set_caption("JOGUINHO") # NOME DA JANELA
janela_aberta = True # LAÇO INFINITO PARA A WINDOW PERMANECER OPEN

while janela_aberta:
    pygame.time.delay(50) # TEMPO EM MILISEGUNDOS PARA SER FEITA A ATUALIZAÇÃO DE POSIÇÂO DO RATO E GATO
    for event in pygame.event.get(): # VERIFICA QUE EVENTO É CHAMADO
        if event.type == pygame.QUIT: # A JANELA SÓ IRÁ FECHAR CASO O BOTÃO EXIT SEJA ACIONADO
            janela_aberta = False # ENQUANTO NÃO FOR, PERMANECERÁ ABERTA

    comandos = pygame.key.get_pressed() # VARIÁVEl PRINCIPAL DOS COMANDOS
    if comandos[pygame.K_LEFT] and x >= 80:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 400:
        x += velocidade

    if(pos_y < -20): # CASO O GATO JÁ NÃO ESTEJA VISIVEL NA TELA, ELA IRÁ VOLTAR PARA 850 PIXELS PARA BAIXO PARA FICAR EM UM LOOP
        pos_y = randint(850,2000)

    if(pos_y_z < -20): # CASO O GATO JÁ NÃO ESTEJA VISIVEL NA TELA, ELA IRÁ VOLTAR PARA 850 PIXELS PARA BAIXO PARA FICAR EM UM LOOP
        pos_y_z = randint(850,2000)

    if (timer < 20): 
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("TEMPO: "+str(tempo_segundo), True, (255,255,100), (0,0,0))
        timer = 0

    if pos_x == x: # SE A POSIÇÃO HORIZONTAL DO 1º GATO FOR IGUAL A POSIÇÃO DO RATO O TEMPO ZERA
        tempo_segundo = 0

    if pos_y == y: # SE A POSIÇÃO VERTICAL DO 1º GATO FOR IGUAL A POSIÇÃO DO RATO O TEMPO ZERA
        tempo_segundo = 0

    if pos_x_z == x: # SE A POSIÇÃO HORIZONTAL DO 2º GATO FOR IGUAL A POSIÇÃO DO RATO O TEMPO ZERA
        tempo_segundo = 0

    if pos_y_z == y: # SE A POSIÇÃO VERTICAL DO 2º GATO FOR IGUAL A POSIÇÃO DO RATO, ADIVINHA?
        tempo_segundo = 0


    pos_y -= velocidade_outros # ISSO FARA COM QUE O PRIMEIRO GATO FIQUE SUBINDO, POIS SUA POSIÇÃO É IGUAL AO DECREMENTO DA VARIAVEL velocidade_outros
    pos_y_z -= velocidade_outros # EXATAMENTE A MESMA COISA QUE A LINHA ACIMA, NO ENTANTO PARA O 2º GATO

    janela.blit(fundo,(0,0)) # POSIÇÃO E CHAMADA DO OBJETO DE FUNDO
    janela.blit(rato,(x,y)) # POSIÇÃO DO JOGADOR PRINCIPAL(RATO)
    janela.blit(gato,(pos_x,pos_y)) # POSIÇÃO DO 1º GATO
    janela.blit(gato2,(pos_x_z,pos_y_z)) # POSIÇÃO DO 2º GATO
    janela.blit(texto, pos_texto) # TEMPO

    pygame.display.update() # ATT PARA O DELAY

pygame.quit()
