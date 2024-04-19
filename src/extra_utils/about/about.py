####################################################
import os
import pyperclip
import flet as ft
import time
####################################################
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
####################################################




class FlowlowMe(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_FlowlowMe=ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    ink=False,                                                      # click effect ripple
                    # bgcolor="#3f449a",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(0),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    content=ft.Column(
                        ##################### PROPERTY BOX
                        controls=[
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                      # click effect ripple
                                                # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                content=ft.Text(
                                                            ##################### PROPERTY
                                                            value           = "FOLLOW ME", # content = ft.Text(value="Compound button", size=12,),
                                                            text_align        = ft.TextAlign.CENTER,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                            font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                            size=16,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                ink=False,                                                # click effect ripple
                                                # bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                content=ft.Row(
                                                                ##################### PROPERTY BOX
                                                                # expand=True,
                                                                # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                # vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                # scroll=True,                                              # center widget
                                                                # tight=True,
                                                                ##################### ADAPT TO SCREEN
                                                                # wrap=True,                                                  # justify in all screen
                                                                # spacing=8,                                                # space widget left right
                                                                # run_spacing=8,                                            # space widget up down
                                                                ##################### WIDGETS
                                                                controls=[
                                                                            ft.IconButton(icon=ft.icons.FACEBOOK),
                                                                            ft.IconButton(icon=ft.icons.TELEGRAM),
                                                                            ft.IconButton(icon=ft.icons.EMAIL_ROUNDED),
                                                                         ],),
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA


        return Drop_FlowlowMe
######## FlowlowMe = FlowlowMe(),# <======= Comma

class ABOUT_BOX(ft.Stack):
    # globalVar='Erase this test'
    INFO_ABOUT = {

                'about_me': """Flet-Box is a powerful framework that enables developers to create interactive multi-user web, desktop, and mobile applications. Whether you're a seasoned developer or just starting out, Flet-Box makes frontend development accessible without prior experience. Here are the key features..."""

    }
    def __init__(self,header='header',body='body',footer='footer'):
        super().__init__()
        # self.title='data'
        self.header = header
        self.body   = body
        self.footer = footer

    def build(self):
        Drop_ABOUT_BOX = ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    padding   = ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    content   = ft.Column(
                                    spacing=18,                                                # space widget left right
                                    ##################### WIDGETS
                                    controls=[
                                                                                            ft.Container( ##################### HEADER ABOUT
                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding   = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin    = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment = ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    content = ft.Text(
                                                                    ##################### PROPERTY
                                                                    value       = self.header, # content = ft.Text(value="Compound button", size=12,),
                                                                    text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    weight      = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                    size=18,
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            ft.Container( ##################### HEADER ABOUT
                                                        # bgcolor = "#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding   = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin    = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment = ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                        width     = 400,
                                                    content = ft.Text(
                                                                    ##################### PROPERTY
                                                                    value       = self.INFO_ABOUT.get(self.body), # content = ft.Text(value="Compound button", size=12,),
                                                                    text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    # weight    = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                    color       =ft.colors.WHITE38,
                                                                    size        =12,
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            ft.Container( ##################### HEADER ABOUT
                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding   = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin    = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment = ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    content = ft.Column(
                                                                    spacing=0,

                                                            controls = [

                                                                ft.Text(
                                                                    ##################### PROPERTY
                                                                    value           = self.footer, # content = ft.Text(value="Compound button", size=12,),
                                                                    text_align      = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                                    size=16,
                                                                    # style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE ), # OVERLINE,
                                                                ),
                                                                ft.Container(height=4,width=124,bgcolor=ft.colors.TEAL_800 ),
                                                                ]),
                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

        return Drop_ABOUT_BOX
######## ABOUT_BOX = ABOUT_BOX(),# <======= Comma

class AboutPage(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):

        self.left_column = ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink=False,                                                      # click effect ripple
                    # bgcolor=ft.colors.BLUE,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(4),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # ===================
                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity=0.1,
                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    # ===================
                    # width=150,
                    # height=150,
                    # image_src = f"my_avatar.png",
                    # image_opacity=0.1,
                    # image_fit='FIT_WIDTH',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Column(
                        ##################### PROPERTY BOX
                        # expand=True,
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        horizontal_alignment=ft.CrossAxisAlignment.START,        # vertical       START,CENTER END
                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                        # scroll=True,                                              # center widget
                        # tight=True,
                        ##################### ADAPT TO SCREEN
                        # spacing=8,                                                # space widget left right
                        # run_spacing=8,                                            # space widget up down
                        ##################### WIDGETS
                        controls=[



                                    ft.Container(height=7,width=123,bgcolor=ft.colors.TEAL_800 ),
                                    ft.Container(
                                                ##################### PROPERTY
                                                ink=False,                                                      # click effect ripple
                                                padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(80),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(2, ft.colors.BLACK45),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=150,
                                                height=150,
                                                bgcolor=ft.colors.BLACK45,
                                                # blur=(20,20),
                                                ##################### WIDGETS
                                                content=ft.Image(
                                                            ##################### PROPERTY
                                                            # img most be inside assets /name_imagen.png
                                                            src               = os.path.join('src/assets','my_avatar.png'),
                                                            fit               = ft.ImageFit.COVER,                      # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                            repeat            = ft.ImageRepeat.NO_REPEAT,
                                                            border_radius   = ft.border_radius.all(80),               # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                            # key             = 'is our id',
                                                            opacity=0.6,
                                                            expand          = True,
                                                            # color_blend_mode = ft.BlendMode.COLOR_DODGE,
                                                            # gapless_playback = True,
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container( ##################### HEADER TEXT
                                                ink       = False,                                                      # click effect ripple
                                                # bgcolor = "#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding   = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin    = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment = ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                width     = 350,
                                                content=ft.Text(
                                                            ##################### PROPERTY
                                                            value       = "I'M Javier, a Web Developer", # content = ft.Text(value="Compound button", size=12,),
                                                            text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            weight      = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                            size        = 48,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container( ##################### HEADER TEXT
                                                ink       = False,                                                      # click effect ripple
                                                # bgcolor = "#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding   = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin    = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment = ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                width     = 350,
                                                content=ft.Text(
                                                            ##################### PROPERTY
                                                            value       = "I'M Javier, a Web Developer", # content = ft.Text(value="Compound button", size=12,),
                                                            text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            # weight      = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                            font_family = "RobotoSlab", #"Consolas ,RobotoSlab
                                                            color=ft.colors.WHITE38,
                                                            size        = 16,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                ink       = False,                                                      # click effect ripple
                                                padding   = ft.padding.all(8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin    = ft.margin.all(8),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                content   = ft.ElevatedButton(
                                                                text           = 'GIT - HUB', # content = ft.Text(value="Compound button", size=12,),
                                                                bgcolor        = ft.colors.TEAL_800 ,     # back color
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

        self.right_column = ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink       = False,                                                      # click effect ripple
                    # bgcolor   = ft.colors.BLUE,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding   = ft.padding.all(8),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    # width=150,
                    # height=150,
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Column(
                                ##################### PROPERTY BOX
                                # expand               = True,
                                alignment            = ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                # horizontal_alignment = ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                # scroll               = True,                                              # center widget
                                # tight                = True,
                                ##################### ADAPT TO SCREEN
                                # wrap                   = True,                                                  # justify in all screen
                                # spacing              = 32,                                                # space widget left right
                                # run_spacing          = 8,                                            # space widget up down
                                ##################### WIDGETS
                                controls=[
                                            ABOUT_BOX(
                                                        header = "FLET-BOX",
                                                        body   = 'about_me',
                                                        footer = "LEARN MORE 🮥",
                                                        ),
                                            ABOUT_BOX(
                                                        header = "MY WORK",
                                                        body   = 'about_me',
                                                        footer = "LEARN MORE 🮥",
                                                        ),
                                            FlowlowMe(),
                                         ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

        Drop_AboutPage=ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink           = False,                                                # click effect ripple
                    bgcolor       = ft.colors.BLACK12,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding       = ft.padding.all(32),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    margin        = ft.margin.all(8),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    border        = ft.border.all(1, ft.colors.TEAL_900),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    height        = 650,
                    width=1200,
                    # visible=False,
                    # ===================
                    # image_src = f"/home/mjay/Pictures/3d-2560x1440-cubes-black-red-639.jpg",
                    # image_opacity=0.1,
                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    # ===================
                    blur=(20,20),
                    content=ft.Row(
                                    ##################### PROPERTY BOX
                                    # expand=True,
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                    ##################### LET MAKE SCROLL IN LONG QUANTITY
                                    # scroll=True,                                              # center widget
                                    # tight=True,
                                    ##################### ADAPT TO SCREEN
                                    # wrap=True,                                                  # justify in all screen
                                    # spacing=8,                                                # space widget left right
                                    # run_spacing=8,                                            # space widget up down
                                    ##################### WIDGETS
                                    controls=[
                                                self.left_column,
                                                self.right_column,
                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA
        return Drop_AboutPage
######## AboutPage = AboutPage(),# <======= Comma

######## IconBrowser = IconBrowser(),# <======= Comma

if __name__ == '__main__':
    def main(page: ft.Page):
        ######################
        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        ######################  COLOR
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        ###################### POSITION OF SC
        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 700
        page.window_width              = 800
        page.padding                   = 0
        page.spacing                   = 0
        page.add(AboutPage())
        ######################
    ft.app(
        target=main,
        assets_dir   = "assets"

        )