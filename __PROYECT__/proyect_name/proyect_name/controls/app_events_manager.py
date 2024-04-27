
"""
NOTE:       This is a global event that all events will be refer to this event_manager

Eg: global scope

is_gloval = 'hello world'

def event_2933(data):
    global is_local         # set a local scope to global

    is_local = 'hello world'

    print(is_gloval)
    print(is_local)

"""
from builder.app_manager import got_to_screen

def event_2936(data):
    #: got_to_screen(to_screen = 'screen_2' ,style='ring')     #: will set the screen
    #: print('demo',data)
    ...

def event_2935(data):
    #: got_to_screen(to_screen = 'main_screen' ,style='ring')  #: will set the screen
    #: print('say hello',data)
    ...