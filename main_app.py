from extra_utils.config.widget_editor import Build_Editor

import flet as ft

def main(page: ft.Page):
    ###################### CONFIGURATION
    # page.title = "Containers - clickable and not"
    # page.window_title_bar_hidden = True
    # page.window_frameless = True
    # page.window_focused=True
    # page.auto_scroll=True #scroll_to()
    # page.fonts = {"RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"}
    # page.scroll="HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
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
    page.window_height=640
    page.window_width=720
    page.padding=8
    page.spacing=8
    page.expand=True
    ######################
    # Double_Widget = DoubleWidget
    ######################
    text_widget  = ft.Container(
                                image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_fit='COVER',
                                # expand=True,
                                bgcolor       = ft.colors.BLACK38,
                                # bgcolor       = ft.colors.BLACK38,
                                # border_radius = ft.border_radius.all(15),
                                # alignment     = ft.alignment.center,
                                width         = 260,
                                height        = 120,
                                # blur=ft.Blur(18, 18, ft.BlurTileMode.MIRROR),
                                # content       = ft.Row(controls=[ft.Text(value='hello world')]),
                                content       = ft.Text(value='hello world',bgcolor='red'),
                                # content       = ft.TextField(value='hello world'),
                                # content       = ft.ElevatedButton(text='hello world'),
                                # border = ft.border.all(2, ft.colors.BLACK),
                                )
    screen_1=ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink=True,                                           # click effect ripple
                    bgcolor= ft.colors.BLACK38,                                # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    # bgcolor= ft.colors.BLACK38,                                # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(8),    # inside box         # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(0),     # outside box        # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                      # top_left, top_center, top_right, center_left, center, center_right, bottom_left, bottom_center, bottom_right.    posicionamiento adentro widget
                    border_radius= ft.border_radius.all(32),          # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border=ft.border.all(3, ft.colors.BLUE),          # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    ###################### MOST BE IN ASSETS
                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity=0.1,
                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    ######################
                    # width=150,
                    # height=150,
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    # widget=text_widget <==== is the widget that we wan modify
                    content=Build_Editor(widget=text_widget),
                    # content=BuildEditor(config_widget='value',widget=text_widget),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                        # on_hover=print('on click over'), on_long_press=print('long press'),
                )

    data_ = ft.Row(controls = [text_widget,screen_1])

    page.add( data_
                )
    page.update()

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

    ft.app(
            # assets_dir="assets",
            target=main,
            # port=8080,
            # view=ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            # web_renderer=ft.WebRenderer.HTML

            )