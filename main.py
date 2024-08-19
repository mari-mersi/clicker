""" Программа, запускающая цикл нажатий ЛКМ при нажатии клавиши 'u'.
 остановка - 'd', завершить программу - 'esc'.u """

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, Key, KeyCode, Controller as KeyboardController
import threading
import time

# Инициализация контроллеров для мыши и клавиатуры
mouse = MouseController()
keyboard = KeyboardController()

# Флаг для управления циклом кликов
clicking = False

def click_mouse():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.01)  # Задержка между кликами, можно изменить при необходимости
        else:
            time.sleep(0.1)  # Задержка для снижения нагрузки на процессор

def on_press(key):
    global clicking

    if key == KeyCode.from_char('u'):  # "u" для запуска
        clicking = True
    elif key == KeyCode.from_char('d'):  # "d" для остановки
        clicking = False

def on_release(key):
    if key == Key.esc:
        # Останавливаем программу при нажатии Esc
        return False

# Запуск потока для кликов мыши
click_thread = threading.Thread(target=click_mouse)
click_thread.daemon = True
click_thread.start()

# Запуск слушателя клавиатуры
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
