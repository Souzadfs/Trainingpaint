import pygame

# Inicializar o pygame
pygame.init()

# Configurar a tela em modo tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()  # Obter largura e altura da tela
pygame.display.set_caption("Simulação de Pintura em Linha Reta com Movimento Vertical")

# Definir cores e variáveis da bola
ball_color = (255, 0, 0)
ball_radius = 20
ball_x = screen_width // 2
ball_speed_x = 5  # Velocidade horizontal da bola no eixo X

# Variáveis de posição vertical
positions_y = [screen_height // 5, 2 * screen_height // 5, 3 * screen_height // 5, 4 * screen_height // 5]  # Quatro posições: superior, meio-superior, meio-inferior, inferior
current_y_index = 0  # Começa na posição superior
ball_y = positions_y[current_y_index]  # Define a posição inicial como superior

# Variável de controle para contagem de rebotes nas extremidades
bounce_count = 0  # Conta quantas vezes a bola bateu nas extremidades horizontais

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
                # Pressionar espaço para iniciar ou parar o movimento
                moving = not moving
            elif event.key == pygame.K_ESCAPE:
                # Pressionar ESC para sair do modo tela cheia
                running = False
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                # Aumentar a velocidade da bola ao pressionar + ou numérico +
                ball_speed_x += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                # Diminuir a velocidade da bola ao pressionar - ou numérico -
                ball_speed_x = max(1, ball_speed_x - 1)  # Garante que a velocidade não fique negativa

    # Atualizar a posição da bola se o movimento estiver ativado
    if moving:
        # Movimento horizontal
        ball_x += ball_speed_x

        # Rebote nas extremidades da tela
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            ball_speed_x = -ball_speed_x  # Inverte a direção horizontal
            bounce_count += 1  # Incrementa o contador de rebotes

            # Após dois rebotes (ida e volta), muda a posição vertical
            if bounce_count == 2:
                bounce_count = 0  # Reseta a contagem de rebotes
                if current_y_index < len(positions_y) - 1:
                    current_y_index += 1  # Vai para a linha de baixo
                else:
                    current_y_index = 0  # Volta para a linha de cima após chegar ao final
                ball_y = positions_y[current_y_index]  # Atualiza a posição vertical da bola

    # Preencher a tela e desenhar a bola
    screen.fill((255, 255, 255))  # Cor de fundo branca
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)  # Manter 60 FPS

pygame.quit()
