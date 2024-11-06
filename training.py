import pygame

# Inicializar o pygame
pygame.init()

# Configurar a tela em modo tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()  # Obter largura e altura da tela
pygame.display.set_caption("Simulação de Pintura em Linha Reta com Rebote")

# Definir cores e variáveis da bola
ball_color = (255, 0, 0)
ball_radius = 20
ball_x, ball_y = screen_width // 2, screen_height // 2  # Começa no meio da tela
ball_speed_x = 5  # Velocidade horizontal da bola no eixo X

# Controle de movimento (iniciar como True para começar em movimento)
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
            ball_speed_x = -ball_speed_x  # Inverte a direção

    # Preencher a tela e desenhar a bola
    screen.fill((255, 255, 255))  # Cor de fundo branca
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)  # Manter 60 FPS

pygame.quit()