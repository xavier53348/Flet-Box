import flet as ft

# from ..settings_var.settings_widget import GLOBAL_VAR

class FourEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = FourEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """

    def __init__(
        self,
        id_name_widget_dict=None,
        config_widget: str="exemple [value,bgcolor,width,height] ....",
        page: object=object(),
        screen_phone: object=object(),
    ):
        super().__init__()
        self.page = page
        self.widget = screen_phone

        self.tooltip="FourEntry"
        self.attribute_widget = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        # size textz
        self.text_size = 12 #GLOBAL_VAR(get_global_var="text_size_input")
        self.padding_only = 4 #GLOBAL_VAR(get_global_var="padding_only")

        #: print(self.attribute_widget)
        #: will change name of entry points

        if self.attribute_widget == "padding" or self.attribute_widget == "margin":
            self.attribute_widget_name_1 = "Left"
            self.attribute_widget_name_2 = "Top"
            self.attribute_widget_name_3 = "Right"
            self.attribute_widget_name_4 = "Bottom"

        if self.attribute_widget == "padding " or self.attribute_widget == "margin ":
            self.attribute_widget_name_1 = "Left"
            self.attribute_widget_name_2 = "Top"
            self.attribute_widget_name_3 = "Right"
            self.attribute_widget_name_4 = "Bottom"

        if self.attribute_widget == "border_radius":
            self.attribute_widget_name_1 = " BL"
            self.attribute_widget_name_2 = " BR"
            self.attribute_widget_name_3 = " TL"
            self.attribute_widget_name_4 = " TR"

    def build(self):
        packet_data = ft.Container(
            ink=False,
            bgcolor=ft.Colors.with_opacity(0.5, ft.colors('black')),
            blur = (8,8),
            padding=ft.padding.all(4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(1.5, ft.Colors.with_opacity(0.28, ft.colors('white'))),
            width=162,
            height=128,
            content=ft.Column(
                wrap=True,
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                        padding=ft.padding.only(left=12, top=0, right=12, bottom=0),
                        alignment=ft.alignment.center,
                        # border=ft.border.all(1, ft.Colors.with_opacity(0.04, ft.colors('white'))),
                        border_radius=ft.border_radius.all(30),
                        height=20,
                        content=ft.Text(
                            value=self.attribute_widget.capitalize().replace("_", " "),
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                        padding=ft.padding.all(2),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.04, ft.colors('white'))),
                        height=36,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.colors('cyan800'), ft.colors('black38')],
                        ),
                        content=ft.Row(
                            spacing=8.7,
                            controls=[
                                ft.Container(
                                    ink=False,
                                    width=68,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_1,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,

                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value=packet_data,
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    ink=False,
                                    width=68,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_2,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,

                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value=packet_data,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(2),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.04, ft.colors('white'))),
                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                        height=36,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.colors('cyan800'), ft.colors('black38')],
                        ),
                        content=ft.Row(
                            spacing=8.7,
                            controls=[
                                ft.Container(
                                    ink=False,
                                    width=68,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_3,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,

                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value=packet_data,
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    ink=False,
                                    width=68,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_4,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,

                                        # ======================= EVENTS ===========================
                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value=packet_data,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

        return packet_data

    def modify_widget_attributes(
        self,
        config_widget,
        value,
    ):
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
        print(f"{config_widget}<==")
        #: ONLY FOR CONTENT
        if config_widget == "padding" or config_widget == "padding ":
            """all values in Box Container"""
            left = (
                value.content.controls[1].content.controls[0].content.value
                if value.content.controls[1].content.controls[0].content.value
                else 0
            )
            top = (
                value.content.controls[1].content.controls[1].content.value
                if value.content.controls[1].content.controls[1].content.value
                else 0
            )
            right = (
                value.content.controls[2].content.controls[0].content.value
                if value.content.controls[2].content.controls[0].content.value
                else 0
            )
            bottom = (
                value.content.controls[2].content.controls[1].content.value
                if value.content.controls[2].content.controls[1].content.value
                else 0
            )
            if self.attribute_widget == "padding ":
                self.widget.padding=0
                self.tab_container = self.page.session.get('SELECTED_SCREEN')
                self.tab_container.content.content.content.padding = ft.padding.only(
                    left=int(left),
                    top=int(top),
                    right=int(right),
                    bottom=int(bottom),
                )
                self.widget = self.tab_container
            else:

                self.widget.padding = ft.padding.only(
                    left=int(left),
                    top=int(top),
                    right=int(right),
                    bottom=int(bottom),
                )
            # print('paddinf')
        if config_widget == "margin":
            """all values in Box Container"""

            left = (
                value.content.controls[1].content.controls[0].content.value
                if value.content.controls[1].content.controls[0].content.value
                else 0
            )
            top = (
                value.content.controls[1].content.controls[1].content.value
                if value.content.controls[1].content.controls[1].content.value
                else 0
            )
            right = (
                value.content.controls[2].content.controls[0].content.value
                if value.content.controls[2].content.controls[0].content.value
                else 0
            )
            bottom = (
                value.content.controls[2].content.controls[1].content.value
                if value.content.controls[2].content.controls[1].content.value
                else 0
            )

            self.widget.margin = ft.margin.only(
                left=int(left),
                top=int(top),
                right=int(right),
                bottom=int(bottom),
            )
        if config_widget == "border_radius":
            """all values in Box Container"""

            top_left = (
                value.content.controls[1].content.controls[0].content.value
                if value.content.controls[1].content.controls[0].content.value
                else 0
            )
            top_right = (
                value.content.controls[1].content.controls[1].content.value
                if value.content.controls[1].content.controls[1].content.value
                else 0
            )
            bottom_left = (
                value.content.controls[2].content.controls[0].content.value
                if value.content.controls[2].content.controls[0].content.value
                else 0
            )
            bottom_right = (
                value.content.controls[2].content.controls[1].content.value
                if value.content.controls[2].content.controls[1].content.value
                else 0
            )

            self.widget.border_radius = ft.border_radius.only(
                top_left=int(top_left),
                top_right=int(top_right),
                bottom_left=int(bottom_left),
                bottom_right=int(bottom_right),
            )

        try:
            self.widget.update()
        except Exception as error:
            self.error_page = self.page.session.get('on_dev')
            self.error_page(
                name_seccion='Error by Dev',
                body_string=error
            )