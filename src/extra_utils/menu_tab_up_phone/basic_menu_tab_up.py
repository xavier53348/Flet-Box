####################################################
import flet as ft
####################################################

class BasicMenuUp(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_BasicMenuUp=ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink=False,                                                # click effect ripple
                    bgcolor=ft.colors.BLACK26,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,TEAL,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    border=ft.border.all(2, ft.colors.BLACK12),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # ===================
                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity=0.1,
                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    # ===================
                    # width=150,
                    height=40,
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.TEAL],),
                    ##################### WIDGETS
                content=ft.Row(
                                ##################### PROPERTY BOX
                                # expand=True,
                                # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                # scroll=True,                                              # center widget
                                tight=True,
                                ##################### ADAPT TO SCREEN
                                # wrap=True,                                                  # justify in all screen
                                spacing=1,                                                # space widget left right
                                # run_spacing=8,                                            # space widget up down
                                ##################### WIDGETS
                            controls=[
                                        ft.Container( #####################
                                                    #####################  PROPERTY
                                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                    # expand=True,
                                                    ink=False,                                                      # click effect ripple
                                                    # bgcolor=ft.colors.TEAL_900,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,TEAL,CYAN,GREY,PINK,TEAL
                                                    padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                    margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    border_radius= ft.border_radius.only(top_left=30, top_right=0, bottom_left=30, bottom_right=0),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border=ft.border.all(2, ft.colors.BLACK12),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    # width=80,
                                                    gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    ##################### WIDGETS
                                                    content=ft.TextButton(
                                                            text='File',
                                                            icon='rule_folder_rounded',

                                                            # bgcolor=ft.colors.BLACK54,
                                                ),
                                                    ##################### EVENTS
                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                        ft.Container( #####################
                                                    #####################  PROPERTY
                                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                    # expand=True,
                                                    ink=False,                                                      # click effect ripple
                                                    # bgcolor=ft.colors.TEAL_900,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,TEAL,CYAN,GREY,PINK,TEAL
                                                    padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                    margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    # border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border=ft.border.all(2, ft.colors.BLACK12),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    # width=80,
                                                    gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    ##################### WIDGETS
                                                    content=ft.TextButton(
                                                            text='Themes',
                                                            icon='compare',

                                                            # bgcolor=ft.colors.BLACK54,
                                                ),
                                                    ##################### EVENTS
                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                        ft.Container( #####################
                                                    #####################  PROPERTY
                                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                    # expand=True,
                                                    ink=False,                                                      # click effect ripple
                                                    # bgcolor=ft.colors.TEAL_900,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,TEAL,CYAN,GREY,PINK,TEAL
                                                    padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                    margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    # border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border=ft.border.all(2, ft.colors.BLACK12),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    # width=80,
                                                    gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    ##################### WIDGETS
                                                    content=ft.TextButton(
                                                            text='Sponsor',
                                                            icon='data_thresholding',

                                                            # bgcolor=ft.colors.BLACK54,
                                                ),
                                                    ##################### EVENTS
                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                        ft.Container( #####################
                                                    #####################  PROPERTY
                                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                    # expand=True,
                                                    ink=False,                                                      # click effect ripple
                                                    # bgcolor=ft.colors.TEAL_900,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,TEAL,CYAN,GREY,PINK,TEAL
                                                    padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                    margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    # border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border=ft.border.all(2, ft.colors.BLACK12),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    # width=80,
                                                    gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    ##################### WIDGETS
                                                    content=ft.TextButton(
                                                            text='Help',
                                                            icon='data_saver_on_outlined',

                                                            # bgcolor=ft.colors.BLACK54,
                                                ),
                                                    ##################### EVENTS
                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                        ft.Container( #####################
                                                    #####################  PROPERTY
                                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                    # expand=True,
                                                    ink=False,                                                      # click effect ripple
                                                    # bgcolor=ft.colors.TEAL_900,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,TEAL,CYAN,GREY,PINK,TEAL
                                                    padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                    margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                    border_radius= ft.border_radius.only(top_left=0, top_right=30, bottom_left=0, bottom_right=30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border=ft.border.all(2, ft.colors.BLACK12),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    # width=80,
                                                    gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.TEAL_900],),
                                                    ##################### WIDGETS
                                                    content=ft.TextButton(
                                                            text='About',
                                                            icon='person_search',

                                                            # bgcolor=ft.colors.BLACK54,
                                                ),
                                                    ##################### EVENTS
                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA
        return Drop_BasicMenuUp



######## BasicMenuUp = BasicMenuUp(),# <======= Comma
if __name__ == '__main__':
    #####################
    # python3 ./.venv/bin/flet run 'main.py' -w #< run as web
    # python3 ./.venv/bin/flet run 'main.py' -r #< run as normal
    ###################### video
    # pip install flet_ivid --upgrade # <===== video
    # from flet_ivid import VideoContainer # import the package
    # vc = VideoContainer("yourvideo.mp4", border_radius=18, expand=True) #lambda _:vc.play() #lambda _:vc.pause()
    ###################### audio
    # ft.Audio( src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True) #lambda _: audio1.pause() #audio1.resume()) audio1.release()) audio1.seek(2000))
    # audio1.volume -= 0.1 #
    # audio1.update()
    BasicMenuUp = BasicMenuUp()
    def main(page: ft.Page):
        ###################### CONFIGURATION
        # page.title = "Containers - clickable and not"
        # page.window_title_bar_hidden = True
        # page.window_frameless = True
        # page.window_focused=True
        # page.auto_scroll=True #scroll_to()
        # page.fonts = {"RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"}
        page.scroll="HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ######################  COLOR
        page.theme_mode = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        # page.bgcolor = ft.colors.TRANSPARENT
        # page.window_bgcolor =  ft.colors.TRANSPARENT
        ###################### POSITION OF SC
        page.window_left = 8
        page.window_top = 8
        # page.window_center()
        ###################### SIZE
        page.window_height=120
        page.window_width=530
        page.padding=8
        page.spacing=8
        page.expand=True
        ######################
        screen_1=BasicMenuUp

        page.add(screen_1)
        page.update()

    ft.app(
            # assets_dir="assets",
            target=main,
            port=8080,
            view=ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            web_renderer=ft.WebRenderer.HTML

            )