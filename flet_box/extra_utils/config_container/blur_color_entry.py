import flet as ft

# from ..settings_var.settings_widget import GLOBAL_VAR

class BlurColorEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """

    def __init__(
        self,
        id_name_widget_dict=None,
        config_widget: str="exemple [value,bgcolor,width,height] ....",
        page: object=None,
        screen_phone: object=None,
    ):
        super().__init__()
        self.page = page
        self.widget = screen_phone

        self.tooltip='BlurColorEntry'
        self.attribute_widget = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        # size textz
        self.text_size = 12 #GLOBAL_VAR(get_global_var="text_size_input")
        self.padding_only = 4 #GLOBAL_VAR(get_global_var="padding_only")

    def build(self):
        Drop_DoubleEntry = ft.Container(
            ink=False,
            # bgcolor=ft.Colors.with_opacity(0.5, ft.colors('black')),
            # blur = (8,8),
            padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            # border=ft.border.all(1.5, ft.Colors.with_opacity(0.28, ft.colors('white'))),
            # border_radius=ft.border_radius.all(14),

            width=165,
            height=80,
            content=ft.Column(
                wrap=True,
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                        padding=ft.padding.only(left=12, top=0, right=12, bottom=0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        height=20,
                        content=ft.Text(
                            value="BLur Effects",
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(2),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.04, ft.colors('white'))),
                        width=154,
                        height=36,
                        tooltip="Double Entry",
                        # gradient=ft.LinearGradient(
                        #     begin=ft.alignment.top_center,
                        #     end=ft.alignment.bottom_center,
                        #     colors=[ft.colors('cyan800'), ft.colors('black38')],
                        # ),
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    ink=False,
                                    width=68,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text="Blur X",
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,
                                        # ======================= EVENTS ===========================
                                        on_change=lambda x: self.modify_right_container_attributes(
                                            data="blur_effect", value=Drop_DoubleEntry
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    border_radius=ft.border_radius.all(30),
                                    ink=False,
                                    width=68,
                                    content=ft.TextField(
                                        hint_text="Blur Y",
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,
                                        on_change=lambda x: self.modify_right_container_attributes(
                                            data="blur_effect", value=Drop_DoubleEntry
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
        Drop_BlurColorEntry = ft.Container(
            ink=False,
            # bgcolor=ft.Colors.with_opacity(0.5, ft.colors('black')),
            # blur = (8,8),
            padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            # border=ft.border.all(1.5, ft.Colors.with_opacity(0.28, ft.colors('white'))),
            # border_radius=ft.border_radius.all(14),
            width=165,
            height=80,
            content=ft.Column(
                wrap=True,
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                        padding=ft.padding.only(left=8, top=0, right=8, bottom=0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        height=20,
                        content=ft.Text(
                            value="Transparent Color",
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.only(left=2, top=0, right=8, bottom=0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.04, ft.colors('white'))),
                        width=152,
                        height=36,
                        # gradient=ft.LinearGradient(
                        #     begin=ft.alignment.top_center,
                        #     end=ft.alignment.bottom_center,
                        #     colors=[ft.colors('cyan800'), ft.colors('black38')],
                        # ),
                        content=ft.Row(
                            spacing=4.5,
                            controls=[
                                ft.Container(
                                    ink=False,
                                    # bgcolor="#44CCCC00",
                                    width=90,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text="Blur Color",
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,
                                        # ======================= EVENTS ===========================
                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value=Drop_BlurColorEntry,
                                        ),
                                        on_submit=lambda x: self.modify_right_container_attributes(
                                            data=self.attribute_widget,
                                            value=Drop_BlurColorEntry,
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    ink=False,
                                    bgcolor=ft.colors('black12'),
                                    width=50.5,
                                    height=30,
                                    border=ft.border.all(1, ft.Colors.with_opacity(0.04, ft.colors('white'))),
                                    border_radius=ft.border_radius.all(30),
                                    on_click=lambda x: self.modify_right_container_attributes(
                                        data=self.attribute_widget,
                                        value=Drop_BlurColorEntry,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
        return ft.Container(
            ink=False,
            bgcolor=ft.Colors.with_opacity(0.5, ft.colors('black')),
            blur = (8,8),
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center_left,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(1.5, ft.Colors.with_opacity(0.28, ft.colors('white'))),
            content=ft.Row( spacing=1,
                            wrap = True,
                            controls=[
                                Drop_DoubleEntry,
                                Drop_BlurColorEntry]),
        )

    def modify_right_container_attributes(self, data, value):
        """
        will activate main widget color when press right Conteiner color box
        """

        #: print(data)
        #: run only in production

        #: ONLY FOR CONTAINER
        if data == "blur":
            self.widget.bgcolor = ft.Colors.with_opacity(
                0.14, value.content.controls[1].content.controls[1].bgcolor
            )

        if data == "blur_effect":
            self.widget.blur = (
                value.content.controls[1].content.controls[0].content.value,
                value.content.controls[1].content.controls[1].content.value,
            )
        #: UPDATE DATA
        try:
            self.widget.update()
        except Exception as error:
            self.error_page = self.page.session.get('on_dev')
            self.error_page(
                name_seccion='Error by Dev',
                body_string=error
            )

    def modify_widget_attributes(
        self,
        config_widget,
        value,
    ):
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

        if self.attribute_widget == "blur":
            value.content.controls[1].content.controls[1].bgcolor = (
                value.content.controls[1].content.controls[0].content.value
            )
            value.content.controls[1].update()

        #: only in production
        #: print(self.widget.uid)
        #: self.BlurColorEntry.content.update()

        #: UPDATE DATA
        try:
            self.widget.update()
        except Exception as error:
            self.error_page = self.page.session.get('on_dev')
            self.error_page(
                name_seccion='Error by Dev',
                body_string=error
            )
