import pygame
import random
import sys
import os

pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 1000, 700
CELL_SIZE = 25
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Warna ular
snake_colors = [GREEN, BLUE, YELLOW, BLACK]
snake_color_names = ["Hijau", "Biru", "Kuning", "Hitam"]
snake_color_index = 0

# Muat suara
eat_sound = pygame.mixer.Sound('eat.mp3')
klik_sound = pygame.mixer.Sound('turn.mp3')
game_over_sound = pygame.mixer.Sound('game_over.mp3')
backsond = pygame.mixer.Sound('ejek.mp3')
intro = pygame.mixer.Sound ('game.intro.mp3')

# Font
font1 = pygame.font.SysFont("ROG FONTS", 100)
font2 = pygame.font.SysFont("chiller", 150)
font3 = pygame.font.SysFont("caurier new", 15)
font = pygame.font.SysFont("Arial", 30)
font_small = pygame.font.SysFont("Arial", 20)

# Buat layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE PYTHON")

# File skor
SCORE_FILE = "top_skor.txt"
MAX_TOP_SCORES = 10 

def load_top_scores():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r") as f:
                lines = f.readlines()
                scores = []
                for line in lines:
                    try:
                        name, score = line.strip().split(',')
                        scores.append([name, int(score)])
                    except ValueError:
                        continue
                return scores
        except Exception as e: 
            print(f"Error loading scores: {e}")
            return []
    return []

def save_top_scores(scores):
    with open(SCORE_FILE, "w") as f:
        for name, score in scores:
            f.write(f"{name},{score}\n")

def clear_top_scores():
    try:
        with open(SCORE_FILE, "w") as f:
            f.write("") 
        return True
    except Exception as e:
        print(f"Error clearing scores: {e}")
        return False

def add_to_top_scores(new_score, player_name="Pemain"):
    top_scores = load_top_scores()
    if len(top_scores) < MAX_TOP_SCORES or new_score > top_scores[-1][1]:
        top_scores.append([player_name, new_score])
        top_scores.sort(key=lambda x: x[1], reverse=True)
        top_scores = top_scores[:MAX_TOP_SCORES]
        save_top_scores(top_scores)
        return True 
    return False 

# Fungsi menggambar grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

# Fungsi menggambar ular
def draw_snake(snake):
    for segment in snake:
        rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, snake_colors[snake_color_index], rect)

