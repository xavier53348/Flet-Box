
import flet as ft


class BoolEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = BoolEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """
    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        self.widget              = widget
        self.attribute_widget    = config_widget
        self.id_name_widget_dict = id_name_widget_dict
        #: will change name of entry points

    def build(self):
        Drop_BoolEntry =  ft.Container(
                    ink           = False,
                    bgcolor       = '#0c0d0e',
                    padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),
                    margin        = ft.margin.all(0),
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
                                            value       = self.attribute_widget.capitalize().replace("_"," "),
                                            font_family = "Consolas",
                                ),),
                            ft.Container(
                                    ink           = False,
                                    bgcolor       = ft.colors.BLACK38,
                                    padding       = ft.padding.all(2),
                                    alignment     = ft.alignment.center,
                                    border_radius = ft.border_radius.all(30),
                                    width         = 152,
                                    height        = 36,
                                    content=ft.Row(
                                                controls=[
                                                   ft.Container(
                                                            ink           = False,
                                                            padding       = ft.padding.only(left=2, top=0, right=8, bottom=0),
                                                            alignment     = ft.alignment.center,
                                                            border_radius = ft.border_radius.all(30),
                                                            border        = ft.border.all(0.1, ft.colors.BLACK38),
                                                            width         = 150,
                                                            height        = 36,
                                                        gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN_800, ft.colors.BLACK38],),
                                                            content=ft.Row(
                                                                            spacing=6,
                                                                            controls=[
                                                                                        ft.Container(
                                                                                            ink           = False,
                                                                                            width         = 88,
                                                                                            height        = 30,
                                                                                            border_radius = ft.border_radius.all(30),
                                                                                            content = ft.TextField(
                                                                                                            disabled  = True,
                                                                                                            hint_text = self.attribute_widget,
                                                                                                            border    = ft.InputBorder.NONE,
                                                                                                            bgcolor   = '#0e0f11',
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                                    ),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            ink    = False,
                                                                                            width  = 42,
                                                                                            height = 30,
                                                                                            content = ft.CupertinoSwitch(
                                                                                                    value        = True if self.attribute_widget == "visible " or  self.attribute_widget == "visible" else False,
                                                                                                    track_color  = 'Black',
                                                                                                    active_color = 'yellow',
                                                                                                    on_change    = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_BoolEntry),
                                                                                            ),
                                                                                        ),
                                                                                     ],),
                                                           )
                                                         ],),
                               )
                         ],
            ),
        )

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
        #: self.widget.content.value = value if config_widget  == "value" else None
        #: will modify attributes of the widget class in real time

        #: use
        #: self.widget.expand <=========== CONTAINER
        #: self.widget.cotntent.expand <=========== CONTAINER.content

        #: ONLY FOR CONTAINER
        #: print(value.content.controls[1].content.controls[0].content.controls[1].content.value)

        if  config_widget   == "expand ":
            self.widget.expand = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "ink ":
            self.widget.ink =    bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "visible ":
            self.widget.visible =bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)

        #: CONTAINER.content = WIDGET
        if  config_widget   == "expand":
            self.widget.expand = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "ink":
            self.widget.ink =    bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "visible":
            self.widget.visible =bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "scroll":
            self.widget.scroll = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "wrap":
            self.widget.wrap =   bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "tight":
            self.widget.tight =  bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "multiline":
            self.widget.multiline = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "disabled":
            self.widget.disabled  = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "read_only":
            self.widget.read_only = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "password":
            self.widget.password  = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "filled":
            self.widget.filled =    bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "adaptive":
            self.widget.adaptive =  bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "tristate":
            self.widget.tristate =  bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "autofocus":
            self.widget.autofocus = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "horizontal":
            self.widget.horizontal = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "can_reveal_password":
            self.widget.can_reveal_password = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "capitalization":
            self.widget.capitalization = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)
        if  config_widget   == "gapless_playback":
            self.widget.gapless_playback = bool(value.content.controls[1].content.controls[0].content.controls[1].content.value)

        #: only in production
        #: print(self.widget.uid)
        #: print(data_usage)
        self.widget.update()

#######
