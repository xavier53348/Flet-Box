import flet as ft


class SmallPaleteColor(ft.Container):

    def __init__(self,pallete_color: str=''):
        super().__init__()

        self.pallete_color=pallete_color
        self.width = 24
        self.height = 24
    def build(self):
        self.content=ft.Container(
                                ink=False,
                                bgcolor=self.pallete_color,
                                padding= ft.padding.all(0),
                                margin = ft.margin.all(0),
                                alignment=ft.alignment.center,
                                border_radius= ft.border_radius.all(6),
                                border=ft.border.all(1.6, ft.colors.BLACK54),
                        )

        self.on_click = lambda _:print(self.pallete_color)

class Screen_palette(ft.Container):

    def __init__(self,data='Erase this test'):
        super().__init__()

        self.padding  = ft.padding.all(8)
        self.margin   = ft.margin.all(0)    #outside box
        self.alignment= ft.alignment.center
        self.width    = 280
        self.border_radius = 20
        self.gradient=ft.LinearGradient( begin=ft.alignment.top_center,
                                        end=ft.alignment.bottom_center,
                                        colors=[
                                                ft.colors.BLACK12,
                                                ft.colors.BLUE_900,
                                                ft.colors.PURPLE_800,
                                                ft.colors.RED_900,
                                        ],)
        self.shadow = ft.BoxShadow(
                   spread_radius=1,
                   blur_radius=8,
                   color=ft.colors.BLACK26,
                   offset=ft.Offset(0, 0),
                   blur_style=ft.ShadowBlurStyle.OUTER,
             )
    def build(self):
        list_started = False

        screen_1=ft.Row(
                        scroll=True,
                        wrap=True,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                                 ],)
        self.content=screen_1

        for key, value in vars(ft.colors).items():
            if key == "RED_50":
                list_started = True
            if list_started:
                if key ==  'GREY_800':
                    break
                screen_1.controls.append(SmallPaleteColor(pallete_color= value))

if __name__ == '__main__':

    def main(page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_left = 0
        page.window_top = 0
        page.window_height=700
        page.window_width=290
        page.padding=0
        page.spacing=0
        page.add(Screen_palette())
        page.update()

    ft.app(
            target=main,
            )