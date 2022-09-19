import pygame
from sys import exit
import random

def get_indexes(id, length):
    row_num = id // length
    col_num = id % length
    return row_num, col_num

def check_bombs(id, tiles):
    surrounding_bombs = 0

    # Top tile
    top_id = id - TILE_NUM
    if top_id >= 0:
        if tiles[top_id].is_bomb:
            surrounding_bombs += 1
    
    # Top-right tile
    top_right_id = (id - TILE_NUM) + 1
    if top_right_id % TILE_NUM > 0:
        if tiles[top_right_id].is_bomb:
            surrounding_bombs += 1

    # Right tile
    right_id = id + 1
    if right_id % TILE_NUM > 0:
        if tiles[right_id].is_bomb:
            surrounding_bombs += 1

    # Bottom-right tile
    bottom_right_id = id + TILE_NUM + 1
    if bottom_right_id % TILE_NUM > 0:
        if tiles[bottom_right_id].is_bomb:
            surrounding_bombs += 1

    # Bottom tile
    bottom_id = id + TILE_NUM
    if bottom_id <= TILE_NUM ** 2:
        if tiles[bottom_id].is_bomb:
            surrounding_bombs += 1

    # Bottom-left tile
    bottom_left_id = id + TILE_NUM - 1
    if bottom_left_id % TILE_NUM < TILE_NUM - 1:
        if tiles[bottom_left_id].is_bomb:
            surrounding_bombs += 1

    # Left tile
    left_id = id - 1
    if left_id % TILE_NUM < TILE_NUM - 1:
        if tiles[left_id].is_bomb:
            surrounding_bombs += 1

    # Top-left tile
    top_left_id = id - 1
    if top_left_id % TILE_NUM < TILE_NUM - 1:
        if tiles[top_left_id].is_bomb:
            surrounding_bombs += 1

    return surrounding_bombs


