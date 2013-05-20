import flet as ft

class FourEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = FourEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget=''):
        super().__init__()
        """ Is neccesary make a filter that will contain name of the widget to use"""
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute

        # will change name of entry points
        ##################### ONLY FOR CONTAINER
        if  self.attribute_widget == "padding " or self.attribute_widget == "margin ":
            self.attribute_widget_name_1 = 'Left'
            self.attribute_widget_name_2 = 'Top'
            self.attribute_widget_name_3 = 'Right'
            self.attribute_widget_name_4 = 'Bottom'

        if  self.attribute_widget == "border_radius ":
            self.attribute_widget_name_1 = '⌜ BL'
            self.attribute_widget_name_2 = '  BR ⌝'
            self.attribute_widget_name_3 = '⌞ TL'
            self.attribute_widget_name_4 = '  TR ⌟'
        #####################
        if  self.attribute_widget == "padding" or self.attribute_widget == "margin":
            self.attribute_widget_name_1 = 'Left'
            self.attribute_widget_name_2 = 'Top'
            self.attribute_widget_name_3 = 'Right'
            self.attribute_widget_name_4 = 'Bottom'

        if  self.attribute_widget == "border_radius":
            self.attribute_widget_name_1 = '⌜ BL'
            self.attribute_widget_name_2 = '  BR ⌝'
            self.attribute_widget_name_3 = '⌞ TL'
            self.attribute_widget_name_4 = '  TR ⌟'

    def build(self):
        packet_data = ft.Container(
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
                            width=162,
                            height=128,
                            # height=128,
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
                                                height=20,
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
                                                            value             = self.attribute_widget.capitalize(), # content = ft.Text(value="Compound button", size=12,),
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
                                                                                        height=30,
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
                                                                                        height=30,
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
                                                                         ],),
                                                                ),#<=== NOTE COMA,
                                            ],
                                ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                        )#<=== NOTE COMA


        return packet_data

    def modify_widget_attributes(self,config_widget,value,):
        """
    NOTE:

    Will modify all attrib inside the widget that we selected

    on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_FourEntry),

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
        ########################################## ONLY FOR CONTAINER
        if  config_widget   == "padding ":
            """ all values in Box Container """

            self.left   = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            self.top    = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            self.right  = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            self.bottom = value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.padding = ft.padding.only(
                                                    left   = self.left,
                                                    top    = self.top,
                                                    right  = self.right,
                                                    bottom = self.bottom
                                                  )
        if  config_widget   == "margin ":
            """ all values in Box Container """

            self.left   = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            self.top    = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            self.right  = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            self.bottom = value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.margin = ft.margin.only(
                                                    left   = self.left,
                                                    top    = self.top,
                                                    right  = self.right,
                                                    bottom = self.bottom
                                                )
        if  config_widget   == "border_radius ":
            """ all values in Box Container """

            self.top_left    = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            self.top_right   = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            self.bottom_left = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            self.bottom_right= value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.border_radius = ft.border_radius.only(
                                                    top_left   = self.top_left,
                                                    top_right    = self.top_right,
                                                    bottom_left  = self.bottom_left,
                                                    bottom_right = self.bottom_right
                                                )
        ########################################## ONLY FOR CONTENT
        if  config_widget   == "padding":
            """ all values in Box Container """

            self.left   = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            self.top    = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            self.right  = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            self.bottom = value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.content.padding = ft.padding.only(
                                                    left   = self.left,
                                                    top    = self.top,
                                                    right  = self.right,
                                                    bottom = self.bottom
                                                  )
        if  config_widget   == "margin":
            """ all values in Box Container """

            self.left   = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            self.top    = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            self.right  = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            self.bottom = value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.content.margin = ft.margin.only(
                                                    left   = self.left,
                                                    top    = self.top,
                                                    right  = self.right,
                                                    bottom = self.bottom
                                                )
        if  config_widget   == "border_radius":
            """ all values in Box Container """

            self.top_left    = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            self.top_right   = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            self.bottom_left = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            self.bottom_right= value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.content.border_radius = ft.border_radius.only(
                                                    top_left   = self.top_left,
                                                    top_right    = self.top_right,
                                                    bottom_left  = self.bottom_left,
                                                    bottom_right = self.bottom_right
                                                )
        # print(self.widget)

        # print(self.widget.uid)
        self.widget.update()

######## Double_Widget = FourEntry(),# <======= Comma