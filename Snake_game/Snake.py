"""
author: Sparks_Shen
2025/4/1
"""
class Snake:
    def __init__(self, body, direction, score):
        self.body = body
        self.direction = direction
        self.score = score

    def move(self, food_pos):
        n = len(self.body)
        self.body_end = self.body[n - 1].copy()

        for i in range(n - 1, 0, -1):
            self.body[i] = self.body[i - 1].copy()

        if self.direction == 'left':
            self.body[0][1] -= 1
        elif self.direction == 'right':
            self.body[0][1] += 1
        elif self.direction == 'up':
            self.body[0][0] -= 1
        elif self.direction == 'down':
            self.body[0][0] += 1

        if self.body[0] == food_pos:
            self.body.append(self.body_end)
            self.score += 1
            return True
        return False

    def collision_examine(self, length, width):
        head = self.body[0]
        if head[0] == 0 or head[0] == width - 1 or head[1] == 0 or head[1] == length - 1:
            print("Damn! You run into the wall.")
            return True
        if head in self.body[1:]:
            print("Auch! You bite on yourself.")
            return True
        return False

    def change_direction(self, new_direction):
        if (self.direction == 'left' and new_direction != 'right' or
                self.direction == 'right' and new_direction != 'left' or
                self.direction == 'up' and new_direction != 'down' or
                self.direction == 'down' and new_direction != 'up'):
            self.direction = new_direction
