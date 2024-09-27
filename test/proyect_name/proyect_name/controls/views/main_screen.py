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
        "image_src": "test/proyect_name/proyect_name/assets/_77203d18-186d-40fa-acc7-982298584979.jpeg",
        "image_opacity": "0.61",
        "image_fit": "cover"
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "blur": {"sigma_x":16,"sigma_y":16,"tile_mode":"mirror"},
        "padding": {"l":16,"t":0,"r":16,"b":0}
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

		ft.Container( # Text
			**self.dict_style('_3991'),
			# on_click= lambda _: event_3992(data='_3992'),
			content= ft.Text(
					**self.dict_style('_3992'),
					# on_click= lambda _: event_3992(data='_3992'),
			),),

		ft.Container(  # Container_Column
			**self.dict_style('_3999'),
			content= ft.Column( # Column
					**self.dict_style('_4000'),
					controls= [

						ft.Container( # Text
								**self.dict_style('_4015'),
								# on_click= lambda _: event_4016(data='_4016'),
								content= ft.Text(
										**self.dict_style('_4016'),
										# on_click= lambda _: event_4016(data='_4016'),
								),),

		],),),
		ft.Container( # Text
			**self.dict_style('_4003'),
			# on_click= lambda _: event_4004(data='_4004'),
			content= ft.Text(
					**self.dict_style('_4004'),
					# on_click= lambda _: event_4004(data='_4004'),
			),),

		ft.Container(  # Container_Row
			**self.dict_style('_4007'),
			content= ft.Row( # Row
					**self.dict_style('_4008'),
					controls= [

				],
		),), #// CLOSE LAYER 0
		ft.Container(  # Container_Row
			**self.dict_style('_4027'),
			on_click= lambda _: event_4027(data='_4027'),
			content= ft.Row( # Row
					**self.dict_style('_4028'),
					controls= [

						ft.Container( # Icon
								**self.dict_style('_4031'),
								on_click= lambda _: event_4032(data='_4032'),
								content= ft.Icon(
										**self.dict_style('_4032'),
										# on_click= lambda _: event_4032(data='_4032'),
								),),

						ft.Container( # Text
								**self.dict_style('_4035'),
								# on_click= lambda _: event_4036(data='_4036'),
								content= ft.Text(
										**self.dict_style('_4036'),
										# on_click= lambda _: event_4036(data='_4036'),
								),),

		],),),
		ft.Container(  # Container_Row
			**self.dict_style('_4043'),
			content= ft.Row( # Row
					**self.dict_style('_4044'),
					controls= [

				],
		),), #// CLOSE LAYER 0
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

