###################### CALL GLOBAL VAR #############
from ..settings_var.settings_widget import GLOBAL_VAR
####################################################
import flet as ft
####################################################

class SelectedWidget(ft.UserControl):
    # globalVar='Erase this test'

     def __init__(self,widget_selected ,type_widget, icon_widget):
          super().__init__()
          # self.title='widget_selected'
          self.widget_selected = GLOBAL_VAR(get_global_var=widget_selected)
          self.type_widget     = type_widget
          self.icon_widget     = icon_widget
     def build(self):
          Drop_SelectedWidget = ft.Container( ##################### SELECTED WIDGET
                                        ink           = False,                                           # click effect ripple
                                        bgcolor       = ft.colors.BLACK12,                               # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                        padding       = ft.padding.all(0),    # inside box               # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin        = ft.margin.all(0),     # outside box              # margin.only (left=8, top=8, right=8, bottom=8),
                                        alignment     = ft.alignment.center_left,                        # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                        border_radius = ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        border        = ft.border.all(2, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        width         = 160,
                                        ##################### WIDGETS
                                   content = ft.Row(
                                             # alignment=ft.MainAxisAlignment.START,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                             # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                             controls = [

                                                  ft.Container(
                                                       margin=ft.margin.only (left=8, top=0, right=0, bottom=0),
                                                       # expand=True,
                                                       content=ft.Icon(name=self.icon_widget),
                                                       ),
                                                  ft.Text(
                                                       ##################### PROPERTY
                                                       value           = f"{self.type_widget}:\n", # content = ft.Text(value="Compound button", size=12,),
                                                       text_align      = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                       weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                       font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                       ##################### COLOR
                                                       # width         = 120,
                                                       size=10,
                                                       #####################
                                                       spans=[ft.TextSpan( self.widget_selected, ft.TextStyle( size=20, color=ft.colors.CYAN,weight=ft.FontWeight.BOLD),),],
                                        ),]),
                                        ##################### EVENTS
                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                        )#<=== NOTE Comanche
          return Drop_SelectedWidget
######## SelectedWidget = SelectedWidget(),# <======= Comma