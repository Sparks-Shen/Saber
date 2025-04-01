"""
author: Sparks_Shen
2025/4/1
"""
from Snake import Snake
from Food import Food
from Matrix import Matrix
import time

import msvcrt


def get_key():
    return msvcrt.getch().decode('utf-8')


def main():
    time.sleep(2)
    print("#########################################")
    print("####  Welcome to Sparks_Shen's Game  ####")
    print("#########################################")
    while True:
        time.sleep(2)
        print("\n")
        print("INTRODUCTION:\n"
        "\033[31m Please maximize the window and change the input method to English.\n"
        "\033[32m 'w''a''s''d' are the four keys to control directions. \033[0m")
        time.sleep(2)

        flag = False
        while not flag:
            print("\n")
            print("PRESS 'enter' TO START GAME")
            key = get_key()
            if ord(key) == 13:
                flag = True
        print("\n")
        print("SNAKE")

        length = 64
        width = 42
        snake = Snake([[width // 2, length // 2], [width // 2, length // 2 + 1]], 'right', 0)
        food = Food(length, width, snake.body)
        matrix = Matrix(length, width, snake, food)

        last_update_time = time.time()
        target_fps = 200
        target_interval = 1 / target_fps

        while True:
            current_time = time.time()
            elapsed_time = current_time - last_update_time
            if elapsed_time >= target_interval:
                print("\033[F" * (width + 1), end="")
                # print("\033c", end="")

            matrix.output()
            print(f"Score: {snake.score}")

            if snake.collision_examine(length, width):
                print("Game Over!")
                break

            if msvcrt.kbhit():
                key = get_key()
                if key.lower() == 'a':
                    snake.change_direction('left')
                elif key.lower() == 'd':
                    snake.change_direction('right')
                elif key.lower() == 'w':
                    snake.change_direction('up')
                elif key.lower() == 's':
                    snake.change_direction('down')

            matrix.update_matrix()
            speed = snake.score // 2
            time.sleep(0.2 - 0.015 * speed)

        while True:
            print("\n")
            print("Press 'y' TO PLAY AGAIN, 'n' TO EXIT.")
            key = get_key()
            if key.lower() == 'y':
                break
            elif key.lower() == 'n':
                return
            else:
                continue


if __name__ == "__main__":
    main()
     
