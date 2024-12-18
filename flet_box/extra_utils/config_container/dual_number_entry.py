import flet as ft

from ..settings_var.settings_widget import GLOBAL_VAR

personal_configuration: dict = {
    "offset_x": {"minimum": -4, "maximum": 4, "division": 800, "value": 0},
    "offset_y": {"minimum": -4, "maximum": 4, "division": 800, "value": 0},
    "scale": {"minimum": -1, "maximum": 1, "division": 1000, "value": 0},
    "radius": {"minimum": 0, "maximum": 360, "division": 360, "value": 0},
    "margin": {"minimum": 0, "maximum": 300, "division": 300, "value": 0},
    "padding": {"minimum": 0, "maximum": 300, "division": 300, "value": 0},
    "height": {"minimum": 0, "maximum": 4000, "division": 4000, "value": 50},
    "size": {"minimum": 0, "maximum": 4000, "division": 4000, "value": 0},
}

GRADIENT_COLOR = ft.LinearGradient(
    begin=ft.alignment.top_left,
    end=ft.alignment.center_right,
    colors=[
        ft.colors.CYAN_800,
        ft.colors.BLACK38,
    ],
)
GRADIENT_COLOR_BUTTON = ft.LinearGradient(
    begin=ft.alignment.top_center,
    end=ft.alignment.bottom_center,
    colors=[
        ft.colors.BLACK12,
        ft.colors.CYAN_800,
        ft.colors.BLACK12,
    ],
)

testing = ft.Container(
    tooltip="padding",
    bgcolor="red",
    width=240,
    height=240,
    padding=8,
    margin=8,
    content=ft.Container(
        ##################### PROPERTY
        ink=False,  # click effect ripple
        bgcolor="#44CCCC00",  # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
        padding=ft.padding.all(
            8
        ),  # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
        margin=ft.margin.all(
            8
        ),  # outside box                # margin.only (left=8, top=8, right=8, bottom=8),
        alignment=ft.alignment.center,  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
        # border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
        # border=ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
        # image_src=f"/icons/icon-512.png",
        # width=150,
        # height=150,
        # tooltip='Container',
        ##################### EFFECTS
        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
        # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
        ##################### WIDGETS
        # content=ft.ElevatedButton("press container",tooltip='buttom'),
        ##################### EVENTS
        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
    ),  # <=== NOTE COMA
)


