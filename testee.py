import pygame

# Inicializar o pygame
pygame.init()

# Configurar a tela como redimensionável
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Simulação de Pintura em Zig-Zag")

# Obter largura e altura da tela
screen_width, screen_height = screen.get_size()

# Carregar a imagem da logo da Embraer e ajustar o tamanho
logo = pygame.image.load("embraer_logo.png")
logo = pygame.transform.scale(logo, (200, 100))  # Redimensionar a logo
logo_x = screen_width - 220  # Ajustar posição X da logo
logo_y = 20  # Ajustar posição Y da logo

# Definir cor, tamanho e variáveis da bola
ball_color = (0, 0, 255)
ball_radius = 100  # Raio da bola
ball_x = ball_radius  # Iniciar a bola na borda esquerda
ball_speed_x = (screen_width - 2 * ball_radius) // 9  # Distância para 9 passos horizontais

# Variáveis de posição vertical para 8 passadas
positions_y = [
    screen_height // 9, 2 * screen_height // 9, 3 * screen_height // 9,
    4 * screen_height // 9, 5 * screen_height // 9, 6 * screen_height // 9,
    7 * screen_height // 9, 8 * screen_height // 9
]
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
        elif event.type == pygame.VIDEORESIZE:
            # Atualizar largura e altura quando a janela for redimensionada
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            
            # Atualizar posições verticais, logo e velocidade
            positions_y = [
                screen_height // 9, 2 * screen_height // 9, 3 * screen_height // 9,
                4 * screen_height // 9, 5 * screen_height // 9, 6 * screen_height // 9,
                7 * screen_height // 9, 8 * screen_height // 9
            ]
            logo_x = screen_width - 220
            ball_speed_x = (screen_width - 2 * ball_radius) // 9
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                moving = not moving  # Iniciar ou parar o movimento
            elif event.key == pygame.K_ESCAPE:
                running = False  # Sair do programa
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                ball_speed_x += 1  # Aumentar a velocidade
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                ball_speed_x = max(1, ball_speed_x - 1)  # Diminuir a velocidade com limite mínimo
            elif event.key == pygame.K_v:  # Alternar visibilidade com a tecla "V"
                visible = not visible  # Alternar visibilidade

    # Atualizar a posição da bola se o movimento estiver ativado
    if moving:
        ball_x += ball_speed_x

        # Verificar se a bola atinge os limites da tela
        if ball_x + ball_radius > screen_width or ball_x - ball_radius < 0:
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
    clock.tick(10)  # Manter 200 FPS

pygame.quit()
