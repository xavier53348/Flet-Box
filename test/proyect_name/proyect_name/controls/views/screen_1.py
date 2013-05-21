#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .screen_1_styles import styles
from .screen_1_events import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "gradient": {"colors":["Blue","Purple","Red","Orange"],"tile_mode":"clamp","begin":{"x":0,"y":1},"end":{"x":0,"y":-1},"type":"linear"},
        "height": "566",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":0,"t":0,"r":0,"b":0},
        "width": "295"
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

class screen_1(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.main_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):

        #: MAIN PHONE CONTAINER
        self.content_box = [ 

		ft.Container(  # Container_GridView
			**self.dict_style('_2969'),
			content= ft.GridView( # GridView
					**self.dict_style('_2970'),
					controls= [

						ft.Container( # Image
								**self.dict_style('_2973'),
								on_click= lambda _: event_2974(data='_2974'),
								content= ft.Image(
										**self.dict_style('_2974'),
										# on_click= lambda _: event_2974(data='_2974'),
								),),

						ft.Container( # Image
								**self.dict_style('_2977'),
								on_click= lambda _: event_2978(data='_2978'),
								content= ft.Image(
										**self.dict_style('_2978'),
										# on_click= lambda _: event_2978(data='_2978'),
								),),

						ft.Container( # Image
								**self.dict_style('_2981'),
								on_click= lambda _: event_2982(data='_2982'),
								content= ft.Image(
										**self.dict_style('_2982'),
										# on_click= lambda _: event_2982(data='_2982'),
								),),

						ft.Container( # Image
								**self.dict_style('_2985'),
								on_click= lambda _: event_2986(data='_2986'),
								content= ft.Image(
										**self.dict_style('_2986'),
										# on_click= lambda _: event_2986(data='_2986'),
								),),

						ft.Container( # Image
								**self.dict_style('_2989'),
								on_click= lambda _: event_2990(data='_2990'),
								content= ft.Image(
										**self.dict_style('_2990'),
										# on_click= lambda _: event_2990(data='_2990'),
								),),

						ft.Container( # Image
								**self.dict_style('_2993'),
								on_click= lambda _: event_2994(data='_2994'),
								content= ft.Image(
										**self.dict_style('_2994'),
										# on_click= lambda _: event_2994(data='_2994'),
								),),

						ft.Container( # Image
								**self.dict_style('_2997'),
								on_click= lambda _: event_2998(data='_2998'),
								content= ft.Image(
										**self.dict_style('_2998'),
										# on_click= lambda _: event_2998(data='_2998'),
								),),

						ft.Container( # Image
								**self.dict_style('_3001'),
								on_click= lambda _: event_3002(data='_3002'),
								content= ft.Image(
										**self.dict_style('_3002'),
										# on_click= lambda _: event_3002(data='_3002'),
								),),

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

