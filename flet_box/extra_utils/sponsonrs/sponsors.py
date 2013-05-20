import os
import flet as ft
# from ..settings_var.settings_widget import GLOBAL_VAR

click_avalidation: bool = False







dictionary_contribution: dict= {

"header":"""
▎Flet-Box: The Future of Development, Built on Freedom""",
"body":"""\
The software landscape is changing.

While many powerful tools are locked behind expensive paywalls, Flet-Box stands as a beacon of open-source innovation, accessible to everyone.
But the reality is, free and open-source projects like ours face constant challenges.  We rely on the generosity of our community to keep our doors open and continue to empower developers of all levels.
Join us in building a future where innovation is truly free.  Contribute today and help us keep Flet-Box alive.  Every contribution, big or small, makes a difference.

We accept donations in the following cryptocurrencies:

             • MATIC    • BNB    • TRON    • ETH

Together, we can ensure that Flet-Box remains a vital resource for the future of development, accessible to everyone, regardless of budget.

""",
"crypto":{
        "Matic":{
                "address":"0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA",
                "path_image":"",
            },

        "Tron":{
                "address":"THi2UTY8SrUYNrzqKek8U3pvLuEF5y4fDQ",
                "path_image":"",
            },
        "Bnb":{
                "address":"bnb1vhe8q5zf2fr6s0ga8dnm5nzaz9uapky6w2xcnr",
                "path_image":"",
            },
        "Sol":{
                "address":"0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA",
                "path_image":"",
            },
            }

}

class InfoProyect(ft.Container):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        self.content=ft.Container(
                                # expand=True,
                                ink=False,                                                      # click effect ripple
                                bgcolor=ft.colors.BLACK45,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding= ft.padding.all(8),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                margin = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment=ft.alignment.top_center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                border_radius= ft.border_radius.all(36),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border=ft.border.all(2, ft.colors.BLACK),                       # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                shadow = ft.BoxShadow(
                                           spread_radius=0,
                                           blur_radius=18,
                                           color=ft.colors.with_opacity(0.8,ft.colors.BLACK),
                                           offset=ft.Offset(0, 0),
                                           blur_style=ft.ShadowBlurStyle.OUTER,
                                     ),
                                gradient=ft.LinearGradient( begin = ft.alignment.top_center,
                                                            end   = ft.alignment.bottom_left,
                                                            colors= [
                                                                     ft.colors.BLACK,
                                                                     ft.colors.BLACK12 ,
                                                                     ft.colors.BLACK,
                                                                     ],),
                                width=360,
                                # height=600,
                                # tooltip='Container',
                                ############################
                            content=ft.Column(
                                           controls = [
                                                        # ft.Text(value=dictionary_contribution.get("header")),
                                                        # ft.Text(value=dictionary_contribution.get("body")),
                                                        ft.Text(
                                                                spans=[
                                                                ft.TextSpan( f"{dictionary_contribution.get('header')}\n\n",
                                                                ft.TextStyle(size=18,
                                                                             color = ft.colors.RED,
                                                                             weight= ft.FontWeight.BOLD,
                                                                             ),),
                                                                ft.TextSpan( dictionary_contribution.get("body"),
                                                                ft.TextStyle(size=15,
                                                                             color=ft.colors.WHITE,
                                                                             # decoration= ft.TextDecoration.LINE_THROUGH,
                                                                             ),),
                                                                ],),
                                           ]
                                           )
                        )

