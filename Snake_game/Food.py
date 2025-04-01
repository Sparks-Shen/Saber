"""
author: Sparks_Shen
2025/3/31
"""
import random

class Food:
    def __init__(self, length, width, body):
        while(True):
            x = random.randint(1, width-2)
            y = random.randint(1, length-2)
            food_pos = [x, y]
            if food_pos not in body:
                self.pos = food_pos
                break

    def update(self, length, width, body):
        while(True):
            x = random.randint(1, width-2)
            y = random.randint(1, length-2)
            food_pos = [x, y]
            if food_pos not in body:
                self.pos = food_pos
                break  
                
