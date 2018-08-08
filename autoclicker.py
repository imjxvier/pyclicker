import keyboard, pyautogui

on, off = 0, 1

print('Welcome to pyclicker!')

while True:
    try:
        cps = int(input('Tell me how many CPS you wanna get. 1 = 10, 2 = 20, 3 = 30, 4 = 40 and like that: '))
    except ValueError:
        print('Invalid input. Your input needs to be a number.\n')
    except KeyboardInterrupt:
        print('\n')
    else:
        print('Thanks!\n')
        break

print('pyclicker\nF1 = ON\nF2 = OFF\nF = Start clicking (When ON)\nCTRL+C = Quit')

try:
    while True:
        if keyboard.is_pressed('F1'):
            on, off = 1, 0
        if keyboard.is_pressed('F2'):
            on, off = 0, 1
        if keyboard.is_pressed('F') and on == 1:
            pyautogui.click(button='left', clicks=cps)
        if keyboard.is_pressed('ctrl+c'):
            print('Goodbye!')
            break
except KeyboardInterrupt:
    print('Goodbye!')
