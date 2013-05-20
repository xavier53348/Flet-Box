import flet as ft



class LiteMenuUpContainer(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,main_page= None , phone_widget_container= None,menu_left_container= None , menu_right_container= None):
        super().__init__()
        self.main_page = main_page
        self.menu_left_container    = menu_left_container
        self.phone_widget_container = phone_widget_container
        self.menu_right_container   = menu_right_container

    def build(self):

        Drop_LiteMenuUpContainer = ft.Container(
                                        ##################### PROPERTY
                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                        # expand=True,
                                        ink             = False,                                         # click effect ripple
                                        bgcolor         = ft.colors.BLACK26,                             # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                        padding         = ft.padding.all(2),    # inside box             # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin          = ft.margin.all(2),    #outside box              # margin.only (left=8, top=8, right=8, bottom=8),
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
                                        # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                        # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                        ##################### WIDGETS
                                content=ft.Row(
                                                ##################### PROPERTY BOX
                                                expand=True,
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
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
                                                            ft.Container( ##################### DEVICES
                                                                        ##################### PROPERTY
                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                        # expand=True,

                                                                        ink=False,                                                # click effect ripple
                                                                        # bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                        padding= ft.padding.only(left=8, top=0, right=8, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                        # margin = ft.margin.all(8),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                                        alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                        border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                        border=ft.border.all(2, ft.colors.BLACK12),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                        # ===================
                                                                        # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                        # image_opacity=0.1,
                                                                        # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                        # ===================
                                                                        # width=150,
                                                                        # height=150,
                                                                        # tooltip='Container',
                                                                        ##################### EFFECTS
                                                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                        # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                        ##################### WIDGETS
                                                                        content=ft.Row(
                                                                                        ##################### PROPERTY BOX
                                                                                        # expand=True,
                                                                                        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
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
                                                                                                    ft.IconButton(icon=ft.icons.SMARTPHONE,tooltip='SMARTPHONE',),
                                                                                                    ft.IconButton(icon=ft.icons.TABLET_ANDROID,tooltip='TABLET'),
                                                                                                    ft.IconButton(icon=ft.icons.TV_OUTLINED,tooltip='PC'),
                                                                                                    ft.IconButton(icon=ft.icons.FEATURED_PLAY_LIST_OUTLINED,tooltip='BROWSER'),
                                                                                                    ft.Container( ##################### NAME DEVICE
                                                                                                                ##################### PROPERTY
                                                                                                                ink=False,                                                      # click effect ripple
                                                                                                                # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                                                padding= ft.padding.all(8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                                                margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                                                ##################### WIDGETS
                                                                                                                content=ft.Text(
                                                                                                                            ##################### PROPERTY
                                                                                                                            value           = "Device IPhone\n", # content = ft.Text(value="Compound button", size=12,),
                                                                                                                            text_align      = ft.TextAlign.LEFT,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                                                                            weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                                                                            font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                                                                                            ##################### COLOR
                                                                                                                            height          = 25,
                                                                                                                            overflow="ellipsis",                                      # FADE,ELLIPSIS,CLIP,VISIBLE
                                                                                                                            #####################
                                                                                                                            spans=[ft.TextSpan( "375(px) x 812(px)", ft.TextStyle( size=8, color=ft.colors.BLUE),),],
                                                                                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                                                 ],),
                                                                        ##################### EVENTS
                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                            ),#<=== NOTE COMA
                                                            ft.Container( ##################### DEVICES
                                                                        ##################### PROPERTY
                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                        # expand=True,
                                                                        padding= ft.padding.only(left=8, top=0, right=8, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),

                                                                        ink=False,                                                # click effect ripple
                                                                        # bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                        # padding= ft.padding.all(8),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                        # margin = ft.margin.all(8),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                                        alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                        border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                        border=ft.border.all(2, ft.colors.BLACK12),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                        # ===================
                                                                        # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                        # image_opacity=0.1,
                                                                        # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                        # ===================
                                                                        # width=150,
                                                                        # height=150,
                                                                        # tooltip='Container',
                                                                        ##################### EFFECTS
                                                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                        # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                        ##################### WIDGETS
                                                                        content=ft.Row(
                                                                                        ##################### PROPERTY BOX
                                                                                        expand=True,
                                                                                        # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
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
                                                                                                    ft.IconButton(icon=ft.icons.SCREEN_ROTATION,tooltip='ROTATE',),
                                                                                                    ft.IconButton(icon=ft.icons.DEBLUR,tooltip='LIGHT / DARK',),
                                                                                                 ],),
                                                                        ##################### EVENTS
                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                            ),#<===
                                                            # ft.ElevatedButton("rotate",tooltip='buttom',on_click=lambda _:self.action_windows(_)),
                                                            # ft.ElevatedButton("press row",tooltip='buttom'),
                                                            # ft.ElevatedButton("press row",tooltip='buttom'),
                                                         ],),
                                ##################### EVENTS
                                # on_click=lambda _:print(_),                                           # on_hover=print('on click over'), on_long_press=print('long press'),
                            )#<=== NOTE COMA
        return Drop_LiteMenuUpContainer

    def action_windows(self,action):

        self.phone_widget_container.controls[0].width , self.phone_widget_container.controls[0].height = self.phone_widget_container.controls[0].height , self.phone_widget_container.controls[0].width
        # self.menu_left_container.controls[0].bgcolor    = 'red' if not self.menu_left_container.controls[0].bgcolor == 'red' else 'black'
        # self.phone_widget_container.controls[0].bgcolor = 'red' if not self.phone_widget_container.controls[0].bgcolor == 'red' else 'black'
        # self.menu_right_container.controls[0].bgcolor   = 'red' if not self.menu_right_container.controls[0].bgcolor == 'red' else 'black'
        # print(self.phone_widget_container.controls[0])


        # self.menu_left_container.controls[0].update()
        self.phone_widget_container.controls[0].update()
        # self.menu_right_container.controls[0].update()
######## LiteMenuUpContainer = LiteMenuUpContainer(),# <======= Comma


# icons.WEBHOOK <=== chat gpt
# icons.WIDTH_NORMAL
# icons.VISIBILITY
# icons.VISIBILITY_OFF
# icons.VOLUNTEER_ACTIVISM
# icons.VRPANO_SHARP
# icons.VIDEO_LABEL
# icons.VIEW_CAROUSEL_ROUNDED
# icons.TRAVEL_EXPLORE_OUTLINED

# icons.TABLET_ANDROID
# icons.TABLET_ROUNDED
# icons.TABLET_MAC
# icons.TOKEN
# icons.TV_OUTLINED
# icons.SCREENSHOT_ROUNDED
# icons.SCREENSHOT_MONITOR
# icons.SENSOR_OCCUPIED
# icons.SELECT_ALL
# icons.SCREEN_ROTATION

# icons.SCREEN_SHARE
# icons.SCHEMA
# icons.SUNNY_SNOWING
# icons.LAPTOP_CHROMEBOOK_SHARP
# icons.DISCORD
if __name__ == '__main__':
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
        page.window_height           = 400
        # page.window_height             = 800
        # page.window_height             = 715
        page.window_width            = 600
        # page.window_width            = 1200
        page.padding                   = 0
        page.spacing                   = 0
        page.expand                    = True
        Lite_MenuUpContainer = LiteMenuUpContainer()
        page.add(Lite_MenuUpContainer)
        page.update()
    ft.app(
            # assets_dir   = "assets",
            target         = main,
            # port         = 8080,
            # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            # web_renderer = ft.WebRenderer.HTML
            )