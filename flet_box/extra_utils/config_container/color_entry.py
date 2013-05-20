
import flet as ft


class ColorEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        self.widget              = widget
        self.attribute_widget    = config_widget
        self.id_name_widget_dict = id_name_widget_dict

    def build(self):
        ColorEntry = ft.Container(
                            ink           = False,
                            bgcolor       = '#0c0d0e',
                            padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),
                            margin        = ft.margin.all(0),
                            alignment     = ft.alignment.center,
                            border_radius = ft.border_radius.all(16),
                            border        = ft.border.all(2, ft.colors.BLACK),
                            width         = 165,
                            height        = 80,
                            content = ft.Column(
                                        wrap     = True,
                                        controls = [
                                            ft.Container(
                                                ink           = False,
                                                bgcolor       = "#0e0f11",
                                                padding       = ft.padding.only(left=8, top=0, right=8, bottom=0),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                height        = 20,
                                                content =ft.Text(

                                                            value       = 'width - height' if self.attribute_widget == 'width' else self.attribute_widget.capitalize().replace("_"," "),
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                ),),
                                            ft.Container(
                                                    ink           = False,
                                                    padding       = ft.padding.only(left=2, top=0, right=8, bottom=0),
                                                    alignment     = ft.alignment.center,
                                                    border_radius = ft.border_radius.all(30),
                                                    border        = ft.border.all(1, ft.colors.BLACK38),
                                                    width         = 152,
                                                    height        = 36,
                                                gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN_800, ft.colors.BLACK38],),
                                                    content = ft.Row(
                                                                    spacing  = 4.5,
                                                                    controls = [
                                                                        ft.Container(

                                                                                    ink           = False,
                                                                                    bgcolor       = "#44CCCC00",
                                                                                    width         = 90,
                                                                                    height        = 30,
                                                                                    border_radius = ft.border_radius.all(30),
                                                                                    content = ft.TextField(
                                                                                                    hint_text = self.attribute_widget,
                                                                                                    border    = ft.InputBorder.NONE,
                                                                                                    bgcolor   = '#0e0f11',
                                                                                                    color     = 'YELLOW',
                                                                                                    text_size = 15,
                                                                                                    #======================= EVENTS ===========================
                                                                                                on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = ColorEntry),
                                                                                                on_submit= lambda x:self.modify_right_container_attributes(data=self.attribute_widget,value = ColorEntry),
                                                                                                    ),
                                                                        ),
                                                                        ft.Container(

                                                                                    ink           = False,
                                                                                    bgcolor       = ft.colors.TRANSPARENT,
                                                                                    width         = 50.5,
                                                                                    height        = 30,
                                                                                    border        = ft.border.all(1, ft.colors.CYAN_800),
                                                                                    border_radius = ft.border_radius.all(30),
                                                                                    on_click      = lambda x:self.modify_right_container_attributes(data=self.attribute_widget,value = ColorEntry),
                                                                        ),
                                                                 ],),
                                                    )
                                         ],
                            ),
                        )
        return ColorEntry

    def modify_right_container_attributes(self,data,value):
        """
        will activate main widget color when press right Conteiner color box
        """

        #: print(data)
        #: run only in production
        print(f'"{data}" <<==== ')

        #: ONLY FOR CONTAINER
        if  data   == "bgcolor":
            self.widget.bgcolor = ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "focused_bgcolor":
            self.widget.focused_bgcolor= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "color":
            self.widget.color= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "fill_color":
            self.widget.fill_color= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "icon_color":
            self.widget.icon_color= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "check_color":
            self.widget.check_color= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "focused_border_color":
            self.widget.focused_border_color= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "border_color":
            self.widget.border_color= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor

        if  data   == "shadow_color":
            self.my_color= ft.colors.TRANSPARENT if value.content.controls[1].content.controls[1].bgcolor == "" else value.content.controls[1].content.controls[1].bgcolor
            self.widget.shadow= ft.BoxShadow(
                                            spread_radius = 0,
                                            blur_radius   = 24,
                                            color         = self.my_color,
                                            offset        = ft.Offset(0, 0),
                                            blur_style    = ft.ShadowBlurStyle.OUTER, # NORMAL # SOLID # OUTER # INNER
                                        )
            # print(self.widget,'data')
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
        #: ONLY FOR CONTAINER
        #: if  self.attribute_widget   == "bgcolor ":
        #:     value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
        #:     value.content.controls[1].update()
        #: ONLY FOR CONTENT CONTAINER
        #: colors inside de box rounded

        if  self.attribute_widget   == "bgcolor":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "focused_bgcolor":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "border_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "focused_border_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "shadow_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "icon_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "check_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "fill_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        if  self.attribute_widget   == "shadow_color":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()
        #: only in production
        #: print(self.widget.uid)
        #: self.ColorEntry.content.update()

        self.widget.update()

#######
