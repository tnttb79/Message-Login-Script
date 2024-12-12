from plyer.platforms.win.notification import instance as win_notification
from plyer import notification
import pyautogui
import keyboard
import time
import sys


def type_keyboard_periodically():
    notification.backend = win_notification()
    print(
        "Keyboard typer initialized\Message will be prompt every 10s\n-----PRESS AND HOLD ESC TO EXIT------\nHappy break time!!!!"
    )
    notification.notify(
        title="Keyboard Script",
        message="Mouse mover initialized\nMouse will be moved every 10s\n-----PRESS AND HOLD ESC TO EXIT------\nHappy break time!!!!",
        timeout=30,
    )
    message = "Hello Thang"

    while True:
        pyautogui.typewrite(message, interval=0.2)
        pyautogui.press("enter")
        for _ in range(120):
            # Check if the 'Esc' key is pressed
            if keyboard.is_pressed("esc"):
                print("Esc key pressed. Exited script.")
                notification.notify(
                    title="Keyboard Script",
                    message="Esc key pressed. Exited script.",
                    timeout=30,
                )
                sys.exit()
            time.sleep(0.5)


if __name__ == "__main__":
    try:
        type_keyboard_periodically()
    except KeyboardInterrupt:
        print("\nThang has exited the script.")
