#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .main_screen_styles import styles
from .main_screen_events import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "height": "566",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":0,"t":0,"r":0,"b":0},
        "width": "295"
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "padding": {"l":0,"t":0,"r":0,"b":0}
    },
    "COLUMN_CONTAINER": {
        "scroll": "HIDDEN",
        "spacing": "2"
    }
}

class main_screen(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.main_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):

        #: MAIN PHONE CONTAINER
        self.content_box = [ 

		ft.Container( # Image
			**self.dict_style('_2943'),
			on_click= lambda _: event_2944(data='_2944'),
			content= ft.Image(
					**self.dict_style('_2944'),
					# on_click= lambda _: event_2944(data='_2944'),
			),),

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

