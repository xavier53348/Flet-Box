import flet as ft
import os


class PhotoSelection(ft.Container):
    def __init__(self, photo_selection: str = ""):
        super().__init__()
        self.tooltip = "PhotoSelection"
        self.photo_selection = photo_selection
        self.width = 50
        self.height = 50
        self.border_radius = ft.border_radius.all(12)

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=4,
            color=ft.Colors.with_opacity(1, ft.colors('black12')),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):
        self.container = ft.Container(
            image=ft.DecorationImage(
                fit=ft.ImageFit.COVER,
                src=self.photo_selection.split('/')[2],
            ),
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(12),
            on_hover=lambda _: self.active_border_color(
                border_container=self.container
            ),
        )

        self.content = self.container
        # self.on_click = lambda _:print(self.photo_selection)
        self.on_click = lambda _: self.modify_widget()

    def active_border_color(self, border_container: object = None):
        border_container.border = (
            ft.border.all(2, ft.colors('transparent'))
            if border_container.border == ft.border.all(2, ft.colors('white54'))
            else ft.border.all(2, ft.colors('white54'))
        )
        border_container.update()

    def modify_widget(self):
        print("[+] change content tab [ photo_selection.py ]")

        attribute_name_image = self.page.session.get(
            'set_attribute_image')  # <== SET (BGCOLOR, ...)
        edit_widget_image = self.page.session.get('set_edit_widget_image')  # <== SET (ft.Container, Image)

        #: SET ATTRIBUTES
        if attribute_name_image == "image_src":
            edit_widget_image.image = ft.DecorationImage(
                src=self.photo_selection.split('/')[2],
                fit=ft.ImageFit.COVER,  #: CONTAIN, FILL, FIT_WIDTH, SCALE_DOWN, COVER, FIT_HEIGHT, NONE
                # opacity=0.06,
            )

        if attribute_name_image == "image_src ":
            self.phone_image = self.page.session.get('SELECTED_SCREEN')

            if self.phone_image.content.content.content.image:
                self.phone_image.image = None
                self.phone_image.content.content.content.image = None
                self.phone_image.update()

            else:
                # self.phone_image.content.content.content.image = None

                self.phone_image.image = ft.DecorationImage(
                   src=self.photo_selection.split('/')[2],
                    fit=ft.ImageFit.COVER,  #: CONTAIN, FILL, FIT_WIDTH, SCALE_DOWN, COVER, FIT_HEIGHT, NONE
                    # opacity=0.06,
                )
            self.phone_image.update()
        # self.page.update()


class ScreenPhotoSelection(ft.Container):
    def __init__(self, data="Erase this test"):
        super().__init__()

        self.padding = ft.padding.only(left=0, top=2, bottom=2, right=0)
        self.margin = ft.margin.all(0)  # outside box
        self.alignment = ft.alignment.top_center
        self.border = ft.border.all(1, ft.colors('white38'))
        self.border_radius = 32
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.center_left,
            colors=[
                ft.Colors.with_opacity(0.7, ft.colors('teal400')),
                ft.colors('black26'),
            ],
        )
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=18,
            # color        = ft.Colors.with_opacity(0.3,ft.colors('teal400')),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        # self.blur = (12,12)

    def build(self):
        screen_1 = ft.Row(
            scroll=True,
            wrap=True,
            spacing=2,
            run_spacing=2,
            controls=[
                ft.Container(
                    width=320,
                    padding=8,
                    content=ft.ElevatedButton(
                        text='Close Image List',
                        icon="crisis_alert_rounded",
                        on_click=lambda _:self.show_menu_tab_editor(),
                    )
                ),

            ],
        )
        self.content = ft.Container(
            # bgcolor  = ft.colors.RED,
            border_radius=12,
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            # on_click=lambda _: self.validate_click(),
            content=screen_1,
        )
        current_dir_path = os.path.relpath(
            # path="./test/proyect_name/proyect_name/assets"
            path="flet_box/assets"
        )
        basename_dict = self.selection_photo_files(
            path_to_check_filename=current_dir_path
        )

        for _ in basename_dict:
            tmp_path = basename_dict.get(_)
            full_path = os.path.join(current_dir_path, tmp_path)
            screen_1.controls.append(PhotoSelection(photo_selection=full_path))

    def show_menu_tab_editor(self):
        "CLICK IN PHOTO SELECTION"
        print("selection data [+] photo_selection.py")
        self.tab_container = self.page.session.get('PHOTO_SELECTION')

        self.tab_container.controls[0].visible = True
        self.tab_container.controls[1].visible = False
        self.tab_container.controls[2].visible = False
        self.tab_container.update()

        #: UPDATE DATA
        try:
            self.tab_container.update()
        except Exception as error:
            self.error_page = self.page.session.get('on_dev')
            self.error_page(
                name_seccion='Error by Dev',
                body_string=error
            )

    def selection_photo_files(self, path_to_check_filename: str = ""):
        all_files_list = os.listdir(path_to_check_filename)
        basename_dict: dict = {}

        for full_name in all_files_list:
            curren_name = os.path.splitext(full_name)[0]
            basename_dict[curren_name] = full_name

        return basename_dict


if __name__ == "__main__":

    def main(page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window_left = 0
        page.window_top = 0
        page.window_height = 600
        page.window_width = 800
        page.padding = 0
        page.spacing = 0
        page.add(ScreenPhotoSelection())
        page.update()

    ft.app(
        target=main,
    )
