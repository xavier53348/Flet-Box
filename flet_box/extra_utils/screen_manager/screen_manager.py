import flet as ft
from ..external_library.sqlite_db import sqlite_db


class screen_phone(ft.Container):
    def __init__(self, data='Erase this test'):
        super().__init__()
        self.expand = True
        self.border_radius = ft.border_radius.all(16)
        self.padding = ft.padding.all(8)
        # self.margin = ft.margin.all(8)
        self.alignment = ft.alignment.center

        # self.shadow = ft.BoxShadow(
        #     spread_radius=1,
        #     blur_radius=15,
        #     color=ft.colors('black'),
        #     offset=ft.Offset(0, 0),
        #     blur_style=ft.ShadowBlurStyle.OUTER,
        # )

    def build(self):
        self.content = ft.Container(
            padding=ft.padding.all(8),
            margin=ft.margin.all(8),
            alignment=ft.alignment.center,
            width=320,
            border_radius=ft.border_radius.all(30),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
        )


class lite_screen_manager(ft.Container):
    selected_text: str = 0

    obtion_list = list()

    def __init__(self, selected_screen: object = None, page: object = None):
        super().__init__()
        self.page = page
        self.selected_screen = selected_screen
        self.ink = False
        self.alignment = ft.alignment.center
        self.list_user_screen()
        # self.user_name = self.page.session.get('user_name')
        # self.user_name = 'kuko53348'


    def build(self):
        self.drop_down = ft.Dropdown(
            border_radius=ft.border_radius.all(16),
            border_width=0,
            width=160,
            label='Select screen',
            options=[
                ft.dropdown.Option(key=f"Screen number: {_}") for _ in self.obtion_list
            ],
            on_change=lambda _: self.change_selected_input(
                payload=_.data)
        )

        self.content = ft.Container(
            width=320,
            padding=ft.padding.all(4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),

            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[

                    # ADD ITEMS
                    ft.IconButton(
                        icon="add",
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.2,
                            color=ft.colors('green')
                        ),
                        on_click=lambda _: self.add_drop_items()
                    ),

                    # DROP DOWN SELECTION ITEMS
                    self.drop_down,

                    # REMOVE ITEMS
                    ft.IconButton(
                        icon="remove",
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.6,
                            color=ft.colors('red')
                        ),
                        on_click=lambda _: self.delete_drop_items()
                    ),

                ],),
        )

    def list_user_screen(self):
        self.obtion_list.clear()
        sqlite_obj = sqlite_db()
        data_returned = sqlite_obj.find_name(
            table_name='user_screen',
            column='user_name',
            # name='kuko53348',
            # name='user_demo',
            name=self.page.session.get('user_name').get('user_name')
        )

        for index, _ in enumerate(data_returned[0]):
            if not _ == "None" and index > 0:
                print(f'index {index} Container')
                self.obtion_list.append(index)
            # else:
            #     print(f'index {index} None')
                # self.obtion_list.append(_)

    def change_selected_input(self, payload):
        # self.selected_text = payload
        # # print(f"event {payload}")

        sqlite_obj = sqlite_db()
        data_returned = sqlite_obj.find_name(
            table_name='user_screen',
            column='user_name',
            # name='kuko53348',
            # name='user_demo',
            name=self.page.session.get('user_name').get('user_name')

        )

        # NECESSARY TAKE SELECTED SCREEN
        self.data_selected = data_returned[0][1]

        self.selected_screen.content.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )

        #  PHONE EDITOR
        self.Build_Phone_Editor = self.page.session.get('user_name_phone')
        self.Build_Phone_Editor.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )

        self.Build_Phone_Editor.update()
        self.page.update()

    def add_drop_items(self):
        return

        print(self.drop_down.options)

    def delete_drop_items(self):
        return
        print(self.drop_down.options)

        # IF ITEMS ARE LESS THAN 0 NO RETURN ERROR
        if len(self.drop_down.options) >= 1:
            self.drop_down.options.pop()

        else:
            print('hello 0')

        self.page.update()

    def load_module_from_string(self, page, string_code: str = str()) -> object:
        import importlib.util
        # import sys

        spec = importlib.util.spec_from_loader('dynamic_module', loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(string_code, module.__dict__)
        # sys.modules['dynamic_module'] = module
        globals()['dynamic_module'] = module

        return dynamic_module.load_module_str()


class go_home_screen(ft.Container):
    # globalVar='Erase this test'

    def __init__(self, page: object = None, main_screen: object = None):
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.main_screen = main_screen

    def build(self):
        self.content = ft.Container(
            width=320,
            # bgcolor=ft.colors('black12'),
            padding=ft.padding.all(8),
            margin=ft.margin.all(8),
            border_radius=ft.border_radius.all(32),

            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.ElevatedButton(
                text="Go main screen",
                bgcolor=ft.Colors.with_opacity(
                    opacity=0.2,
                    color=ft.colors('green')
                ),
                on_click=lambda _: self.go_main_screen(),

            ),
        )

    def go_main_screen(self):
        print('hello <<<<<')
        self.page.views[1].controls[1].visible = False
        self.page.views[1].controls[0].visible = True
        self.page.views[1].update()


class screen_manager(ft.Container):

    def __init__(self, page: object = None, visible: bool = True):
        super().__init__()
        self.page = page
        self.visible = visible
        self.expand = True
        self.bgcolor = ft.colors('black12')
        self.padding = ft.padding.all(8)
        self.margin = ft.margin.all(8)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(32)

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors('black'),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):
        tmp_screen_phone = screen_phone()
        self.content = ft.Column(
            controls=[
                lite_screen_manager(
                    selected_screen=tmp_screen_phone, page=self.page),
                tmp_screen_phone,
                go_home_screen(page=self.page, main_screen=self)
            ],
        )


if __name__ == '__main__':

    def main(page: ft.Page):
        page.scroll = "HIDDEN"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        page.window.left = 8
        page.window.top = 8
        page.window.height = 640
        page.window.width = 320
        page.padding = 8
        page.spacing = 8
        page.expand = True

        screen_1 = screen_manager(page=page)

        page.add(screen_1)
        page.update()

    ft.app(
        target=main,
    )
