
import flet as ft

class DoubleEntry(ft.Stack):
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

        #: print(self.attribute_widget)
        #: CONTAINER STR
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

        #: CONTAINER STR
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
                                ink           = False,
                                bgcolor       = '#0c0d0e',
                                padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),
                                margin        = ft.margin.all(0),
                                alignment     = ft.alignment.center,
                                border_radius = ft.border_radius.all(16),
                                border        = ft.border.all(2, ft.colors.BLACK),
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

                                                                    value       = 'Width - Height' if self.attribute_widget == "width " else self.attribute_widget.capitalize().replace('_',' '),
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
                                                                                                            hint_text = self.attribute_widget_name_1,
                                                                                                            border    = ft.InputBorder.NONE,
                                                                                                            bgcolor   = '#0e0f11',
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                            #======================= EVENTS ===========================
                                                                                                        on_change = lambda x:self.modify_widget_attributes( config_widget = self.attribute_widget ,
                                                                                                                                                                    value = Drop_DoubleEntry),
                                                                                                            ),
                                                                                ),
                                                                                ft.Container(

                                                                                            border_radius = ft.border_radius.all(30),
                                                                                            ink           = False,
                                                                                            width         = 68,
                                                                                            content = ft.TextField(
                                                                                                            hint_text = self.attribute_widget_name_2,
                                                                                                            border    = ft.InputBorder.NONE,
                                                                                                            bgcolor   = '#0e0f11',
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,

                                                                                                         on_change= lambda x:self.modify_widget_attributes( config_widget = self.attribute_widget ,
                                                                                                                                                                    value = Drop_DoubleEntry),
                                                                                                            ),
                                                                                ),
                                                                             ],),
                                                                )
                                                         ],
                                            ),
                                )

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
        #: print(config_widget)
        #: print(value)

        #: self.widget.content.value = value if config_widget  == "value" else None
        #: will modify attributes of the widget class in real time

        if  config_widget == "width " or config_widget == "height ":
            self.widget.width   = value.content.controls[1].content.controls[0].content.value
            self.widget.height  = value.content.controls[1].content.controls[1].content.value

        if  config_widget == "blur ":
            self.widget.blur    =  ft.Blur(
                                            int(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0,
                                            int(value.content.controls[1].content.controls[1].content.value) if value.content.controls[1].content.controls[1].content.value else 0,
                                            ft.BlurTileMode.MIRROR,
                                            )
        if  config_widget == "border ":
            self.widget.border = ft.border.all(
                                                value.content.controls[1].content.controls[0].content.value ,
                                                value.content.controls[1].content.controls[1].content.value ,
                                                )
        if  config_widget == "offset ":
            self.widget.offset =(
                                 value.content.controls[1].content.controls[0].content.value ,
                                 value.content.controls[1].content.controls[1].content.value ,
                                 )
        if  config_widget == "width" or config_widget == "height":
            self.widget.width   = value.content.controls[1].content.controls[0].content.value
            self.widget.height  = value.content.controls[1].content.controls[1].content.value

        if  config_widget == "blur":
            self.widget.blur    =  ft.Blur(
                                            int(value.content.controls[1].content.controls[0].content.value) if value.content.controls[1].content.controls[0].content.value else 0,
                                            int(value.content.controls[1].content.controls[1].content.value) if value.content.controls[1].content.controls[1].content.value else 0,
                                            ft.BlurTileMode.MIRROR,
                                            )
        if  config_widget == "border":
            self.widget.border = ft.border.all(
                                                value.content.controls[1].content.controls[0].content.value ,
                                                value.content.controls[1].content.controls[1].content.value ,
                                                )
        if  config_widget == "offset":
            self.widget.offset =(
                                 value.content.controls[1].content.controls[0].content.value ,
                                 value.content.controls[1].content.controls[1].content.value ,
                                 )
        #: run only in production
        #: print(self.widget.uid)
        self.widget.update()

#######
