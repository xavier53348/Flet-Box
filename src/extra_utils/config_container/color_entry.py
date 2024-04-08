####################################################
import flet as ft
####################################################

class ColorEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute
        self.id_name_widget_dict = id_name_widget_dict

    def build(self):
        ColorEntry = ft.Container(
                            ##################### PROPERTY COLUMN
                            ink           = False,                                                       # click effect ripple
                            bgcolor       = ft.colors.BLACK45,                                           # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                            padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),           # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                            margin        = ft.margin.all(0),    # outside box                           # margin.only (left=8, top=8, right=8, bottom=8),
                            alignment     = ft.alignment.center,                                         # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                            border_radius = ft.border_radius.all(16),                                    # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                            border        = ft.border.all(2, ft.colors.BLACK),                           # ft.border.only(Left=8, top=8, right=8, bottom=8),
                            width         = 165,
                            height        = 80,
                            content = ft.Column(
                                        ##################### PROPERTY BOX
                                        wrap     = True,                                                 # justify in all screen
                                        controls = [
                                            ft.Container( ##################### Text label
                                                ink           = False,                                            # click effect ripple
                                                bgcolor       = "#0e0f11",                                        # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding       = ft.padding.only(left=8, top=0, right=8, bottom=0),# inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                alignment     = ft.alignment.center,                              # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(30),                         # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                height        = 20,
                                                content =ft.Text(
                                                            ##################### PROPERTY
                                                            value       = 'width - height' if self.attribute_widget == 'width' else self.attribute_widget.capitalize().replace("_"," "), # content = ft.Text(value="Compound button", size=12,),
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                            ft.Container(
                                                    ##################### PROPERTY
                                                    ink           = False,                                            # click effect ripple
                                                    padding       = ft.padding.only(left=2, top=0, right=8, bottom=0),# inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                    alignment     = ft.alignment.center,                              # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                    border_radius = ft.border_radius.all(30),                         # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border        = ft.border.all(1, ft.colors.BLACK38),              # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    width         = 152,
                                                    height        = 36,
                                                    ##################### EFFECTS
                                                    gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12, ft.colors.BLACK38 , ft.colors.BLACK54],),
                                                    ##################### WIDGETS
                                                    content = ft.Row(
                                                                    ##################### PROPERTY BOX
                                                                    spacing  = 4.5,                                                # space widget left right
                                                                    controls = [
                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                          # click effect ripple
                                                                                            bgcolor       = "#44CCCC00",                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                            width         = 90,
                                                                                            height        = 30,
                                                                                            border_radius = ft.border_radius.all(30),       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            content = ft.TextField(
                                                                                                            hint_text = self.attribute_widget,
                                                                                                            border    = ft.InputBorder.NONE,    # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                            bgcolor   = 'dark',                 # inside box
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
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
                                                                                            ink           = False,                             # click effect ripple
                                                                                            bgcolor       = ft.colors.TRANSPARENT,             # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                            width         = 50.5,
                                                                                            height        = 30,
                                                                                            border        = ft.border.all(1, ft.colors.RED),
                                                                                            border_radius = ft.border_radius.all(30),          # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            ##################### EVENTS
                                                                                            on_click      = lambda x:self.modify_right_container_attributes(data=self.attribute_widget,value = ColorEntry),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                            # on_click=lambda _:print(_.__dict__),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                             ],),

                                                    ##################### EVENTS
                                                    # on_click=lambda _:print(_),  # on_hover=print('on click over'), on_long_press=print('long press'),
                                                    )#<=== NOTE COMA,
                                         ],
                            ),#<=== NOTE COMA [NOTE]                               # for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                            ##################### EVENTS
                            # on_click=lambda _:print(_),                          # on_hover=print('on click over'), on_long_press=print('long press'),
                        )#<=== NOTE COMA

        return ColorEntry

    def modify_right_container_attributes(self,data,value):
        """will activate main widget color when press right Conteiner color box"""
        # print(data)
        ################ ONLY FOR CONTAINER
        print(f'"{data}" <<==== ')

        if  data   == "bgcolor":
            self.widget.bgcolor        = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "focused_bgcolor":
            self.widget.focused_bgcolor= value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "shadow_color":
            self.widget.shadow_color = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "color":
            self.widget.color        = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "fill_color":
            self.widget.fill_color   = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "icon_color":
            self.widget.icon_color   = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "check_color":
            self.widget.check_color  = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "focused_border_color":
            self.widget.focused_border_color = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']
        if  data   == "border_color":
            self.widget.border_color   = value.content.controls[1].content.controls[1].bgcolor # <=== Atribute 0 ['width']

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

        self.widget.content.value = value if config_widget  == "value" else None
        will modify attributes of the widget class in real time
        change circle right color in streaming
        """
        ########################################### ONLY FOR CONTAINER
        # if  self.attribute_widget   == "bgcolor ":
        #     value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        #     value.content.controls[1].update()
        ########################################### ONLY FOR CONTENT CONTAINER
        # colors inside de box rounded
        if  self.attribute_widget   == "bgcolor":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "focused_bgcolor":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "border_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "focused_border_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "shadow_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "icon_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "check_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()
        if  self.attribute_widget   == "fill_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
            value.content.controls[1].update()

        # print(self.widget.uid)
        # self.ColorEntry.content.update()
        ####################
        self.widget.update()

######## Double_Widget = DoubleEntry(),# <======= Comma