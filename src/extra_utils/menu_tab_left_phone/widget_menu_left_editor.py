###################### CALL GLOBAL VAR #############
from ..settings_var.settings_widget import GLOBAL_VAR
####################################################
import flet as ft
####################################################

class MenuLeftContainer(ft.UserControl):
    # globalVar='Erase this test'

     def __init__(self,main_page='Erase this test'):
          super().__init__()
          # self.title='data'
          self.main_page     = main_page
          self.icon_browser  = GLOBAL_VAR(get_global_var='ICON_BROWSER_CONTAINER')
          self.color_browser = GLOBAL_VAR(get_global_var='COLOR_BROWSER_CONTAINER')
          self.gpt_browser   = GLOBAL_VAR(get_global_var='GPT_BROWSER_CONTAINER')

     def build(self):


          Drop_MenuLeftContainer =  ft.Container( ###################### MENU LEFT CONTAINER
                                             ##################### PROPERTY
                                             ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                             expand          = True,
                                             ink             = False,                                                # click effect ripple
                                             bgcolor         = ft.colors.BLACK38,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                             padding         = ft.padding.only(left=0, top=8, right=0, bottom=8),    # inside box              # padding.only(left=8, top=8, right=8, bottom=8),
                                             margin          = ft.margin.all(0),     # outside box                   # margin.only (left=8, top=8, right=8, bottom=8),
                                             alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                             # border_radius   = ft.border_radius.all(30),                           # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                             # border        = ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                             #               ===================
                                             # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                             # image_opacity = 0.1,
                                             # image_fit     ='COVER',                                               # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                             #               ===================
                                             width           = 60,
                                             # height          = 700,
                                             # tooltip       = 'Container',
                                             ##################### EFFECTS
                                             gradient        = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12,ft.colors.CYAN, ft.colors.BLACK12],),
                                             # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                    ##################### WIDGETS
                                        content=ft.Column(
                                                            ##################### PROPERTY BOX
                                                            # expand             = True,
                                                            # alignment          = ft.MainAxisAlignment.SPACE_AROUND,       # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,            # vertical       START,CENTER END
                                                            #####################  LET MAKE SCROLL IN LONG QUANTITY
                                                            # scroll             = True,                                    # center widget
                                                            # tight              = True,
                                                            #####################  ADAPT TO SCREEN
                                                            # wrap               = True,                                    # justify in all screen
                                                            # spacing            = 8,                                       # space widget left right
                                                            # run_spacing        = 8,                                       # space widget up down
                                                            ##################### WIDGETS
                                                            controls =[
                                                                        ft.IconButton(icon=ft.icons.SUPERVISED_USER_CIRCLE),

                                                                        ft.Container(
                                                                                    ##################### PROPERTY COLUMN
                                                                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                    expand    = True,
                                                                                    ink       = False,                                                      # click effect ripple
                                                                                    # bgcolor = "#3f449a",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                    padding   = ft.padding.all(0),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                    margin    = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                    alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                    ##################### EFFECTS
                                                                                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                    ##################### WIDGETS
                                                                                    content=ft.Column(
                                                                                        ##################### PROPERTY BOX
                                                                                        # expand             = True,
                                                                                        alignment            = ft.MainAxisAlignment.CENTER,                      # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                        # scroll             = True,                                              # center widget
                                                                                        # tight              = True,
                                                                                        ##################### ADAPT TO SCREEN
                                                                                        # wrap               = True,                                                # justify in all screen
                                                                                        spacing              = 8,                                                  # space widget left right
                                                                                        # run_spacing        = 8,                                            # space widget up down
                                                                                        ##################### WIDGETS
                                                                                        controls=[
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='ICONS',content=ft.IconButton(icon=ft.icons.DELIVERY_DINING_ROUNDED , on_click=lambda _:self.show_widgets(show_widget='icon_browser')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='COLORS',content=ft.IconButton(icon=ft.icons.IMAGESEARCH_ROLLER_ROUNDED , on_click=lambda _:self.show_widgets(show_widget='color_browser')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='CODE'     ,content=ft.IconButton(icon=ft.icons.CODE_ROUNDED , on_click=lambda _:self.on_developing('Code')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='TREE'     ,content=ft.IconButton(icon=ft.icons.ACCOUNT_TREE_ROUNDED , on_click=lambda _:self.on_developing('Tree')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='GIT-HUB'  ,content=ft.IconButton(icon=ft.icons.ENGINEERING_SHARP , on_click=lambda _:self.on_developing('Git-Hub')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='CHAT-GPT' ,content=ft.IconButton(icon=ft.icons.SMART_TOY ,  on_click=lambda _:self.show_widgets(show_widget='gpt_browser')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                 ],
                                                                                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                                    ##################### EVENTS
                                                                                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                        ),#<=== NOTE COMA


                                                                        ft.IconButton(icon=ft.icons.SETTINGS),
                                                                     ],),
                                            ##################### EVENTS
                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                        )#<=== NOTE COMA
          return Drop_MenuLeftContainer

     def show_widgets(self,show_widget):

          if show_widget == "icon_browser":
               self.icon_browser.visible  = True if not self.icon_browser.visible else False
               self.icon_browser.update()

          if show_widget == "color_browser":
               self.color_browser.visible  = True if not self.color_browser.visible else False
               self.color_browser.update()

          if show_widget == "gpt_browser":
               self.gpt_browser.visible  = True if not self.gpt_browser.visible else False
               self.gpt_browser.update()

     def on_developing(self,name_seccion):
          page        = GLOBAL_VAR(get_global_var='PAGE')

          self.data = f"""
          Hello, User!

          {name_seccion.upper()}: is not aviable yet, please keep calm will be soon...
          thanks very much
          """
          dlg = ft.AlertDialog(
                              title=ft.Text(self.data,size=15), on_dismiss=lambda e: print("Dialog dismissed!")
                              )
          page.dialog = dlg
          dlg.open = True
          page.update()

     def action_windows(self,action):

          if action == 'Close':
            self.main_page.window_close()

          elif action == 'Minimize':
            self.main_page.window_minimized = True

          elif action == 'Resize':
            self.main_page.window_maximizable =True
          self.main_page.update()
######## MenuLeftContainer = MenuLeftContainer(),# <======= Comma