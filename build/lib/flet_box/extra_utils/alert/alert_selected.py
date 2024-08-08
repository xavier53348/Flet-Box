import flet as ft

from ..settings_var.settings_widget import GLOBAL_VAR


class AlertSelected(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_AlertSelected=ft.Container(
                               bgcolor       = ft.colors.GREEN_900,
                               padding       = ft.padding.all(8),
                               margin        = ft.margin.all(8),
                               alignment     = ft.alignment.center,
                               border_radius = ft.border_radius.all(30),
                               border      = ft.border.all(2, ft.colors.BLACK),
                               width         = 260,
                               height        = 40,
                               offset        = (0,-7),
                               opacity       = 0.8,
                               visible       = False,
                               content       = ft.Row(
                                            alignment          = ft.MainAxisAlignment.CENTER,
                                            vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                        ft.Icon(name=ft.icons.CHECK_CIRCLE),
                                                        ft.Text(value='SUCCESSFUL'),
                                              ]
                                ),
                            )

        GLOBAL_VAR(set_global_var={'ALERT_WIDGET':Drop_AlertSelected})

        return Drop_AlertSelected