def perform_lookaround(tile, tiles):
    global game_over
    ## FIRST CHECK IF THERE ARE MINES SURROUNDING TILE
    # First check top tile, then go around clockwise

    if tile.is_bomb:
        game_over = True
        for tile in tiles:
            if tile.is_bomb:
                tile.image = pygame.image.load('assets/tile_mine.png')
        return

    if tile.is_visited:
        return
    else:
        surrounding_bombs = 0

        # Top tile
        top_id = tile.id - TILE_NUM
        #print("TOP ID:", top_id)
        if top_id >= 0 and top_id < TILE_NUM ** 2:
            if tiles[top_id].is_bomb:
                surrounding_bombs += 1
        else:
            top_id = None
        
        # Top-right tile
        top_right_id = (tile.id - TILE_NUM) + 1
        #print("TOP RIGHT ID:", top_right_id)
        if top_right_id % TILE_NUM > 0 and top_right_id >= 0:
            if tiles[top_right_id].is_bomb:
                surrounding_bombs += 1
        else:
            top_right_id = None

        # Right tile
        right_id = tile.id + 1
        #print("RIGHT ID:", right_id)
        if right_id % TILE_NUM > 0 and right_id < TILE_NUM ** 2 and right_id >= 0:
            if tiles[right_id].is_bomb:
                surrounding_bombs += 1
        else:
            right_id = None

        # Bottom-right tile
        bottom_right_id = tile.id + TILE_NUM + 1
        #print("BOTTOM RIGHT ID:", bottom_right_id)
        if bottom_right_id % TILE_NUM > 0 and bottom_right_id < TILE_NUM ** 2 and bottom_right_id >= 0:
            if tiles[bottom_right_id].is_bomb:
                surrounding_bombs += 1
        else:
            bottom_right_id = None

        # Bottom tile
        bottom_id = tile.id + TILE_NUM
        #print("BOTTOM ID:", bottom_id)
        if bottom_id < TILE_NUM ** 2 and bottom_id >= 0:
            if tiles[bottom_id].is_bomb:
                surrounding_bombs += 1
        else:
            bottom_id = None

        # Bottom-left tile
        bottom_left_id = tile.id + TILE_NUM - 1
        #print("BOTTOM LEFT ID:", bottom_left_id)
        if bottom_left_id % TILE_NUM < TILE_NUM - 1 and bottom_left_id < TILE_NUM ** 2 and bottom_left_id >= 0:
            if tiles[bottom_left_id].is_bomb:
                surrounding_bombs += 1
        else:
            bottom_left_id = None

        # Left tile
        left_id = tile.id - 1
        #print("LEFT ID:", left_id)
        if left_id % TILE_NUM < TILE_NUM - 1 and left_id >= 0:
            if tiles[left_id].is_bomb:
                surrounding_bombs += 1
        else:
            left_id = None

        # Top-left tile
        top_left_id = tile.id - TILE_NUM - 1
        #print("TOP LEFT ID:", top_left_id)
        if top_left_id % TILE_NUM < TILE_NUM - 1 and top_left_id >= 0:
            if tiles[top_left_id].is_bomb:
                surrounding_bombs += 1
        else:
            top_left_id = None


        tile.image = pygame.image.load('assets/tile_pressed.png').convert_alpha()
        tile.is_visited = True
        if surrounding_bombs > 0:
            tile.number = surrounding_bombs
            return
        else:
            
            # Top tile
            if top_id != None:
                perform_lookaround(tiles[top_id], tiles)
            if top_right_id != None:
                perform_lookaround(tiles[top_right_id], tiles)
            if right_id != None:
                perform_lookaround(tiles[right_id], tiles)
            if bottom_right_id != None:
                perform_lookaround(tiles[bottom_right_id], tiles)
            if bottom_id != None:
                perform_lookaround(tiles[bottom_id], tiles)
            if bottom_left_id != None:
                perform_lookaround(tiles[bottom_left_id], tiles)
            if left_id != None:
                perform_lookaround(tiles[left_id], tiles)
            if top_left_id != None:
                perform_lookaround(tiles[top_left_id], tiles)
    
    

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, pos, id):
        super().__init__()
        self.image = pygame.image.load('assets/tile_normal.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.id = id
        self.number = 0
        self.marked = False
        self.is_bomb = False
        self.is_visited = False

    def draw_num(self):
        if self.number > 0:
            num = num_font.render(f'{self.number}', 1, (0, 0, 0))
            screen.blit(num, (self.rect.x, self.rect.y))

    def set_marked(self, mouse_pos, right_mouse_click):
        if mouse_pos[0] >= self.rect.left and mouse_pos[0] <= self.rect.right and mouse_pos[1] >= self.rect.top and mouse_pos[1] <= self.rect.bottom and right_mouse_click and not self.is_visited:
            if not self.marked:
                self.image = pygame.image.load('assets/tile_marked.png').convert_alpha()
                self.marked = True
                BOMB_NUM -= 1
            else:
                self.image = pygame.image.load('assets/tile_normal.png').convert_alpha()
                self.marked = False
                BOMB_NUM += 1
        

    def update(self, mouse_pos=(-999, -999), left_mouse_click=None, right_mouse_click=None):
        global BOMB_NUM
            

        if game_over == False:
            if mouse_pos[0] >= self.rect.left and mouse_pos[0] <= self.rect.right and mouse_pos[1] >= self.rect.top and mouse_pos[1] <= self.rect.bottom:

                if left_mouse_click and not self.marked:
                    perform_lookaround(self, tiles_group.sprites())

                elif right_mouse_click and not self.is_visited:
                    if not self.marked:
                        self.image = pygame.image.load('assets/tile_marked.png').convert_alpha()
                        self.marked = True
                        BOMB_NUM -= 1
                    else:
                        self.image = pygame.image.load('assets/tile_normal.png').convert_alpha()
                        self.marked = False
                        BOMB_NUM += 1

        if self.number > 0:
            num = num_font.render(f'{self.number}', 1, (0, 0, 0))
            screen.blit(num, (self.rect.x + 1, self.rect.y + 1))
            
        

            



# Settings
MENU_BAR_HEIGHT = 40
TILE_SIZE = 20 # The size of each tile
TILE_NUM = 20 # The number of tiles on each row and on each column
SCREEN_WIDTH = TILE_SIZE * TILE_NUM
SCREEN_HEIGHT = SCREEN_WIDTH + MENU_BAR_HEIGHT
BOMB_NUM = 50

game_over = False
win = False

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

num_font = pygame.font.SysFont('Arial', 12)
text_font = pygame.font.SysFont('Arial', 15)
text_font_small = pygame.font.SysFont('Arial', 10)

grid = []
tiles_group = pygame.sprite.Group()

# Rendering grid
tile_id = 0
for row_num in range(TILE_NUM):
    for col_num in range(TILE_NUM):
        x = col_num * TILE_SIZE
        y = row_num * TILE_SIZE
        tiles_group.add(Tile(TILE_SIZE, (x, y + MENU_BAR_HEIGHT), tile_id))
        tile_id += 1


indexes = []
for num in range(BOMB_NUM):
    index = random.randint(0, (TILE_NUM ** 2) - 1)
    while index in indexes:
        index = random.randint(0, (TILE_NUM ** 2) - 1)
    tiles_group.sprites()[index].is_bomb = True
    indexes.append(index)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            tiles_group.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2])

        if game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for index in range(len(tiles_group)):
                        tiles_group.sprites()[index].number = 0
                        tiles_group.sprites()[index].marked = False
                        tiles_group.sprites()[index].is_bomb = False
                        tiles_group.sprites()[index].is_visited = False
                        tiles_group.sprites()[index].image = pygame.image.load('assets/tile_normal.png').convert_alpha()

                    indexes = []
                    for num in range(BOMB_NUM):
                        index = random.randint(0, (TILE_NUM ** 2) - 1)
                        while index in indexes:
                            index = random.randint(0, (TILE_NUM ** 2) - 1)
                        tiles_group.sprites()[index].is_bomb = True
                        indexes.append(index)
                    
                    game_over = False
                    win = False


    screen.fill((0, 0, 0))
    tiles_group.draw(screen)
    tiles_group.update()
    
    screen.blit(text_font.render(f'Mines left: {BOMB_NUM}', 1, (255, 255, 255)), (10, 10))

    tiles_left = (TILE_NUM ** 2) - BOMB_NUM 

    for tile in tiles_group.sprites():
        if not tile.is_bomb:
            if tile.is_visited:
                tiles_left -= 1

    if tiles_left <= 0:
        win = True
        game_over = True

    if game_over:
        if win:
            screen.blit(text_font.render('SUCCESS!', 1, (255, 255, 255)), (SCREEN_WIDTH - 20, 5))
        else:
            screen.blit(text_font.render('FAILED!', 1, (255, 255, 255)), (SCREEN_WIDTH - 115, 5))

        screen.blit(text_font_small.render('Press SPACE to play again', 1, (255, 255, 255)), (SCREEN_WIDTH - 150, 24))

        




    pygame.display.update()