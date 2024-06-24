import os
import time
import flet as ft
from ..settings_var.settings_widget import GLOBAL_VAR
import pyperclip # type: ignore

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

             • Solana    • Matic    • Bnb    • Tron

Together, we can ensure that Flet-Box remains a vital resource for the future of development, accessible to everyone, regardless of budget.

""",
"crypto":{
       "Matic":{
                "address":"0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA",
                "path_image":".wallet_matic.jpg",
                "red":"ERC-20",
            },

        "Tron":{
                "address":"THi2UTY8SrUYNrzqKek8U3pvLuEF5y4fDQ",
                "path_image":".wallet_tron.jpg",
                "red":"TRC-10",
            },
        "Bnb":{
                "address":"bnb1vhe8q5zf2fr6s0ga8dnm5nzaz9uapky6w2xcnr",
                "path_image":".wallet_bnb.jpg",
                "red":"BEP-20",
            },
     "Solana":{
                "address":"6jsNmgn4ad9D7LzNxaabvjZ1WsBGMDYFHiDCESCHCoSv",
                "path_image":".wallet_solana.jpg",
                "red":"",
            },
            }

}


class InfoProyect(ft.Container):
    """INFO PROYECT READ TEXT"""
    def __init__(self,data='Erase this test'):
        super().__init__()
        self.title=data

    def build(self):
        self.content=ft.Container(
                                ink=False,
                                bgcolor=ft.colors.BLACK45,
                                padding= ft.padding.all(8),
                                margin = ft.margin.all(0),
                                alignment=ft.alignment.top_center,
                                border_radius= ft.border_radius.all(36),
                                border=ft.border.all(2, ft.colors.BLACK),
                                width=360,
                                height=590,
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

                            content=ft.Column(
                                           controls = [
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
                                                                             ),),
                                                                ],),
                                           ]
                                           )
                        )

class CardPrice(ft.Container):
    """PRICE OF THE CARDS"""

    def __init__(self,card_color: bool=False,card_plan: int=1,card_price: int=1,card_type: str=""):
        super().__init__()

        self.card_color = card_color
        self.card_plan  = card_plan
        self.card_type  = card_type
        self.card_price = card_price
        self.gold_color = ft.colors.YELLOW_ACCENT_400 if self.card_color else ft.colors.BLUE_900

        if self.card_plan == 1: self.buy_card = [ True, False, False, False, False ]
        if self.card_plan == 2: self.buy_card = [ True, True,  False, False, False ]
        if self.card_plan == 3: self.buy_card = [ True, True,  True,  True,  True  ]

    def build(self):
        self.content=ft.Container(
                                expand=True,
                                ink=False,
                                bgcolor=ft.colors.BLACK45,
                                padding= ft.padding.all(8),
                                margin = ft.margin.all(8),
                                alignment=ft.alignment.center,
                                border_radius= ft.border_radius.all(30),
                                width=240,
                                height=360,
                                border=ft.border.all(6, ft.colors.BLACK45),
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
                                                                     ],
                                                        ),
                            content=ft.Column(
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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

class InfoPrices(ft.Container):

    def __init__(self,data='Erase this test'):
        super().__init__()
        self.title=data

    def build(self):
        self.content=ft.Container(
                                # expand   = True,
                                ink      = False,
                                bgcolor  = ft.colors.BLACK26,
                                padding  = ft.padding.only(left=8,right=8,bottom=1,top=1 ),
                                margin   = ft.margin.all(0),
                                alignment= ft.alignment.center,
                                border_radius= ft.border_radius.all(36),
                                border = ft.border.all(2, ft.colors.BLACK),

                            content = ft.Row(
                                           controls = [
                                           CardPrice(card_plan=1, card_price=110 ,card_type="Standar"),
                                           CardPrice(card_plan=3 ,card_price=200 ,card_type="Pro" ,card_color=True),
                                           CardPrice(card_plan=2, card_price=160 ,card_type="Teams"),
                                           ]
                                           )
                        )

class WalletDirection(ft.Container):
    token_crypto = "0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA"

    def __init__(self,data='Erase this test'):
        super().__init__()
        self.title=data

    def build(self):
        self.alert_dialog = ft.Container(
                                visible       = False,
                                # height        = 40,
                                width         = 110,
                                bgcolor       = 'red',
                                # rotate=1.8,
                                # offset        = (0,-1.5),
                                alignment     = ft.alignment.center,
                                border_radius = ft.border_radius.all(16),
                            content = ft.Text(
                                                value = 'Done',
                                                )
                                )
        self.box_wallet_addres = ft.Container(
                                    bgcolor  =ft.colors.BLACK26,
                                    padding  = ft.padding.only(left=12, top=24, right=8, bottom=8),
                                    margin   = ft.margin.all(8),
                                    width    = 450,
                                    border_radius= ft.border_radius.all(24),
                                    content=ft.Column(
                                                      run_spacing=8,
                                                      spacing =8,

                                                      controls=[
                                                      ft.Row(
                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                            vertical_alignment=ft.CrossAxisAlignment.START,          # vertical       START,CENTER END

                                                            controls=[
                                                                    ft.Text(value="ERC-20 Matic",size=24, weight = ft.FontWeight.BOLD),

                                                                    self.alert_dialog,
                                                                    ]
                                                                    ,
                                                             ),

                                                      ft.Row(
                                                             run_spacing=0,
                                                             spacing    =4,
                                                             controls=[
                                                             ft.ElevatedButton(text="Copy",elevation=12,bgcolor=ft.colors.RED_800,on_click=lambda _:self.copy_clipboad()),
                                                             ft.TextButton(
                                                                      text="0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA",
                                                                      width=360,
                                                                      height=40
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

                        ),)#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
        self.image_box = ft.Image(
                    src               = "/home/mjay/Desktop/testing_create_package/flet_box/assets/.wallet_matic.jpg",
                    fit               = ft.ImageFit.COVER,
                    border_radius   = ft.border_radius.all(30),
                    )



        self.content=ft.Container(
                            bgcolor      = ft.colors.BLACK45,
                            padding      = ft.padding.all(0),
                            margin       = ft.margin.all(0),
                            alignment    = ft.alignment.center,
                            border_radius= ft.border_radius.all(30),
                            border       = ft.border.all(2, ft.colors.BLACK),
                            image_src = f"/home/mjay/Desktop/testing_create_package/flet_box/assets/.cripto.webp",
                            image_opacity=0.05,
                            image_fit='COVER',
                            expand=True,
                            content=ft.Row(
                                       controls=[

                                            ft.Container(
                                                        ink=False,
                                                        bgcolor  = ft.colors.BLACK45,
                                                        padding  = ft.padding.all(8),
                                                        margin   = ft.margin.all(4),
                                                        alignment= ft.alignment.center,
                                                        width    = 190,
                                                        height   = 190,
                                                        border_radius= ft.border_radius.all(30),
                                                        shadow = ft.BoxShadow(
                                                                   spread_radius=0,
                                                                   blur_radius=18,
                                                                   color=ft.colors.with_opacity(0.8,ft.colors.BLACK),
                                                                   offset=ft.Offset(0, 0),
                                                                   blur_style=ft.ShadowBlurStyle.OUTER,
                                                             ),
                                                        content=self.image_box,
                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                            ft.Container(
                                                        ink=False,
                                                        padding  = ft.padding.all(8),
                                                        margin   = ft.margin.all(8),
                                                        alignment= ft.alignment.center_left,
                                                        border_radius= ft.border_radius.all(30),
                                                        content=ft.Column(
                                                                          controls=[

                                                                          ft.ElevatedButton(text="Solana",elevation=12,bgcolor=ft.colors.RED_800    ,on_click=lambda _: self.edit_box_wallet_address(wallet_name="Solana",widget_box = self.box_wallet_addres)),
                                                                          ft.ElevatedButton(text="Matic" ,elevation=12,bgcolor=ft.colors.BLUE_800   ,on_click=lambda _: self.edit_box_wallet_address(wallet_name="Matic" ,widget_box = self.box_wallet_addres)),
                                                                          ft.ElevatedButton(text="Bnb"   ,elevation=12,bgcolor=ft.colors.CYAN_900   ,on_click=lambda _: self.edit_box_wallet_address(wallet_name="Bnb"   ,widget_box = self.box_wallet_addres)),
                                                                          ft.ElevatedButton(text="Tron"  ,elevation=12,bgcolor=ft.colors.PURPLE_900 ,on_click=lambda _: self.edit_box_wallet_address(wallet_name="Tron"  ,widget_box = self.box_wallet_addres)),

                                                                          ]
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            self.box_wallet_addres,
                                       ]
                                    )
                        )

    def copy_clipboad(self):
        pyperclip.copy(self.token_crypto)
        # print(self.token_crypto)

        self.alert_dialog.visible = True
        self.alert_dialog.content.value = f"Done:"
        self.alert_dialog.update()
        time.sleep(0.5)
        self.alert_dialog.visible = False
        self.alert_dialog.update()


    def edit_box_wallet_address(self,wallet_name,widget_box):
        self.tmp_data   = dictionary_contribution.get('crypto').get(wallet_name)
        self.address    = self.tmp_data.get('address')
        self.path_image = self.tmp_data.get('path_image')
        self.red        = self.tmp_data.get('red')

        self.token_crypto = self.address

        widget_box.content.controls[0].controls[0].value = f"{self.red} {wallet_name}"
        widget_box.content.controls[1].controls[1].text=self.address
        self.image_box.src = self.path_image


        widget_box.content.controls[1].controls[1].update()
        widget_box.content.controls[0].controls[0].update()
        self.image_box.update()

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
                    expand        = True,
                    blur=(60,60),
                on_hover= lambda _: self.validate_click(),
                content=ft.Row(
                                    controls=[
                                                ft.Container(
                                                             content=ft.Column(
                                                                    controls=[
                                                                            InfoPrices(),
                                                                            WalletDirection(),
                                                                    ] )
                                                             ),
                                                InfoProyect(),
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

        page.padding                   = 0
        page.spacing                   = 0
        page.add(SponsorPage())

    ft.app(
        target=main,
        assets_dir   = "assets"

        )