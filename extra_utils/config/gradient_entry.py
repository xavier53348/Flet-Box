import flet as ft

class GradientEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = GradientEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget=''):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute

        ################# CONTAINER STR
        if self.attribute_widget == "gradient":
            """top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right"""
            self.options_tmp_1 = [
                                    ft.dropdown.Option(" Linear "),
                                    ft.dropdown.Option(" Radial "),
                                    ]
            self.options_tmp_2 = [
                                    ft.dropdown.Option(" Linear "),
                                    ft.dropdown.Option(" Radial "),
                                    ]
            self.attribute_widget_name_1 = 'Color'
            self.attribute_widget_name_2 = 'Color'
            self.attribute_widget_name_3 = 'Color'
            self.attribute_widget_name_4 = 'Color'

    def build(self):

        Drop_GradientEntry = ft.Container(
                            ##################### PROPERTY COLUMN
                            ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                            # expand=True,
                            ink=False,                                                      # click effect ripple
                            bgcolor=ft.colors.BLACK45,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                            padding= ft.padding.all(4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                            margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                            alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                            border_radius= ft.border_radius.all(16),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                            border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                            # ===================
                            # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                            # image_opacity=0.1,
                            # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                            # ===================
                            # rotate=-29,
                            width=360,
                            height=150,
                            # height=128,
                            # tooltip='Container',
                            ##################### EFFECTS
                            # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                            # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                            ##################### WIDGETS
                            content=ft.Column(
                                        ##################### PROPERTY BOX
                                        # expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                        # horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
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
                                                            ink=False,                                                # click effect ripple
                                                            bgcolor=ft.colors.BLACK38,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                            padding= ft.padding.all(4),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                            margin = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                            alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                            border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                            # border=ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                            # ===================
                                                            # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                            # image_opacity=0.1,
                                                            # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                            # ===================
                                                            # width=150,
                                                            height=38,
                                                            # tooltip='Container',
                                                            ##################### EFFECTS
                                                            # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                            # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                            ##################### WIDGETS
                                                            content=ft.Row(
                                                                            ##################### PROPERTY BOX
                                                                            # expand=True,
                                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
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
                                                                                        # ft.ElevatedButton("press row",tooltip='buttom'),
                                                                                        # ft.ElevatedButton("press row",tooltip='buttom'),
                                                                                        ft.Container( ##################### Text label
                                                                                                ##################### PROPERTY
                                                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                                # expand=True,
                                                                                                ink=False,                                                      # click effect ripple
                                                                                                bgcolor="#0e0f11",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                                padding= ft.padding.only(left=12, top=0, right=12, bottom=0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                                # margin = ft.margin.all(1),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                                border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                                # ===================
                                                                                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                                                # image_opacity=0.1,
                                                                                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                                                # ===================
                                                                                                # width=150,
                                                                                                height=35,
                                                                                                # tooltip='Container',
                                                                                                ##################### EFFECTS
                                                                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                                # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                                                ##################### WIDGETS
                                                                                                content=ft.Text(
                                                                                                            ##################### PROPERTY
                                                                                                            # key             = 'is our id',
                                                                                                            # expand          = True,
                                                                                                            # data            = 'value of the button',                                  # store data in the button
                                                                                                            value             = self.attribute_widget.capitalize().replace('_',' '), # content = ft.Text(value="Compound button", size=12,),
                                                                                                            # tooltip         = 'ElevatedButton',
                                                                                                            # text_align        = ft.TextAlign.CENTER,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                                                            # style           = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE ), # OVERLINE,
                                                                                                            # weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_680, W_800,W_900
                                                                                                            # italic          = True,
                                                                                                            font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                                                                            ##################### COLOR
                                                                                                            # color           = 'yellow',  # text color
                                                                                                            # bgcolor         = 'red',     # back color
                                                                                                            ##################### ATTRIB
                                                                                                            # visible         = False,
                                                                                                            # opacity         = 0.1,

                                                                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                                            ft.Container(
                                                                                                    ##################### PROPERTY
                                                                                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                                    # expand=True,
                                                                                                    ink=False,                                                # click effect ripple
                                                                                                    bgcolor="#3e4046",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                                    padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                                    alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                    border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                    border=ft.border.all(2, '#646871'),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                                    width=150,
                                                                                                    height=35,
                                                                                                    # tooltip='Container',
                                                                                                    ##################### EFFECTS
                                                                                                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                                    ##################### WIDGETS
                                                                                                    content=ft.Dropdown(
                                                                                                                        # label='width',
                                                                                                                        hint_text=" Linear",
                                                                                                                        width=140,
                                                                                                                        # border_width=1,
                                                                                                                        # dense=120,
                                                                                                                        content_padding=ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                                                        alignment=ft.alignment.center_left,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                                        border_radius= ft.border_radius.all(15),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                                                        # autofocus=True,
                                                                                                                        border=ft.InputBorder.NONE,

                                                                                                                        options=self.options_tmp_1,
                                                                                                                        ##################### EVENTS
                                                                                                                        # on_change=lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                                                                                        # on_change=lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data')),
                                                                                                                        # on_change=lambda _:print(_.__dict__.get('data')),
                                                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                                                                    ##################### EVENTS
                                                                                                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                        ),#<=== NOTE COMA,

                                                                                     ],),
                                                            ##################### EVENTS
                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                ),#<=== NOTE COMA


                                            ft.Container( ##################### First Dual Entry
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink           = False,                                                # click effect ripple
                                                bgcolor       = "#0e0f11",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                # bgcolor       = 'red',                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding       = ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border        = ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                # width       = 304,
                                                height        = 36,
                                                # tooltip     = 'Container',
                                                ##################### EFFECTS
                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                ##################### WIDGETS
                                                content=ft.Row(
                                                                ##################### PROPERTY BOX
                                                                # expand=True,
                                                                # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                # vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                # scroll = True,                                              # center widget
                                                                # tight  = True,
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
                                                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=35,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text=self.attribute_widget_name_1,
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
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
                                                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=35,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        # icon='home',
                                                                                                        hint_text=self.attribute_widget_name_2,
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
                                                                                                    # on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                            ft.Container(width=28),

                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                # click effect ripple
                                                                                        bgcolor="#3e4046",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                        alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                        border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        border=ft.border.all(2, '#646871'),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                        width=150,
                                                                                        height=35,
                                                                                        # tooltip='Container',
                                                                                        ##################### EFFECTS
                                                                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                        ##################### WIDGETS
                                                                                        content=ft.Dropdown(
                                                                                                            # label='width',
                                                                                                            hint_text=" Linear ",
                                                                                                            width=140,
                                                                                                            # border_width=1,
                                                                                                            # dense=120,
                                                                                                            content_padding=ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                                            alignment=ft.alignment.center_left,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                            border_radius= ft.border_radius.all(15),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                                            # autofocus=True,
                                                                                                            border=ft.InputBorder.NONE,

                                                                                                            options=self.options_tmp_2,
                                                                                                            ##################### EVENTS
                                                                                                            # on_change=lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                                                                            # on_change=lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data')),
                                                                                                            # on_change=lambda _:print(_.__dict__.get('data')),
                                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA,
                                                                         ],),
                                                                    ##################### EVENTS
                                                                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                    ),#<=== NOTE COMA,
                                            ft.Container( ##################### Secon Dual Entry
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="#0e0f11",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                # width=304,
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
                                                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                        content=ft.TextField(
                                                                                                        hint_text=self.attribute_widget_name_3,
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
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
                                                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                        width=68,
                                                                                        height=30,
                                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        content=ft.TextField(
                                                                                                        hint_text=self.attribute_widget_name_4,
                                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor='dark',                                 # inside box
                                                                                                        color='YELLOW',
                                                                                                        text_size=15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                    on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
                                                                                                    # on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                        ),
                                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                            ft.Container(width=28),
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                        # expand=True,
                                                                                        ink=False,                                                # click effect ripple
                                                                                        bgcolor="#3e4046",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                        alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                        border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        border=ft.border.all(2, '#646871'),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                        width=150,
                                                                                        height=35,
                                                                                        # tooltip='Container',
                                                                                        ##################### EFFECTS
                                                                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                        ##################### WIDGETS
                                                                                        content=ft.Dropdown(
                                                                                                            # label='width',
                                                                                                            hint_text=" Linear ",
                                                                                                            width=140,
                                                                                                            # border_width=1,
                                                                                                            # dense=120,
                                                                                                            content_padding=ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                                            alignment=ft.alignment.center_left,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                            border_radius= ft.border_radius.all(15),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                                            # autofocus=True,
                                                                                                            border=ft.InputBorder.NONE,

                                                                                                            options=[
                                                                                                                    ft.dropdown.Option(" Linear "),
                                                                                                                    ft.dropdown.Option(" Radial "),

                                                                                                            ],
                                                                                                            ##################### EVENTS
                                                                                                            # on_change=lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                                                                            # on_change=lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data')),
                                                                                                            # on_change=lambda _:print(_.__dict__.get('data')),
                                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                                                        ##################### EVENTS
                                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA,
                                                                         ],),
                                                                ),#<=== NOTE COMA,
                                            ],
                                ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                        )#<=== NOTE COMA
        return Drop_GradientEntry

    def modify_widget_attributes(self,config_widget,value,):
        """
    NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_GradientEntry),

    EXEMPLE:

        width:      value
        height:     value
        bgcolor:    value
        value:      value
        """
        # print(config_widget)
        # print(value)

        # self.widget.content.value = value if config_widget  == "value" else None
        # will modify attributes of the widget class in real time
        ################################# ONLY FOR CONTAINER

        if  config_widget == "width " or config_widget == "height ":
            self.widget.width   = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            self.widget.height  = value.content.controls[1].content.controls[1].content.value # <=== Atribute 1 ['height']

        if  config_widget == "blur ":
            self.widget.blur    =  ft.Blur(
                                            int(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0,
                                            int(value.content.controls[1].content.controls[1].content.value) if value.content.controls[1].content.controls[1].content.value else 0,
                                            ft.BlurTileMode.MIRROR,
                                            )# <=== Atribute 0 ['width']
        if  config_widget == "border ":
            self.widget.border = ft.border.all(
                                                value.content.controls[1].content.controls[0].content.value ,
                                                value.content.controls[1].content.controls[1].content.value ,
                                                ) # <=== Atribute 0 ['width']
        if  config_widget == "offset ":
            self.widget.offset =(
                                 value.content.controls[1].content.controls[0].content.value ,
                                 value.content.controls[1].content.controls[1].content.value ,
                                 ) # <=== Atribute 0 ['width']
        #################################
        if  config_widget == "width" or config_widget == "height":
            self.widget.content.width   = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            self.widget.content.height  = value.content.controls[1].content.controls[1].content.value # <=== Atribute 1 ['height']

        if  config_widget == "blur":
            self.widget.content.blur    =  ft.Blur(
                                            int(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0,
                                            int(value.content.controls[1].content.controls[1].content.value) if value.content.controls[1].content.controls[1].content.value else 0,
                                            ft.BlurTileMode.MIRROR,
                                            )# <=== Atribute 0 ['width']
        if  config_widget == "border":
            self.widget.content.border = ft.border.all(
                                                value.content.controls[1].content.controls[0].content.value ,
                                                value.content.controls[1].content.controls[1].content.value ,
                                                ) # <=== Atribute 0 ['width']
        if  config_widget == "offset":
            self.widget.content.offset =(
                                 value.content.controls[1].content.controls[0].content.value ,
                                 value.content.controls[1].content.controls[1].content.value ,
                                 ) # <=== Atribute 0 ['width']
        # print(self.widget.uid)
        self.widget.update()

######## Double_Widget = GradientEntry(),# <======= Comma