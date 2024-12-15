skeleton_data: dict = {

"class_flet_box": """#: MAIN WIDGET SCREEN CLASS

import flet as ft

from .SYTLE_RENAME_styles import styles
from .EVENT_RENAME_events import *

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

""",

"event_manager": '''
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen''',

"event_skeleton": """

def eventRENAME(data): # event_NAME_ID
    # EASY WAY GO TROUGHT DIFERENT SCREENS NO LAG BETWEEN THEM
    # rotation: set changes if rotate, gridview col 2 if rotate gridview col 3
    # got_to_screen(to_screen='screen_name' , rotation=False  )
    print(f"Demo App: {data} event_NAME_ID")
    ...""",
}


def get_skeleton(name: str = ""):
    """
    Gets the skeleton.

    :param      name:  The name
    :type       name:  str

    :returns:   The skeleton.
    :rtype:     { return_type_description }
    """
    return skeleton_data.get(name)
