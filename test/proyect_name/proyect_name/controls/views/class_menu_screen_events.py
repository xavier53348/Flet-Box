
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen
from ..app_screen_db import GLOBAL_VAR


def event_4029(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4037(data): # ID: main_screen, event_Elevatedbutton
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Elevatedbutton")
    ...

def event_4109(data): # ID: main_screen, event_Icon
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Icon")
    ...

def event_4113(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4089(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4125(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4124(data): # ID: main_screen, event_Text
    #: WE SET STREAMING VAR DATA TOREAD IN DOCUMENTATION
    GLOBAL_VAR(set_global_var=data)
    got_to_screen(to_screen= 'documentation_screen' ,time_style=0.1) #,style='ring' ,time_style=0.8
    # print(f"Demo App: {data} event_Text")
