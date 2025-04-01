import os
import time
import random
import getkey
from getkey import keys, getkey
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text


version = str("0-0-5")
columns = 39
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
    
    
def wrapText(text, wrap="║║", total_width=39):
    if len(wrap) != 2:
        raise ValueError("reqs failed, wrapper isn't two characters long.")
    
    plain_text = Text.from_markup(text).plain
    text_length = len(plain_text)
    
    padding_width = total_width - len(wrap) - text_length - 8
    if padding_width < 0:
        raise ValueError(f"Text is too long. Should be less than {total_width}.")
    
    padded_text = f"{text}{' ' * padding_width}"
    
    return f"{wrap[0]} {padded_text} {wrap[1]}"




def mainMenu():
    clear()
    

    
    
    
if __name__ == "__main__":
    clear()
    titlehr(wrapText("[red]RMAD[/] CS [dim]by Pale Raven Systems[/]"))
    print(wrapText("      └────── Version: v" + version))
    print(wrapText("this is a test."))
    print(wrapText("this is a test. do not worry."))
