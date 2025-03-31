from Snake import Snake
from Food import Food
from Matrix import Matrix
import time

import msvcrt
def get_key():
    return msvcrt.getch().decode('utf-8')

def main():
    length = 64
    width = 42
    snake = Snake([[width//2, length//2],[width//2, length//2+1]], 'right', 0)
    food = Food(length, width, snake.body)
    matrix = Matrix(length, width, snake, food)

    last_update_time = time.time()
    target_fps = 200
    target_interval = 1 / target_fps

    time.sleep(2)
    print("#########################################")
    print("####  Welcome to Sparks_Shen's Game  ####")
    print("#########################################")
    time.sleep(3)
    
    while True:
        
        current_time = time.time()
        elapsed_time = current_time - last_update_time
        if elapsed_time >= target_interval:
            print("\033c", end="")

        matrix.output()
        print(f"Score: {snake.score}")

        if snake.collision_examine(length, width):
            print("Game Over!")
            break

        
        if msvcrt.kbhit():
            key = get_key()
            if key == 'a':
                snake.change_direction('left')
            elif key == 'd':
                snake.change_direction('right')
            elif key == 'w':
                snake.change_direction('up')
            elif key == 's':
                snake.change_direction('down')

        matrix.update_matrix()
        speed = snake.score // 2
        time.sleep(0.2 - 0.015*speed)


if __name__ == "__main__":
    main()
    