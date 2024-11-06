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
positions_y = [screen_height // 4, screen_height // 2, 3 * screen_height // 4]  # Topo, centro, fundo
current_y_index = 0  # Começa na posição superior
ball_y = positions_y[current_y_index]  # Define a posição inicial como topo

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
                ball_speed_x = max(1, ball_speed_x - 1)  # Garante que
