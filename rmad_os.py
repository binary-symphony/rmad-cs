import os
import time
import random
import rich
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
import pytz
from datetime import datetime
import digitalio
import board

from adafruit_rgb_display.rgb import color565
from adafruit_rgb_display import st7789

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()




version = str("alpha3b")
columns = 45
titlecolumns = columns
selected_item = 0
global total_width
total_width = columns



def wait(sec):
    time.sleep(sec)
    
    
def wait(sec):
    time.sleep(sec)


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def hr():
    print(columns * "═")
  
  
def titlehr(title):
    titlecolumns = columns - len(title)
    print(title + titlecolumns * "═")
    
    
def wrapText(text, wrap="║║", total_width=columns):
    if len(wrap) != 2:
        raise ValueError("reqs failed, wrapper isn't two characters long.")
    
    plain_text = Text.from_markup(text).plain
    text_length = len(plain_text)
    
    padding_width = total_width - len(wrap) - text_length - 2
    if padding_width < 0:
        raise ValueError(f"Text is too long. Should be less than {total_width}.")
    
    padded_text = f"{text}{' ' * padding_width}"
    
    return f"{wrap[0]} {padded_text} {wrap[1]}"




def mainMenu():
    selected_item = 0
    items = ["Watch Mode", "Config", "Exit"]
    item_desc = ["< [dim]Open Watch Mode[/] >",
                 "< [dim]Access settings.[/] >",
                 "< [dim]Exit the OS.[/] >"]
    titlehr(wrapText("[red]RMAD[/] CS [dim]by Pale Raven Systems[/]"))
    print(wrapText("      └─── Version: v " + version))
    while True:
        if buttonB.value and not buttonA.value:
            wait(.25)
            selected_item = (selected_item + 1) % len(items)
            clear()
            titlehr(wrapText("[red]RMAD[/] CS [dim]by Pale Raven Systems[/]"))
            print(wrapText("      └─── Version: v " + version))
            print(wrapText(items[selected_item]))
            print(wrapText(item_desc[selected_item]))
        if buttonA.value and not buttonB.value:
            wait(.1)
            if selected_item == 0:
                watchMode()
                break
            elif selected_item == 1:
                configureDevices()
                break
            elif selected_item == 2:
                exit(0)
            

def watchMode():
    clear()
    while True:
        titlehr(wrapText("[red]RMAD[/] CS [dim]by Pale Raven Systems[/]"))
        print(wrapText("      └─── Watch Mode"))
        print(wrapText("[dim]Press any key to exit.[/]"))
        # Get the current time in EST for Georgia, US
        est = pytz.timezone('US/Eastern')
        current_time = datetime.now(est).strftime("%H:%M:%S")
        print(wrapText(f"Current Time (EST): {current_time}"))
        wait(1)
        clear()
        if buttonA.value is False:
            break
    mainMenu()
    
if __name__ == "__main__":
    clear()
    mainMenu()
