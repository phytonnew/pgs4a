import pygame
import sys

# --- Configurações do Jogo ---
LARGURA_TELA = 800
ALTURA_TELA = 600
VELOCIDADE_JOGADOR = 5
TAMANHO_JOGADOR = 50
TAMANHO_MOEDA = 30
COR_CEU = (135, 206, 235)  # Azul celeste
COR_CHAO = (34, 139, 34)   # Verde floresta
COR_JOGADOR = (255, 0, 0)  # Vermelho
COR_MOEDA = (255, 223, 0)  # Amarelo ouro
FONT_COR = (255, 255, 255) # Branco para o texto

# --- Inicialização do Pygame ---
pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Coletor de Moedas")
clock = pygame.time.Clock()

# --- Posições Iniciais ---
# Jogador no centro inferior do chão
jogador_x = LARGURA_TELA // 2 - TAMANHO_JOGADOR // 2
jogador_y = ALTURA_TELA - TAMANHO_JOGADOR - 50 # Acima do chão

# Posições das moedas (x, y)
moedas = [
    pygame.Rect(100, ALTURA_TELA - 100, TAMANHO_MOEDA, TAMANHO_MOEDA),   # Moeda 1 (esquerda)
    pygame.Rect(250, ALTURA_TELA - 100, TAMANHO_MOEDA, TAMANHO_MOEDA),   # Moeda 2 (esquerda)
    pygame.Rect(LARGURA_TELA - 150, ALTURA_TELA - 100, TAMANHO_MOEDA, TAMANHO_MOEDA) # Moeda 3 (direita)
]
moedas_coletadas = 0

# --- Loop Principal do Jogo ---
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # --- Movimento do Jogador ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_x -= VELOCIDADE_JOGADOR
    if teclas[pygame.K_RIGHT]:
        jogador_x += VELOCIDADE_JOGADOR

    # Limita o jogador na tela
    if jogador_x < 0:
        jogador_x = 0
    if jogador_x > LARGURA_TELA - TAMANHO_JOGADOR:
        jogador_x = LARGURA_TELA - TAMANHO_JOGADOR

    # --- Colisão com as Moedas ---
    jogador_rect = pygame.Rect(jogador_x, jogador_y, TAMANHO_JOGADOR, TAMANHO_JOGADOR)
    
    moedas_restantes = []
    for moeda in moedas:
        if jogador_rect.colliderect(moeda):
            moedas_coletadas += 1
        else:
            moedas_restantes.append(moeda)
    moedas = moedas_restantes # Remove as moedas coletadas

    # --- Desenhar na Tela ---
    tela.fill(COR_CEU) # Céu azul
    pygame.draw.rect(tela, COR_CHAO, (0, ALTURA_TELA - 70, LARGURA_TELA, 70)) # Chão verde

    # Desenha o jogador
    pygame.draw.rect(tela, COR_JOGADOR, (jogador_x, jogador_y, TAMANHO_JOGADOR, TAMANHO_JOGADOR))

    # Desenha as moedas
    for moeda in moedas:
        pygame.draw.circle(tela, COR_MOEDA, moeda.center, TAMANHO_MOEDA // 2)

    # Exibe a quantidade de moedas
    fonte = pygame.font.Font(None, 36)
    texto_moedas = fonte.render(f"Moedas: {moedas_coletadas}/3", True, FONT_COR)
    tela.blit(texto_moedas, (10, 10))

    # --- Condição de Vitória ---
    if moedas_coletadas >= 3:
        fonte_vitoria = pygame.font.Font(None, 74)
        texto_vitoria = fonte_vitoria.render("VOCÊ VENCEU!", True, FONT_COR)
        texto_vitoria_rect = texto_vitoria.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
        tela.blit(texto_vitoria, texto_vitoria_rect)
        executando = False # Termina o jogo após vencer

    # --- Atualizar a Tela ---
    pygame.display.flip()

    # --- Controle de FPS ---
    clock.tick(60) # Limita o jogo a 60 frames por segundo

# --- Finalização do Pygame ---
pygame.quit
