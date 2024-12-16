# from ..settings_var.settings_widget import GLOBAL_VAR
import flet as ft


class SelectedWidget(ft.Container):
    """ONLY FUNCTION IS SHOW SELECTED WIDGET IN PHONE"""

    def __init__(self, widget_selected, type_widget: str="None", icon_widget: str='Home'):
        super().__init__()

        # Drop_SelectedWidget = ft.Container(
        self.alignment=ft.alignment.center_left
        self.bgcolor=ft.Colors.with_opacity(0.02, 'white'),
        # self.border=ft.border.all(2, ft.Colors.with_opacity(0.02, 'red'))
        self.border_radius=ft.border_radius.all(30)
        self.icon_widget = icon_widget
        self.ink=False
        self.margin=ft.margin.all(0)
        self.padding=ft.padding.all(0)
        self.type_widget = type_widget

        self.widget_selected = type_widget
        self.width=160

        # self.expand = True
    def build(self):
        self.content=ft.Row(

                controls=[
                    ft.Container(
                        margin=ft.margin.only(left=8, top=0, right=0, bottom=0),
                        content=ft.Icon(name=self.icon_widget),

                    ),
                    ft.Container(
                        # width=140,
                        # expand = True,
                        content=    ft.Text(
                                value=f"{self.type_widget}:\n",
                                text_align=ft.TextAlign.LEFT,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",  # "Consolas ,RobotoSlab
                                size=8,
                                spans=[
                                    ft.TextSpan(
                                        self.widget_selected,
                                        ft.TextStyle(
                                            size=17,
                                            color=ft.colors('cyan'),
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                ],
                            ),
                        )
                ]
            )
            # ),
        # return Drop_SelectedWidget
