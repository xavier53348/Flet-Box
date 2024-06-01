from ..app_style_manager import styles
from ..app_events_manager import *

import flet as ft


class Screen2(ft.Container):
    def __init__(self):
        super().__init__()

        dict_keys: dict = self.dict_style('_4444')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):
        self.content = ft.Container(
                                **self.dict_style('_2921'),
                                content = ft.Column(
                                            **self.dict_style('_2922'),
                                            controls = [
                                                        ft.ElevatedButton(
                                                        **self.dict_style('_2934'),
                                                        on_click=lambda _: event_4444(data='_4444'),
                                                            ),
                                    ],),) # <<< LAYER 0 END BRAKETS


    def dict_style(self,code):
        return styles.get(code)