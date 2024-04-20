####################################################
import os
import pyperclip
import flet as ft
import time
####################################################
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
################################# CALL GLOBAL VAR ####
from ..settings_var.settings_widget import GLOBAL_VAR
######################################################

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
                    ink       = False,                                  # click effect ripple
                    padding   = ft.padding.all(0),    # inside box      # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(0),     # outside box     # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment = ft.alignment.center,                    # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget

                content   = ft.Column(

                        ##################### PROPERTY BOX
                        controls=[
                                    ft.Container(
                                                ##################### PROPERTY
                                                ink       = False,                            # click effect ripple
                                                padding   = ft.padding.all(0), # inside box   # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin    = ft.margin.all(0),  # outside box  # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment = ft.alignment.center,              # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                content=ft.Text(
                                                            ##################### PROPERTY
                                                            value       = "FOLLOW ME",                         # content = ft.Text(value="Compound button", size=12,),
                                                            text_align  = ft.TextAlign.CENTER,                 # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            weight      = ft.FontWeight.BOLD,                  # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                            font_family = "Consolas",                          # "Consolas ,RobotoSlab
                                                            size        = 16,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container(
                                                ##################### PROPERTY
                                                ink       = False,                                          # click effect ripple
                                                padding   = ft.padding.all(0),    # inside box              # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin    = ft.margin.all(0),     # outside box             # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                content=ft.Row(
                                                                controls=[
                                                                            ft.IconButton(icon=ft.icons.FACEBOOK        ,tooltip='FACEBOOK',                url='https://facebook.com/groups/315046001621078/?mibextid=rS40aB7S9Ucbxw6v',),
                                                                            ft.IconButton(icon=ft.icons.DISCORD         ,tooltip='@legend_53348#0000',      ),
                                                                            ft.IconButton(icon=ft.icons.CHAT            ,tooltip='WHATSAPP GROUP',          url='https://chat.whatsapp.com/ELFB8fSbdMS2chOjXiYAMo'),
                                                                            ft.IconButton(icon=ft.icons.EMAIL_ROUNDED   ,tooltip='xavier53348@gmail.com',   url='mailto:xavier53348@gmail.com'),
                                                                            ft.IconButton(icon=ft.icons.PHONE           ,tooltip='(+53) 54448442',          ),
                                                                            ft.IconButton(icon=ft.icons.VIDEO_COLLECTION,tooltip='YOUTUBE',                 url='https://www.youtube.com/@flet-box'),
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

                'about_me': """With Flet-Box GUI, you can seamlessly build apps that run smoothly on various platforms, from desktop to mobile. Say goodbye to platform-specific limitations and hello to a unified development experience. Plus, with Python3 as the language of choice, you'll enjoy the simplicity and versatility that comes with one of the most popular programming languages in the world.""",
              'invitation': """So, are you ready to join us on this exciting adventure? Whether you're a developer looking to build your next big project or simply curious about the world of cross-platform app development, Flet-Box GUI welcomes you with open arms. Let's embark on this journey together and unlock the full potential of Flet framework.\nFeel free to reach out for inquiries or collaboration opportunities.""",

    }
    def __init__(self,header='header',body='body',footer='footer',ref_url='reference'):
        super().__init__()
        # self.title='data'
        self.header = header
        self.body   = body
        self.footer = footer
        self.reference = ref_url

    def build(self):
        Drop_ABOUT_BOX = ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    padding   = ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(0),     # outside box               # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment = ft.alignment.center,                              # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    content   = ft.Column(
                                    spacing=18,                                   # space widget left right
                                    ##################### WIDGETS
                                    controls=[
                                                                                            ft.Container( ##################### HEADER ABOUT
                                                        # bgcolor="#44CCCC00",                          # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding   = ft.padding.all(0), # inside box     # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin    = ft.margin.all(0),  # outside box    # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment = ft.alignment.center_left,           # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    content = ft.Text(
                                                                    ##################### PROPERTY
                                                                    value       = self.header,          # content = ft.Text(value="Compound button", size=12,),
                                                                    text_align  = ft.TextAlign.LEFT,    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    weight      = ft.FontWeight.BOLD,   # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    font_family = "Consolas",           #"Consolas ,RobotoSlab
                                                                    size=18,
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            ft.Container( ##################### HEADER ABOUT
                                                        # bgcolor = "#44CCCC00",                                          # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding   = ft.padding.all(0), # inside box                       # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin    = ft.margin.all(0),  # outside box                      # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment = ft.alignment.center_left,                             # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                        width     = 400,
                                                    content = ft.Text(
                                                                    ##################### PROPERTY
                                                                    value       = self.INFO_ABOUT.get(self.body),         # content = ft.Text(value="Compound button", size=12,),
                                                                    text_align  = ft.TextAlign.LEFT,                      # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    # weight    = ft.FontWeight.BOLD,                     # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    font_family = "Consolas",                             # "Consolas ,RobotoSlab
                                                                    color       =ft.colors.WHITE38,
                                                                    size        =12,
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            ft.Container( ##################### HEADER ABOUT
                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding   = ft.padding.all(0), # inside box                       # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin    = ft.margin.all(0),  # outside box                      # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment = ft.alignment.center_left,                             # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    content = ft.Column(
                                                                    spacing=0,

                                                            controls = [

                                                                ft.TextButton(
                                                                    ##################### PROPERTY
                                                                    text       = self.footer,                           # content = ft.Text(value="Compound button", size=12,),
                                                                    # text_align  = ft.TextAlign.LEFT,                     # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    # weight      = ft.FontWeight.BOLD,                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    # font_family = "Consolas",                            #"Consolas ,RobotoSlab
                                                                    # size        = 16,
                                                                    # style     = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE ), # OVERLINE,
                                                                    url         = self.reference,
                                                                ),
                                                                ft.Container(height=4,width=124,bgcolor=ft.colors.TEAL_800 ),
                                                                ]),
                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:print(_), # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

        return Drop_ABOUT_BOX
######## ABOUT_BOX = ABOUT_BOX(),# <======= Comma

class AboutPage(ft.Stack):
    # globalVar='Erase this test'

    data_dev = {
        'profile':"""Experienced software developer with a passion for creating intuitive graphical user interfaces (GUIs) across multiple platforms. Dedicated to delivering high-quality, user-centric applications tailored to meet specific client needs.
        """
    }
    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):

        self.left_column = ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    ink       = False,                                                      # click effect ripple
                    padding   = ft.padding.all(4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(4),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    ##################### WIDGETS
                    content=ft.Column(
                        ##################### PROPERTY BOX
                        # expand             =True,
                        alignment            =ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        horizontal_alignment =ft.CrossAxisAlignment.START,        # vertical       START,CENTER END
                        ##################### WIDGETS
                        controls=[



                                    ft.Container(height=7,width=123,bgcolor=ft.colors.TEAL_800 ),
                                    ft.Container(
                                                ##################### PROPERTY
                                                ink           = False,                                                      # click effect ripple
                                                padding       = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin        = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(80),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border        = ft.border.all(2, ft.colors.BLACK45),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width         = 150,
                                                height        = 150,
                                                bgcolor       = ft.colors.BLACK45,
                                                # blur=(20,20),
                                                ##################### WIDGETS
                                                content=ft.Image(
                                                            ##################### PROPERTY
                                                            src                = os.path.join('src/assets','my_avatar.png'),
                                                            fit                = ft.ImageFit.COVER,                      # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                            repeat             = ft.ImageRepeat.NO_REPEAT,
                                                            border_radius      = ft.border_radius.all(80),               # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                            opacity            = 0.6,
                                                            expand             = True,
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
                                                            value       = "Hi There!!", # content = ft.Text(value="Compound button", size=12,),
                                                            text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            weight      = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                            size        = 24,
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
                                                            value       = "DEV:      Maenys Javier Quesada Reyes\nFrom:    CUBA", # content = ft.Text(value="Compound button", size=12,),
                                                            text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            weight      = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                            size        = 18,
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
                                                            value       = self.data_dev.get('profile'), # content = ft.Text(value="Compound button", size=12,),
                                                            text_align  = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            font_family = "RobotoSlab", #"Consolas ,RobotoSlab
                                                            color       = ft.colors.WHITE38,
                                                            size        = 12,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                ink       = False,                                                      # click effect ripple
                                                padding   = ft.padding.all(8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin    = ft.margin.all(8),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                content   = ft.ElevatedButton(
                                                                            text      = 'GIT-HUB', # content = ft.Text(value="Compound button", size=12,),
                                                                            bgcolor   = ft.colors.TEAL_800 ,     # back color
                                                                            url       = 'https://github.com/xavier53348/Flet-Box',
                                                                            elevation = 16,
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
                                                        header  = "FLET-BOX",
                                                        body    = 'about_me',
                                                        footer  = "LEARN MORE 🮥",
                                                        ref_url = 'https://github.com/xavier53348/Flet-Box/blob/main/docs/Roadmap.md',
                                                        ),
                                            ABOUT_BOX(
                                                        header  = "WORK TOGETHER",
                                                        body    = 'invitation',
                                                        footer  = "LEARN MORE 🮥",
                                                        ref_url = 'https://github.com/xavier53348/Flet-Box/blob/main/WIDGET.md',
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
                    blur=(20,20),
                    #################### EVENT
                on_click  = lambda _:self.show_widgets(show_widget='about_page'),
                #####################
                content=ft.Row(
                                    ##################### PROPERTY BOX
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                    ##################### WIDGETS
                                    controls=[
                                                self.left_column,
                                                self.right_column,
                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA
        return Drop_AboutPage


    def show_widgets(self,show_widget):
        """SHOW PAGES"""
        if show_widget == "about_page":
            self.about_page  = GLOBAL_VAR(get_global_var='ABOUT_CONTAINER')
            self.about_page.visible  = True if not self.about_page.visible else False
            self.about_page.update()

######## AboutPage = AboutPage(),# <======= Comma
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