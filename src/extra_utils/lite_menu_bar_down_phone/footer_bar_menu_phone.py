from .selected_widget import SelectedWidget
from ..settings_var.settings_widget import GLOBAL_VAR

import flet as ft

class LiteMenuDownContainer(ft.Stack):
    def __init__(self,main_page='Erase this test'):
        super().__init__()
        main_page = main_page

    def build(self):
        Selected_Widget_in_dragg_container = SelectedWidget(widget_selected='SHOW_TEXT_SELECTED_DRAGG_WIDGET',type_widget = 'DRAGG BOX',icon_widget='drag_indicator')
        Selected_Widget_in_phone_container = SelectedWidget(widget_selected='SHOW_TEXT_SELECTED_PHONE_WIDGET',type_widget = 'PHONE BOX',icon_widget='phone_iphone')
        GLOBAL_VAR(set_global_var={'SHOW_TEXT_SELECTED_DRAGG_WIDGET':Selected_Widget_in_dragg_container})
        GLOBAL_VAR(set_global_var={'SHOW_TEXT_SELECTED_PHONE_WIDGET':Selected_Widget_in_phone_container})

        Drop_LiteMenuDownContainer = ft.Container(
                                        ink             = False,
                                        bgcolor         = ft.colors.BLACK26,
                                        padding         = ft.padding.all(0),
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
                                                                           width         = 150,
                                                                      content=ft.Row(
                                                                                expand=True,
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                spacing=8,
                                                                           controls=[
                                                                                     ft.Container(
                                                                                               ink           = False,
                                                                                               padding       = ft.padding.all(0),
                                                                                               alignment     = ft.alignment.center,
                                                                                               border_radius = ft.border_radius.all(30),
                                                                                               border        = ft.border.all(2, ft.colors.BLACK12),
                                                                                               height        = 35,
                                                                                           content = ft.Dropdown(
                                                                                                               hint_text       = '   Screen 1',
                                                                                                               width           = 140,
                                                                                                               content_padding = ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                                               alignment       = ft.alignment.center_left,
                                                                                                               border_radius   = ft.border_radius.all(15),
                                                                                                               border          = ft.InputBorder.NONE,
                                                                                                               options         = [
                                                                                                                                  ft.dropdown.Option("   Screen 1"),
                                                                                                                                  ft.dropdown.Option("   Screen 2"),
                                                                                                                                  ft.dropdown.Option("   Screen 3"),
                                                                                                                                  ft.dropdown.Option("   Screen 4"),
                                                                                                                                  ft.dropdown.Option("   Screen 5"),
                                                                                                               ],
                                                                                                   ),
                                                                                     ),
                                                                 ],
                                                                 ),),
                                                            Selected_Widget_in_dragg_container,
                                                            Selected_Widget_in_phone_container,
                                                            ft.Container(
                                                                           ink           = False,
                                                                           bgcolor       = ft.colors.BLACK26,
                                                                           padding       = ft.padding.only(left=4, top=0, right=2, bottom=0),
                                                                           margin        = ft.margin.all(0),    #outside box
                                                                           alignment     = ft.alignment.center,
                                                                           border_radius = ft.border_radius.all(30),
                                                                           border        = ft.border.all(2, ft.colors.BLACK12),
                                                                           width         = 150,
                                                                      content=ft.Row(
                                                                                expand               = True,
                                                                                alignment            = ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                spacing              = 8,
                                                                           controls=[
                                                                                     ft.Container(
                                                                                                 ink           = False,
                                                                                                 width         = 95,
                                                                                                 height        = 30,
                                                                                                 border_radius = ft.border_radius.all(30),
                                                                                                 content = ft.TextField(
                                                                                                                 hint_text ='Name Scr',
                                                                                                                 border    = ft.InputBorder.NONE,
                                                                                                                 bgcolor   = ft.colors.BLACK12,
                                                                                                                 color     = 'White',
                                                                                                                 text_size = 15,
                                                                                                                 ),
                                                                                     ),
                                                                                     ft.IconButton(
                                                                                             icon          = ft.icons.PLUS_ONE,
                                                                                             selected_icon = ft.icons.BATTERY_FULL,
                                                                                             icon_color    = ft.colors.TEAL,
                                                                                             selected      = False,
                                                                                             bgcolor       = ft.colors.BLACK12,
                                                                                     ),],
                                                                 ),),
                                                              ],),
                            )#<=== NOTE COMA
        return Drop_LiteMenuDownContainer

    def action_windows(self,action):

        if action == 'Close':
            self.main_page.window_close()

        elif action == 'Minimize':
            self.main_page.window_minimized = True

        elif action == 'Resize':
            self.main_page.window_maximizable =True
        self.main_page.update()

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