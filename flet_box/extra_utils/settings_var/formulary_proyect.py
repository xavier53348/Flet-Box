import flet as ft


class sitch_selection(ft.Container):

    def __init__(self,
                 text_value: str = 'Test Value',
                 bool_value: bool = False,
                 ):
        super().__init__()
        self.text_value = text_value
        self.bool_value = bool_value
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center

    def build(self):
        self.content = ft.CupertinoSwitch(
            label=self.text_value,
            value=self.bool_value,
        )


class check_box(ft.Container):

    def __init__(self,
                 text_value: str = 'Test Value',
                 bool_value: bool = False,

                 ):
        super().__init__()
        self.text_value = text_value

        self.bool_value = bool_value
        self.expand = True
        self.ink = False
        self.padding = ft.padding.all(4)
        self.margin = ft.margin.all(4)
        self.alignment = ft.alignment.center

    def build(self):
        self.content = ft.Checkbox(
            value=self.bool_value,
            label=self.text_value,
            check_color=ft.colors.GREY,
            fill_color={
                ft.MaterialState.HOVERED: ft.colors.CYAN,
                ft.MaterialState.FOCUSED: ft.colors.RED,
                ft.MaterialState.DEFAULT: ft.colors.BLACK12,
            },
        )  # <=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR


class input_field(ft.Container):

    def __init__(self,
                 info_text: str = "Text exemple"
                 ):
        super().__init__()
        self.info_text = info_text
        self.expand = True
        self.ink = False
        self.padding = ft.padding.all(2)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.colors.BLACK,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):
        self.content = ft.TextField(
            label=self.info_text,
            bgcolor='dark',
            prefix_icon=ft.icons.COLOR_LENS,
            min_lines=1,
            border_color=ft.colors.BLACK12,
            focused_border_color='CYAN,0.4',
            border_radius=32,
            border_width=1,
            capitalization=True,
            text_size=16,
        )


class formulary_export(ft.Container):

    def __init__(self, data='Erase this test'):
        super().__init__()

        self.title = data
        self.padding = ft.padding.all(25)
        self.margin = ft.margin.all(12)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.blur = (20, 20)

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.BLACK,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):
        self.content = ft.Column(
            #: PROPERTY BOX
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,
            run_spacing=8,
            #: WIDGETS
            controls=[
                ft.Text(value="FLET-BOX\nLet's create your App..",
                        size=40,
                        width=440,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        ),

                ft.Row(
                    #: PROPERTY BOX
                    controls=[
                        input_field(info_text="Project name"),
                        sitch_selection(
                            text_value='Over write project', bool_value=True),
                    ],
                ),
                ft.Row(
                    controls=[
                        input_field(info_text="Python version"),
                        sitch_selection(
                            text_value=' Index old project', bool_value=True),
                    ]
                ),
                ft.Row(
                    #: PROPERTY BOX
                    controls=[
                        input_field(info_text="App version"),
                        input_field(info_text="Build number"),
                    ],
                ),
                input_field(info_text="Description"),
                ft.Row(
                    #: PROPERTY BOX
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value="Select plataform",
                                size=24,

                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",),
                    ],
                ),

                ft.Row(
                    #: PROPERTY BOX
                    controls=[

                    check_box(text_value="Android", bool_value=True),
                    check_box(text_value="iphone",  bool_value=False),
                    check_box(text_value="Windows", bool_value=False),
                    check_box(text_value="Linux",   bool_value=False),
                    check_box(text_value="MacOS",   bool_value=False),

                    ],),
                ft.Row(
                    #: PROPERTY BOX

                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=32,
                    run_spacing=32,
                    controls=[

                        ft.ElevatedButton(
                            text="Accept",
                            #: COLOR
                            icon="Home",
                            bgcolor='Cyan,0.2',
                            #: ATTRIB
                            elevation=12,
                            #: POSITION
                            scale=1.5,
                        ),

                        ft.ElevatedButton(
                            scale=1.5,
                            text="Cancel",
                            #: COLOR
                            icon="Home",
                            bgcolor='red,0.4',
                            #: ATTRIB
                            elevation=12,
                            #: POSITION
                        )
                    ],),
            ],

        )


if __name__ == "__main__":

    def main(page: ft.Page):
        # page.scroll = "HIDDEN"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        page.window.bgcolor = ft.colors.RED_100
        page.window.left = 3
        page.window.top = 3
        page.window.height = 720
        page.window.width = 650
        page.padding = 0
        page.spacing = 0
        page.add(formulary_export())

    ft.app(target=main)
