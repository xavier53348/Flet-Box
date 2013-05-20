####################################################
import flet as ft
####################################################

class BoolEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = BoolEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """
    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute
        self.id_name_widget_dict = id_name_widget_dict
        # will change name of entry points

    def build(self):
        Drop_BoolEntry =  ft.Container(
                    ##################### PROPERTY COLUMN
                    ink           = False,                                                # click effect ripple
                    bgcolor       = ft.colors.BLACK45,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin        = ft.margin.all(0),    # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    border_radius = ft.border_radius.all(16),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    border        = ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    width         = 165,
                    height        = 80,
                    ##################### WIDGETS
                    content=ft.Column(
                                wrap=True,                                          # justify in all screen
                                ##################### WIDGETS
                                controls=[
                                        ft.Container( ##################### Text label
                                            ink           = False,                                               # click effect ripple
                                            bgcolor       = "#0e0f11",                                           # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                            padding       = ft.padding.only(left=12, top=0, right=12, bottom=0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                            alignment     = ft.alignment.center,                                 # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                            border_radius = ft.border_radius.all(30),                            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                            height        = 20,
                                            content = ft.Text(
                                                        ##################### PROPERTY
                                                        value       = self.attribute_widget.capitalize().replace("_"," "), # content = ft.Text(value="Compound button", size=12,),
                                                        font_family = "Consolas", #"Consolas ,RobotoSlab
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                        ft.Container( ##################### Container Bool
                                                ##################### PROPERTY
                                                ink           = False,                                           # click effect ripple
                                                bgcolor       = ft.colors.BLACK38,                               # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding       = ft.padding.all(2),    # inside box               # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment     = ft.alignment.center,                             # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border        = ft.border.all(1, ft.colors.BLACK38),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                width         = 152,
                                                height        = 36,
                                                ##################### WIDGETS
                                                content=ft.Row(
                                                                ##################### PROPERTY BOX
                                                                controls=[
                                                                           ft.Container(
                                                                                    ##################### PROPERTY
                                                                                    ink           = False,                                              # click effect ripple
                                                                                    bgcolor       = ft.colors.BLACK87,                                  # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                    padding       = ft.padding.only(left=2, top=0, right=8, bottom=0),  # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                    alignment     = ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                    border_radius = ft.border_radius.all(30),                           # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                    border        = ft.border.all(1, ft.colors.BLACK38),                # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                    width         = 150,
                                                                                    height        = 36,
                                                                                    content=ft.Row(
                                                                                                    ##################### PROPERTY BOX
                                                                                                    spacing=6,                                          # space widget left right
                                                                                                    controls=[
                                                                                                                ft.Container(
                                                                                                                            ##################### PROPERTY
                                                                                                                            ink           = False,                               # click effect ripple
                                                                                                                            width         = 88,
                                                                                                                            height        = 30,
                                                                                                                            border_radius = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                                            content = ft.TextField(
                                                                                                                                            disabled  = True,
                                                                                                                                            hint_text = self.attribute_widget,
                                                                                                                                            border    = ft.InputBorder.NONE,     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                                                            bgcolor   = 'dark',                  # inside box
                                                                                                                                            color     = 'YELLOW',
                                                                                                                                            text_size = 15,
                                                                                                                                            #======================= EVENTS ===========================
                                                                                                                                        # on_change = lambda x:print('Pressed [< Write inside > ]'),
                                                                                                                                        # on_submit = lambda x:print('Pressed [< Enter > ]'),
                                                                                                                                        # on_focus  = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                                                        # on_blur   = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                                                            ),
                                                                                                                            ##################### EVENTS
                                                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                                                                ft.Container(
                                                                                                                            ##################### PROPERTY
                                                                                                                            ink    = False,                                     # click effect ripple
                                                                                                                            width  = 42,
                                                                                                                            height = 30,
                                                                                                                            content = ft.CupertinoSwitch(
                                                                                                                                    value        = True if self.attribute_widget == "visible " or  self.attribute_widget == "visible" else False,
                                                                                                                                    track_color  = 'Black',
                                                                                                                                    active_color = 'yellow',
                                                                                                                                    on_change    = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_BoolEntry),
                                                                                                                    ),
                                                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                                                             ],),
                                                                        ##################### EVENTS
                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                       )#<=== NOTE COMA,
                                                                     ],),
                                            ##################### EVENTS
                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                       )#<=== NOTE COMA,
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

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
        # self.widget.content.value = value if config_widget  == "value" else None
        # will modify attributes of the widget class in real time

        # use
        # self.widget.expand <=========== CONTAINER
        # self.widget.cotntent.expand <=========== CONTAINER.content

        ############################################################################### ONLY FOR CONTAINER
        # print(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "expand ":
            self.widget.expand = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "ink ":
            self.widget.ink =    bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "visible ":
            self.widget.visible =bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']

        ############################################################################### CONTAINER.content = WIDGET
        if  config_widget   == "expand":
            self.widget.expand = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "ink":
            self.widget.ink =    bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "visible":
            self.widget.visible =bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "scroll":
            self.widget.scroll = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "wrap":
            self.widget.wrap =   bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "tight":
            self.widget.tight =  bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "multiline":
            self.widget.multiline = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['multiline']
        if  config_widget   == "disabled":
            self.widget.disabled  = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['disabled']
        if  config_widget   == "read_only":
            self.widget.read_only = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['read_only']
        if  config_widget   == "password":
            self.widget.password  = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "filled":
            self.widget.filled =    bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "adaptive":
            self.widget.adaptive =  bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "tristate":
            self.widget.tristate =  bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "autofocus":
            self.widget.autofocus = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "horizontal":
            self.widget.horizontal = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "can_reveal_password":
            self.widget.can_reveal_password = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "capitalization":
            self.widget.capitalization = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']
        if  config_widget   == "gapless_playback":
            self.widget.gapless_playback = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value) # <=== Atribute 0 ['width']

        # print(self.widget.uid)
        # print(data_usage)
        self.widget.update()

######## Double_Widget = BoolEntry(),# <======= Comma