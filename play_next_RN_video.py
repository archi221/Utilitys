import pyautogui
from time import sleep
from pynput import keyboard

from signal import signal, SIGINT, SIGTERM, SIG_DFL

signal(SIGINT, SIG_DFL)
signal(SIGTERM, SIG_DFL)


"""
    Für den lapto
"""
position_speed_options = (1413, 870)
position_speed_faster = (1413, 650)

"""
    Für ESE Raum
"""
#position_speed_options = (-506, 1359)
#position_speed_faster = (-595, 1188)

PAUSE_TIME = 0.1

TAG_WIDTH = 20

def print_status(tag, message):
    print(f"[{tag.ljust(TAG_WIDTH)}] {message}")

def main():
    
    print_status("main", "starting super loop")
    while True:
        scan_for_enter()
        close_tab()
        sleep(PAUSE_TIME)
        config_video()

def config_video():
    print_status("config_video", "setting up speed and skipping start")
    pyautogui.press('k')
    sleep(PAUSE_TIME)
    pyautogui.moveTo(position_speed_options)
    pyautogui.click()
    sleep(PAUSE_TIME)
    pyautogui.moveTo(position_speed_faster)
    pyautogui.click()
    sleep(PAUSE_TIME)
    pyautogui.press('m')
    sleep(PAUSE_TIME)
    pyautogui.press('L')
    sleep(PAUSE_TIME)
    pyautogui.press('f')
    


def close_tab():
   print_status("close_tab", "Drücke Escape und (ctrl w)!")
   pyautogui.press('esc')
   pyautogui.hotkey('ctrl', 'w')

def scan_for_enter():
    """
    Blockiert das Programm, bis die Enter-Taste systemweit gedrückt wird.
    """
    print_status("scan_for_enter", "Warte auf Enter (systemweit)...")
    
    # Der Listener wird hier mit 'with' gestartet und 'join' lässt ihn blockieren
    with keyboard.Listener(on_press=lambda key: key != keyboard.Key.enter) as listener:
        listener.join()
    
    print_status("scan_for_enter", "Enter erkannt")



if __name__ == "__main__":
    main()