from ..settings_var.settings_widget import GLOBAL_VAR

import flet as ft

class BasicMenuUp(ft.Stack):

    def __init__(self):
        super().__init__()

        self.about_page  = GLOBAL_VAR(get_global_var='ABOUT_CONTAINER')

    def build(self):
        Drop_BasicMenuUp = ft.Container(
                    ink           = False,
                    bgcolor       = ft.colors.BLACK26,
                    padding       = ft.padding.all(0),
                    margin        = ft.margin.all(0),    #outside box
                    alignment     = ft.alignment.center,
                    border_radius = ft.border_radius.all(30),
                    border        = ft.border.all(2, ft.colors.BLACK12),
                    height        = 40,

            content=ft.Row(
                            vertical_alignment = ft.CrossAxisAlignment.CENTER,
                            tight              = True,
                            spacing            = 1,
                            controls=[
                                        ft.Container(
                                                    ink           = False,
                                                    padding       = ft.padding.all(0),
                                                    margin        = ft.margin.all(0),
                                                    alignment     = ft.alignment.center,
                                                    border_radius = ft.border_radius.only(top_left=30, top_right=0, bottom_left=30, bottom_right=0),
                                                    border        = ft.border.all(2, ft.colors.BLACK12),
                                                    gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    content=ft.TextButton(
                                                            text='File',
                                                            icon='rule_folder_rounded',
                                                ),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                        ft.Container(
                                                    ink             = False,
                                                    padding         = ft.padding.all(0),
                                                    margin          = ft.margin.all(0),
                                                    alignment       = ft.alignment.center,
                                                    border          = ft.border.all(2, ft.colors.BLACK12),
                                                    gradient        = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    content=ft.TextButton(
                                                            text='Themes',
                                                            icon='compare',
                                                ),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                        ft.Container(
                                                    ink             = False,
                                                    padding         = ft.padding.all(0),
                                                    margin          = ft.margin.all(0),
                                                    alignment       = ft.alignment.center,
                                                    border          = ft.border.all(2, ft.colors.BLACK12),
                                                    gradient        = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    content=ft.TextButton(
                                                            text = 'Sponsor',
                                                            icon = 'data_thresholding',
                                                ),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                        ft.Container(
                                                    ink             = False,
                                                    padding         = ft.padding.all(0),
                                                    margin          = ft.margin.all(0),
                                                    alignment       = ft.alignment.center,
                                                    border          = ft.border.all(2, ft.colors.BLACK12),
                                                    gradient        = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    content=ft.TextButton(
                                                            text='Help',
                                                            icon='data_saver_on_outlined',
                                                ),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                        ft.Container(
                                                    ink           = False,
                                                    padding       = ft.padding.all(0),
                                                    margin        = ft.margin.all(0),
                                                    alignment     = ft.alignment.center,
                                                    border_radius = ft.border_radius.only(top_left=0, top_right=30, bottom_left=0, bottom_right=30),
                                                    border        = ft.border.all(2, ft.colors.BLACK12),
                                                    gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    content=ft.TextButton(
                                                                            text = 'About',
                                                                            icon = 'person_search',
                                                                        on_click  = lambda _:self.show_widgets(show_widget='about_page'),
                                                                        ),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                    ],),
        )#<=== NOTE COMA

        return Drop_BasicMenuUp

    def show_widgets(self,show_widget):
        """SHOW PAGES"""
        if show_widget == "about_page":
            self.about_page.visible  = True if not self.about_page.visible else False
            self.about_page.update()

if __name__ == '__main__':

    BasicMenuUp = BasicMenuUp()

    def main(page: ft.Page):
        page.scroll="HIDDEN"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        page.window_left = 8
        page.window_top = 8
        page.window_height=120
        page.window_width=530
        page.padding=8
        page.spacing=8
        page.expand=True
        screen_1=BasicMenuUp
        page.add(screen_1)
        page.update()

    ft.app(
            target       = main,
            port         = 8080,
            view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            web_renderer = ft.WebRenderer.HTML

            )