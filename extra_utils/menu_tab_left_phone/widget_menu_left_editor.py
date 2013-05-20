import flet as ft

class MenuLeftContainer(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,main_page='Erase this test'):
        super().__init__()
        # self.title='data'
        self.main_page=main_page

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
                                                                                    expand=True,
                                                                                    ink=False,                                                      # click effect ripple
                                                                                    # bgcolor="#3f449a",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                    padding= ft.padding.all(0),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                    margin = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                    ##################### EFFECTS
                                                                                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                    ##################### WIDGETS
                                                                                    content=ft.Column(
                                                                                        ##################### PROPERTY BOX
                                                                                        # expand=True,
                                                                                        alignment=ft.MainAxisAlignment.CENTER,                      # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                        # scroll=True,                                              # center widget
                                                                                        # tight=True,
                                                                                        ##################### ADAPT TO SCREEN
                                                                                        # wrap=True,                                                # justify in all screen
                                                                                        spacing=8,                                                  # space widget left right
                                                                                        # run_spacing=8,                                            # space widget up down
                                                                                        ##################### WIDGETS
                                                                                        controls=[
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='Find'     ,content=ft.IconButton(icon=ft.icons.FIND_REPLACE_OUTLINED),
                                                                                                        bgcolor=ft.colors.BLACK45,
                                                                                                        height=45,
                                                                                                        width=45,
                                                                                                        border_radius=ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='Code'     ,content=ft.IconButton(icon=ft.icons.CODE_ROUNDED),
                                                                                                        bgcolor=ft.colors.BLACK45,
                                                                                                        height=45,
                                                                                                        width=45,
                                                                                                        border_radius=ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='Tree'     ,content=ft.IconButton(icon=ft.icons.ACCOUNT_TREE_ROUNDED),
                                                                                                        bgcolor=ft.colors.BLACK45,
                                                                                                        height=45,
                                                                                                        width=45,
                                                                                                        border_radius=ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='Git-Hub'  ,content=ft.IconButton(icon=ft.icons.ENGINEERING_SHARP),
                                                                                                        bgcolor=ft.colors.BLACK45,
                                                                                                        height=45,
                                                                                                        width=45,
                                                                                                        border_radius=ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='Drive'    ,content=ft.IconButton(icon=ft.icons.ADD_TO_DRIVE_SHARP),
                                                                                                        bgcolor=ft.colors.BLACK45,
                                                                                                        height=45,
                                                                                                        width=45,
                                                                                                        border_radius=ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='Chat-Gpt' ,content=ft.IconButton(icon=ft.icons.SMART_TOY),
                                                                                                        bgcolor=ft.colors.BLACK45,
                                                                                                        height=45,
                                                                                                        width=45,
                                                                                                        border_radius=ft.border_radius.all(16)
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

    def action_windows(self,action):

        if action == 'Close':
            self.main_page.window_close()

        elif action == 'Minimize':
            self.main_page.window_minimized = True

        elif action == 'Resize':
            self.main_page.window_maximizable =True
        self.main_page.update()
######## MenuLeftContainer = MenuLeftContainer(),# <======= Comma