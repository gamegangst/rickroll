


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






