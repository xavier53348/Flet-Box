#: MAIN WIDGET SCREEN CLASS
import flet as ft

from ..views.main_screen_style import styles
from ..app_events_manager import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "gradient": {"colors":["BLue","Purple","Red","Orange"],"tile_mode":"clamp","begin":{"x":0,"y":1},"end":{"x":0,"y":-1},"type":"linear"},
        "image_src": "logo.jpg",
        "image_opacity": "0.4"
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "blur": {"sigma_x":20,"sigma_y":20,"tile_mode":"mirror"},
        "padding": {"l":0,"t":0,"r":0,"b":0}
    },
    "COLUMN_CONTAINER": {
        "scroll": "HIDDEN",
        "spacing": "2"
    }
}

class CustomPage(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.main_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):

        #: MAIN PHONE CONTAINER
        self.content_box = [ 

		ft.Container(  # Container_Column
			**self.dict_style('_2942'),
			content= ft.Column( # Column
					**self.dict_style('_2943'),
					controls= [

						ft.Container( # Text
								**self.dict_style('_2946'),
								# on_click= lambda _: event_2947(data='_2947'),
								content= ft.Text(
										**self.dict_style('_2947'),
										# on_click= lambda _: event_2947(data='_2947'),
								),),

						ft.Container( # TextField
								**self.dict_style('_2950'),
								# on_click= lambda _: event_2951(data='_2951'),
								content= ft.TextField(
										**self.dict_style('_2951'),
										# on_click= lambda _: event_2951(data='_2951'),
								),),

						ft.Container( # TextField
								**self.dict_style('_2954'),
								# on_click= lambda _: event_2955(data='_2955'),
								content= ft.TextField(
										**self.dict_style('_2955'),
										# on_click= lambda _: event_2955(data='_2955'),
								),),

						ft.Container( # Text
								**self.dict_style('_2958'),
								# on_click= lambda _: event_2959(data='_2959'),
								content= ft.Text(
										**self.dict_style('_2959'),
										# on_click= lambda _: event_2959(data='_2959'),
								),),

						ft.Container(  # Container_Row
								**self.dict_style('_2962'),
								content= ft.Row( # Row
										**self.dict_style('_2963'),
										controls= [

												ft.Container( # ElevatedButton
														**self.dict_style('_2966'),
														# on_click= lambda _: event_2967(data='_2967'),
														content= ft.ElevatedButton(
																**self.dict_style('_2967'),
																on_click= lambda _: event_2967(data='_2967'),
														),),

												ft.Container( # TextButton
														**self.dict_style('_2970'),
														# on_click= lambda _: event_2971(data='_2971'),
														content= ft.TextButton(
																**self.dict_style('_2971'),
																on_click= lambda _: event_2971(data='_2971'),
														),),

								],),), #// LAYER 1 END
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

