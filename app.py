#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
movement = 0

previous_position = [0, 0]

try:
    while True:
        x, y = pyautogui.position()
        if (previous_position != [x, y]):
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            x_traveled = abs(previous_position[0] - x)
            y_traveled = abs(previous_position[1] - y)
            movement = (movement + x_traveled + y_traveled)
            previous_position = [x, y]
            print(movement)
except KeyboardInterrupt:
    print('\n')