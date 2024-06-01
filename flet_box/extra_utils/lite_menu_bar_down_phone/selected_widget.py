from ..settings_var.settings_widget import GLOBAL_VAR
import flet as ft

class SelectedWidget(ft.Stack):
     """ONLY FUNCTION IS SHOW SELECTED WIDGET IN PHONE"""

     def __init__(self,widget_selected ,type_widget, icon_widget):
          super().__init__()

          self.widget_selected = GLOBAL_VAR(get_global_var=widget_selected)
          self.type_widget     = type_widget
          self.icon_widget     = icon_widget

     def build(self):

          Drop_SelectedWidget = ft.Container(
                                        ink           = False,
                                        bgcolor       = ft.colors.BLACK12,
                                        padding       = ft.padding.all(0),
                                        margin        = ft.margin.all(0),
                                        alignment     = ft.alignment.center_left,
                                        border_radius = ft.border_radius.all(30),
                                        border        = ft.border.all(2, ft.colors.BLACK38),
                                        width         = 208,
                                   content = ft.Row(
                                             controls = [
                                                  ft.Container(
                                                       margin=ft.margin.only (left=8, top=0, right=0, bottom=0),
                                                       content=ft.Icon(name=self.icon_widget),
                                                       ),
                                                  ft.Text(
                                                       value           = f"{self.type_widget}:\n",
                                                       text_align      = ft.TextAlign.LEFT,
                                                       weight          = ft.FontWeight.BOLD,
                                                       font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                       size=10,
                                                       spans=[ft.TextSpan( self.widget_selected, ft.TextStyle( size=20, color=ft.colors.CYAN,weight=ft.FontWeight.BOLD),),],
                                        ),]),
                                        )#<=== NOTE Comanche
          return Drop_SelectedWidget