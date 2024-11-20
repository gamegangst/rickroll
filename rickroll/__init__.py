import subprocess
import sys
import ctypes

try:
    import pygame
except ImportError:
    print("Устанавливаю pygame...")
    # Передаем команду как список аргументов
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

