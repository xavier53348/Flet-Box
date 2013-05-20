import flet as ft

class BoolEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = BoolEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget=''):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute

        # will change name of entry points

    def build(self):
        Drop_BoolEntry = ft.Container(
                                ##################### PROPERTY
                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                # expand=True,
                                ink=False,                                                # click effect ripple
                                bgcolor=ft.colors.BLACK87,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
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
                                                                        # bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                        width=90,
                                                                        height=30,
                                                                        border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                        content=ft.TextField(
                                                                                        disabled=True,
                                                                                        hint_text=self.attribute_widget,
                                                                                        border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                        bgcolor='dark',                                 # inside box
                                                                                        color='YELLOW',
                                                                                        text_size=15,
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
                                                                        # bgcolor="Blue",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                        # alignment=ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                        width=45,
                                                                        height=30,
                                                                        # border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                        ##################### EVENTS
                                                                        content= ft.CupertinoSwitch(
                                                                                label="Cupertino Switch",
                                                                                value=False,
                                                                                # thumb_color=ft.colors.BLUE,
                                                                                track_color='Red',
                                                                                active_color ='yellow',
                                                                                on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_BoolEntry),
                                                                ),
                                                                        # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                         ],),

                                ##################### EVENTS
                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                    )#<=== NOTE COMA,
        return Drop_BoolEntry

    def modify_widget_attributes(self,config_widget,value,):
        """
    NOTE:

    Will modify all attrib inside the widget that we selected

    on_change= lambda x:self.modify_widget_attributes(config_widget =self.config_widget ,value = Drop_BoolEntry),

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

        # use
        # self.widget.expand <=========== CONTAINER
        # self.widget.cotntent.expand <=========== CONTAINER.content

        ################ CONTAINER STR

        if  config_widget   == "expand":
            self.widget.expand = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "ink":
            self.widget.ink =    bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "visible":
            self.widget.visible =    bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']

        ################################################################################ CONTAINER.content = WIDGET

        if  config_widget   == "scroll":
            self.widget.content.scroll = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "wrap":
            self.widget.content.wrap =   bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "tight":
            self.widget.content.tight =  bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "multiline":
            self.widget.content.multiline = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['multiline']
        if  config_widget   == "disabled":
            self.widget.content.disabled  = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['disabled']
        if  config_widget   == "read_only":
            self.widget.content.read_only = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['read_only']
        if  config_widget   == "password":
            self.widget.content.password  = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "filled":
            self.widget.content.filled = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "adaptive":
            self.widget.content.adaptive = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "tristate":
            self.widget.content.tristate = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "autofocus":
            self.widget.content.autofocus = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "horizontal":
            self.widget.content.horizontal = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "can_reveal_password":
            self.widget.content.can_reveal_password = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "capitalization":
            self.widget.content.capitalization = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "gapless_playback":
            self.widget.content.gapless_playback = bool(value.content.controls[1].content.value) # <=== Atribute 0 ['width']

        # print(self.widget.uid)
        self.widget.update()

######## Double_Widget = BoolEntry(),# <======= Comma