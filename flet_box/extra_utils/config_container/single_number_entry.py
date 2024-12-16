import flet as ft

# from ..settings_var.settings_widget import GLOBAL_VAR
#


class SingleNumeberEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    widget_content = "data"

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

        self.tooltip="SingleNumeberEntry"
        self.widget_name = config_widget
        self.widget_content = self.widget_content
        self.id_name_widget_dict = id_name_widget_dict

        self.personal_configuration: dict = {
            "image_opacity": {"minimum": 0, "maximum": 1, "division": 100, "value": 0},
            "opacity": {"minimum": 0, "maximum": 1, "division": 100, "value": 0},
            "child_aspect_ratio": {
                "minimum": -1,
                "maximum": 1,
                "division": 1000,
                "value": 0,
            },
            "aspect_ratio": {"minimum": -1, "maximum": 1, "division": 1000, "value": 0},
            "scale": {"minimum": -1, "maximum": 1, "division": 1000, "value": 0},
            "rotate": {"minimum": -3.14, "maximum": 3.14, "division": 3140, "value": 0},
            "size": {"minimum": 0, "maximum": 320, "division": 320, "value": 0},
            "text_size": {"minimum": 0, "maximum": 100, "division": 25, "value": 0},
            "min_lines": {"minimum": 0, "maximum": 300, "division": 300, "value": 0},
            "max_lines": {"minimum": 0, "maximum": 300, "division": 300, "value": 0},
            "runs_count": {"minimum": 0, "maximum": 300, "division": 300, "value": 0},
            "run_spacing": {"minimum": 0, "maximum": 300, "division": 300, "value": 0},
            "spacing": {"minimum": 0, "maximum": 300, "division": 300, "value": 0},
            "max_extent": {"minimum": 0, "maximum": 100, "division": 100, "value": 0},
            "border_width": {"minimum": 0, "maximum": 100, "division": 100, "value": 0},
            "elevation": {"minimum": 0, "maximum": 100, "division": 100, "value": 0},
            "spread_radius": {
                "minimum": 0,
                "maximum": 100,
                "division": 100,
                "value": 0,
            },
        }

        #: WE SET NEW NAME
        self.value_data = self.personal_configuration.get(config_widget)

        self.new_name = config_widget
        self.minimum = self.value_data.get("minimum")
        self.maximum = self.value_data.get("maximum")
        self.division = self.value_data.get("division")
        self.value = self.value_data.get("value")

    def build(self):
        tmp_slider_count = ft.Slider(
            min=self.minimum,
            max=self.maximum,
            divisions=self.division,
            value=self.value,
            overlay_color=ft.colors('red'),
            # ======================= EVENTS ===========================
            # on_change   = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = SingleNumeberEntry),
            on_change=lambda x: self.modify_widget_attributes(
                slider_value=x.control.value,
                slider_widget=tmp_slider_count,
            ),
        )
        SingleNumeberEntry = ft.Container(
            ink=False,
            bgcolor="#0c0d0e",
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(2, ft.colors('black')),
            width=165,
            height=80,
            content=ft.Column(
                wrap=True,
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor="#0e0f11",
                        padding=ft.padding.only(left=12, top=0, right=12, bottom=0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        height=20,
                        content=ft.Text(
                            value=self.new_name,
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                        ),
                    ),  # <=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                    ft.Container(
                        ink=False,
                        bgcolor=ft.colors('black38'),
                        padding=ft.padding.all(2),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(2, ft.colors('cyan900')),
                        width=152,
                        height=36,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.center_right,
                            colors=[ft.colors('cyan800'), ft.colors('black38')],
                        ),
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    ink=False,
                                    # bgcolor       = "#44CCCC00",
                                    width=146,
                                    height=30,
                                    border_radius=ft.border_radius.all(30),
                                    content=tmp_slider_count,
                                ),  # <=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                            ],
                        ),
                    ),  # <=== NOTE COMA,
                ],
            ),  # <=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
        )  # <=== NOTE COMA

        return SingleNumeberEntry

    def modify_widget_attributes(self, slider_value, slider_widget):
        slider_widget.label = f"{slider_value:.2f}"
        slider_widget.update()
        # print(self.widget, "single")

        #:
        if self.widget_name == "image_opacity":
            self.widget.image.opacity =  1 - slider_value

        if self.widget_name == "scale":
            self.widget.scale = 1 - slider_value
        if self.widget_name == "aspect_ratio":
            self.widget.aspect_ratio = 1 - slider_value
        if self.widget_name == "opacity":
            self.widget.opacity = 1 - slider_value

        if self.widget_name == "child_aspect_ratio":
            self.widget.child_aspect_ratio = 1 - slider_value

        if self.widget_name == "spread_radius":
            self.widget.spread_radius = slider_value
        if self.widget_name == "size":
            self.widget.size = slider_value
        if self.widget_name == "elevation":
            self.widget.elevation = slider_value
        if self.widget_name == "runs_count":
            self.widget.runs_count = slider_value
        if self.widget_name == "run_spacing":
            self.widget.run_spacing = slider_value
        if self.widget_name == "spacing":
            self.widget.spacing = slider_value
        if self.widget_name == "max_extent":
            self.widget.max_extent = slider_value
        if self.widget_name == "min_lines":
            self.widget.min_lines = slider_value
        if self.widget_name == "max_lines":
            self.widget.max_lines = slider_value
        if self.widget_name == "border_width":
            self.widget.border_width = slider_value
        if self.widget_name == "text_size":
            self.widget.text_size = slider_value
        if self.widget_name == "rotate":
            self.widget.rotate = slider_value

        #: UPDATE DATA
        self.widget.update()


if __name__ == "__main__":

    def main(page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window_left = 0
        page.window_top = 0
        page.window_height = 700
        page.window_width = 290
        page.padding = 0
        page.spacing = 0
        page.add(SingleNumeberEntry())
        page.update()

    ft.app(
        target=main,
    )
