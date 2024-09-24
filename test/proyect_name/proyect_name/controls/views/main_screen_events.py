
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen


def event_4025(data): # ID: main_screen, event_Image
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Image")
    ...

def event_4029(data): # ID: main_screen, event_Image
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Image")
    ...

def event_4033(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4037(data): # ID: main_screen, event_Elevatedbutton
    got_to_screen(to_screen= 'class_menu_screen' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Elevatedbutton")
