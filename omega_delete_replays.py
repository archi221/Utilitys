import pyautogui
from time import sleep
import argparse
import keyboard
import threading

from signal import signal, SIGINT, SIGTERM, SIG_DFL

signal(SIGINT, SIG_DFL)
signal(SIGTERM, SIG_DFL)

position_delete = (400, 55)
position_replay = (250, 250)

def main():
    parser = argparse.ArgumentParser(
                    prog='Omeaga Delete Replays',
                    description='deltes the specified amount of replays in ygo omega',
                    epilog='HI')
    
    parser.add_argument('-c', '--count', default=20) 
    args = parser.parse_args()
    try:
        replays = int(args.count)
    except Exception:
        print("Error in parsing count argument")

    stop_event = threading.Event()
    keyboard.on_press_key("esc", lambda _: stop_event.set())

    for i in range(replays):
        if stop_event.is_set():
            break
        print(f"deleting Replay: {i}", end='\r', flush=True)
        pyautogui.moveTo(position_replay)
        pyautogui.click()
        pyautogui.moveTo(position_delete)
        pyautogui.click()
    if stop_event.is_set():
        print(f"Canceled after Deleting {replays} replays")
    else: 
        print(f"Deletet {replays} replays                ")

if __name__ == "__main__":
    main()