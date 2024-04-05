####################################################
import flet as ft
####################################################

class DoubleEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """
    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget=''):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute

        ################# CONTAINER STR
        if self.attribute_widget == "width ":
            self.attribute_widget_name_1 = 'Width'
            self.attribute_widget_name_2 = 'Height'

        if self.attribute_widget == "border ":
            self.attribute_widget_name_1 = 'Border'
            self.attribute_widget_name_2 = 'Color'
        if self.attribute_widget == "offset ":
            self.attribute_widget_name_1 = 'Offset'
            self.attribute_widget_name_2 = 'Offset'

        if self.attribute_widget == "blur ":
            self.attribute_widget_name_1 = 'X Blur'
            self.attribute_widget_name_2 = 'Y Blur'

        ################# CONTAINER STR
        if self.attribute_widget == "width":
            self.attribute_widget_name_1 = 'Width'
            self.attribute_widget_name_2 = 'Height'

        if self.attribute_widget == "border":
            self.attribute_widget_name_1 = 'Border'
            self.attribute_widget_name_2 = 'Color'
        if self.attribute_widget == "offset":
            self.attribute_widget_name_1 = 'Offset'
            self.attribute_widget_name_2 = 'Offset'

        if self.attribute_widget == "blur":
            self.attribute_widget_name_1 = 'X blur'
            self.attribute_widget_name_2 = 'Y blur'
    def build(self):

        Drop_DoubleEntry = ft.Container(
                                ##################### PROPERTY COLUMN
                                ink           = False,                                               # click effect ripple
                                bgcolor       = ft.colors.BLACK45,                                   # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),   # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                margin        = ft.margin.all(0),    # outside box                   # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment     = ft.alignment.center,                                 # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                border_radius = ft.border_radius.all(16),                            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border        = ft.border.all(2, ft.colors.BLACK),                   # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                width         = 165,
                                height        = 80,
                                content=ft.Column(
                                            ##################### PROPERTY BOX
                                            wrap=True,                                               # justify in all screen
                                            ##################### WIDGETS
                                            controls=[
                                                    ft.Container( ##################### Text label
                                                        ##################### PROPERTY
                                                        ink           = False,                                                # click effect ripple
                                                        bgcolor       = "#0e0f11",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                        padding       = ft.padding.only(left=12, top=0, right=12, bottom=0),  # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                        alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                        border_radius = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                        height        = 20,
                                                        ##################### WIDGETS
                                                        content = ft.Text(
                                                                    ##################### PROPERTY
                                                                    value       = 'Width - Height' if self.attribute_widget == "width " else self.attribute_widget.capitalize().replace('_',' '), # content = ft.Text(value="Compound button", size=12,),
                                                                    font_family = "Consolas", #"Consolas ,RobotoSlab
                                                        ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                    ft.Container(
                                                        ##################### PROPERTY
                                                        ink           = False,                                          # click effect ripple
                                                        padding       = ft.padding.all(2),                              # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                        alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                        border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                        border        = ft.border.all(2, ft.colors.BLACK12),            # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                        width         = 154,
                                                        height        = 36,
                                                        tooltip       = 'Double Entry',
                                                        ##################### EFFECTS
                                                        gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12, ft.colors.BLACK38 , ft.colors.BLACK54],),
                                                        ##################### WIDGETS
                                                        content=ft.Row(
                                                                    ##################### PROPERTY BOX
                                                                    ##################### WIDGETS
                                                                    controls=[
                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                                          # click effect ripple
                                                                                            width         = 68,
                                                                                            border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            content = ft.TextField(
                                                                                                            hint_text = self.attribute_widget_name_1,
                                                                                                            border    = ft.InputBorder.NONE,                # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                            bgcolor   = 'dark',                             # inside box
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                            #======================= EVENTS ===========================
                                                                                                        on_change = lambda x:self.modify_widget_attributes( config_widget = self.attribute_widget ,
                                                                                                                                                                    value = Drop_DoubleEntry),
                                                                                                                                                           # value = Drop_DoubleEntry.content.value),
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
                                                                                            border_radius = ft.border_radius.all(30),                         # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            ink           = False,                                            # click effect ripple
                                                                                            width         = 68,
                                                                                            content = ft.TextField(
                                                                                                            hint_text = self.attribute_widget_name_2,
                                                                                                            border    = ft.InputBorder.NONE,                  # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                            bgcolor   = 'dark',                               # inside box
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                            ##################### EVENTS #####################
                                                                                                         on_change= lambda x:self.modify_widget_attributes( config_widget = self.attribute_widget ,
                                                                                                                                                                    value = Drop_DoubleEntry),
                                                                                                        # on_change = lambda x:print('Pressed [< Write inside > ]'),
                                                                                                        # on_submit = lambda x:print('Pressed [< Enter > ]'),
                                                                                                        # on_focus  = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                        # on_blur   = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                            ),
                                                                                            ##################### EVENTS
                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
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

        return Drop_DoubleEntry

    def modify_widget_attributes(self,config_widget,value,):
        """
    NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_DoubleEntry),

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
        if  config_widget == "width" or config_widget == "height":
            self.widget.width   = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            self.widget.height  = value.content.controls[1].content.controls[1].content.value # <=== Atribute 1 ['height']

        if  config_widget == "blur":
            self.widget.blur    =  ft.Blur(
                                            int(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0,
                                            int(value.content.controls[1].content.controls[1].content.value) if value.content.controls[1].content.controls[1].content.value else 0,
                                            ft.BlurTileMode.MIRROR,
                                            )# <=== Atribute 0 ['width']
        if  config_widget == "border":
            self.widget.border = ft.border.all(
                                                value.content.controls[1].content.controls[0].content.value ,
                                                value.content.controls[1].content.controls[1].content.value ,
                                                ) # <=== Atribute 0 ['width']
        if  config_widget == "offset":
            self.widget.offset =(
                                 value.content.controls[1].content.controls[0].content.value ,
                                 value.content.controls[1].content.controls[1].content.value ,
                                 ) # <=== Atribute 0 ['width']
        # print(self.widget.uid)
        self.widget.update()

######## Double_Widget = DoubleEntry(),# <======= Comma