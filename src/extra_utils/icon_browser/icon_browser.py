# import logging
import os
# from itertools import islice

import flet as ft
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


class IconBrowser(ft.UserControl):
    """
    lite module to find icons by name
    """

    def __init__(self,blur_effect = False):
        super().__init__()

        # preparing list with all icons inside
        self.list_icons = self.preparing_list_icons()

        if blur_effect:
            self.blur = 20
        else:
            self.blur = None

    def build(self):

        self.Search_Gridwiew = ft.GridView(
                        ##################### PROPERTY GRIDVIEW
                        runs_count         =10,                                             # column's number
                        run_spacing        =5,                                            # space between widget
                        padding            =8,
                        spacing            =5,                                                # space widget left right
                        expand             =1,
                        child_aspect_ratio =1,                                   # scale of widget
                        # horizontal       =False,
                        max_extent         =150,                                         # lateral_size max
                        ##################### WIDGETS
                    controls=[
                                 ],
                        )

        self.Drop_IconBrowser=ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    expand=True,
                    ink=False,                                                      # click effect ripple
                    # bgcolor ="#3f449a",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding   = ft.padding.all(8),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment =ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_fit ='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    ##################### WIDGETS
                    # right  = 350,
                    # left   = 350,
                    # top    = 100,
                    # bottom = 100,

                    content   = ft.Column(
                        ##################### PROPERTY BOX
                        controls=[
                                    ft.Container( ##################### TEXT FIELD
                                                ##################### PROPERTY
                                                ink           =False,                                                      # click effect ripple
                                                padding       = ft.padding.all(4), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin        = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment     =ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                blur          =self.blur,
                                                height        =50,
                                                ##################### WIDGETS
                                                content=ft.TextField(
                                                                label=" Search Icon name",
                                                                border=ft.InputBorder.OUTLINE,              # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                bgcolor              =ft.colors.BLACK12,                               # inside box
                                                                focused_bgcolor      =ft.colors.BLACK12,                     # inside box after click
                                                                border_color         =ft.colors.TEAL,                           # border box
                                                                focused_border_color =ft.colors.TRANSPARENT,                 # border box after click
                                                                border_radius        =30,                              # corner
                                                                text_size=16,
                                                            on_submit = lambda _: self.search_icons(_),
                                                                ),
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container( ##################### GRID VIEW
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand      = True,
                                                ink             = False,                                                # click effect ripple
                                                bgcolor         = ft.colors.BLACK38,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding         = ft.padding.all(8),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin          = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment       = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius   = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border          = ft.border.all(0.8, ft.colors.TEAL),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                blur            = self.blur,
                                                height          = 500,
                                                ##################### WIDGETS
                                                content=self.Search_Gridwiew,
                                                #<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA


        return self.Drop_IconBrowser

    def preparing_list_icons(self):
        icons_list   = []
        list_started = False

        for key, value in vars(ft.icons).items():

            if key == "TEN_K":
                list_started = True
            if list_started:
                icons_list.append(value)

        return icons_list

    def search_icons(self,e):
        # print('hello',e.control.value)
        search_term = e.control.value
        self.Search_Gridwiew.controls =[]

        def run_upload_icons():
            for _ in self.list_icons:
                if _.startswith(search_term):
                    # print(_)
                    # yield _
                    self.Search_Gridwiew.controls.append(

                        ft.TextButton(
                                            content=ft.Container(
                                                # bgcolor=ft.color.BLACK,
                                                content=ft.Column(
                                                    [
                                                        ft.Icon(name=_, size=30),
                                                        ft.Text(
                                                            value=_,
                                                            size=12,
                                                            width=100,
                                                            no_wrap=True,
                                                            text_align="center",
                                                            # color=colors.ON_SURFACE_VARIANT,
                                                        ),
                                                    ],
                                                    spacing=5,
                                                    alignment="center",
                                                    horizontal_alignment="center",
                                                ),
                                                alignment=ft.alignment.center,
                                            ),
                                            # tooltip=f"{_}\nClick to copy to a clipboard",
                                            # on_click=copy_to_clipboard,
                                            # data=icon_key,
                                        )
                        )

        run_upload_icons()

        self.Drop_IconBrowser.update()

######## IconBrowser = IconBrowser(),# <======= Comma
# from flet import (
#     Column,
#     Container,
#     GridView,
#     Icon,
#     IconButton,
#     Page,
#     Row,
#     SnackBar,
#     Text,
#     TextButton,
#     TextField,
#     UserControl,
#     alignment,
#     colors,
#     icons,
# )

# # logging.basicConfig(level=logging.INFO)

# os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


# class IconBrowser(UserControl):
#     def __init__(self, expand=False, height=500):
#         super().__init__()
#         if expand:
#             self.expand = expand
#         else:
#             self.height = height

#     def build(self):
#         def batches(iterable, batch_size):
#             iterator = iter(iterable)
#             while batch := list(islice(iterator, batch_size)):
#                 yield batch

#         # fetch all icon constants from icons.py module
#         icons_list = []
#         list_started = False
#         for key, value in vars(icons).items():
#             if key == "TEN_K":
#                 list_started = True
#             if list_started:
#                 icons_list.append(value)

#         search_txt = TextField(
#             expand=1,
#             hint_text="Enter keyword and press search button",
#             autofocus=True,
#             on_submit=lambda e: display_icons(e.control.value),
#         )

#         def search_click(e):
#             display_icons(search_txt.value)

#         search_query = Row(
#             [search_txt, IconButton(icon=icons.SEARCH, on_click=search_click)]
#         )

#         search_results = GridView(
#             expand=1,
#             runs_count=10,
#             max_extent=150,
#             spacing=5,
#             run_spacing=5,
#             child_aspect_ratio=1,
#         )
#         status_bar = Text()

#         def copy_to_clipboard(e):
#             icon_key = e.control.data
#             print("Copy to clipboard:", icon_key)
#             self.page.set_clipboard(e.control.data)
#             self.page.show_snack_bar(SnackBar(Text(f"Copied {icon_key}"), open=True))

#         def search_icons(search_term: str):
#             for icon_name in icons_list:
#                 if search_term != "" and search_term in icon_name:
#                     yield icon_name

#         def display_icons(search_term: str):

#             # clean search results
#             search_query.disabled = True
#             self.update()

#             search_results.clean()

#             for batch in batches(search_icons(search_term.lower()), 200):
#                 for icon_name in batch:
#                     icon_key = f"icons.{icon_name.upper()}"
#                     search_results.controls.append(
#                         TextButton(
#                             content=Container(
#                                 # bgcolor=ft.color.BLACK,
#                                 content=Column(
#                                     [
#                                         Icon(name=icon_name, size=30),
#                                         Text(
#                                             value=f"{icon_name}",
#                                             size=12,
#                                             width=100,
#                                             no_wrap=True,
#                                             text_align="center",
#                                             color=colors.ON_SURFACE_VARIANT,
#                                         ),
#                                     ],
#                                     spacing=5,
#                                     alignment="center",
#                                     horizontal_alignment="center",
#                                 ),
#                                 alignment=alignment.center,
#                             ),
#                             tooltip=f"{icon_key}\nClick to copy to a clipboard",
#                             on_click=copy_to_clipboard,
#                             data=icon_key,
#                         )
#                     )
#                 status_bar.value = f"Icons found: {len(search_results.controls)}"
#                 self.update()

#             if len(search_results.controls) == 0:
#                 self.page.show_snack_bar(SnackBar(Text("No icons found"), open=True))
#             search_query.disabled = False
#             self.update()

#         return Column(
#             [
#                 search_query,
#                 search_results,
#                 status_bar,
#             ],
#             expand=True,
#         )

if __name__ == '__main__':
    def main(page: ft.Page):
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
        page.window_left               = 3
        page.window_top                = 3
        # page.window_center()
        ###################### SIZE
        # page.window_height           = 400
        # page.window_height             = 800
        page.window_height             = 400
        page.window_width              = 400
        # page.window_width            = 1200
        page.padding                   = 0
        page.spacing                   = 0
        # page.expand                    = True
        page.add(IconBrowser())


    ft.app(target=main)
