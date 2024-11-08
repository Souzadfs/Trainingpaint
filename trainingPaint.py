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

# Definir cor, tamanho e variáveis da bola
ball_color = (0, 0, 255)
ball_radius = 100  # Raio da bola
ball_x = screen_width // 2  # Centraliza a bola horizontalmente
ball_speed_x = 5  # Velocidade horizontal da bola

# Variáveis de posição vertical
positions_y = [screen_height // 5, 2 * screen_height // 5, 3 * screen_height // 5, 4 * screen_height // 5]
current_y_index = 0  # Começa na posição superior
ball_y = positions_y[current_y_index]  # Define a posição inicial da bola

# Variável de controle para contagem de rebotes nas extremidades e direção
bounce_count = 0  # Conta quantas vezes a bola bateu nas extremidades horizontais
moving_down = True  # Define a direção vertical inicial (para baixo)

# Controle de movimento
moving = True  # Define se a bola está em movimento ou parada

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
                ball_speed_x += 1  # Aumentar velocidade
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                ball_speed_x = max(1, ball_speed_x - 1)  # Diminuir velocidade

    # Atualizar a posição da bola se o movimento estiver ativado
    if moving:
        ball_x += ball_speed_x

        # Rebote nas extremidades da tela
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            ball_speed_x = -ball_speed_x
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

                ball_y = positions_y[current_y_index]  # Atualiza a posição vertical da bola

    # Preencher a tela com cinza e desenhar a logo
    screen.fill((169, 169, 169))  # Fundo cinza
    screen.blit(logo, (logo_x, logo_y))  # Desenha a logo na tela

    # Desenhar a bola
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(200)  # Manter 60 FPS

pygame.quit()
