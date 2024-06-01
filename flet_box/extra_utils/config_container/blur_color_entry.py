import flet as ft

class BlurColorEntry(ft.Stack):
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
        Drop_DoubleEntry = ft.Container(
                                ink           = False,
                                bgcolor       = "#0c0d0e",
                                padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),
                                margin        = ft.margin.all(0),
                                alignment     = ft.alignment.center,
                                border_radius = ft.border_radius.only(top_left=16,bottom_left=16),
                                # border        = ft.border.all(2, ft.colors.BLACK38),
                                width         = 165,
                                height        = 80,
                                content=ft.Column(
                                            wrap=True,
                                            controls=[
                                                    ft.Container(
                                                        ink           = False,
                                                        bgcolor       = "#0e0f11",
                                                        padding       = ft.padding.only(left=12, top=0, right=12, bottom=0),
                                                        alignment     = ft.alignment.center,
                                                        border_radius = ft.border_radius.all(30),
                                                        height        = 20,
                                                        content = ft.Text(
                                                                    value       = 'BLur Effects',
                                                                    font_family = "Consolas", #"Consolas ,RobotoSlab
                                                        ),),

                                                    ft.Container(
                                                        ink           = False,
                                                        padding       = ft.padding.all(2),
                                                        alignment     = ft.alignment.center,
                                                        border_radius = ft.border_radius.all(30),
                                                        border        = ft.border.all(0.1, ft.colors.BLACK38),
                                                        width         = 154,
                                                        height        = 36,
                                                        tooltip       = 'Double Entry',
                                                        gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN_800, ft.colors.BLACK38],),
                                                        content=ft.Row(
                                                                    controls=[
                                                                                ft.Container(

                                                                                            ink           = False,
                                                                                            width         = 68,
                                                                                            border_radius = ft.border_radius.all(30),
                                                                                            content = ft.TextField(
                                                                                                            hint_text = "Blur X",
                                                                                                            border    = ft.InputBorder.NONE,
                                                                                                            bgcolor   = '#0e0f11',
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                            #======================= EVENTS ===========================
                                                                                                        on_change = lambda x:self.modify_right_container_attributes( data = "blur_effect" ,
                                                                                                                                                                    value = Drop_DoubleEntry),
                                                                                                            ),
                                                                                ),
                                                                                ft.Container(

                                                                                            border_radius = ft.border_radius.all(30),
                                                                                            ink           = False,
                                                                                            width         = 68,
                                                                                            content = ft.TextField(
                                                                                                            hint_text = "Blur Y",
                                                                                                            border    = ft.InputBorder.NONE,
                                                                                                            bgcolor   = '#0e0f11',
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,

                                                                                                         on_change= lambda x:self.modify_right_container_attributes( data = "blur_effect" ,
                                                                                                                                                                    value = Drop_DoubleEntry),
                                                                                                            ),
                                                                                ),
                                                                             ],),
                                                                )
                                                         ],
                                            ),
                                )
        Drop_BlurColorEntry = ft.Container(
                            ink           = False,
                            bgcolor       = "#0c0d0e",
                            padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),
                            margin        = ft.margin.all(0),
                            alignment     = ft.alignment.center,
                            border_radius = ft.border_radius.only(top_right=16,bottom_right=16),
                            # border        = ft.border.all(2, ft.colors.BLACK38),
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

                                                            value       = 'Transparent Color',
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
                                                                                                    hint_text = "Blur Color",
                                                                                                    border    = ft.InputBorder.NONE,
                                                                                                    bgcolor   = '#0e0f11',
                                                                                                    color     = 'YELLOW',
                                                                                                    text_size = 15,
                                                                                                    #======================= EVENTS ===========================
                                                                                                on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_BlurColorEntry),
                                                                                                on_submit= lambda x:self.modify_right_container_attributes(data=self.attribute_widget,value = Drop_BlurColorEntry),
                                                                                                    ),
                                                                        ),
                                                                        ft.Container(

                                                                                    ink           = False,
                                                                                    bgcolor       = ft.colors.TRANSPARENT,
                                                                                    width         = 50.5,
                                                                                    height        = 30,
                                                                                    border        = ft.border.all(1, ft.colors.CYAN_800),
                                                                                    border_radius = ft.border_radius.all(30),
                                                                                    on_click      = lambda x:self.modify_right_container_attributes(data=self.attribute_widget,value = Drop_BlurColorEntry),
                                                                        ),
                                                                 ],),
                                                    )
                                         ],
                            ),
                        )
        return ft.Container(
                            ink           = False,
                            bgcolor       = '#0a0b0c',
                            padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),
                            margin        = ft.margin.all(0),
                            alignment     = ft.alignment.center,
                            border_radius = ft.border_radius.all(16),
                            border        = ft.border.all(2, ft.colors.BLACK),
                            content = ft.Row(
                                             spacing=0,
                                             controls=[
                                                Drop_DoubleEntry,
                                                Drop_BlurColorEntry
                                        ])
                            )

    def modify_right_container_attributes(self,data,value):
        """
        will activate main widget color when press right Conteiner color box
        """

        #: print(data)
        #: run only in production

        #: ONLY FOR CONTAINER
        if  data   == "blur":
            self.widget.bgcolor = ft.colors.with_opacity(0.08, value.content.controls[1].content.controls[1].bgcolor)

        if  data == "blur_effect":
            self.widget.blur = (
                                value.content.controls[1].content.controls[0].content.value ,
                                value.content.controls[1].content.controls[1].content.value ,
                                )
        self.widget.update()

    def modify_widget_attributes(self,config_widget,value,):
        """
        NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = BlurColorEntry),

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

        if  self.attribute_widget   == "blur":
            value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
            value.content.controls[1].update()

        #: only in production
        #: print(self.widget.uid)
        #: self.BlurColorEntry.content.update()

        self.widget.update()

#######
