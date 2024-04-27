
import flet as ft

class FourEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = FourEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """
    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        """ Is neccesary make a filter that will contain name of the widget to use"""
        self.widget              = widget
        self.attribute_widget    = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        #: print(self.attribute_widget)
        #: will change name of entry points

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
                            ink           = False,
                            bgcolor       = '#0c0d0e',
                            padding       = ft.padding.all(4),
                            margin        = ft.margin.all(0),
                            alignment     = ft.alignment.center,
                            border_radius = ft.border_radius.all(16),
                            border        = ft.border.all(2, ft.colors.BLACK),
                            width         = 162,
                            height        = 128,
                            content = ft.Column(
                                        wrap = True,
                                        controls=[
                                            ft.Container(
                                                ink           = False,
                                                bgcolor       = "#0e0f11",
                                                padding       = ft.padding.only(left=12, top=0, right=12, bottom=0),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                height        = 20,
                                                content=ft.Text(

                                                            value       = self.attribute_widget.capitalize().replace('_',' '),
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                ),),
                                            ft.Container(
                                                ink           = False,
                                                bgcolor       = "#0e0f11",
                                                padding       = ft.padding.all(2),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                border        = ft.border.all(0.1, ft.colors.BLACK38),
                                                height        = 36,
                                                gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN_800, ft.colors.BLACK38],),
                                                content       = ft.Row(
                                                                spacing=8.7,
                                                                controls=[
                                                                            ft.Container(
                                                                                        ink           = False,
                                                                                        width         = 68,
                                                                                        height        = 30,
                                                                                        border_radius = ft.border_radius.all(30),
                                                                                        content = ft.TextField(
                                                                                                        hint_text = self.attribute_widget_name_1,
                                                                                                        border    = ft.InputBorder.NONE,
                                                                                                        bgcolor   = '#0e0f11',
                                                                                                        color     = 'YELLOW',
                                                                                                        text_size = 15,
                                                                                                on_change = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
                                                                                                        ),
                                                                            ),
                                                                            ft.Container(
                                                                                        ink           = False,
                                                                                        width         = 68,
                                                                                        height        = 30,
                                                                                        border_radius = ft.border_radius.all(30),
                                                                                        content = ft.TextField(
                                                                                                        hint_text = self.attribute_widget_name_2,
                                                                                                        border    = ft.InputBorder.NONE,
                                                                                                        bgcolor   = '#0e0f11',
                                                                                                        color     = 'YELLOW',
                                                                                                        text_size = 15,
                                                                                                on_change = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
                                                                                                        ),
                                                                            ),
                                                                         ],),
                                                                    ),
                                            ft.Container(
                                                ink           = False,
                                                padding       = ft.padding.all(2),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                border        = ft.border.all(1, ft.colors.BLACK38),
                                                height        = 36,
                                                gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN_800, ft.colors.BLACK38],),
                                                content = ft.Row(
                                                                spacing  = 8.7,
                                                                controls = [
                                                                            ft.Container(
                                                                                        ink           = False,
                                                                                        width         = 68,
                                                                                        height        = 30,
                                                                                        border_radius = ft.border_radius.all(30),
                                                                                        content = ft.TextField(
                                                                                                        hint_text = self.attribute_widget_name_3,
                                                                                                        border    = ft.InputBorder.NONE,
                                                                                                        bgcolor   = '#0e0f11',
                                                                                                        color     = 'YELLOW',
                                                                                                        text_size = 15,
                                                                                                on_change = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
                                                                                                        ),
                                                                            ),
                                                                            ft.Container(

                                                                                        ink           = False,
                                                                                        width         = 68,
                                                                                        height        = 30,
                                                                                        border_radius = ft.border_radius.all(30),
                                                                                        content = ft.TextField(
                                                                                                        hint_text = self.attribute_widget_name_4,
                                                                                                        border    = ft.InputBorder.NONE,
                                                                                                        bgcolor   = '#0e0f11',
                                                                                                        color     = 'YELLOW',
                                                                                                        text_size = 15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = packet_data),
                                                                                                        ),
                                                                            ),
                                                                         ],),
                                                                ),
                                            ],
                                ),
                        )

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
        #: print(config_widget)
        #: print(value)

        #: self.widget.content.value = value if config_widget  == "value" else None
        #: will modify attributes of the widget class in real time
        #: ONLY FOR CONTENT
        if  config_widget   == "padding":
            """ all values in Box Container """
            left   = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            top    = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            right  = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            bottom = value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.padding = ft.padding.only(
                                                    left   = int(left),
                                                    top    = int(top),
                                                    right  = int(right),
                                                    bottom = int(bottom),
                                                )
        if  config_widget   == "margin":
            """ all values in Box Container """

            left   = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            top    = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            right  = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            bottom = value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.margin = ft.margin.only(
                                                    left   = int(left),
                                                    top    = int(top),
                                                    right  = int(right),
                                                    bottom = int(bottom),
                                                )
        if  config_widget   == "border_radius":
            """ all values in Box Container """

            top_left    = value.content.controls[1].content.controls[0].content.value if value.content.controls[1].content.controls[0].content.value else 0
            top_right   = value.content.controls[1].content.controls[1].content.value if value.content.controls[1].content.controls[1].content.value else 0
            bottom_left = value.content.controls[2].content.controls[0].content.value if value.content.controls[2].content.controls[0].content.value else 0
            bottom_right= value.content.controls[2].content.controls[1].content.value if value.content.controls[2].content.controls[1].content.value else 0

            self.widget.border_radius = ft.border_radius.only(
                                                        top_left     = int(top_left),
                                                        top_right    = int(top_right),
                                                        bottom_left  = int(bottom_left),
                                                        bottom_right = int(bottom_right),
                                                    )
        self.widget.update()

#######
