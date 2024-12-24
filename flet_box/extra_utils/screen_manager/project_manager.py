import flet as ft
import random

testing = False

# COMENT THIS 2 LINES IN TESTING
from ..external_library.sqlite_db import sqlite_db
testing = True


class screen_phone(ft.Container):
    def __init__(self, data='Erase this test'):
        super().__init__()
        self.expand = True
        self.border_radius = ft.border_radius.all(16)
        self.padding = ft.padding.all(8)
        self.alignment = ft.alignment.center

    def build(self):
        self.content = ft.Container(
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            width=320,
            border_radius=ft.border_radius.all(2),
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
    old_payload = 0
    obtion_list = list()

    def __init__(self, selected_screen: object = None, page: object = None):
        super().__init__()
        self.page = page
        self.selected_screen = selected_screen
        self.ink = False
        self.alignment = ft.alignment.center

        # COMENT IF WILL DEV IN NORMAL MODE
        if testing:
            self.list_user_screen()

    def build(self):
        self.drop_down = ft.Dropdown(
            border_radius=ft.border_radius.all(16),
            border_width=0,
            width=160,
            label='Select screen',
            options=[
                ft.dropdown.Option(
                    key=f"Screen number: {_}"
                ) for _ in self.obtion_list
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

                    # UPDATE ITEMS
                    ft.IconButton(
                        icon="update",
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.6,
                            color=ft.colors('blue')
                        ),
                        on_click=lambda _: self.update_drop_items()
                    ),
                ],),
        )

    def update_drop_items(self):
        self.list_user_screen()
        self.drop_down.options = [ft.dropdown.Option(key=f"Screen number: {_}") for _ in self.obtion_list]
        self.drop_down.update()

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

        if self.old_payload == payload:
            # ESCAPE ERROR MULTYPLES THREATHS
            # ONLY NEW SUBMIT WILL BE AVIABLES
            # if self.old_payload:
            #     # IF PRESS DOUBLE CLICK IN SAME PAGE WILL NO CONTINUE
            #     self.old_payload = False
            #     self.drop_down.options.clear()
            #     self.drop_down.update()
            #     return

            # self.old_payload = True
            self.drop_down.options.clear()
            self.drop_down.update()

            return

        self.old_payload = payload
        print(f"changing {payload}")

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
        # self.selected_screen.content.content = ft.Container(bgcolor="red",height=120,width=120)
        self.selected_screen.content.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )

        # WRITE IN  PHONE EDITOR
        self.Build_Phone_Editor = self.page.session.get('user_name_phone')
        self.Build_Phone_Editor.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )
        self.Build_Phone_Editor.update()
        #

        self.drop_down.options.clear()

        self.updating_phone(phone_attrib=self.Build_Phone_Editor.content.content)

        self.page.update()


    def updating_phone(self,phone_attrib: object=None):
        phone_attrib = phone_attrib
        print(self.Build_Phone_Editor.content.content.bgcolor,"<<<<<")
        print(self.Build_Phone_Editor.content.content.content.bgcolor,"<<<<<")
        print(self.Build_Phone_Editor.content.content.image)

        # main_container in export data
        self.Build_Phone_Editor.parent.image=self.Build_Phone_Editor.content.content.image
        self.Build_Phone_Editor.parent.gradient=self.Build_Phone_Editor.content.content.gradient

        # second_container
        self.Build_Phone_Editor.content.content.bgcolor=self.Build_Phone_Editor.content.content.content.bgcolor
        self.Build_Phone_Editor.content.content.blur=self.Build_Phone_Editor.content.content.content.blur
        # self.Build_Phone_Editor.content.content.padding=self.Build_Phone_Editor.content.content.content.padding

        # self.Build_Phone_Editor.content.content.padding='red'
        # self.Build_Phone_Editor.parent.blur=(0,0)

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
        tmp_module = dynamic_module.load_module_str()
        return tmp_module


class go_home_screen(ft.Container):

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
                    selected_screen=tmp_screen_phone,
                    page=self.page
                ),
                tmp_screen_phone,
                go_home_screen(
                    page=self.page,
                    main_screen=self
                )
            ],
        )