# Fungsi menggambar makanan
def draw_food(position, blink):
    color = RED if blink else YELLOW
    rect = pygame.Rect(position[0]*CELL_SIZE, position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

# Menampilkan skor
def show_score(score):
    score_text = font.render(f"Skor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
# Fungsi untuk input nama pemain
def get_player_name(score):
    input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 20, 300, 40)
    color_inactive = BLACK
    color_active = BLUE
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        screen.fill(WHITE)
        title_text = font.render(f"Skor Anda: {score}", True, BLACK)
        prompt_text = font.render("Masukkan nama Anda:", True, BLACK)
        enter_text = font_small.render("(Tekan ENTER untuk melanjutkan)", True, BLACK)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 200))
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, 250))
        
        txt_surface = font.render(text, True, color)
        width = max(300, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        screen.blit(enter_text, (WIDTH // 2 - enter_text.get_width() // 2, input_box.y + input_box.height + 10))

        pygame.display.flip()
    
    return text if text else "Pemain" 

    

# Menu utama
def main_menu():
    global snake_color_index
    while True:
        intro.play()
        screen.fill(WHITE)
        title = font1.render("SNAPPY", True, BLACK)
        start = font.render("SPACE : mulai", True, BLACK)
        color = font.render("  C   : ganti warna ular", True, BLACK)
        top_score_btn = font.render("  T   : Top Skor", True, BLACK) 
        exit_game = font.render(" ESC  : keluar", True, BLACK)
        current_color = font.render(f"Warna ular: {snake_color_names[snake_color_index]}", True, BLACK)
        title1 = font3.render("By:Kelompok 48 |Nanda(2210433004)|Lidea(2410431024)|", True, BLACK)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        screen.blit(start, (WIDTH//2 - start.get_width()//2, 250))
        screen.blit(color, (WIDTH//2 - color.get_width()//2, 280))
        screen.blit(top_score_btn, (WIDTH//2 - top_score_btn.get_width()//2, 310)) 
        screen.blit(exit_game, (WIDTH//2 - exit_game.get_width()//2, 340))
        screen.blit(current_color, (WIDTH//2 - current_color.get_width()//2, 380))
        screen.blit(title1, (WIDTH//2.4 - start.get_width()//2, 430)) 

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro.stop()
                    return
                elif event.key == pygame.K_c:
                    snake_color_index = (snake_color_index + 1) % len(snake_colors)
                elif event.key == pygame.K_t: 
                    intro.stop()
                    show_top_scores_screen()
                    intro.play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Fungsi konfirmasi untuk penghapusan skor
def confirm_clear_scores():
    while True:
        screen.fill(WHITE)
        confirm_text = font.render("Yakin ingin menghapus semua skor?", True, BLACK)
        yes_text = font_small.render("Tekan Y untuk YA", True, BLACK)
        no_text = font_small.render("Tekan N untuk TIDAK", True, BLACK)

        screen.blit(confirm_text, (WIDTH // 2 - confirm_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(yes_text, (WIDTH // 2 - yes_text.get_width() // 2, HEIGHT // 2 + 10))
        screen.blit(no_text, (WIDTH // 2 - no_text.get_width() // 2, HEIGHT // 2 + 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                if event.key == pygame.K_n:
                    return False

# Layar Top Skor
def show_top_scores_screen():
    while True:
        top_scores = load_top_scores()  
        screen.fill(WHITE)
        title = font.render("TOP SKOR", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        y_offset = 120
        if not top_scores:
            no_scores_text = font_small.render("Belum ada skor tercatat.", True, BLACK)
            screen.blit(no_scores_text, (WIDTH // 2 - no_scores_text.get_width() // 2, y_offset))
        else:
            header_text = font_small.render("Peringkat | Nama             | Skor", True, BLACK)
            screen.blit(header_text, (WIDTH // 2 - header_text.get_width() // 2, y_offset - 30))
            pygame.draw.line(screen, BLACK, (WIDTH // 2 - header_text.get_width() // 2, y_offset - 5), 
                                            (WIDTH // 2 + header_text.get_width() // 2, y_offset - 5), 1)

            for i, (name, score) in enumerate(top_scores):
                score_display = f"{i+1:<8} {name:<20} {score}"
                score_text = font_small.render(score_display, True, BLACK)
                screen.blit(score_text, (WIDTH // 2 - header_text.get_width() // 2, y_offset + i * 30))

        # Opsi untuk kembali dan menghapus
        back_text = font_small.render("Tekan ESC untuk kembali ke menu", True, BLACK)
        delete_text = font_small.render("Tekan D untuk Hapus Semua Skor", True, RED) 
        
        screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 80))
        screen.blit(delete_text, (WIDTH // 2 - delete_text.get_width() // 2, HEIGHT - 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_d: 
                    if confirm_clear_scores(): 
                        clear_top_scores()
                        print("Semua skor telah dihapus!")

# Game over screen
def game_over_screen(score):
    top_scores = load_top_scores()
    should_get_name = False
    if len(top_scores) < MAX_TOP_SCORES:
        should_get_name = True
    elif top_scores and score > top_scores[-1][1]: 
        should_get_name = True

    player_name = "Pemain"
    if should_get_name:
        player_name = get_player_name(score) 
        add_to_top_scores(score, player_name) 
    while True:
        screen.fill(WHITE)
        over = font2 .render("GAME OVER", True, RED)
        skor = font.render(f"Skor Kamu: {score}", True, BLACK)
        name_display = font.render(f"Nama: {player_name}", True, BLACK) 
        instr1 = font.render("Tekan R untuk main lagi", True, BLACK)
        instr2 = font.render("Tekan M untuk kembali ke menu", True, BLACK)

        screen.blit(over, (WIDTH//2 - over.get_width()//2, 140))
        screen.blit(skor, (WIDTH//2 - skor.get_width()//2, 300))
        if should_get_name: 
            screen.blit(name_display, (WIDTH//2 - name_display.get_width()//2, 270)) 
        screen.blit(instr1, (WIDTH//2 - instr1.get_width()//2, 330))
        screen.blit(instr2, (WIDTH//2 - instr2.get_width()//2, 360))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over_sound.stop()
                    backsond.stop()
                    return True
                elif event.key == pygame.K_m:
                    return False

# Fungsi utama game
def main_game():
    clock = pygame.time.Clock()
    snake = [(COLS // 2, ROWS // 2)]
    direction = (1, 0)
    food = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
    score = 0
    speed = 5
    blink_timer = 0
    blink = True
    MAX_SPEED = 20

    running = True
    while running:
        clock.tick(speed)
        blink_timer += 1
        if blink_timer % 10 == 0:
            blink = not blink

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, 1):
            direction = (0, -1)
            klik_sound.play()
        elif keys[pygame.K_DOWN] and direction != (0, -1):
            direction = (0, 1)
            klik_sound.play()
        elif keys[pygame.K_LEFT] and direction != (1, 0):
            direction = (-1, 0)
            klik_sound.play()
        elif keys[pygame.K_RIGHT] and direction != (-1, 0):
            direction = (1, 0)
            klik_sound.play()

        head = snake[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])

        # Cek tabrakan
        if (
            new_head[0] < 0 or new_head[0] >= COLS or
            new_head[1] < 0 or new_head[1] >= ROWS or
            new_head in snake[1:] 
        ):
            backsond.play()
            game_over_sound.play() 
            print(f"Game Over! Skor: {score}")
            running = False

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            eat_sound.play() 
            if speed < MAX_SPEED:
                speed += 1
                
            while True:
                food = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
                if food not in snake:
                    break
        else:
            snake.pop()

        screen.fill(WHITE)
        draw_grid()
        draw_snake(snake)
        draw_food(food, blink)
        show_score(score) 
        pygame.display.flip()

    # Tampilkan layar game over dan opsi main ulang atau kembali menu
    if game_over_screen(score):
        main_game()

# Jalankan aplikasi
if __name__ == "__main__":
    while True:
        main_menu()
        main_game()