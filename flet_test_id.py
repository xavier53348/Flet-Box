import flet as ft

class Row_Container(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_Row_Container=ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    expand=True,
                    ink=False,                                                      # click effect ripple
                    bgcolor="#3f449a",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(8),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
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
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Column(
                        ##################### PROPERTY BOX
                        # expand=True,
                        # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                        # scroll=True,                                              # center widget
                        # tight=True,
                        ##################### ADAPT TO SCREEN
                        wrap=True,                                                  # justify in all screen
                        # spacing=8,                                                # space widget left right
                        # run_spacing=8,                                            # space widget up down
                        ##################### WIDGETS
                        controls=[
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=152,
                                                height=36,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
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
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,

                                                                                        content=ft.TextField(
                                                                                                        hint_text="height",
                                                                                                        border=ft.InputBorder.NONE,              # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                               # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                         ],),

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=152,
                                                height=36,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
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
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=146,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="Color",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                                         ],),

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#44CCCC00",                                      # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.only(left=2, top=0, right=8, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),               # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=152,
                                                height=36,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
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
                                                                spacing=4.5,                                                # space widget left right
                                                                # run_spacing=8,                                            # space widget up down
                                                                ##################### WIDGETS
                                                                controls=[
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=90,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="Color",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="Blue",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=50.5,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        ##################### EVENTS
                                                                                        on_click=lambda _:print(_.__dict__),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                         ],),

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.only(left=2, top=0, right=8, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=152,
                                                height=36,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
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
                                                                spacing=0,                                                # space widget left right
                                                                # run_spacing=8,                                            # space widget up down
                                                                ##################### WIDGETS
                                                                controls=[
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=90,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="Color",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        # bgcolor="Blue",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=45,
                                                                                        height=30,
                                                                                        # border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        ##################### EVENTS
                                                                                        content= ft.CupertinoSwitch(
                                                                                                label="Cupertino Switch",
                                                                                                value=True,
                                                                                ),
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                         ],),

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=304,
                                                height=36,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
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
                                                                spacing=8.7,                                                # space widget left right
                                                                # run_spacing=8,                                            # space widget up down
                                                                ##################### WIDGETS
                                                                controls=[
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                         ],),

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=304,
                                                height=36,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
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
                                                                spacing=8.7,                                                # space widget left right
                                                                # run_spacing=8,                                            # space widget up down
                                                                ##################### WIDGETS
                                                                controls=[
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor=ft.colors.BLACK38,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=222,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.Slider(
                                                                                                        # hint_text="width",
                                                                                                        # border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        # bgcolor='dark',                                 # inside box
                                                                                                        # color='YELLOW',
                                                                                                        # text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    # on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        read_only=True,
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                         ],),

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#3e4046",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(2, '#646871'),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=152,
                                                height=35,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
                                                content=ft.Dropdown(
                                                                    # label='width',
                                                                    hint_text='Colores',
                                                                    width=120,
                                                                    # border_width=1,
                                                                    # dense=120,
                                                                    content_padding=ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                    alignment=ft.alignment.center_left,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                    border_radius= ft.border_radius.all(15),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                    # autofocus=True,
                                                                    border=ft.InputBorder.NONE,
                                                                    options=[
                                                                        ft.dropdown.Option("Red"),
                                                                        ft.dropdown.Option("Green"),
                                                                        ft.dropdown.Option("Blue"),
                                                                    ],
                                                                    ##################### EVENTS
                                                                    # on_change=lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                                    on_change=lambda _:print(_.__dict__.get('data')),
                                                                    # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width=304,
                                                height=36,
                                                # tooltip='Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
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
                                                                spacing=8.7,                                                # space widget left right
                                                                # run_spacing=8,                                            # space widget up down
                                                                ##################### WIDGETS
                                                                controls=[
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                      # click effect ripple
                                                                                        bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text="width",
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                         ],),

                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA,
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))

                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA


        return Drop_Row_Container
######## RowContainer = Row_Container(),# <======= Comma

def main(page: ft.Page):
    ###################### CONFIGURATION
    # page.title = "Containers - clickable and not"
    # page.window_title_bar_hidden = True
    # page.window_frameless = True
    # page.window_focused=True
    # page.scroll=True
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
    page.window_width=600
    page.padding=8
    page.spacing=8
    page.expand=True
    ######################
    RowContainer = Row_Container()
    screen_1=ft.Container(
                    ##################### PROPERTY
                    expand=True,
                    ink=True,                                           # click effect ripple
                    bgcolor="#44CCCC00",                                # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(8),    # inside box         # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(8),     # outside box        # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                      # top_left, top_center, top_right, center_left, center, center_right, bottom_left, bottom_center, bottom_right.    posicionamiento adentro widget
                    # border_radius= ft.border_radius.all(30),          # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border=ft.border.all(3, ft.colors.BLUE),          # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # image_src=f"/icons/icon-512.png",
                    # width=150,
                    # height=150,
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=RowContainer,
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                        # on_hover=print('on click over'), on_long_press=print('long press'),
                )


    page.add(screen_1)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)