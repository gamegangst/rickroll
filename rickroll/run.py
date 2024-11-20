import subprocess
import sys
import webbrowser
import time

# module import


try:
    import pygame
except ImportError:
    print("Устанавливаю pygame...")
    # Передаем команду как список аргументов
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
# courtesy of chatgpt, because I only need one custom module and for some reason I spent a lot of time trying to understand how to automatically install it through pip

from funcs import *
play_music('data/rickroll.mid')
# plays midi version of never gonna give you up

while True:
    user_input = input("Введите команду!!!!!:")
    if user_input == "help":
        pygame.mixer_music.stop()
        prikol()

    if user_input == "roulette":
        roulette()

    if user_input == "history":
        historicmoment()

    if user_input == "what":
        webbrowser.open(url="https://ru.wikipedia.org/wiki/Рикроллинг")

    else:
        title = "КОПИРАЙТ ИНКРИНЖМЕНТ"
        mymessage = "Бро, ты выдал кринж, нет такой команды!!!!"
        ctypes.windll.user32.MessageBoxW(0, mymessage, title, 0)
# type in commands and get functions, nuff said






