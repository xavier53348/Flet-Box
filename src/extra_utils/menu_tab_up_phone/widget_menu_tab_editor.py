from ..menu_tab_up_phone.basic_menu_tab_up import BasicMenuUp
import flet as ft

class MenuUpContainer(ft.Stack):

     def __init__(self,main_page='Erase this test'):
          super().__init__()

          self.main_page=main_page

     def build(self):

          Basic_MenuUp = BasicMenuUp()

          Drop_MenuUpContainer = ft.Container(
                                   ink             = False,
                                   bgcolor         = ft.colors.BLACK38,
                                   padding         = ft.padding.all(0),
                                   margin          = ft.margin.all(0),
                                   alignment       = ft.alignment.center,
                                   border_radius   = ft.border_radius.all(30),
                                   height          = 40,
                              content = ft.WindowDragArea(
                                             content  = ft.Row(
                                                            expand   = True,
                                                            spacing  = 0,
                                                            controls = [
                                                                 ft.Row(
                                                                      controls=[

                                                                 ft.Container(
                                                                           padding =  ft.padding.only(left=16, top=0, right=0, bottom=0),
                                                                           height  = 32 ,
                                                                           bgcolor = 'Black',
                                                                           content = ft.Image(
                                                                                          src           = 'logo.jpg',
                                                                                          border_radius = ft.border_radius.all(0),
                                                                                          fit           = ft.ImageFit.CONTAIN,
                                                                                          )
                                                                            ),
                                                                 ft.Container(
                                                                           ink           = False,
                                                                           bgcolor       = ft.colors.BLACK26,
                                                                           padding       = ft.padding.only(left=2, top=0, right=16, bottom=0),
                                                                           margin        = ft.margin.all(0),
                                                                           alignment     = ft.alignment.center,
                                                                           border_radius = ft.border_radius.only(top_left=0, top_right=30, bottom_left=0, bottom_right=30),
                                                                           content = ft.Text(
                                                                                          value       = "LET BOX\n",
                                                                                          text_align  = ft.TextAlign.LEFT,
                                                                                          weight      = ft.FontWeight.BOLD,
                                                                                          font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                                          size        = 20,
                                                                                          spans = [ ft.TextSpan( "Powered by Flet Framework",
                                                                                                              ft.TextStyle(

                                                                                                                        size     = 10,
                                                                                                                        color    = ft.colors.TEAL,
                                                                                                                        weight   = ft.FontWeight.BOLD,
                                                                                                                        ),),],
                                                                ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                 ],),

                                                                 ft.Container(
                                                                      width=125,
                                                                 ),#<=== NOTE COMA

                                                                 Basic_MenuUp,
                                                                 ft.Container(
                                                                             expand=True,
                                                                 ),#<=== NOTE COMA

                                                                 ft.Container(
                                                                      border_radius = ft.border_radius.all(30),
                                                                      bgcolor       = ft.colors.BLACK38,
                                                                      gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.BLACK12],),
                                                                      content = ft.Row(
                                                                                     spacing=0,
                                                                                     controls=[
                                                                                          ft.Container(
                                                                                                      tooltip       = 'SAVE PROYECT',
                                                                                                      ink           = True,
                                                                                                      ink_color     = ft.colors.RED,
                                                                                                      bgcolor       = ft.colors.RED_900,
                                                                                                      margin        = ft.margin.only(left=2, top=2, right=8, bottom=2),
                                                                                                      alignment     = ft.alignment.center,
                                                                                                      border_radius = ft.border_radius.all(30),
                                                                                                      border        = ft.border.all(2, ft.colors.BLACK12),
                                                                                                      width         = 60,
                                                                                                      on_click=lambda _:print(_),
                                                                                                      content=ft.Icon(
                                                                                                                      name           = ft.icons.SAVE_AS_ROUNDED,

                                                                                          ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                                                                          ft.IconButton(
                                                                                                        ft.icons.CIRCLE,
                                                                                                        icon_color='Yellow',
                                                                                                        tooltip="Minimize",
                                                                                               on_click = lambda _: self.action_windows(action = "Minimize"),
                                                                                                        ),
                                                                                          ft.IconButton(
                                                                                                        ft.icons.CIRCLE,

                                                                                                        icon_color='Green',
                                                                                                        tooltip="Resize",

                                                                                                        content=ft.Text(value='X',color='White'),
                                                                                               on_click = lambda _: self.action_windows(action = "Resize"),
                                                                                                        ),
                                                                                          ft.IconButton(
                                                                                                        ft.icons.CIRCLE,

                                                                                                        icon_color='Red',

                                                                                                        tooltip="Close",
                                                                                               on_click = lambda _: self.action_windows(action = "Close"),

                                                                                     ),])
                                                                           ),


                                                                      ]

                                                                      ),
                                                            ))
          return Drop_MenuUpContainer

     def yes_click(self,data,alert):
          if data == 'yes':
               self.main_page.window_close()
          elif data == 'close':
               alert.open = False
               self.main_page.update()

     def action_windows(self,action):

          if   action == 'Close':
               confirm_dialog = ft.AlertDialog(
                                        modal   = True,
                                        title   = ft.Text("Please confirm"),
                                        content = ft.Text("Do you really want to exit this app?"),
                                   actions=[
                                              ft.ElevatedButton("Yes",on_click=lambda _:self.yes_click(data='yes',alert=confirm_dialog),bgcolor=ft.colors.RED_900),
                                              ft.OutlinedButton("No", on_click=lambda _:self.yes_click(data='close',alert=confirm_dialog)
                                             ),
                                        ],
                                        actions_alignment="end",
                                        )
               self.main_page.dialog = confirm_dialog
               confirm_dialog.open = True

          elif action == 'Minimize':
               self.main_page.window_minimized   = True

          elif action == 'Resize':
               self.main_page.window_maximizable = True

          self.main_page.update()

#######
