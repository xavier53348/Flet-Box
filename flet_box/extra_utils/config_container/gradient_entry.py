import flet as ft

# from ..settings_var.settings_widget import GLOBAL_VAR

class GradientEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = GradientEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    # "#94a3b8",
    # "#64748b",
    # "#475569",
    # "#334155",
    # "#1e293b",
    # "#0f172a",

    # "#14b8a6",
    # "#0d9488",
    # "#0f766e",
    # "#115e59",
    # "#134e4a",

    # "#f472b6",
    # "#ec4899",
    # "#db2777",
    # "#be185d",
    color_1 = "Blue"
    color_2 = "Purple"
    color_3 = "Red"
    color_4 = "Orange"

    main_gradient = None
    start_gradient = " bottom_center "
    end_gradient = " top_center "
    data_color = list()

    effects_gradients = {
        " top_left": ft.alignment.top_left,
        " top_center": ft.alignment.top_center,
        " top_right": ft.alignment.top_right,
        " center_left": ft.alignment.center_left,
        " center": ft.alignment.center,
        " center_right": ft.alignment.center_right,
        " bottom_left": ft.alignment.bottom_left,
        " bottom_center": ft.alignment.bottom_center,
        " bottom_right": ft.alignment.bottom_right,
        " top_left ": ft.alignment.top_left,
        " top_center ": ft.alignment.top_center,
        " top_right ": ft.alignment.top_right,
        " center_left ": ft.alignment.center_left,
        " center ": ft.alignment.center,
        " center_right ": ft.alignment.center_right,
        " bottom_left ": ft.alignment.bottom_left,
        " bottom_center ": ft.alignment.bottom_center,
        " bottom_right ": ft.alignment.bottom_right,
    }

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

        self.tooltip="GradientEntry"
        self.attribute_widget = config_widget
        self.id_name_widget_dict = id_name_widget_dict
        # print(self.widget)
        # size textz
        self.text_size = 12 #GLOBAL_VAR(get_global_var="text_size_input")
        self.padding_only = 4 #GLOBAL_VAR(get_global_var="padding_only")
        self.content_padding = 4  # LOBAL_VAR(get_global_var="content_padding")

        if self.attribute_widget == "gradient":
            """top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right"""

            self.options_tmp = [
                ft.dropdown.Option(" None "),
                ft.dropdown.Option(" Linear "),
                ft.dropdown.Option(" Radial "),
            ]
            self.options_tmp_1 = [
                ft.dropdown.Option(" top_left "),
                ft.dropdown.Option(" top_center "),
                ft.dropdown.Option(" top_right "),
                ft.dropdown.Option(" center_left "),
                ft.dropdown.Option(" center "),
                ft.dropdown.Option(" center_right "),
                ft.dropdown.Option(" bottom_left "),
                ft.dropdown.Option(" bottom_center "),
                ft.dropdown.Option(" bottom_right "),
            ]
            self.options_tmp_2 = [
                ft.dropdown.Option(" top_left"),
                ft.dropdown.Option(" top_center"),
                ft.dropdown.Option(" top_right"),
                ft.dropdown.Option(" center_left"),
                ft.dropdown.Option(" center"),
                ft.dropdown.Option(" center_right"),
                ft.dropdown.Option(" bottom_left"),
                ft.dropdown.Option(" bottom_center"),
                ft.dropdown.Option(" bottom_right"),
            ]
            self.attribute_widget_name_1 = self.color_1
            self.attribute_widget_name_2 = self.color_2
            self.attribute_widget_name_3 = self.color_3
            self.attribute_widget_name_4 = self.color_4

    def build(self):
        self.main_gradient_widget = ft.Container(
            ink=False,
            bgcolor="#0e0f11",
            padding=ft.padding.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            border=ft.border.all(2, "#0e0f11"),
            # width=150,
            # width=20
            expand=True,
            height=35,
            content=ft.Dropdown(
                value=" None ",
                width=140,
                content_padding=self.content_padding,
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(30),
                border_color = ft.Colors('transparent'),
                options=self.options_tmp,
                on_change=lambda _: self.modify_widget_attributes(
                    config_widget=_.__dict__.get("data"),
                    value="form_gradient",
                    widget=Drop_GradientEntry,
                ),
            ),
        )
        Drop_GradientEntry = ft.Container(
            ink=False,
            bgcolor="#0c0d0e",
            padding=ft.padding.all(4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(2, ft.colors('black')),
            # width=360,
            expand=True,
            height=150,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor=ft.colors('black38'),
                        padding=ft.padding.all(4),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        height=38,

                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                self.main_gradient_widget,
                                ft.Container(
                                    ink=True,
                                    alignment=ft.alignment.center,
                                    disabled=True,
                                    border_radius=ft.border_radius.all(30),
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.alignment.bottom_center,
                                        colors=[ft.colors('cyan800'), ft.colors('black38')],
                                    ),
                                    content=ft.ElevatedButton(
                                        text=f"Apply {self.attribute_widget.capitalize()}".replace(
                                            "_", " "
                                        ),
                                        color=ft.colors('white'),
                                        on_click=lambda _: self.apply_gradient(),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        bgcolor="#0e0f11",

                        padding=ft.padding.all(2),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(1, ft.colors('black38')),
                        height=36,
                        disabled=True,
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
                                    width=64,
                                    height=35,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_1,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor="#0e0f11",
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,

                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value="color_1",
                                            widget=Drop_GradientEntry,
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    ink=False,
                                    width=64,
                                    height=35,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_2,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor="#0e0f11",
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,
                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value="color_2",
                                            widget=Drop_GradientEntry,
                                        ),
                                    ),
                                ),
                                # ft.Container(width=18),
                                ft.Container(
                                    ink=False,
                                    bgcolor="#0e0f11",
                                    padding=ft.padding.all(0),
                                    alignment=ft.alignment.center,
                                    border_radius=ft.border_radius.all(30),
                                    border=ft.border.all(2, "#0e0f11"),
                                    # width=150,
                                    expand=True,
                                    height=35,
                                    content=ft.Dropdown(
                                        value=" bottom_center ",
                                        width=140,
                                        content_padding=self.content_padding,
                                        alignment=ft.alignment.center_left,
                                        border_radius=ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        options=self.options_tmp_1,
                                        on_change=lambda _: self.modify_widget_attributes(
                                            config_widget=_.__dict__.get("data"),
                                            value="begin gradient",
                                            widget=Drop_GradientEntry,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        bgcolor="#0e0f11",
                        padding=ft.padding.all(2),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(1, ft.colors('black38')),
                        height=36,
                        disabled=True,
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
                                    width=64,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_3,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor="#0e0f11",
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,

                                        # ======================= EVENTS ===========================
                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value="color_3",
                                            widget=Drop_GradientEntry,
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    ink=False,
                                    width=64,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.TextField(
                                        hint_text=self.attribute_widget_name_4,
                                        border_radius =ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        bgcolor="#0e0f11",
                                        color="YELLOW",
                                        text_size=self.text_size,
                                        content_padding=self.padding_only,
                                        on_change=lambda x: self.modify_widget_attributes(
                                            config_widget=self.attribute_widget,
                                            value="color_4",
                                            widget=Drop_GradientEntry,
                                        ),
                                    ),
                                ),
                                # ft.Container(width=18),
                                ft.Container(
                                    ink=False,
                                    bgcolor="#0e0f11",
                                    padding=ft.padding.all(0),
                                    alignment=ft.alignment.center,
                                    border_radius=ft.border_radius.all(30),
                                    border=ft.border.all(2, "#0e0f11"),
                                    # width=150,
                                    expand=True,
                                    height=35,
                                    content=ft.Dropdown(
                                        value=" top_center",
                                        width=140,
                                        content_padding=self.content_padding,
                                        alignment=ft.alignment.center_left,
                                        border_radius=ft.border_radius.all(30),
                                        border_color = ft.Colors('transparent'),
                                        options=self.options_tmp_2,
                                        on_change=lambda _: self.modify_widget_attributes(
                                            config_widget=_.__dict__.get("data"),
                                            value="end gradient",
                                            widget=Drop_GradientEntry,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
        return Drop_GradientEntry

    def apply_gradient(self):
        #: all_data = f"""
        #:                 color 1:        {self.color_1}
        #:                 color 2:        {self.color_2}
        #:                 color 3:        {self.color_3}
        #:                 color 4:        {self.color_4}

        #:                 main gradient:  {self.main_gradient}
        #:                 begin gradient: {self.start_gradient}
        #:                 end gradient:   {self.end_gradient}
        #:                         """
        #: all_x = [self.color_1]
        # print(self.main_gradient)
        if self.main_gradient == " Linear ":
            if self.color_1 and self.color_2:
                if self.color_1 and self.color_2 and self.color_3 and self.color_4:
                    self.data_color = [
                        self.color_1,
                        self.color_2,
                        self.color_3,
                        self.color_4,
                    ]
                elif self.color_1 and self.color_2 and self.color_3:
                    self.data_color = [self.color_1, self.color_2, self.color_3]
                else:
                    self.data_color = [self.color_1, self.color_2]

                self.widget.gradient = ft.LinearGradient(
                    begin=self.effects_gradients.get(self.start_gradient),
                    end=self.effects_gradients.get(self.end_gradient),
                    colors=self.data_color,
                )
        elif self.main_gradient == " Radial ":
            if self.color_1 and self.color_2:
                if self.color_1 and self.color_2 and self.color_3 and self.color_4:
                    self.data_color = [
                        self.color_1,
                        self.color_2,
                        self.color_3,
                        self.color_4,
                    ]
                elif self.color_1 and self.color_2 and self.color_3:
                    self.data_color = [self.color_1, self.color_2, self.color_3]
                else:
                    self.data_color = [self.color_1, self.color_2]

                self.widget.gradient = ft.RadialGradient(
                    colors=self.data_color,
                )
        elif self.main_gradient == " None ":
            self.widget.gradient = (ft.colors('transparent'),)

        self.widget.update()

    def modify_widget_attributes(self, config_widget, value, widget):
        """
        NOTE:

            Will modify all attrib inside the widget that we selected

            on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_GradientEntry),

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

        #: ONLY FOR CONTAINER

        # : print(self.main_gradient_widget.content.value,'asdasd')
        #: widget.content.controls[1].disabled = False
        #: widget.content.controls[1].content.update()
        # : print(self.widget)
        #: self.widget.bgcolor = 'Red'

        if config_widget == " None ":
            widget.content.controls[1].disabled = True
            widget.content.controls[2].disabled = True
            widget.content.controls[0].content.controls[1].disabled = True
            self.widget.gradient = None
            widget.content.update()

        elif config_widget == " Linear ":
            widget.content.controls[1].disabled = False
            widget.content.controls[2].disabled = False

            widget.content.controls[0].content.controls[1].disabled = False
            widget.content.controls[1].content.controls[2].content.disabled = False
            widget.content.controls[2].content.controls[2].content.disabled = False
            widget.content.update()

        elif config_widget == " Radial ":
            widget.content.controls[1].disabled = False
            widget.content.controls[2].disabled = False
            widget.content.controls[0].content.controls[1].disabled = False
            widget.content.controls[1].content.controls[2].content.disabled = True
            widget.content.controls[2].content.controls[2].content.disabled = True
            widget.content.update()

        if self.attribute_widget == "gradient":
            if value == "color_1":
                self.color_1 = (
                    widget.content.controls[1].content.controls[0].content.value
                )
            if value == "color_2":
                self.color_2 = (
                    widget.content.controls[1].content.controls[1].content.value
                )
            if value == "color_3":
                self.color_3 = (
                    widget.content.controls[2].content.controls[0].content.value
                )
            if value == "color_4":
                self.color_4 = (
                    widget.content.controls[2].content.controls[1].content.value
                )

            if config_widget == " Linear ":
                self.main_gradient = config_widget
            if config_widget == " Radial ":
                self.main_gradient = config_widget

            if value == "begin gradient":
                self.start_gradient = config_widget
            if value == "end gradient":
                self.end_gradient = config_widget

        # print(self.widget)
        # self.widget.update()
