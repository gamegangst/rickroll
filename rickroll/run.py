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
# type in commands and get functions, nuff said






