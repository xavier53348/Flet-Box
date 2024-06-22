import os
import flet as ft
# from ..settings_var.settings_widget import GLOBAL_VAR


class InfoPrices(ft.Container):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        self.content=ft.Container(
                                # expand=True,
                                ink=False,                                                      # click effect ripple
                                bgcolor="#3f9a64",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding= ft.padding.all(0),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                margin = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border=ft.border.all(2, ft.colors.BLACK),                       # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                # ===================
                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_opacity=0.1,
                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # ===================
                                width=150,
                                # height=150,
                                # tooltip='Container',
                                ############################
                            content=ft.Text(f"{self.title}")
                        )
######## InfoPrices = InfoPrices(),# <======= Comma

class WalletDirection(ft.Container):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        self.content=ft.Container(
                            # expand=True,
                            bgcolor      = ft.colors.BLACK45,
                            padding      = ft.padding.all(0),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                            margin       = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                            alignment    = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                            border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                            border       = ft.border.all(2, ft.colors.BLACK),                       # ft.border.only(Left=8, top=8, right=8, bottom=8),
                            # ===================
                            # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                            # image_opacity=0.1,
                            # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                            # ===================
                            width    = 320,
                            height   = 320,
                            # tooltip='Container',
                            ############################
                            content=ft.Column(
                                       controls=[
                                            ft.Container(
                                                        ink=False,                                                      # click effect ripple
                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding  = ft.padding.all(8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin   = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment= ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                        width    = 320,
                                                        height   = 320,
                                                        border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                        content=ft.Image(
                                                                    ##################### PROPERTY
                                                                    # img most be inside assets /name_imagen.png
                                                                    src               = f"/home/mjay/Desktop/testing_create_package/flet_box/assets/.matic_wallet.jpg",
                                                                    fit               = ft.ImageFit.COVER,                      # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                    # repeat          = ft.ImageRepeat.NO_REPEAT,
                                                                    border_radius   = ft.border_radius.all(30),               # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                    # key             = 'is our id',
                                                                    # expand          = True,
                                                                    # data            = 'value of the button',                  # store data in the button
                                                                    # tooltip         = 'Image',
                                                                    ##################### COLOR
                                                                    # color           = 'yellow',                               # text color
                                                                    ##################### ATTRIB
                                                                    # visible         = False,
                                                                    # opacity         = 1,
                                                                    # disabled        = True,
                                                                    # semantics_label = "Double dollars",
                                                                    ##################### POSITION
                                                                    # rotate          = 20 ,
                                                                    # offset          = (0,1),
                                                                    # scale           = 0.9,
                                                                    # aspect_ratio    = 2,
                                                                    ##################### MULTI LABEL
                                                                    # width           = 240,
                                                                    # height          = 32,
                                                                    ##################### STYLES TEXT
                                                                    # src_base64      = "iVBORw0KGgoAAAANSUhEUgAAAOYAAAA7CAYAAABvyvZKAAAAGXRFWHRTb2Z0d2FyZQB"),
                                                                    # base64 -i <image.png> -o <image-base64.txt>
                                                                    #####################
                                                                    # src_base64       = data_base64.data_imagen,
                                                                    # CLEAR ,COLOR ,COLOR_BURN ,COLOR_DODGE ,DARKEN ,DIFFERENCE ,DST ,DST_A_TOP ,DST_IN ,DST_OUT ,DST_OVER ,EXCLUSION  HARD_LIGHT ,HUE ,LIGHTEN
                                                                    # LUMINOSITY , MODULATE (default) ,MULTIPLY ,OVERLAY ,PLUS ,SATURATION ,SCREEN ,SOFT_LIGHT ,SRC ,SRC_A_TOP ,SRC_IN ,SRC_OUT ,SRC_OVER ,VALUES ,XOR
                                                                    # color_blend_mode = ft.BlendMode.COLOR_BURN,
                                                                    # gapless_playback = True,
                                                        ##################### EVENTS
                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                       ]
                                    )
                        )
######## InfoPrices = InfoPrices(),# <======= Comma

class SponsorPage(ft.Stack):
    data_dev = {
        'profile':"""Experienced software developer with a passion for creating intuitive graphical user interfaces (GUIs) across multiple platforms. Dedicated to delivering high-quality, user-centric applications tailored to meet specific client needs.
        """
    }
    def __init__(self,data='Erase this test'):
        super().__init__()
        self.title=data

    def build(self):
        self.left_column = ft.Container(
                    ink       = False,
                    padding   = ft.padding.all(4),
                    margin    = ft.margin.all(4),
                    alignment = ft.alignment.center,
                    content=ft.Column(
                        alignment            =ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment =ft.CrossAxisAlignment.START,

                        controls=[

                                 ],
                    ),#<=== NOTE COMA [NOTE]
        )#<=== NOTE COMA

        self.right_column = ft.Container(
                    ink       = False,
                    padding   = ft.padding.all(8),
                    margin    = ft.margin.all(8),
                    alignment = ft.alignment.center,
                    content=ft.Column(
                                alignment = ft.MainAxisAlignment.SPACE_AROUND,
                                controls  = [

                                         ],
                    ),#<=== NOTE COMA [NOTE]
        )#<=== NOTE COMA

        Drop_SponsorPage=ft.Container(
                    ink           = False,
                    bgcolor       = ft.colors.BLACK12,
                    padding       = ft.padding.all(32),
                    margin        = ft.margin.all(8),
                    alignment     = ft.alignment.center,
                    border_radius = ft.border_radius.all(30),
                    border        = ft.border.all(1, ft.colors.TEAL_900),
                    height        = 650,
                    width=1200,
                    blur=(20,20),
                    ###################
                on_click  = lambda _:self.show_widgets(show_widget='about_page'),
                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                                # self.left_column,
                                                InfoPrices(),
                                                WalletDirection(),
                                                # self.right_column,
                                             ],),
        )#<=== NOTE COMA
        return Drop_SponsorPage

    def show_widgets(self,show_widget):
        """SHOW PAGES"""
        if show_widget == "about_page":
            self.about_page  = GLOBAL_VAR(get_global_var='ABOUT_CONTAINER')
            self.about_page.visible  = True if not self.about_page.visible else False
            self.about_page.update()


if __name__ == '__main__':
    def main(page: ft.Page):

        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER

        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100

        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 700
        page.window_width              = 800
        page.padding                   = 0
        page.spacing                   = 0
        page.add(SponsorPage())

    ft.app(
        target=main,
        assets_dir   = "assets"

        )