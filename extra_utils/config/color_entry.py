import flet as ft

class ColorEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget=''):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute

    def build(self):
        ColorEntry = ft.Container(
                            ##################### PROPERTY COLUMN
                            ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                            # expand=True,
                            ink=False,                                                      # click effect ripple
                            bgcolor=ft.colors.BLACK45,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                            padding= ft.padding.only(left=4, top=4, right=4, bottom=4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                            margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                            alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                            border_radius= ft.border_radius.all(16),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                            border=ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                            # ===================
                            # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                            # image_opacity=0.1,
                            # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                            # ===================
                            width=165,
                            height=80,
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
                                                padding= ft.padding.only(left=8, top=0, right=8, bottom=0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
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
                                                            value             = 'width - height' if self.attribute_widget == 'width' else self.attribute_widget.capitalize(), # content = ft.Text(value="Compound button", size=12,),
                                                            # tooltip         = 'ElevatedButton',
                                                            # text_align        = ft.TextAlign.CENTER,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                            # style           = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE ), # OVERLINE,
                                                            # weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_630, W_800,W_900
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
                                                    # bgcolor="#44CCCC00",                                      # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                    padding= ft.padding.only(left=2, top=0, right=8, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                    alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                    border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border=ft.border.all(1, ft.colors.BLACK38),               # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    width=152,
                                                    height=36,
                                                    # tooltip='Container',
                                                    ##################### EFFECTS
                                                    gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12, ft.colors.BLACK38 , ft.colors.BLACK54],),
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
                                                                                                            hint_text=self.attribute_widget,
                                                                                                            border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                            bgcolor='dark',                                 # inside box
                                                                                                            color='YELLOW',
                                                                                                            text_size=15,
                                                                                                            #======================= EVENTS ===========================
                                                                                                        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = ColorEntry),
                                                                                                        # on_change= lambda x:print('Pressed [< Write inside > ]'),
                                                                                                        on_submit= lambda x:self.modify_right_container_attributes(data=self.attribute_widget,value = ColorEntry),
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
                                                                                            bgcolor=ft.colors.BLUE_900,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                            # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                            width=50.5,
                                                                                            height=30,
                                                                                            border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            ##################### EVENTS
                                                                                            on_click= lambda x:self.modify_right_container_attributes(data=self.attribute_widget,value = ColorEntry),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                            # on_click=lambda _:print(_.__dict__),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                             ],),

                                                    ##################### EVENTS
                                                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                    )#<=== NOTE COMA,
                                         ],
                            ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                            ##################### EVENTS
                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA










        return ColorEntry

    def modify_right_container_attributes(self,data,value):
        """will activate main widget color when press right Conteiner color box"""
        # print(data)
        ################ CONTAINER STR
        if  data   == "bgcolor":
            self.widget.bgcolor        = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "focused_bgcolor":
            self.widget.focused_bgcolor= value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']

        if  data   == "shadow_color":
            self.widget.shadow_color = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']


        ################################################################################ CONTAINER.content = WIDGET

        if  data   == "color":
            self.widget.content.color        = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "fill_color":
            self.widget.content.fill_color   = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "icon_color":
            self.widget.content.icon_color   = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "check_color":
            self.widget.content.check_color  = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "focused_border_color":
            self.widget.content.focused_border_color = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "border_color":
            self.widget.content.border_color   = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']


        ####################
        self.widget.update()


    def modify_widget_attributes(self,config_widget,value,):
        """
        NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = ColorEntry),

        EXEMPLE:

            width:      value
            height:     value
            bgcolor:    value
            value:      value
        """
        # self.widget.content.value = value if config_widget  == "value" else None
        # will modify attributes of the widget class in real time
        # change circle right color in streaming

        if  self.attribute_widget   == "bgcolor":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "focused_bgcolor":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "border_color":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "focused_border_color":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "color":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "shadow_color":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "icon_color":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "check_color":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "fill_color":
            value.content.controls[1].content.controls[1].bgcolor=value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()


        # print(self.widget.uid)
        # self.ColorEntry.content.update()
        ####################
        self.widget.update()

######## Double_Widget = DoubleEntry(),# <======= Comma