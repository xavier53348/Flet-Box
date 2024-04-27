from builder.app_manager  import builder_app
from controls.app_style   import styles
from controls.app_screens import screens

import flet as ft

def main(page: ft.Page):

    page.scroll               = "HIDDEN"              #: AUTO ADAPTIVE ALWAYS HIDDEN
    page.vertical_alignment   = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #:  COLOR
    page.theme_mode           = ft.ThemeMode.DARK     #: ft.ThemeMode.LIGHT
    # page.bgcolor            = ft.colors.TRANSPARENT
    # page.window_bgcolor     = ft.colors.TRANSPARENT

    #: POSITION OF SCREENS
    page.window_left          = 8
    page.window_top           = 8
    # page.window_center()

    #: SIZE
    page.window_height        = 320
    page.window_width         = 320
    page.padding              = 8
    page.spacing              = 8
    page.expand               = True

    #: SCREEN BUILDER
    tmp_screens = builder_app(styles = styles ,screen= screens ,main_page=page) #: it's necessary to call all screens
    all_screens = tmp_screens.get('show_all_screens')                           #: return one dict with all  screens inside
    show_screen = tmp_screens.get('builder_app')                                #: return exactly first screen

    #: WE SET HOT SCOPE VAR
    page.add(show_screen)
    page.update()

if __name__ == '__main__':

    ft.app(
            target=main,

            )