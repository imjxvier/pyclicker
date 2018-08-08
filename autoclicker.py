import keyboard
import pyautogui

on, off = False, True

print('\nWelcome to pyclicker!')

while True:
    try:
        cps = int(input(
            '\nHow many CPS you wanna get? 1 = 10, 2 = 20, 3 = 30, (...): '))
    except ValueError:
        print('Invalid input. Your input needs to be a number.')
    except KeyboardInterrupt:
        print('\nGoodbye!')
        break
    else:
        break

print('\npyclicker\nF1: ON\nF: Start clicking\nF2: OFF\nCTRL+C: Quit')

try:
    while True:
        if keyboard.is_pressed('F1'):
            on, off = True, False
        if keyboard.is_pressed('F2'):
            on, off = False, True
        if keyboard.is_pressed('F') and on:
            pyautogui.click(button='left', clicks=cps)
        if keyboard.is_pressed('ctrl+c'):
            print('Goodbye!')
            break
except KeyboardInterrupt:
    print('\nGoodbye!')
