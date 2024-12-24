import flet as ft

# from ..settings_var.settings_widget import GLOBAL_VAR

class DoubleEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
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

        self.tooltip="DoubleEntry"
        self.attribute_widget = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        self.text_size = 12 # GLOBAL_VAR(get_global_var="text_size_input")
        self.padding_only = 4 # GLOBAL_VAR(get_global_var="padding_only")


        #: print(self.attribute_widget)
        #: CONTAINER STR
        if self.attribute_widget == "width ":
            self.attribute_widget_name_1 = "Width"
            self.attribute_widget_name_2 = "Height"

        if self.attribute_widget == "border ":
            self.attribute_widget_name_1 = "Border"
            self.attribute_widget_name_2 = "Color"
        if self.attribute_widget == "offset ":
            self.attribute_widget_name_1 = "Offset"
            self.attribute_widget_name_2 = "Offset"

        if self.attribute_widget == "blur ":
            self.attribute_widget_name_1 = "X Blur"
            self.attribute_widget_name_2 = "Y Blur"

        #: CONTAINER STR
        if self.attribute_widget == "width":
            self.attribute_widget_name_1 = "Width"
            self.attribute_widget_name_2 = "Height"

        if self.attribute_widget == "border":
            self.attribute_widget_name_1 = "Border"
            self.attribute_widget_name_2 = "Color"
        if self.attribute_widget == "offset":
            self.attribute_widget_name_1 = "Offset"
            self.attribute_widget_name_2 = "Offset"

        if self.attribute_widget == "blur":
            self.attribute_widget_name_1 = "X blur"
            self.attribute_widget_name_2 = "Y blur"

    def build(self):
        Drop_DoubleEntry = ft.Container(
            ink=False,
            bgcolor=ft.Colors.with_opacity(0.5, ft.colors('black')),
            blur = (8,8),
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(1.5, ft.Colors.with_opacity(0.28, ft.colors('white'))),
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
                            value="Width - Height"
                            if self.attribute_widget == "width "
                            else self.attribute_widget.capitalize().replace("_", " "),
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
                        #    colors=[
                        #         ft.Colors.with_opacity(0.04, ft.colors('white')),
                        #         ft.Colors.with_opacity(0.24, ft.colors('white')),
                        #         ft.colors('black38'),
                        #     ],
                        # ),
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    ink=False,
                                    width=68,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_1,
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        # ======================= EVENTS ===========================
                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value=Drop_DoubleEntry,
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    border_radius=ft.border_radius.all(30),
                                    ink=False,
                                    width=68,
                                    content=ft.TextField(
                                        # prefix_text=self.attribute_widget_name_2,
                                        hint_text=self.attribute_widget_name_2,
                                        bgcolor=ft.Colors.with_opacity(0.04, ft.colors('white')),
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        text_align          = ft.TextAlign.CENTER,        # [LEFT,RIGHT,CENTER,JUSTIFY,START,END]
                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value=Drop_DoubleEntry,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

        return Drop_DoubleEntry

    def modify_widget_attributes(
        self,
        config_widget,
        value,
    ):
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

        if config_widget == "width " or config_widget == "height ":
            self.widget.width = (
                value.content.controls[1].content.controls[0].content.value
            )
            self.widget.height = (
                value.content.controls[1].content.controls[1].content.value
            )

        if config_widget == "blur ":
            self.widget.blur = ft.Blur(
                int(value.content.controls[1].content.controls[0].content.value)
                if value.content.controls[1].content.controls[0].content.value
                else 0,
                int(value.content.controls[1].content.controls[1].content.value)
                if value.content.controls[1].content.controls[1].content.value
                else 0,
                ft.BlurTileMode.MIRROR,
            )
        if config_widget == "border ":
            self.widget.border = ft.border.all(
                value.content.controls[1].content.controls[0].content.value,
                value.content.controls[1].content.controls[1].content.value,
            )
        if config_widget == "offset ":
            self.widget.offset = (
                value.content.controls[1].content.controls[0].content.value,
                value.content.controls[1].content.controls[1].content.value,
            )
        if config_widget == "width" or config_widget == "height":
            self.widget.width = (
                value.content.controls[1].content.controls[0].content.value
            )
            self.widget.height = (
                value.content.controls[1].content.controls[1].content.value
            )

        if config_widget == "blur":
            self.widget_tmp = self.page.session.get("SELECTED_SCREEN")  # <== SELECTED PHONE SCREEN
            self.widget_tmp.content.content.content.blur = ft.Blur(
                int(value.content.controls[1].content.controls[0].content.value)
                if value.content.controls[1].content.controls[0].content.value
                else 0,
                int(value.content.controls[1].content.controls[1].content.value)
                if value.content.controls[1].content.controls[1].content.value
                else 0,
                ft.BlurTileMode.MIRROR,
            )
            self.widget = self.widget_tmp

        if config_widget == "border":
            self.widget.border = ft.border.all(
                value.content.controls[1].content.controls[0].content.value,
                value.content.controls[1].content.controls[1].content.value,
            )
        if config_widget == "offset":
            self.widget.offset = (
                value.content.controls[1].content.controls[0].content.value,
                value.content.controls[1].content.controls[1].content.value,
            )
        #: run only in production
        #: print(self.widget.uid)
        #: UPDATE DATA
        try:
            # self.widget.update()
            # self.widget_tmp.update()
            self.page.update()

        except Exception as error:
            self.error_page = self.page.session.get('on_dev')
            self.error_page(
                name_seccion='Error by Dev',
                body_string=error
            )