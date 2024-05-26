from .selected_widget import SelectedWidget
from ..settings_var.settings_widget import GLOBAL_VAR

import flet as ft

class LiteMenuDownContainer(ft.Stack):
    def __init__(self,main_page='Erase this test'):
        super().__init__()
        main_page = main_page

        #: SHOW SCREEN MANAGER
        self.show_screen_manager = GLOBAL_VAR(get_global_var='SCREEN_CONTAINER')

    def build(self):
        Selected_Widget_in_dragg_container = SelectedWidget(widget_selected='SHOW_TEXT_SELECTED_DRAGG_WIDGET',type_widget = 'DRAGG BOX',icon_widget='drag_indicator')
        Selected_Widget_in_phone_container = SelectedWidget(widget_selected='SHOW_TEXT_SELECTED_PHONE_WIDGET',type_widget = 'PHONE BOX',icon_widget='phone_iphone')
        GLOBAL_VAR(set_global_var={'SHOW_TEXT_SELECTED_DRAGG_WIDGET':Selected_Widget_in_dragg_container})
        GLOBAL_VAR(set_global_var={'SHOW_TEXT_SELECTED_PHONE_WIDGET':Selected_Widget_in_phone_container})

        self.change_text_screen = ft.Text(value="main_screen")
        GLOBAL_VAR(set_global_var={'change_text_screen':self.change_text_screen})

        Drop_LiteMenuDownContainer = ft.Container(
                                        ink             = False,
                                        bgcolor         = ft.colors.BLACK26,
                                        padding         = ft.padding.all(4),
                                        margin          = ft.margin.all(0),    #outside box
                                        alignment       = ft.alignment.center,
                                        border_radius   = ft.border_radius.all(30),
                                   content=ft.Row(
                                                  alignment          = ft.MainAxisAlignment.SPACE_BETWEEN,
                                                  vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                            ft.Container(
                                                                           ink           = False,
                                                                           bgcolor       = ft.colors.BLACK12,
                                                                           padding       = ft.padding.only(left=4, top=0, right=2, bottom=0),
                                                                           margin        = ft.margin.all(0),    #outside box
                                                                           alignment     = ft.alignment.center,
                                                                           border_radius = ft.border_radius.all(30),
                                                                           border        = ft.border.all(2, ft.colors.BLACK12),
                                                                           # width         = 150,
                                                                      content=ft.Row(
                                                                                expand=True,
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                spacing=8,
                                                                           controls=[
                                                                                     ft.Container(
                                                                                               ink           = True,
                                                                                               ink_color     = ft.colors.RED_900,
                                                                                               padding       = ft.padding.all(0),
                                                                                               alignment     = ft.alignment.center,
                                                                                               border_radius = ft.border_radius.all(30),
                                                                                               border        = ft.border.all(2, ft.colors.TEAL_900),
                                                                                               height        = 38,
                                                                                               width         = 130,
                                                                                               bgcolor       = ft.colors.WHITE10,
                                                                                               on_click      = lambda _: self.action_buttons(action='show'),
                                                                                           content = self.change_text_screen,
                                                                                     ),
                                                                                    ft.Container(
                                                                                        padding = ft.padding.only(left=4, top=0, right=2, bottom=0),
                                                                                        content = ft.IconButton(
                                                                                                     icon            = ft.icons.ADD_CIRCLE,
                                                                                                     selected_icon   = ft.icons.BATTERY_FULL,
                                                                                                     highlight_color = 'Red',
                                                                                                     icon_color      = ft.colors.TEAL_900,
                                                                                                     selected        = False,
                                                                                                     # bgcolor         = ft.colors.TEAL,
                                                                                                     on_click        = lambda _: self.action_buttons(action='show'),
                                                                                                 ),
                                                                                        ),
                                                                                    ],
                                                                 ),),
                                                            Selected_Widget_in_dragg_container,
                                                            Selected_Widget_in_phone_container,
                                                              ],),
                            )#<=== NOTE COMA
        return Drop_LiteMenuDownContainer

    def action_buttons(self,action):
        if action == 'show':
            self.show_screen_manager.visible = True
            self.show_screen_manager.update()

if __name__ == '__main__':

    def main(page: ft.Page):
         page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
         page.vertical_alignment        = ft.MainAxisAlignment.CENTER
         page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
         page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
         page.window_bgcolor            = ft.colors.RED_100
         page.window_left               = 20
         page.window_top                = 20
         page.window_height           = 120
         page.window_width            = 600
         page.padding                   = 0
         page.spacing                   = 0
         page.expand                    = True
         Lite_MenudDownContainer = LiteMenuDownContainer()
         page.add(Lite_MenudDownContainer)
         page.update()
    ft.app(
            target         = main,
            )