class CardPrice(ft.Container):
    # globalVar='Erase this test'

    def __init__(self,card_color: bool=False,card_plan: int=1,card_price: int=1,card_type: str=""):
        super().__init__()
        # self.title='data'
        self.card_color=card_color
        self.card_plan = card_plan
        self.card_type = card_type
        self.card_price = card_price
        self.gold_color = ft.colors.YELLOW_ACCENT_400 if self.card_color else ft.colors.BLUE_900


        if self.card_plan == 1: self.buy_card = [ True, False, False, False, False ]
        if self.card_plan == 2: self.buy_card = [ True, True,  False, False, False ]
        if self.card_plan == 3: self.buy_card = [ True, True,  True,  True,  True  ]

    def build(self):
        self.content=ft.Container(
                                expand=True,
                                ink=False,                                                      # click effect ripple
                                bgcolor=ft.colors.BLACK45,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding= ft.padding.all(8),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                margin = ft.margin.all(8),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border=ft.border.all(6, ft.colors.BLACK45),                       # ft.border.only(Left=8, top=8, right=8, bottom=8),

                                shadow = ft.BoxShadow(
                                       spread_radius=0,
                                       blur_radius=16,
                                       color=ft.colors.with_opacity(0.8,ft.colors.BLACK26),
                                       offset=ft.Offset(0, 0),
                                       blur_style=ft.ShadowBlurStyle.OUTER,
                                 ),

                                gradient=ft.LinearGradient( begin = ft.alignment.top_center,
                                                            end   = ft.alignment.bottom_left,
                                                            colors= [
                                                                     ft.colors.BLACK,
                                                                     self.gold_color ,
                                                                     ft.colors.BLACK,
                                                                     ],),
                                # ===================
                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_opacity=0.1,
                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # ===================
                                width=240,
                                height=360,
                                # tooltip='Container',
                                ############################
                            content=ft.Column(
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                    spacing=0,
                                                    run_spacing=0,
                                                    controls=[
                                                        ft.Text(value=self.card_type,size=16, weight = ft.FontWeight.BOLD),
                                                        ft.Text(spans=[
                                                                        ft.TextSpan( f"${self.card_price}",
                                                                        ft.TextStyle(size=24,
                                                                                     color=ft.colors.WHITE38,
                                                                                     weight= ft.FontWeight.BOLD,
                                                                                     decoration= ft.TextDecoration.LINE_THROUGH,
                                                                                     ),),
                                                                        ft.TextSpan( f"${self.card_price//2} ",
                                                                        ft.TextStyle(size=45,
                                                                                     color=ft.colors.WHITE,
                                                                                     weight= ft.FontWeight.BOLD,
                                                                                     # decoration= ft.TextDecoration.LINE_THROUGH,
                                                                                     ),),],


                                                        ),
                                                        ft.Text(value="Per Month",size=16, weight = ft.FontWeight.BOLD,),

                                                        ft.Checkbox(label="Core Plataform Features", value=self.buy_card[0]),
                                                        ft.Checkbox(label="Unlimit Compilate App",   value=self.buy_card[1]),
                                                        ft.Checkbox(label="Code Download",           value=self.buy_card[2]),
                                                        ft.Checkbox(label="GitHub Integration",      value=self.buy_card[3]),
                                                        ft.Checkbox(label="App & Play Store Dev",    value=self.buy_card[4]),
                                                        ft.ElevatedButton(
                                                                          text="FREE",
                                                                          bgcolor=ft.colors.BLACK45,
                                                                          )
                                               ]
                                              )
                        )
######## CardPrice = CardPrice(),# <======= Comma


