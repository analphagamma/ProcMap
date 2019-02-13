from random import randint
from time import sleep

class Tile:

    def __init__(self, x, y, weight=0):
        self._x = x
        self._y = y
        self.weight = weight

class Board:

    def __init__(self, x_size, y_size, weight_base, weight_dropoff, weight_threshold):
        self.x_size = x_size
        self.y_size = y_size
        self.weight_base = weight_base
        self.weight_dropoff = weight_dropoff
        self.weight_threshold = weight_threshold
        self.tiles = []

    def add_tiles(self, tile_obj):
        self.tiles.append(tile_obj)

    def adjacent_non_empty_tiles(self, tile):
        adjacent = []
        ti = self.tiles.index(tile)
        adj_i = [ti-1,
                 ti+1,
                 ti+self.x_size,
                 ti-self.x_size,
                 ti+self.x_size-1,
                 ti-self.x_size-1,
                 ti+self.x_size+1,
                 ti-self.x_size+1]
        for pos in adj_i:
            if pos <= 0:
                next
            else:
                adjacent.append({'index': pos,
                                 'weight': self.tiles[pos].weight})
        return adjacent

    def create_empty_board(self):
        for i in range(1, self.x_size+1):
            for j in range(1, self.y_size+1):
               self.add_tiles(Tile(i, j))

    def generate_board(self, iterations):
        # pick random tile whose texture is None
        # check if adjacent tiles are empty
            # if yes, add weight_base to tile
            # if not, weight = highest adjacent weight - weight_dropoff
        while iterations > 0:
            tile_i = randint(0, len(self.tiles)-1)
            if self.tiles[tile_i].weight == 0:
                self.tiles[tile_i].weight = self.weight_base
                iterations -= 1
            else:
                # recursively place weight (current weight-weight_dropoff)
                # until weight=0
                pass

    def draw_board(self):
        # if weight > weight_threshold draw L(and), else draw S(ea)
        for i, tile in enumerate(self.tiles):
            if tile.weight > self.weight_threshold:
                print("O", end=' ')
            else:
                print(".", end=' ')

            if (i+1) % self.x_size == 0:
                print()

class Engine:

    def __init__(self, board):
        self.board = board

    def setup(self):
        self.board.create_empty_board()
        self.board.generate_board()

    def refresh(self, pause):
        sleep(pause)
        self.board.draw_board()

'''Select a point on the map. Place desired tile type with a base value such as 40. Keep track of where you placed your newly desired tile. Add the starting point to a list.

For each point in this list, you visit all neighbours. While you have enough power left (started at 40) add a desired tile and add it to the list to be visited. Give the new tile less power, determined by you. Easiest = random lowering. After you visited the tile from the list, remove it. Start over again by visiting any unvisited but created tiles.'''

if __name__ == '__main__':
    game = Engine(Board(20, 20, 50, 5, 30))
    game.setup()
    game.refresh(0)
