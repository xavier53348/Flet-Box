import flet as ft

class SingleEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """
    widget_content = 'data'
    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget=''):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute
        self.widget_content   = self.widget_content
    def build(self):
        SingleEntry = ft.Container(
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
                    content = ft.Column(
                                ##################### PROPERTY BOX
                                ##################### ADAPT TO SCREEN
                                wrap=True,                                                # justify in all screen
                                ##################### WIDGETS
                                controls = [
                                        ft.Container( ##################### Text label
                                            ink           = False,                                                # click effect ripple
                                            bgcolor       = "#0e0f11",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                            padding       = ft.padding.only(left=12, top=0, right=12, bottom=0),  # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                            alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                            border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                            height        = 20,
                                            ##################### WIDGETS
                                            content = ft.Text(
                                                        ##################### PROPERTY
                                                        value       = 'width - height' if self.attribute_widget == 'width' else self.attribute_widget.capitalize().replace('_',' '), # content = ft.Text(value="Compound button", size=12,),
                                                        font_family = "Consolas", #"Consolas ,RobotoSlab
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                    ft.Container(
                                            ##################### PROPERTY
                                            ink           = False,                                          # click effect ripple
                                            bgcolor       = ft.colors.BLACK38,                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                            padding       = ft.padding.all(2),    # inside box              # padding.only(left=8, top=8, right=8, bottom=8),
                                            alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                            border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                            border        = ft.border.all(1, ft.colors.BLACK38),            # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                            width         = 152,
                                            height        = 36,
                                            ##################### WIDGETS
                                            content=ft.Row(
                                                            ##################### PROPERTY BOX
                                                            ##################### WIDGETS
                                                            controls=[
                                                                        ft.Container(
                                                                                    ##################### PROPERTY
                                                                                    ink=False,                                                      # click effect ripple
                                                                                    bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                    width=146,
                                                                                    height=30,
                                                                                    border_radius= ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                                                                                    content=ft.TextField(
                                                                                                    hint_text=self.attribute_widget.capitalize().replace('_',' '),
                                                                                                    border=ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                    bgcolor='dark',                                 # inside box
                                                                                                    color='YELLOW',
                                                                                                    text_size=15,
                                                                                                    #======================= EVENTS ===========================
                                                                                            on_change   = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = SingleEntry),
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

        return SingleEntry

    def modify_widget_attributes(self,config_widget,value,):
        """
        NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = SingleEntry),

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
        # self.widget.bgcolor='red'  #<<< cmain container

        """ Container
         'width', 'rotate', 'alignment', 'animate', 'bgcolor', 'blur', 'border', 'border_radius', 'padding',
         'url_target', 'url', 'margin', 'clip_behavior', 'content', 'gradient', 'image_fit', 'image_opacity',
         'image_repeat', 'image_src', 'image_src_base64', 'blend_mode', 'ink', 'rtl', 'shadow', 'shape',
         'theme_mode', 'theme',
        """
        ################ CONTAINER STR

        if  config_widget   == "image_src ":
            self.widget.image_src              = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "tooltip ":
            self.widget.tooltip                = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "rotate ":
            self.widget.rotate                    = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0 # <=== Atribute 0 ['width']
        if  config_widget   == "scale ":
            self.widget.scale                     = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 1# <=== Atribute 0 ['width']
        if  config_widget   == "image_opacity ":
            self.widget.image_opacity             = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        ################ CONTAINER STR
        if  config_widget   == "text":
            self.widget.content.text           = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "tooltip":
            self.widget.content.tooltip        = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "image_src":
            self.widget.content.image_src    = f"{value.content.controls[1].content.controls[0].content.value }"# <=== Atribute 0 ['width']
        if  config_widget   == "url":
            self.widget.content.url            = value.content.controls[1].content.controls[0].content.value  # <=== Atribute 0 ['width']
        if  config_widget   == "url_target":
            self.widget.content.url_target     = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "blur_radius":
            self.widget.content.blur_radius       = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0# <=== Atribute 0 ['width']
        if  config_widget   == "image_opacity":
            self.widget.content.image_opacity     = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 1# <=== Atribute 0 ['width']
        if  config_widget   == "rotate":
            self.widget.content.rotate            = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0 # <=== Atribute 0 ['width']
        if  config_widget   == "scale":
            self.widget.content.scale             = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "label":
            self.widget.content.label          = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "value":
            self.widget.content.value          = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "key":
            self.widget.content.key            = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "hint_text":
            self.widget.content.hint_text      = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "counter_text":
            self.widget.content.counter_text   = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "suffix_text":
            self.widget.content.suffix_text    = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "icon":
            self.widget.content.icon           = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "src":
            self.widget.content.src            = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "data":
            self.widget.content.data           = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "semantics_label":
            self.widget.content.semantics_label= value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        if  config_widget   == "src_base64":
            self.widget.content.src_base64     = value.content.controls[1].content.controls[0].content.value # <=== Atribute 0 ['width']
        ######################################## INT
        if  config_widget   == "spread_radius":
            self.widget.content.spread_radius     = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "size":
            self.widget.content.size              = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "elevation":
            self.widget.content.elevation         = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "aspect_ratio":
            self.widget.content.aspect_ratio      = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "runs_count":
            self.widget.content.runs_count        = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "run_spacing":
            self.widget.content.run_spacing       = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "spacing":
            self.widget.content.spacing           = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "child_aspect_ratio":
            self.widget.content.child_aspect_ratio= float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "max_extent":
            self.widget.content.max_extent        = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "min_lines":
            self.widget.content.min_lines         = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "max_lines":
            self.widget.content.max_lines         = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "border_width":
            self.widget.content.border_width      = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "text_size":
            self.widget.content.text_size         = float(value.content.controls[1].content.controls[0].content.value)  if value.content.controls[1].content.controls[0].content.value else 1 # <=== Atribute 0 ['width']
        if  config_widget   == "opacity":
            self.widget.content.opacity           = float(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 1# <=== Atribute 0 ['width']

        ########################################
        # print(self.widget.uid)
        # print(self.widget.content)
        # self.SingleEntry.content.update()
        self.widget.update()

######## Double_Widget = DoubleEntry(),# <======= Comma