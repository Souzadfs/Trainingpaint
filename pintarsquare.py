import pygame

# Inicializar o pygame
pygame.init()

# Configurar a tela em modo tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()  # Obter largura e altura da tela
pygame.display.set_caption("Simulação de Pintura em Linha Reta com Movimento Vertical")

# Carregar a imagem da logo da Embraer e ajustar o tamanho
logo = pygame.image.load("embraer_logo.png")
logo = pygame.transform.scale(logo, (200, 100))  # Redimensionar a logo, ajuste conforme necessário
logo_x = screen_width - 1360  # Ajustar posição X da logo
logo_y = 20  # Ajustar posição Y da logo

# Definir cor, tamanho e variáveis do quadrado
square_color = (0, 0, 255)  # Cor do quadrado ao descer (pintura)
erase_color = (169, 169, 169)  # Cor para apagar (mesma cor de fundo) ao subir
square_size = 100  # Tamanho do quadrado
square_x = screen_width // 2  # Centraliza o quadrado horizontalmente
square_speed_x = 5  # Velocidade horizontal do quadrado

# Variáveis de posição vertical
positions_y = [screen_height // 5, 2 * screen_height // 5, 3 * screen_height // 5, 4 * screen_height // 5]
current_y_index = 0  # Começa na posição superior
square_y = positions_y[current_y_index]  # Define a posição inicial do quadrado

# Variável de controle para contagem de rebotes nas extremidades e direção
bounce_count = 0  # Conta quantas vezes o quadrado bateu nas extremidades horizontais
moving_down = True  # Define a direção vertical inicial (para baixo)

# Controle de movimento e visibilidade
moving = True  # Define se o quadrado está em movimento ou parado
visible = True  # Define se o quadrado está visível ou invisível

# Preencher a tela inicialmente com cinza e desenhar a logo
screen.fill((169, 169, 169))  # Fundo cinza
screen.blit(logo, (logo_x, logo_y))  # Desenha a logo uma vez

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                moving = not moving  # Iniciar ou parar o movimento
            elif event.key == pygame.K_ESCAPE:
                running = False  # Sair do modo tela cheia
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                square_speed_x += 1  # Aumentar velocidade
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                square_speed_x = max(1, square_speed_x - 1)  # Diminuir velocidade
            elif event.key == pygame.K_v:  # Alternar visibilidade com a tecla "V"
                visible = not visible  # Alternar visibilidade

    # Atualizar a posição do quadrado se o movimento estiver ativado
    if moving:
        square_x += square_speed_x

        # Rebote nas extremidades da tela
        if square_x - square_size // 2 <= 0 or square_x + square_size // 2 >= screen_width:
            square_speed_x = -square_speed_x
            bounce_count += 1

            # Após dois rebotes, mudar a posição vertical
            if bounce_count == 2:
                bounce_count = 0
                if moving_down:
                    if current_y_index < len(positions_y) - 1:
                        current_y_index += 1
                    else:
                        moving_down = False  # Muda para subir
                        current_y_index -= 1
                else:
                    if current_y_index > 0:
                        current_y_index -= 1
                    else:
                        moving_down = True  # Muda para descer
                        current_y_index += 1

                square_y = positions_y[current_y_index]  # Atualiza a posição vertical do quadrado

    # Define a cor para "pintar" ou "apagar" com base na direção do movimento
    paint_color = square_color if moving_down else erase_color

    # Desenhar o quadrado se estiver visível
    if visible:
        pygame.draw.rect(screen, paint_color, (square_x - square_size // 2, square_y - square_size // 2, square_size, square_size))

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(200)  # Manter 200 FPS

pygame.quit()
