#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .documentation_screen_styles import styles
from .documentation_screen_events import *
from ..app_screen_db import GLOBAL_VAR


#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        # "alignment": {"x":0,"y":0},
        # "height": "566",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":6,"t":6,"r":6,"b":46},
        "bgcolor": "black12",

        # "width": "295",
        "image_src": "Restaurante.png",
        "image_fit": "cover"
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "width": 50,
        "bgcolor": "transparent",
        # "blur": {"sigma_x":20,"sigma_y":20,"tile_mode":"mirror"},
        "border_radius": {"bl":24,"br":24,"tl":24,"tr":24},

    },
    "COLUMN_CONTAINER": {
        # "alignment": "spaceBetween",
        "scroll": "HIDDEN",
        # "spacing": "16.0",
        "horizontal_alignment": "center"
    }
}

class documentation_screen(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.documentation_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):

        self.increase_text = ft.Text(
                                    value = GLOBAL_VAR(get_global_var="value_title"),
                                    **self.dict_style('_4149'),
                                    size = GLOBAL_VAR(get_global_var="text_size"),

                                    # on_click= lambda _: event_4149(data='_4149'),
                            )

        #: MAIN PHONE CONTAINER
        self.content_box = [

		ft.Container(  # Container_Column
			**self.dict_style('_4120'),
			content= ft.Column( # Column
					**self.dict_style('_4121'),
					controls= [


						ft.Container(  # Container_Column
								**self.dict_style('_4136'),
								content= ft.Column( # Column
										**self.dict_style('_4137'),
										controls= [

												ft.Container( # Text
														**self.dict_style('_4140'),
														# on_click= lambda _: event_4141(data='_4141'),
														content= ft.Text(
                                                                value = GLOBAL_VAR(get_global_var="title"),
                                                                **self.dict_style('_4141'),
																# on_click= lambda _: event_4141(data='_4141'),
														),
                                                        ),

												ft.Container(  # Container_Column
														**self.dict_style('_4144'),
														content= ft.Column( # Column
																**self.dict_style('_4145'),
																controls= [

																		ft.Container( # Text
																				**self.dict_style('_4148'),
																				# on_click= lambda _: event_4149(data='_4149'),
																				content= self.increase_text),

												],),), #// LAYER 2 END
						],),), #// LAYER 1 END
		                      ft.Container(  # Container_Row
                                **self.dict_style('_4124'),
                                content= ft.Row( # Row
                                        **self.dict_style('_4125'),
                                        controls= [

                                                ft.Container( # Icon
                                                        **self.dict_style('_4128'),
                                                        on_click= lambda _: event_4129(data='_4129'),
                                                        content= ft.Icon(
                                                                **self.dict_style('_4129'),
                                                                # on_click= lambda _: event_4129(data='_4129'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4132'),
                                                        # on_click= lambda _: event_4133(data='_4133'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4133'),
                                                                value = GLOBAL_VAR(get_global_var="selected_cap"),
                                                                # on_click= lambda _: event_4133(data='_4133'),
                                                        ),),

                                                ft.Container(  # Container_Row
                                                        **self.dict_style('_4152'),
                                                        content= ft.Row( # Row
                                                                **self.dict_style('_4153'),
                                                                controls= [

                                                                        ft.Container( # Icon
                                                                                **self.dict_style('_4156'),
                                                                                on_click= lambda _: event_4157(data=self.increase_text),
                                                                                content= ft.Icon(
                                                                                        **self.dict_style('_4157'),
                                                                                        # on_click= lambda _: event_4157(data='_4157'),
                                                                                ),),

                                                                        ft.Container( # Icon
                                                                                **self.dict_style('_4160'),
                                                                                on_click= lambda _: event_4161(data=self.increase_text),
                                                                                content= ft.Icon(
                                                                                        **self.dict_style('_4161'),
                                                                                        # on_click= lambda _: event_4161(data='_4161'),
                                                                                ),),

                                                ],),), #// LAYER 2 END
                        ],),), #// LAYER 1 END
            ],),),
        ]

        #: MAIN PHONE CONTAINER
        self.content = ft.Container(
                            **self.documentation_screen_style(code='MAIN_EFFECTS_CONTAINER'),
                            content = ft.Column(
                                        **self.documentation_screen_style(code='COLUMN_CONTAINER'),
                                        controls = self.content_box
                                        ),
                                )

    def documentation_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)

