
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen
from ..app_screen_db import GLOBAL_VAR


def event_4129(data): # ID: main_screen, event_Icon
    got_to_screen(to_screen= 'class_menu_screen' ,time_style=0.1 ) # ,style='ring'
    # print(f"Demo App: {data} event_Icon")

def event_4133(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4157(data): # ID: main_screen, event_Icon
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Icon")
    data.size += 1
    data.update()

    GLOBAL_VAR(set_global_var={'text_size':data.size})

def event_4161(data): # ID: main_screen, event_Icon
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Icon")
    data.size -= 1
    data.update()
    GLOBAL_VAR(set_global_var={'text_size':data.size})

def event_4141(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4149(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...