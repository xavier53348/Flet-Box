from .app_style import styles
from .app_events_manager import *
import flet as ft

def json_style(code):
    return styles.get(code)

#: only edit this seccion
screens = {

'main_screen': ft.Container(
        **json_style('_2921'),
        content = ft.Column(
                **json_style('_2922'),
                controls = [
                        ft.Container(
                                **json_style('_2925'),
                                content = ft.Text(
                                        **json_style('_2926'),
                                        # on_click=lambda _: event_2926(data='_2926'),
                                ),),
                        ft.Container(
                                **json_style('_2929'),
                                content = ft.ElevatedButton(
                                        **json_style('_2930'),
                                        # on_click=lambda _: event_2930(data='_2930'),
                                ),),
        ],),), #: <<< LAYER 0 END BRAKETS
'screen_2': ft.Column( controls = [
############
                ft.Container(
                        **json_style('_2921'),
                        content = ft.Column(
                                **json_style('_2922'),
                                controls = [
                                        ft.Container(
                                                **json_style('_2925'),
                                                content = ft.Text(
                                                        **json_style('_2926'),
                                                ),),
                                        ft.Container(
                                                **json_style('_2929'),
                                                content = ft.TextField(
                                                        **json_style('_2930'),
                                                ),),
                                        ft.Container(
                                                **json_style('_2933'),
                                                content = ft.ElevatedButton(
                                                        **json_style('_2935'),
                                                        on_click=lambda _:event_2935(data='_2935')
                                                ),),
        ],),), #: <<< LAYER 0 END BRAKETS
    ]),
}



