import flet as ft



class MenuUpContainer(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,main_page='Erase this test'):
        super().__init__()
        # self.title='data'
        self.main_page=main_page

    def build(self):
        # ft.Container( ###################### MENU UP CONTAINER
        #             ##################### PROPERTY
        #             ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
        #             # expand        = True,
        #             ink             = False,                                                # click effect ripple
        #             bgcolor         = ft.colors.BLACK38,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
        #             padding         = ft.padding.all(00),    # inside box                   # padding.only(left=8, top=8, right=8, bottom=8),
        #             margin          = ft.margin.all(0),      # outside box                  # margin.only (left=8, top=8, right=8, bottom=8),
        #             alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
        #             border_radius   = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
        #             # border        = ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
        #             #               ===================
        #             # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
        #             # image_opacity = 0.1,
        #             # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
        #             #               ===================
        #             # width         = 150,
        #             height          = 40,
        #             # tooltip       = 'Container',
        #             ##################### EFFECTS
        #             # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
        #             # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
        #             ##################### WIDGETS
        #     content=ft.Row(
        #                     ##################### PROPERTY BOX
        #                     # expand             = True,
        #                     # alignment          = ft.MainAxisAlignment.SPACE_AROUND,        # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
        #                     # vertical_alignment = ft.CrossAxisAlignment.CENTER,             # vertical       START,CENTER END
        #                     ##################### LET MAKE SCROLL IN LONG QUANTITY
        #                     # scroll             = True,                                     # center widget
        #                     # tight              = True,
        #                     ##################### ADAPT TO SCREEN
        #                     # wrap               = True,                                     # justify in all screen
        #                     # spacing            = 8,                                        # space widget left right
        #                     # run_spacing        =8,                                         # space widget up down
        #                     ##################### WIDGETS
        #                 controls=[
        #                             MenuUpContainer(),
        #                             # ft.ElevatedButton("press row",tooltip='buttom'),
        #                             # ft.ElevatedButton("press row",tooltip='buttom'),
        #                             # ft.ElevatedButton("press row",tooltip='buttom'),
        #                          ],),
        #     ##################### EVENTS
        #     # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        # ),#<=== NOTE COMA
        Drop_MenuUpContainer = ft.Container(
                                    ##################### PROPERTY
                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                    # expand        = True,
                                    ink             = False,                                                # click effect ripple
                                    bgcolor         = ft.colors.BLACK38,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                    padding         = ft.padding.all(0),    # inside box                   # padding.only(left=8, top=8, right=8, bottom=8),
                                    margin          = ft.margin.all(0),      # outside box                  # margin.only (left=8, top=8, right=8, bottom=8),
                                    alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                    border_radius   = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                    # border        = ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                    #               ===================
                                    # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                    # image_opacity = 0.1,
                                    # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                    #               ===================
                                    # width         = 150,
                                    # height          = 140,
                                    height          = 40,
                                    # tooltip       = 'Container',
                                    ##################### EFFECTS
                                    # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                    # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                    ##################### WIDGETS
                                content = ft.WindowDragArea(
                                                content  = ft.Row(
                                                            expand=True,
                                                            spacing=0,
                                                            controls = [

                                                                ft.Container(
                                                                            padding         =  ft.padding.only(left=16, top=0, right=0, bottom=0),
                                                                            # width         = 140,
                                                                            height          = 32 ,
                                                                            bgcolor         = 'Black',
                                                                            # border_radius = ft.border_radius.all(32),
                                                                            content=ft.Image(
                                                                                            src           = 'logo.jpg',
                                                                                            border_radius = ft.border_radius.all(0),
                                                                                            fit           = ft.ImageFit.CONTAIN,
                                                                                            )
                                                                            ),
                                                                ft.Container(
                                                                            ##################### PROPERTY
                                                                            ink       = False,                                                      # click effect ripple
                                                                            bgcolor   = ft.colors.BLACK26,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                            padding   = ft.padding.only(left=2, top=0, right=16, bottom=0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                            margin    = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                            alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                            border_radius= ft.border_radius.only(top_left=0, top_right=30, bottom_left=0, bottom_right=30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                            # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                            ##################### WIDGETS
                                                                            content=ft.Text(
                                                                                        ##################### PROPERTY
                                                                                        value       = "LET BOX\n", # content = ft.Text(value="Compound button", size=12,),
                                                                                        text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                                        weight      = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                                        # italic    = True,
                                                                                        font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                                        size        = 20,
                                                                                        #####################
                                                                                        spans=[ ft.TextSpan( "Powered by Flet framework",
                                                                                                            ft.TextStyle(
                                                                                                                         # italic = True,
                                                                                                                         size     = 10,
                                                                                                                         color    = ft.colors.TEAL,
                                                                                                                         weight   = ft.FontWeight.BOLD,
                                                                                                                         ),),],
                                                                ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                ft.Container(expand=True),

                                                                ft.Container( ##################### ICONS MAXIMIZE CLOSE MINIMIZE
                                                                        border_radius   = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                        bgcolor=ft.colors.BLACK38,
                                                                        # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),

                                                                        content = ft.Row(
                                                                                    spacing=0,

                                                                                    controls=[

                                                                                        ft.IconButton(
                                                                                                        ft.icons.CIRCLE,
                                                                                                        # icon_size=12,
                                                                                                        icon_color='Yellow',
                                                                                                        # bgcolor='red',
                                                                                                        tooltip="Minimize",
                                                                                                on_click = lambda _: self.action_windows(action = "Minimize"),
                                                                                                        ),
                                                                                        ft.IconButton(
                                                                                                        ft.icons.CIRCLE,
                                                                                                        # icon_size=12,
                                                                                                        icon_color='Green',
                                                                                                        tooltip="Resize",
                                                                                                        # bgcolor='red',
                                                                                                        content=ft.Text(value='X',color='White'),
                                                                                                on_click = lambda _: self.action_windows(action = "Resize"),
                                                                                                        ),
                                                                                        ft.IconButton(
                                                                                                        ft.icons.CIRCLE,
                                                                                                        # icon_size=12,
                                                                                                        icon_color='Red',
                                                                                                        # bgcolor='red',
                                                                                                        tooltip="Close",
                                                                                                on_click = lambda _: self.action_windows(action = "Close"),

                                                                                        ),])
                                                                            ),
                                                                        # here

                                                                        ]

                                                                        ),
                                                            ))
        return Drop_MenuUpContainer

    def action_windows(self,action):

        if action == 'Close':
            self.main_page.window_close()

        elif action == 'Minimize':
            self.main_page.window_minimized = True

        elif action == 'Resize':
            self.main_page.window_maximizable =True
        self.main_page.update()
######## MenuUpContainer = MenuUpContainer(),# <======= Comma