class InfoPrices(ft.Container):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        self.content=ft.Container(
                                expand=True,
                                ink=False,                                                      # click effect ripple
                                bgcolor  = ft.colors.BLACK26,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding  = ft.padding.all(0),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                margin   = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment= ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                border_radius= ft.border_radius.all(36),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border = ft.border.all(2, ft.colors.BLACK),                       # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                # ===================
                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_opacity=0.1,
                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # ===================
                                # width=150,
                                # height=150,
                                # tooltip='Container',
                                ############################
                            content = ft.Row(
                                           controls = [
                                           CardPrice(card_plan=1, card_price=110 ,card_type="Standar"),
                                           CardPrice(card_plan=3 ,card_price=200 ,card_type="Pro" ,card_color=True),
                                           CardPrice(card_plan=2, card_price=160 ,card_type="Teams"),
                                           ]
                                           )
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
                            image_src = f"/home/mjay/Desktop/testing_create_package/flet_box/assets/.cripto.webp",
                            image_opacity=0.05,
                            image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                            # ===================
                            # width    = 220,
                            # height   = 220,
                            # tooltip='Container',
                            expand=True,
                            ############################
                            content=ft.Row(
                                       controls=[
                                            ft.Container(
                                                        ink=False,                                                      # click effect ripple
                                                        bgcolor  = ft.colors.BLACK45,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding  = ft.padding.all(8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin   = ft.margin.all(8),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment= ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                        width    = 190,
                                                        height   = 190,
                                                        border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                        shadow = ft.BoxShadow(
                                                                   spread_radius=0,
                                                                   blur_radius=18,
                                                                   color=ft.colors.with_opacity(0.8,ft.colors.BLACK),
                                                                   offset=ft.Offset(0, 0),
                                                                   blur_style=ft.ShadowBlurStyle.OUTER,
                                                             ),
                                                        content=ft.Image(
                                                                    ##################### PROPERTY
                                                                    # img most be inside assets /name_imagen.png
                                                                    src               = f"/home/mjay/Desktop/testing_create_package/flet_box/assets/.matic_wallet.jpg",
                                                                    fit               = ft.ImageFit.COVER,                      # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                    # repeat          = ft.ImageRepeat.NO_REPEAT,
                                                                    border_radius   = ft.border_radius.all(30),               # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            ft.Container(
                                                        ink=False,                                                      # click effect ripple
                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding  = ft.padding.all(8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin   = ft.margin.all(8),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                        alignment= ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                        # width    = 555,
                                                        # height   = 220,
                                                        border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                        content=ft.Column(
                                                                          controls=[

                                                                          ft.ElevatedButton(text="Solana",elevation=12,bgcolor=ft.colors.RED_800),
                                                                          ft.ElevatedButton(text="Matic" ,elevation=12,bgcolor=ft.colors.BLUE_800),
                                                                          ft.ElevatedButton(text="Bnb"   ,elevation=12,bgcolor=ft.colors.CYAN_900),
                                                                          ft.ElevatedButton(text="Tron"  ,elevation=12,bgcolor=ft.colors.PURPLE_900),

                                                                          ]
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                            ft.Container(
                                                        # ink=False,                                                      # click effect ripple
                                                        bgcolor  =ft.colors.BLACK26,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding  = ft.padding.only(left=12, top=24, right=8, bottom=8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        margin   = ft.margin.all(8),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                        # alignment= ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                        width    = 450,
                                                        # height   = 220,
                                                        border_radius= ft.border_radius.all(24),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                        content=ft.Column(
                                                                          run_spacing=8,
                                                                          spacing =8,
                                                                          controls=[


                                                                          ft.Row(
                                                                                controls=[
                                                                                        ft.Text(value="Matic:   TRC20 ",size=24, weight = ft.FontWeight.BOLD),
                                                                                        ],
                                                                                 ),

                                                                          ft.Row(
                                                                                 run_spacing=0,
                                                                                 spacing    =4,
                                                                                 controls=[
                                                                                 ft.ElevatedButton(text="Copy",elevation=12,bgcolor=ft.colors.RED_800),
                                                                                 ft.TextButton(
                                                                                          text="0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA",
                                                                                          ),
                                                                                 ]),
                                                                          ft.Text(
                                                                                    spans=[

                                                                                    ft.TextSpan( "Hello Dev:   You may invite me a beer ;)\n",
                                                                                    ft.TextStyle(size=20,
                                                                                                 weight= ft.FontWeight.BOLD,
                                                                                                 color=ft.colors.BLUE_ACCENT_200,
                                                                                                 ),),
                                                                                    ],
                                                                                        ),

                                                                          ]
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                       ]
                                    )
                        )
######## InfoPrices = InfoPrices(),# <======= Comma

class SponsorPage(ft.Stack):

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
                    # height        = 650,
                    # width=950,
                    expand        = True,
                    blur=(60,60),
                    ###################
                # on_hover= lambda _: self.validate_click(),
                content=ft.Row(
                                    # alignment=ft.MainAxisAlignment.CENTER,
                                    # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                                # self.left_column,
                                                ft.Container(
                                                             content=ft.Column(
                                                                    controls=[
                                                                            InfoPrices(),
                                                                            WalletDirection(),
                                                                    ] )
                                                             ),
                                                InfoProyect(),
                                                # self.right_column,
                                             ],),
        )#<=== NOTE COMA
        return Drop_SponsorPage

    def validate_click(self):
        global click_avalidation
        self.donation_page_browser  = GLOBAL_VAR(get_global_var='DONATION_BROWSER_CONTAINER')

        if click_avalidation:
            click_avalidation = False
            self.donation_page_browser.visible = False
            self.donation_page_browser.update()
        else:
            click_avalidation = True


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
        # page.window_width              = 1200
        page.padding                   = 0
        page.spacing                   = 0
        page.add(SponsorPage())

    ft.app(
        target=main,
        assets_dir   = "assets"

        )