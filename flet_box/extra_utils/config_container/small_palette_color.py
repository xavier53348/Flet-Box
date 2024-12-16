import flet as ft

from ..config_container.color_entry import ColorEntry

click_avalidation: bool = False


class SmallPaleteColor(ft.Container):
    def __init__(self, pallete_color: str = ""):
        super().__init__()
        self.pallete_color = pallete_color
        self.width = 24
        self.height = 24

    def build(self):
        self.container = ft.Container(
            ink=False,
            tooltip=self.pallete_color,
            bgcolor=self.pallete_color,
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(6),
            # border       = ft.border.all(1.6, ft.colors.WHITE12),
            on_hover=lambda _: self.active_border_color(
                border_container=self.container
            ),
            # on_click=lambda _: self.modify_widget(),
        )
        self.content = self.container

        self.on_click = lambda _: self.change_color_widget(color=self.pallete_color)

    def change_color_widget(self, color: str = ""):
        self.attibute_color = self.page.session.get('set_attribute_color')
        self.widget_color = self.page.session.get('set_edit_widget_color')

        # : SET ATTRIBUTES
        if self.attibute_color == "bgcolor":
            self.widget_color.bgcolor = color
        if self.attibute_color == "focused_bgcolor":
            self.widget_color.focused_bgcolor = color
        if self.attibute_color == "border_color":
            self.widget_color.border_color = color
        if self.attibute_color == "focused_border_color":
            self.widget_color.focused_border_color = color
        if self.attibute_color == "color":
            self.widget_color.color = color
        if self.attibute_color == "icon_color":
            self.widget_color.icon_color = color
        if self.attibute_color == "check_color":
            self.widget_color.check_color = color
        if self.attibute_color == "fill_color":
            self.widget_color.fill_color = color

        if self.attibute_color == "shadow_color":
            self.widget_color.parent.shadow = ft.BoxShadow(
                                           spread_radius= 1,
                                           blur_radius  = 15,
                                           color        = color,
                                           offset       = ft.Offset(0, 0),
                                           blur_style   = ft.ShadowBlurStyle.OUTER,
            )

        # print(self.widget_color)
        # print(self.widget_color.parent)
        self.page.update()

    def active_border_color(self, border_container):
        border_container.border = (
            ft.border.all(2, ft.colors('transparent'))
            if border_container.border == ft.border.all(2, ft.colors('white'))
            else ft.border.all(2, ft.colors('white'))
        )
        border_container.update()


class Screen_palette(ft.Container):
    def __init__(self, data="Erase this test"):
        super().__init__()

        self.padding = ft.padding.all(8)
        self.margin = ft.margin.all(0)  # outside box
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(20)
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.center_right,
            colors=[
                ft.colors('black12'),
                ft.colors('blue900'),
                ft.colors('purple800'),
                ft.colors('blue600'),
                ft.colors('black12'),
            ],
        )

    def build(self):
        list_started = False

        screen_1 = ft.Row(
            scroll=True,
            wrap=True,
            spacing=0.08,
            run_spacing=0.08,
            controls=[
                    ft.Container(
                            width=320,
                            padding=8,
                            content=ft.ElevatedButton(
                                text='Close Color List',
                                icon="crisis_alert_rounded",
                                on_click=lambda _:self.show_menu_tab_editor(),
                                )
                            ),
            ],
        )
        self.content = screen_1

        for key, value in vars(ft.colors).items():
            if key == "PRIMARY":
                list_started = True
            if list_started:
                if key == "GREY_800":
                    break
                screen_1.controls.append(SmallPaleteColor(pallete_color=value))

    def show_menu_tab_editor(self):
        "CLICK IN PHOTO SELECTION"
        print("selection data [+] photo_selection.py")
        self.tab_container = self.page.session.get('PHOTO_SELECTION')

        self.tab_container.controls[0].visible = True
        self.tab_container.controls[1].visible = False
        self.tab_container.controls[2].visible = False
        self.tab_container.update()


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
        page.add(Screen_palette())
        page.update()

    ft.app(
        target=main,
    )
