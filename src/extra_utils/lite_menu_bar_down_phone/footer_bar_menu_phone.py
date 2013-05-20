import flet as ft



class LiteMenuDownContainer(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,main_page='Erase this test'):
        super().__init__()
        # self.title='data'
        # self.main_page=main_page

        main_page = main_page
    def build(self):
        Drop_LiteMenuDownContainer = ft.Container(
                                        # expand=True,
                                        ink             = False,                                         # click effect ripple
                                        bgcolor         = ft.colors.BLACK26,                             # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                        padding         = ft.padding.all(0),    # inside box             # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin          = ft.margin.all(0),    #outside box              # margin.only (left=8, top=8, right=8, bottom=8),
                                        alignment       = ft.alignment.center,                           # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                        border_radius   = ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        # border        = ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        #               ===================
                                        # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                        # image_opacity = 0.1,
                                        # image_fit     = 'COVER',                                       # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                        #               ===================
                                        # width         = 150,
                                        # height        = 150,
                                        # tooltip       = 'Container',
                                        ##################### EFFECTS
                                        # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.BLACK12],),
                                        # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                        ##################### WIDGETS
                                   content=ft.Row(
                                                  ##################### PROPERTY BOX
                                                  # expand           = True,
                                                  alignment          = ft.MainAxisAlignment.SPACE_BETWEEN,    # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                  vertical_alignment = ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                  ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                  # scroll=True,                                              # center widget
                                                  # tight=True,
                                                  ##################### ADAPT TO SCREEN
                                                  # wrap=True,                                                # justify in all screen
                                                  # spacing=8,                                                # space widget left right
                                                  # run_spacing=8,                                            # space widget up down
                                                  ##################### WIDGETS
                                                  ##################### ADAPT TO SCREEN
                                                  # wrap=True,                                                # justify in all screen
                                                  # spacing=8,                                                # space widget left right
                                                  # run_spacing=8,                                            # space widget up down
                                                  ##################### WIDGETS
                                                controls=[
                                                            ft.Container( ############ NAME SCREEN
                                                                        ##################### PROPERTY
                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                        # expand=True,
                                                                           ink           = False,                                                # click effect ripple
                                                                           bgcolor       = ft.colors.BLACK12,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                           padding       = ft.padding.only(left=4, top=0, right=2, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                           margin        = ft.margin.all(0),    #outside box                     # margin.only (left=8, top=8, right=8, bottom=8),
                                                                           alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                           border_radius = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                           border        = ft.border.all(2, ft.colors.BLACK12),
                                                                           width         = 150,
                                                                      content=ft.Row(
                                                                                ##################### PROPERTY BOX
                                                                                expand=True,
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,               # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                # vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                # scroll=True,                                              # center widget
                                                                                # tight=True,
                                                                                ##################### ADAPT TO SCREEN
                                                                                # wrap=True,                                                # justify in all screen
                                                                                spacing=8,                                                  # space widget left right
                                                                                # run_spacing=8,                                            # space widget up down
                                                                                ##################### WIDGETS
                                                                           controls=[

                                                                                     ft.Container(
                                                                                                 ##################### PROPERTY
                                                                                               ink           = False,                                   # click effect ripple
                                                                                               # bgcolor     = ft.colors.BLACK12,                       # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                               padding       = ft.padding.all(0),    # inside box       # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                               alignment     = ft.alignment.center,                     # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                               border_radius = ft.border_radius.all(30),                # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                               border        = ft.border.all(2, ft.colors.BLACK12),     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                               # width         = 150,
                                                                                               height        = 35,
                                                                                           content = ft.Dropdown(
                                                                                                               hint_text       = '   Screen 1',
                                                                                                               width           = 140,
                                                                                                               content_padding = ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                                               alignment       = ft.alignment.center_left,            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                               border_radius   = ft.border_radius.all(15),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                               border          = ft.InputBorder.NONE,
                                                                                                               options         = [
                                                                                                                                  ft.dropdown.Option("   Screen 1"),
                                                                                                                                  ft.dropdown.Option("   Screen 2"),
                                                                                                                                  ft.dropdown.Option("   Screen 3"),
                                                                                                                                  ft.dropdown.Option("   Screen 4"),
                                                                                                                                  ft.dropdown.Option("   Screen 5"),
                                                                                                               ],
                                                                                                               ##################### EVENTS
                                                                                                       # on_change = lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                                                                       # on_change   = lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data')),
                                                                                                       # on_change = lambda _:print(_.__dict__.get('data')),
                                                                                                       # on_click  = lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                   ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                                                 ##################### EVENTS
                                                                                                 # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                     ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                 ],
                                                                 ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                            ft.Container( ##################### SELECTED WIDGET
                                                                        ink           = False,                                           # click effect ripple
                                                                        bgcolor       = ft.colors.BLACK12,                               # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                        padding       = ft.padding.all(0),    # inside box               # padding.only(left=8, top=8, right=8, bottom=8),
                                                                        margin        = ft.margin.all(0),     # outside box              # margin.only (left=8, top=8, right=8, bottom=8),
                                                                        alignment     = ft.alignment.center_left,                        # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                        border_radius = ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                        border        = ft.border.all(2, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                        width         = 160,
                                                                        ##################### WIDGETS
                                                                        content=ft.Row(
                                                                                # alignment=ft.MainAxisAlignment.START,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                                                controls = [

                                                                                     ft.Container(
                                                                                               margin=ft.margin.only (left=8, top=0, right=0, bottom=0),
                                                                                               # expand=True,
                                                                                               content=ft.Icon(name=ft.icons.SELECT_ALL_ROUNDED),
                                                                                          ),
                                                                                     ft.Text(
                                                                                         ##################### PROPERTY
                                                                                         value           = "Selected:\n", # content = ft.Text(value="Compound button", size=12,),
                                                                                         text_align      = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                                         weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                                         font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                                                         ##################### COLOR
                                                                                         # width           = 120,
                                                                                         size=10,
                                                                                         #####################
                                                                                         spans=[ft.TextSpan( "Image", ft.TextStyle( size=20, color=ft.colors.BLUE,weight=ft.FontWeight.BOLD),),],
                                                                           ),]),
                                                                        ##################### EVENTS
                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                            ),#<=== NOTE COMA
                                                            ft.Container( ############ NAME SCREEN
                                                                        ##################### PROPERTY
                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                        # expand=True,
                                                                           ink=False,                                                     # click effect ripple
                                                                           bgcolor=ft.colors.BLACK26,                                     # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                           padding= ft.padding.only(left=4, top=0, right=2, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                           margin = ft.margin.all(0),    #outside box                     # margin.only (left=8, top=8, right=8, bottom=8),
                                                                           alignment=ft.alignment.center,                                 # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                           border_radius= ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                           border=ft.border.all(2, ft.colors.BLACK12),
                                                                           width=150,
                                                                      content=ft.Row(
                                                                                ##################### PROPERTY BOX
                                                                                expand=True,
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                # vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                # scroll=True,                                              # center widget
                                                                                # tight=True,
                                                                                ##################### ADAPT TO SCREEN
                                                                                # wrap=True,                                                  # justify in all screen
                                                                                spacing=8,                                                # space widget left right
                                                                                # run_spacing=8,                                            # space widget up down
                                                                                ##################### WIDGETS
                                                                           controls=[

                                                                                     ft.Container(
                                                                                                 ##################### PROPERTY
                                                                                                 ink           = False,                          # click effect ripple
                                                                                                 # bgcolor       = "#44CCCC00",                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                                 width         = 95,
                                                                                                 height        = 30,
                                                                                                 border_radius = ft.border_radius.all(30),       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                 content = ft.TextField(
                                                                                                                 hint_text ='Name Scr',
                                                                                                                 border    = ft.InputBorder.NONE,    # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                                 bgcolor   = ft.colors.BLACK12,                 # inside box
                                                                                                                 color     = 'White',
                                                                                                                 text_size = 15,
                                                                                                                 ),
                                                                                                 ##################### EVENTS
                                                                                                 # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                     ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                                     ft.IconButton(
                                                                                             ##################### PROPERTY
                                                                                             icon          = ft.icons.PLUS_ONE,
                                                                                             selected_icon = ft.icons.BATTERY_FULL,
                                                                                             icon_color    = ft.colors.TEAL,
                                                                                             selected      = False,
                                                                                             #####################
                                                                                             # icon_size   = 20,
                                                                                             bgcolor       = ft.colors.BLACK12,     # back color
                                                                                             ##################### ATTRIB
                                                                             ##################### EVENTS
                                                                             # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                     ),],
                                                                 ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                                            # ft.Container( ##################### SELECTED WIDGET
                                                            #             ink           = False,                                                # click effect ripple
                                                            #             bgcolor       = ft.colors.BLACK12,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                            #             padding       = ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                            #             margin        = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                            #             alignment     = ft.alignment.center_left,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                            #             border_radius = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                            #             border        = ft.border.all(2, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                            #             width         = 160,
                                                            #             ##################### WIDGETS
                                                            #             content=ft.Row(
                                                            #                     # alignment          = ft.MainAxisAlignment.START,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                            #                     # vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                                            #                     controls = [

                                                            #                          ft.Container(
                                                            #                                    margin   = ft.margin.only (left=8, top=0, right=0, bottom=0),
                                                            #                                    # expand = True,
                                                            #                                    content  = ft.Icon(name=ft.icons.SELECT_ALL_ROUNDED),
                                                            #                               ),
                                                            #                          ft.Text(
                                                            #                              ##################### PROPERTY
                                                            #                              value           = "Selected:\n", # content = ft.Text(value="Compound button", size=12,),
                                                            #                              text_align      = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            #                              weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                            #                              font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                            #                              ##################### COLOR
                                                            #                              # width           = 120,
                                                            #                              size=10,
                                                            #                              #####################
                                                            #                              spans=[ft.TextSpan( "Image", ft.TextStyle( size=20, color=ft.colors.BLUE,weight=ft.FontWeight.BOLD),),],
                                                            #                ),]),
                                                            #             ##################### EVENTS
                                                            #             # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                            # ),#<=== NOTE COMA
                                                         ],),
                                ##################### EVENTS
                                # on_click=lambda _:print(_),                                           # on_hover=print('on click over'), on_long_press=print('long press'),
                            )#<=== NOTE COMA
        return Drop_LiteMenuDownContainer

    def action_windows(self,action):

        if action == 'Close':
            self.main_page.window_close()

        elif action == 'Minimize':
            self.main_page.window_minimized = True

        elif action == 'Resize':
            self.main_page.window_maximizable =True
        self.main_page.update()
######## LiteMenuDownContainer = LiteMenuDownContainer(),# <======= Comma






if __name__ == '__main__':

     def main(page: ft.Page):
         ###################### CONFIGURATION
         # page.title                   = "Containers - clickable and not"
         # page.window_title_bar_hidden   = True
         # page.window_title_bar_buttons_hidden = True
         # page.window_focused            = True
         # page.window_skip_task_bar    = True
         # page.window_frameless
         # print(dir(page))
         # page.window_frameless        = True
         # page.auto_scroll             = True #scroll_to()
         # page.fonts                   = {"RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"}
         # page.splash                  = ft.Image(src=f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg")
         # page.splash                    = True
         page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
         page.vertical_alignment        = ft.MainAxisAlignment.CENTER
         page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
         ######################  COLOR
         page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
         page.window_bgcolor            = ft.colors.RED_100
         # page.bgcolor                 = ft.colors.BLACK
         # page.window_bgcolor          =  ft.colors.RED
         # page.window_bgcolor          =  ft.colors.TRANSPARENT
         ###################### POSITION OF SC
         page.window_left               = 20
         page.window_top                = 20
         # page.window_center()
         ###################### SIZE
         page.window_height           = 120
         # page.window_height             = 800
         # page.window_height             = 715
         page.window_width            = 600
         # page.window_width            = 1200
         page.padding                   = 0
         page.spacing                   = 0
         page.expand                    = True
         Lite_MenudDownContainer = LiteMenuDownContainer()
         page.add(Lite_MenudDownContainer)
         page.update()
     #####################
     # python3 ./.venv/bin/flet run 'main.py' -w #< run as web
     # python3 ./.venv/bin/flet run 'main.py' -r #< run as normal
     ###################### video
     # pip install flet_ivid --upgrade # <===== video
     # from flet_ivid import VideoContainer # import the package


     # vc            = VideoContainer("yourvideo.mp4", border_radius=18, expand=True) #lambda _:vc.play() #lambda _:vc.pause()
     ###################### audio
     # ft.Audio( src ="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True) #lambda _: audio1.pause() #audio1.resume()) audio1.release()) audio1.seek(2000))
     # audio1.volume -= 0.1 #
     # audio1.update()

     ft.app(
            # assets_dir   = "assets",
            target         = main,
            # port         = 8080,
            # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            # web_renderer = ft.WebRenderer.HTML
            )