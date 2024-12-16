import flet as ft

from extra_utils import Build_Drag_Editor
from extra_utils import Build_Phone_Editor
from extra_utils import Build_Editor

from extra_utils import MenuUpContainer  #: TAB MENU CONTAINER
from extra_utils import MenuLeftContainer
from extra_utils import LiteMenuDownContainer
from extra_utils import LiteMenuUpContainer  #: LITE MENU RIGHT PHONE AND DOWN
from extra_utils import login_page  #: LOGIN PAGE
from extra_utils import screen_manager  #: LOGIN PAGE

class header_container(ft.Container):

    def __init__(self, page):
        super().__init__()
        self.ink = False
        self.page = page
        self.alignment = ft.alignment.center
        self.margin = ft.margin.all(0)
        self.padding = ft.padding.all(0)
        self.visible = True if self.page.window.width >= 640.0 else False

    def build(self):
        self.content = ft.Row(
            scroll=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            run_spacing=0,
            controls=[
                MenuUpContainer(page=self.page)
            ]
        )


class row_middle_container(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)
        self.border_radius = ft.border_radius.all(30)
        self.expand = True
        self.ink = False

        # DRAG CONTAINER
        self.drag_container = Build_Drag_Editor(page=self.page)

        # PHONE CONTAINER
        self.phone_container = Build_Phone_Editor(
            page=self.page,
            color_data=ft.colors("black12")
        ).build()

        #  CONFIG PHONE CONTAINER
        self.config_widget_container = ft.Container(
            alignment=ft.alignment.center,
            visible=False if self.page.width <= 1040 else True,
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            border_radius=ft.border_radius.all(30),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=True,
                controls=[

                    Build_Editor(
                        page=self.page,
                        main_phone=self.phone_container,
                    )
                ]
            )
        )
        # # CHECK WINDOWS SIZE
        # if self.page.window.width <= 270:
        #     self.config_widget_container.visible=False

        self.page.session.set("SELECTED_SCREEN", self.phone_container)

    def build(self):
        self.content = ft.Row(
            spacing=4,
            # expand = True,
            controls=[
                ft.Container(
                    padding=ft.padding.all(0),
                    border_radius=ft.border_radius.all(30),
                    bgcolor='cyan,0.08',
                    width=60,

                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[

                            MenuLeftContainer(
                                page=self.page,
                                phone_container=self.drag_container,
                                menu_right_container=self.config_widget_container,
                            ),
                        ]
                    )
                ),
                ft.Container(
                    # visible=False,
                    border_radius=ft.border_radius.all(48),
                    content=ft.Row(
                        scroll="ALLWAYS",
                        controls=[
                            #: drag_container/widget_drag_editor.py
                            self.drag_container
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.all(0),
                    margin=ft.margin.all(0),
                    # border_radius=ft.border_radius.all(30),
                    expand=True,
                    # bgcolor="red",
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            # header_container(page=self.page),
                            #: phone_container/widget_phone_editor.py
                            ft.Container(expand=True),
                            #
                            LiteMenuUpContainer(
                                page=self.page,
                                menu_left_container=self.drag_container,
                                phone_widget_container=self.phone_container,
                                menu_right_container=self.config_widget_container,
                            ),
                            ft.Container(expand=True),
                            self.phone_container,
                            ft.Container(expand=True),
                        ]
                    )
                ),
                self.config_widget_container,
            ]
        )


class footer_container(ft.Container):

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.visible = True
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.ink = False
        self.margin = ft.margin.all(0)
        self.padding = ft.padding.all(2)

    def build(self):
        self.content = ft.Row(
            # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,          # space widget left right
            run_spacing=0,      # space widget up down
            controls=[
                header_container(page=self.page),
                LiteMenuDownContainer(),
                ft.Container(width=285),
            ]
        )


class column_container(ft.Container):
    bgcolor_container = "Dark"

    def __init__(self, page: object = None):
        super().__init__(
        )
        self.page = page
        self.alignment = ft.alignment.center
        self.image = ft.DecorationImage(
            src='designer_1.jpeg',
            fit=ft.ImageFit.COVER,  #: CONTAIN, FILL, FIT_WIDTH, SCALE_DOWN, COVER, FIT_HEIGHT, NONE
            opacity=0.08 if self.page.window.width <= 620 else 0.2,
        )
        self.expand = True
        self.ink = False
        self.margin = ft.margin.all(0)
        self.padding = ft.padding.only(
            left=8,
            top=8,
            right=8,
            bottom=8
        )

    def build(self):
        self.content = ft.Container(
            blur=(18, 18),

            content=ft.Column(
                spacing=8,
                run_spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[

                    row_middle_container(page=self.page),
                    footer_container(page=self.page),
                ],
            ))


class flet_box:
    ONLY_CONTROLS_ADDING_IN_APP: list = [
        'Row',
        "GridView",
        "Column",
        "Stack",
        "ResponsiveRow",
        "ListView",
    ]

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.main()

    def main(self):
        #
        self.page.session.set("list_filter_controls",
                              self.ONLY_CONTROLS_ADDING_IN_APP)

        self.page.window.focused = True
        self.page.scroll = "HIDDEN"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # self.page.theme_mode = ft.ThemeMode.DARK # ft.ThemeMode.LIGHT

        self.page.window.maximizable = True
        self.page.window.left = 3
        self.page.window.top = 3
        self.page.padding = 0
        self.page.spacing = 0

        # self.page.window.width=365
        # self.page.window.width=360
        # self.page.window.width=761
        # self.page.window.width=860
        # print(self.page.window.width)
        self.setting_only_append_controls()

        def route_change(route):
            """
            ALWAYS WILL BE CHANGE TO NEW USER TO ROOT '/' PAGE

            :param      route:  The route
            :type       route:  { type_description }
            """
            # print(self.page.window.width)
            print(f"Session id: {self.page._session_id} width: {self.page.width}")

            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    padding=0,
                    route="/",
                    controls=[
                        login_page(page=self.page),
                    ],
                )
            )
            if self.page.route == "/home":
                self.page.views.append(
                    ft.View(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        padding=0,
                        route="/home",
                        controls=[
                            column_container(page=self.page),
                            screen_manager(page=self.page,visible=False),
                        ],
                    )
                )
            # if self.page.route == "/screen_manager":
            #     self.page.views.append(
            #         ft.View(
            #             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            #             vertical_alignment=ft.MainAxisAlignment.CENTER,
            #             padding=0,
            #             route="/screen_manager",
            #             controls=[
            #                 screen_manager(page=self.page),
            #             ],
            #         )
            #     )
            self.page.update()

        self.page.on_route_change = route_change
        self.page.theme_mode = ft.ThemeMode.DARK

        # FIRST SCREEN
        # self.page.go('/home')
        self.page.go('/')
        # self.page.go('/screen_manager')

    def setting_only_append_controls(self):
        self.widgetFilter = [_.lower()
                             for _ in self.ONLY_CONTROLS_ADDING_IN_APP]
        self.page.session.set("ONLY_CONTROLS_ADDING_IN_APP", self.widgetFilter)


if __name__ == "__main__":
    ft.app(
        target=flet_box,
        assets_dir="assets",
        # port=8081,
        # view=ft.AppView.WEB_BROWSER, #
        # view=ft.WEB_BROWSER,
        # web_renderer=ft.WebRenderer.HTML
        # view=ft.AppView.FLET_APP_HIDDEN
    )
