skeleton_data: dict = {

'class_flet_box':'''#: MAIN WIDGET SCREEN CLASS
import flet as ft

from ..views.SYTLE_RENAME import styles
from ..app_events_manager import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = CHANGE_STYLE

class CustomPage(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.main_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):

        #: MAIN PHONE CONTAINER
        self.content_box = [ CHANGE_ATTRIBUTES
        ]

        #: MAIN PHONE CONTAINER
        self.content = ft.Container(
                            **self.main_screen_style(code='MAIN_EFFECTS_CONTAINER'),
                            content = ft.Column(
                                        **self.main_screen_style(code='COLUMN_CONTAINER'),
                                        controls = self.content_box
                                        ),
                                )

    def main_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)

''',

'event_manager':'''
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen''',

'event_skeleton':"""
def eventRENAME(data): # event_NAME_ID
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_NAME_ID")
    ...""",

}

def get_skeleton(name: str=""):
    """
        GET SKELETON OF THE CLASS WIDGET TO EACH SCREEN
    """
    return skeleton_data.get(name)