# main file
from Pieces import *

pg.init()

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Chess")

board = [[None for x in range(8)] for y in range(8)]
for piece in pieces:
    board[piece.pos[0]][piece.pos[1]] = piece

selected = None
selected_piece = None

clock = pg.time.Clock()
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            pg.quit()
            quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            mouse_x //= 60
            mouse_y //= 60
            if not selected:
                selected = (mouse_x, mouse_y) if board[mouse_y][mouse_x] else None
                selected_piece = board[mouse_y][mouse_x]
                print(selected_piece)
            else:
                if (mouse_y, mouse_x) in selected_piece.get_moves(board):
                    board[selected_piece.pos[0]][selected_piece.pos[1]].pos = (mouse_y, mouse_x)
                    selected = None

    screen.fill(cream)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (-1)**(i + j) < 0:
                screen.fill(brown, (60*i, 60*j, 60, 60))

    for row in board:
        for tile in row:
            if tile:
                screen.blit(tile.image, (tile.pos[1]*60, tile.pos[0]*60))

    if selected:
        pg.draw.rect(screen, yellow, (selected[0]*60, selected[1]*60, 60, 60), 3)

    pg.display.update()
    clock.tick(30)
