import time
import random
import pyautogui
import math
from pynput import mouse

top_left_x = 737
top_left_y = 255

box_width = 32
box_height = 32

#change based on difficulty
game_width = 9
game_height = 9 
pyautogui.PAUSE = 0
def randomClicking():
    start_time = time.time()
    while time.time() - start_time < 5:
        win_pixel = pyautogui.pixel(880, 197)
        loss_pixel = pyautogui.pixel(872, 211)

        if(win_pixel == (0,0,0)):
             return True
        if (loss_pixel ==(0,0,0)):
             return False
        
        random_x = random.randint(top_left_x, top_left_x+ box_width * game_width)
        random_y = random.randint(top_left_y, top_left_y+ box_height * game_height)

        click_x = random_x + box_width//2
        click_y = random_y+box_height//2

        pyautogui.click(click_x, click_y)

        


gameCounter = 0; 
while True:
    yipee = randomClicking()
    if yipee:
        print("You won on game ", gameCounter)  
    if not yipee:
        print("Not yipee ): Game: ", gameCounter)
        gameCounter+=1
        pyautogui.click(880, 197)


# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')