class projects_made(ft.Container):
    def __init__(self, data='Erase this test'):
        super().__init__()
        self.border_radius = ft.border_radius.all(30)
        self.margin = ft.margin.all(0)
        self.padding = ft.padding.all(4)
        self.alignment = ft.alignment.center
        self.bgcolor = ft.Colors.with_opacity(0.05, ft.colors('white'))
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, ft.colors('black')),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):
        self.ink = True
        self.ink_color = ft.Colors.with_opacity(0.8, ft.colors('cyan'))
        self.on_click = lambda _: print('hello')

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    run_spacing=0,

                    controls=[
                        ft.IconButton(
                            # bgcolor='white',
                            icon=ft.icons('star'),
                            selected_icon=ft.icons('star'),
                            selected=False,
                        ),  # for _ in range(3)

                        ft.Text(
                            text_align=ft.TextAlign.CENTER,
                            expand=True,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                            color=ft.Colors.with_opacity(
                                0.8, ft.colors('white')),
                            value="0"
                        ),  # for _ in range(3)
                    ]
                ),
                ft.Text(
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD,
                    font_family="Consolas",  # "Consolas ,RobotoSlab
                    color=ft.Colors.with_opacity(0.7, ft.colors('cyan')),
                    size=13,
                    value='testing first demo app',
                ),

            ]
        )


class project_manager(ft.Container):
    TABS_PROJECTS: list = {
        # 'Login',
        # 'Menu',
        # 'Profile',
        # 'Slider Image',
        # 'Splash',
        # 'Time Line',
        'About': ft.Icons('account_box'),
        'Article': ft.Icons('article'),
        'Chat': ft.Icons('chat'),
        'DashBoard': ft.Icons('dashboard'),
        'Grid View': ft.Icons('grid_view_rounded'),
        'List': ft.Icons('grading'),
        'Music': ft.Icons('speaker_group_rounded'),
        'No Item Page': ft.Icons('do_not_touch'),
        'Payment': ft.Icons('account_balance_wallet'),
        'Search Page': ft.Icons('find_in_page'),
        'Settings': ft.Icons('settings'),
        'Shopping': ft.Icons('shopping_bag'),
        'Verification': ft.Icons('verified'),
    }

    def __init__(self, page: object = None, visible: bool = True):
        super().__init__()
        self.page = page
        self.expand = True
        self.visible = visible

    def build(self):

        self.nav_rail = ft.NavigationRail(
            # selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            elevation=20,
            indicator_color=ft.Colors.with_opacity(0.2, ft.colors('red')),
            min_width=100,
            min_extended_width=200,
            extended=True,
            leading=ft.FloatingActionButton(
                height=50,
                icon=ft.Icons('generating_tokens'),
                text="Apply project",
                # on_click=lambda e: self.change_rail_extended(),
            ),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icon(self.TABS_PROJECTS.get(tabs_name)),
                    selected_icon=ft.Icon(ft.Icons.SCREEN_SHARE),
                    label=tabs_name,

                ) for tabs_name in self.TABS_PROJECTS
            ],
            on_change=lambda e: self.change_rail_position(
                index_rail=e.control.selected_index),
        )

        self.middle_container = ft.Container(
            expand=True,
            ink=False,
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.all(8),
            margin=ft.margin.all(8),
            alignment=ft.alignment.center,
            bgcolor=ft.colors('black12'),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            #: WIDGETS
            content=ft.GridView(
                #: PROPERTY GRIDVIEW
                runs_count=3,
                run_spacing=8,
                padding=8,
                spacing=8,
                expand=1,
                max_extent=100,
                #: WIDGETS
                controls=[
                    # projects_made() for _ in range(20)
                ],
            ),
        )  # <=== NOTE COMA

        self.content = ft.Row(
            controls=[
                # NAV RAIL
                self.nav_rail,

                # RIGHT WIDGETS
                self.middle_container,
                # screen_phone(),
                screen_manager(page=self.page)
            ],
            # expand=True,
        )

    def change_rail_position(self, index_rail: int = int()):
        self.grid_widget = self.middle_container.content
        self.grid_widget.controls.clear()

        # print(index_rail)

        match index_rail:
            case 0:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(0,9))]

            case 1:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(0,9))]

            case 2:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 3:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 4:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 5:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 6:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 7:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 8:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 9:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 10:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 11:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

            case 12:
                self.grid_widget.controls = [projects_made() for _ in range(random.randint(1,9))]

        self.grid_widget.update()

    def change_rail_extended(self, ):
        # self.nav_rail.leading = self.nav_rail.destinations[index_rail]
        self.nav_rail.extended = True if not self.nav_rail.extended else False
        self.page.update()


if __name__ == '__main__':

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT DARK
        screen_1 = project_manager(page=page)
        page.add(screen_1)
        page.update()

    ft.app(
        target=main,
    )
