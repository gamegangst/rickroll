import pygame
import ctypes
import time
import os


import webbrowser
import random
def play_music(midi_filename):
    '''Stream music_file in a blocking manner'''
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play(-1)

freq = 44100  # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

pygame.mixer.music.set_volume(1.0)


midi_filename = 'data/rickroll.mid'

# ^^^ Basically this sucks and I've borrowed it because I don't want to spend 999999 hours trying to start the midi file



def popup():
    '''Starting popup that shows whenever you're starting programm'''
    title = "РИК (РИК ЭСТЛИ) ЭСТЛИ" # Revolver (Revolver Ocelot) Ocelot
    mymessage =  "Добро пожаловать в музей Рика Эстли!\nЗдесь вы можете быть ЗАРИКРОЛЛЕНЫ\nИли зарикроллить ваших друзей!!"
    ctypes.windll.user32.MessageBoxW(0, mymessage, title, 1)



def prikol():
    """Rickrolls you whenever you're asking for help and typing 'help'"""
    import webbrowser

    webbrowser.open_new(url='https://www.youtube.com/watch?v=xvFZjo5PgG0')
    time.sleep(9) # wait till  video ends

    pygame.mixer.music.load('data/trollolol.swf.mp3')
    pygame.mixer.music.play()
    title = "ТРОЛОЛО" # trololo
    mymessage = "ЧЕЛ ТЫ БЫЛ ЗАРИКРОЛЛЕН ХАХАХАХАХАХАХАХАХАХАХАХАХАХ"
    ctypes.windll.user32.MessageBoxW(0, mymessage, title, 0)


def roulette():
    import pygame
    import random
    import webbrowser
    '''Has a ton of imported sound effects. 1/6 chance of listening to Never Gonna Give You Up instead of Together Forever'''

    pygame.mixer.music.load('data/punk.mp3')
    pygame.mixer.music.play()

    time.sleep(10) # Wait till line ends
    title = "РИК-РУЛЕТКА"
    mymessage = "Well, do ya, punk?"
    ctypes.windll.user32.MessageBoxW(0, mymessage, title, 3) # Doesn't matter which one you choose, like in Bethesda's games HAHAHAHAHAHAHa


    pygame.mixer.music.load('data/spin.mp3')
    pygame.mixer.music.play()
    time.sleep(1)

    bang = random.randint(1, 6) # Time to decide

    pygame.mixer.init()
    pygame.mixer.music.load('data/heartbeat.mp3') # SHOOT SHOOT SHOOT
    pygame.mixer.music.play()

    time.sleep(6)
    if bang == 1:
        pygame.mixer.music.load('data/bang.ogg') # you've been shot
        pygame.mixer.music.play()
        time.sleep(2)
        webbrowser.open_new(url='https://youtu.be/dQw4w9WgXcQ?si=YezphDNelMTuxoS3')
        time.sleep(2)
        title = "Земля Риком Эстли.!"
        mymessage = "Хоронить будут в закрытом гробу."
        ctypes.windll.user32.MessageBoxW(0, mymessage, title, 0)
    else:
        pygame.mixer.music.load('data/lucky.ogg') # lucky you!
        pygame.mixer.music.play()
        time.sleep(2)
        webbrowser.open_new(url='https://youtu.be/yPYZpwSpKmA?si=O9bZ2vY88899NRmo')
        time.sleep(2)
        title = "Повезло!"
        mymessage = "Пожалуйста, подумай о маме, не играй больше в русскую рулетку.............."
        ctypes.windll.user32.MessageBoxW(0, mymessage, title, 0)

def historicmoment():
    '''returns one of two HISTORIC articles about rickrolling.'''
    news = random.randint(1, 2)
    if news == 1:
        webbrowser.open_new(url='https://daily.afisha.ru/infoporn/15991-pevec-rik-estli-iz-rozygrysha-s-rikrollom-sam-popalsya-na-rikroll/') # rick astley var
    else:
        webbrowser.open_new(url='https://youtu.be/tfXc740DJtk?si=NwbYax0f6JvPDFbY') # youtube var



