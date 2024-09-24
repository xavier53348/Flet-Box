#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .main_screen_styles import styles
from .main_screen_events import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "height": "625",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":0,"t":0,"r":0,"b":0},
        "width": "460",
        "image_src": "ServicioBanquetes.png",
        "image_fit": "cover"
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "white24",
        "blur": {"sigma_x":20,"sigma_y":8,"tile_mode":"mirror"},
        "padding": {"l":0,"t":0,"r":0,"b":0}
    },
    "COLUMN_CONTAINER": {
        "alignment": "center",
        "scroll": "HIDDEN",
        "spacing": "2",
        "tight": "false",
        "horizontal_alignment": "center"
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

		ft.Container(  # Container_Row
			**self.dict_style('_4020'),
			content= ft.Row( # Row
					**self.dict_style('_4021'),
					controls= [

						ft.Container( # Image
								**self.dict_style('_4024'),
								# on_click= lambda _: event_4025(data='_4025'),
								content= ft.Image(
										**self.dict_style('_4025'),
										# on_click= lambda _: event_4025(data='_4025'),
								),),

						ft.Container( # Image
								**self.dict_style('_4028'),
								# on_click= lambda _: event_4029(data='_4029'),
								content= ft.Image(
										**self.dict_style('_4029'),
										# on_click= lambda _: event_4029(data='_4029'),
								),),

		],),),
		ft.Container( # Text
			**self.dict_style('_4032'),
			# on_click= lambda _: event_4033(data='_4033'),
			content= ft.Text(
					**self.dict_style('_4033'),
					# on_click= lambda _: event_4033(data='_4033'),
			),),

		ft.Container( # ElevatedButton
			**self.dict_style('_4036'),
			# on_click= lambda _: event_4037(data='_4037'),
			content= ft.ElevatedButton(
					**self.dict_style('_4037'),
					on_click= lambda _: event_4037(data='_4037'),
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

