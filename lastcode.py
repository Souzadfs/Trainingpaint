import pygame

# Inicializar o pygame
pygame.init()

# Configurar a tela em modo tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()  # Obter largura e altura da tela
pygame.display.set_caption("Simulação de Pintura em Zig-Zag")

# Carregar a imagem da logo da Embraer e ajustar o tamanho
logo = pygame.image.load("embraer_logo.png")
logo = pygame.transform.scale(logo, (200, 100))  # Redimensionar a logo, ajuste conforme necessário
logo_x = screen_width - 1360  # Ajustar posição X da logo
logo_y = 20  # Ajustar posição Y da logo

# Definir cor, tamanho e variáveis da bola
ball_color = (0, 0, 255)
ball_radius = 100  # Raio da bola
ball_x = ball_radius  # Iniciar a bola na borda esquerda
ball_speed_x = 5  # Velocidade horizontal da bola

# Variáveis de posição vertical
positions_y = [screen_height // 5, 2 * screen_height // 5, 3 * screen_height // 5, 4 * screen_height // 5]
current_y_index = 0  # Começa na posição superior
ball_y = positions_y[current_y_index]  # Define a posição inicial da bola

# Controle de movimento e visibilidade
moving = True  # Define se a bola está em movimento ou parada
visible = True  # Define se a bola está visível ou invisível

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
            elif event.key == pygame.K_v:  # Alternar visibilidade com a tecla "V"
                visible = not visible  # Alternar visibilidade

    # Atualizar a posição da bola se o movimento estiver ativado
    if moving:
        ball_x += ball_speed_x

        # Verificar se a bola atinge as extremidades da tela
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            # Inverter a direção horizontal
            ball_speed_x = -ball_speed_x
            
            # Mover para a próxima posição vertical
            current_y_index += 1
            if current_y_index >= len(positions_y):
                current_y_index = 0  # Reiniciar do topo se atingir o fim das posições

            ball_y = positions_y[current_y_index]  # Atualiza a posição vertical

    # Preencher a tela com cinza e desenhar a logo
    screen.fill((169, 169, 169))  # Fundo cinza
    screen.blit(logo, (logo_x, logo_y))  # Desenha a logo na tela

    # Desenhar a bola se estiver visível
    if visible:
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(200)  # Manter 200 FPS

pygame.quit()