class config_number_widget(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(
        self,
        label_widget: str = "X",
        button_name: str = "X",
        number: str = "X",
        widget_to_modify="",
    ):
        super().__init__()
        self.tooltip="config_number_widget"
        self.config_widget = label_widget
        self.button_name = button_name
        self.widget_new = widget_to_modify

        # print(self.widget_new, "xxxxx")

    def build(self):
        self.show_info_bar = ft.Container(
            expand=True,
            alignment=ft.alignment.center_right,
            content=ft.Text(
                value=0,
                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
            ),
        )

        #: WE SET NEW NAME
        self.value_data = personal_configuration.get(self.config_widget)

        self.new_name = self.config_widget
        self.minimum = self.value_data.get("minimum")
        self.maximum = self.value_data.get("maximum")
        self.division = self.value_data.get("division")
        self.value = self.value_data.get("value")

        self.tmp_slider_count = ft.Slider(
            min=self.minimum,
            max=self.maximum,
            divisions=self.division,
            value=self.value,
            overlay_color=ft.colors.RED,
            # ======================= EVENTS ===========================
            on_change=lambda x: self.modify_widget_attributes(
                slider_value=x.control.value,
                slider_widget=self.tmp_slider_count,
                info_tex=self.show_info_bar,
                name_id=self.widget_new,
            ),
        )
        self.text_value = ft.Container(
            ink=True,
            bgcolor="#0e0f11",
            padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            height=30,
            width=30,
            on_click=lambda _: self.apply_config(
                configuration=self.config_widget,
                name_id=self.widget_new,
            ),
            ink_color="red",
            content=ft.Icon(
                name="touch_app",
                # value       = number,
                # font_family = "Consolas", #"Consolas ,RobotoSlab
            ),
        )

        self.Elevation_button = ft.Container(
            ink=False,
            bgcolor=ft.colors.BLACK38,
            padding=ft.padding.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            border=ft.border.all(2, ft.colors.CYAN_900),
            # ink=True,
            ink_color=ft.colors.PURPLE_600,
            # width         = 152,
            height=36,
            gradient=GRADIENT_COLOR_BUTTON,
            content=ft.TextButton(
                text=self.button_name,
            ),
        )

        main_container_config_selection = ft.Row(
            spacing=8,
            run_spacing=0,
            controls=[
                self.text_value,
                ft.Container(
                    ink=False,
                    bgcolor=ft.colors.BLACK38,
                    padding=ft.padding.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    border=ft.border.all(2, ft.colors.CYAN_900),
                    width=152,
                    height=36,
                    gradient=GRADIENT_COLOR,
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                ink=False,
                                width=146,
                                height=30,
                                border_radius=ft.border_radius.all(30),
                                content=self.tmp_slider_count,
                            ),  # <=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                        ],
                    ),
                ),
                self.show_info_bar,
                self.Elevation_button,
            ],
        )
        return main_container_config_selection

    def apply_config(self, configuration="", name_id=""):
        if name_id == "mix_container":
            self.widget_to_modify = GLOBAL_VAR(
                get_global_var="SELECT_DROPP_WIDGET_CONTAINER"
            )
        if name_id == "mix_container_content":
            self.widget_to_modify = GLOBAL_VAR(
                get_global_var="SELECT_DROPP_WIDGET_CONTAINER_CONTENT"
            )

        tmp_value_configuration = personal_configuration.get(configuration).get("value")

        if configuration == "padding":
            self.widget_to_modify.padding = ft.padding.all(tmp_value_configuration)
        if configuration == "margin":
            self.widget_to_modify.margin = ft.margin.all(tmp_value_configuration)
        if configuration == "radius":
            self.widget_to_modify.border_radius = ft.border_radius.all(
                tmp_value_configuration
            )

        if configuration == "size":
            self.widget_to_modify.width = float(tmp_value_configuration)
            self.widget_to_modify.height = float(tmp_value_configuration)

        if configuration == "offset_x" or configuration == "offset_y":
            tmp_x = personal_configuration.get("offset_x").get("value")
            tmp_y = personal_configuration.get("offset_y").get("value")
            self.widget_to_modify.offset = (int(tmp_x), int(tmp_y))

        # print(tmp_value_configuration)
        # print(self.widget_to_modify , "widget_to_edit <<<<<")
        # print(configuration)
        # print(configuration,personal_configuration.get(configuration).get('value'))

        self.widget_to_modify.update()

    def modify_widget_attributes(self, slider_value, slider_widget, info_tex, name_id):
        self.widget_name = self.config_widget

        data_filter = ["padding", "margin", "size"]

        if self.widget_name in data_filter:
            slider_widget.label = int(slider_value)
            info_tex.content.value = int(slider_value)

        else:
            slider_widget.label = f"{slider_value:.1f}"
            info_tex.content.value = f"{slider_value:.1f}"

        if name_id == "mix_container":
            self.widget_to_modify = GLOBAL_VAR(
                get_global_var="SELECT_DROPP_WIDGET_CONTAINER"
            )
        if name_id == "mix_container_content":
            self.widget_to_modify = GLOBAL_VAR(
                get_global_var="SELECT_DROPP_WIDGET_CONTAINER_CONTENT"
            )

        # print(name_id,'<<<<<<>>>>>>>>>',self.widget_to_modify)
        # #:
        # print(self.widget_name, slider_value, "<<<<<<>>>>>>>>>", self.widget_new)
        if self.widget_name == "padding":
            self.widget_to_modify.padding = ft.padding.all(slider_value)
            personal_configuration[self.widget_name][
                "value"
            ] = self.widget_to_modify.padding

        if self.widget_name == "margin":
            self.widget_to_modify.margin = ft.margin.all(slider_value)
            personal_configuration[self.widget_name][
                "value"
            ] = self.widget_to_modify.margin

        if self.widget_name == "radius":
            self.widget_to_modify.border_radius = ft.border_radius.all(slider_value)
            personal_configuration[self.widget_name]["value"] = slider_value

        if self.widget_name == "border":
            self.widget_to_modify.border = slider_value
            personal_configuration[self.widget_name][
                "value"
            ] = self.widget_to_modify.border

        if self.widget_name == "size":
            self.widget_to_modify.width = int(slider_value)
            self.widget_to_modify.height = int(slider_value)
            personal_configuration[self.widget_name][
                "value"
            ] = self.widget_to_modify.height

        if self.widget_name == "offset_x":
            self.widget_to_modify.offset = (
                slider_value,
                personal_configuration.get("offset_y").get("value"),
            )
            personal_configuration[self.widget_name]["value"] = slider_value

        if self.widget_name == "offset_y":
            self.widget_to_modify.offset = (
                personal_configuration.get("offset_x").get("value"),
                slider_value,
            )

            personal_configuration[self.widget_name]["value"] = slider_value

        # # #: UPDATE DATA

        info_tex.content.update()
        slider_widget.update()

        self.widget_to_modify.update()


class DualNumeberEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    widget_content = "data"

    def __init__(self, config_widget="max_lines", widget="", id_name_widget_dict=None):
        super().__init__()

        self.widget = widget
        self.widget_name = config_widget
        self.widget_content = self.widget_content
        self.id_name_widget_dict = id_name_widget_dict
        # print(self.widget_name, self.widget)

    def build(self):
        TmpDualNumeberEntry = ft.Container(
            ink=False,
            bgcolor="#0c0d0e",
            padding=ft.padding.only(left=2, top=8, right=2, bottom=2),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(2, ft.colors.BLACK),
            # width         = 330,
            expand=True,
            # height        = 240,
            content=ft.Column(
                # wrap=True,
                # controls = ,
            ),  # <=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
        )  # <=== NOTE COMA
        self.button_all = ft.Container(
            content=ft.Text(
                value="ALL",
            ),
            alignment=ft.alignment.center,
            padding=0,
            margin=0,
            width=360,
        )

        self.row_main_conttainer = ft.Container(
            content=ft.Row(
                spacing=0,
                run_spacing=0,
                controls=[
                    TmpDualNumeberEntry,
                ],
            )
        )
        self.column_data = ft.Container(
            border=ft.border.all(2, ft.colors.BLACK),
            width=360,
            border_radius=ft.border_radius.all(16),
            gradient=GRADIENT_COLOR_BUTTON,
            ink=True,
            ink_color=ft.colors.RED,
            on_click=lambda _: print("hello"),
            padding=ft.padding.only(left=1, right=1, top=8, bottom=2),
            content=ft.Column(controls=[self.row_main_conttainer, self.button_all]),
        )
        TmpDualNumeberEntry.content.controls.append(
            config_number_widget(
                label_widget="padding",
                button_name="padding",
                widget_to_modify=self.widget_name,
            )
        )
        TmpDualNumeberEntry.content.controls.append(
            config_number_widget(
                label_widget="margin",
                button_name=" margin ",
                widget_to_modify=self.widget_name,
            )
        )
        TmpDualNumeberEntry.content.controls.append(
            config_number_widget(
                label_widget="radius",
                button_name="  border ",
                widget_to_modify=self.widget_name,
            )
        )
        TmpDualNumeberEntry.content.controls.append(
            config_number_widget(
                label_widget="size",
                button_name="    size    ",
                widget_to_modify=self.widget_name,
            )
        )
        TmpDualNumeberEntry.content.controls.append(
            config_number_widget(
                label_widget="offset_x",
                button_name=" offset x ",
                widget_to_modify=self.widget_name,
            )
        )
        TmpDualNumeberEntry.content.controls.append(
            config_number_widget(
                label_widget="offset_y",
                button_name=" offset y ",
                widget_to_modify=self.widget_name,
            )
        )
        return self.column_data


if __name__ == "__main__":

    def main(page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window_left = 0
        page.window_top = 0
        page.window_height = 700
        page.window_width = 400
        page.padding = 0
        page.spacing = 0
        page.add(testing)
        page.add(DualNumeberEntry(widget=testing))
        page.update()

    ft.app(
        target=main,
    )
