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

		ft.Container(  # Container_Column
			**self.dict_style('_3871'),
			content= ft.Column( # Column
					**self.dict_style('_3872'),
					controls= [

				],
		),), #// CLOSE LAYER 0
		ft.Container(  # Container_Column
			**self.dict_style('_3879'),
			content= ft.Column( # Column
					**self.dict_style('_3880'),
					controls= [

						ft.Container(  # Container_Column
								**self.dict_style('_3883'),
								content= ft.Column( # Column
										**self.dict_style('_3884'),
										controls= [

										],
								),), #// CLOSE LAYER 1
		],),),  
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

