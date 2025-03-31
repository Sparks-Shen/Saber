class Matrix:
    def __init__(self, length, width, snake, food):
        self.length = length
        self.width = width
        self.snake = snake
        self.food = food

        self.matrix = [['background' for _ in range(self.length)] for _ in range(self.width)]
        for i in range(self.width):
            self.matrix[i][0] = 'wall'
            self.matrix[i][self.length - 1] = 'wall'
        for j in range(self.length):
            self.matrix[0][j] = 'wall'
            self.matrix[self.width - 1][j] = 'wall'

        for block in self.snake.body:
            self.matrix[block[0]][block[1]] = 'snake'
        self.matrix[self.food.pos[0]][self.food.pos[1]] = 'food'


    def update_matrix(self):
        ate_food = self.snake.move(self.food.pos)
        self.matrix[self.snake.body[0][0]][self.snake.body[0][1]] = 'snake'
        if not ate_food:
            self.matrix[self.snake.body_end[0]][self.snake.body_end[1]] = 'background'
        if ate_food:
            self.food.update(self.length, self.width, self.snake.body)
            self.matrix[self.food.pos[0]][self.food.pos[1]] = 'food'


    def output(self):
        for row in self.matrix:
            line = ""
            for cell in row:
                if cell == "background":
                    line += "  "
                elif cell == "snake":
                    line += "\033[042m  \033[0m"
                elif cell == "food":
                    line += "\033[41m  \033[0m"
                else:
                    line += "\033[47m  \033[0m"
            print(line.rstrip())
