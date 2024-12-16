import flet as ft

# from ..menu_tab_up_phone.basic_menu_tab_up import BasicMenuUp
# from ..settings_var.settings_widget import GLOBAL_VAR


class MenuUpContainer(ft.Container):
    # class imported
    # create_frame_app =saving_all_class_screens_in_file

    def __init__(self, page: object=None):
        super().__init__()

        self.page = page

        # Drop_MenuUpContainer = ft.Container(
        self.ink = False
        self.border_radius = ft.border_radius.only(top_left=32, top_right=18, bottom_left=18, bottom_right=32)                #: ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

        self.bgcolor = ft.Colors.with_opacity(0.1, ft.colors('white'))
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center
        # self.border_radius = ft.border_radius.only(0)
        self.height = 50
        self.border = ft.border.all(
            0.6,
            ft.Colors.with_opacity(0.1, ft.colors('cyan')),
        )
        # self.shadow = ft.BoxShadow(
        #     spread_radius=1,
        #     blur_radius=8,
        #     color=ft.Colors.with_opacity(0.8, ft.colors('black12')),
        #     offset=ft.Offset(0, 0),
        #     blur_style=ft.ShadowBlurStyle.OUTER,
        # )
        self.blur = (16,16)

    def build(self):
        # Basic_MenuUp = BasicMenuUp()

        self.content=ft.Row(
                    expand=True,
                    spacing=0,
                    run_spacing=0,
                    controls=[
                        ft.Container(
                            border_radius=ft.border_radius.only(
                                top_left=28,
                                top_right=14,
                                bottom_left=14,
                                bottom_right=28,
                            ),
                            border=ft.border.all(
                                0.1,
                                ft.Colors.with_opacity(
                                    0.4, ft.colors('cyan800')),
                            ),
                            margin=2,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.center_right,
                                colors=[
                                    ft.colors('blue500'),
                                    ft.colors('purple200'),
                                    ft.colors('cyan800'),
                                ],
                            ),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=18,
                                color=ft.Colors.with_opacity(
                                    0.1, ft.colors('white12')),
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        margin=ft.padding.only(
                                            left=18,
                                            top=1,
                                            right=0,
                                            bottom=1
                                        ),
                                        padding=ft.padding.only(
                                            left=0,
                                            top=0,
                                            right=0,
                                            bottom=0
                                        ),
                                        image =ft.DecorationImage(
                                                src='logo.jpg',
                                                fit="COVER",
                                                ),
                                        border=ft.border.all(
                                                            2,
                                                            ft.Colors.with_opacity(
                                                                0.8, ft.colors('white')
                                                            ),
                                        ),
                                        width=60,
                                        border_radius=ft.border_radius.all(12),
                                        shadow=ft.BoxShadow(
                                            spread_radius=1,
                                            blur_radius=8,
                                            color=ft.colors('black'),
                                            offset=ft.Offset(0, 0),
                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                        ),
                                    ),
                                    ft.Container(
                                        ink=False,
                                        padding=ft.padding.only(
                                            left=0,
                                            top=0,
                                            right=16,
                                            bottom=0
                                        ),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Column(
                                            run_spacing=0,
                                            spacing=0,
                                            controls=[
                                                ft.Container(
                                                    margin=ft.margin.only(
                                                        left=0,
                                                        top=0,
                                                        right=0,
                                                        bottom=0),
                                                    padding=ft.padding.only(
                                                        left=8,
                                                        top=0,
                                                        right=8,
                                                        bottom=0),
                                                    border_radius=ft.border_radius.all(
                                                        8),
                                                    content=ft.Text(
                                                        weight=ft.FontWeight.BOLD,
                                                        value="FLET - BOX",
                                                        size=17,
                                                        color=ft.colors('white'),
                                                    ),
                                                ),
                                                ft.Container(
                                                    margin=ft.margin.only(
                                                        left=0,
                                                        top=0,
                                                        right=0,
                                                        bottom=0),
                                                    padding=ft.padding.only(
                                                        left=8,
                                                        top=2,
                                                        right=8,
                                                        bottom=0),
                                                    border_radius=ft.border_radius.all(
                                                        8),
                                                    border=ft.border.all(
                                                        1, ft.Colors.with_opacity(0.5, ft.colors('white12')),),
                                                    gradient=ft.LinearGradient(
                                                        begin=ft.alignment.top_center,
                                                        end=ft.alignment.center_right,
                                                        colors=[
                                                            ft.colors('blue500'),
                                                            ft.colors('cyan800'),
                                                            ft.colors('cyan800'),
                                                        ],
                                                    ),
                                                    # blur=(15,15),
                                                    shadow=ft.BoxShadow(
                                                        spread_radius=1,
                                                        blur_radius=22,
                                                        color=ft.Colors.with_opacity(
                                                            0.8, ft.colors('black26')),
                                                        offset=ft.Offset(0, 0),
                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                    ),
                                                    content=ft.Text(
                                                        value="Based on FLet framework",
                                                        weight=ft.FontWeight.BOLD,
                                                        size=12,
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        # ft.Container(
                        #     width=60,
                        # ),  # <=== NOTE COMA
                        # Basic_MenuUp,
                        # ft.Container(
                        #     expand=True,
                        # ),  # <=== NOTE COMA
                        # ft.Container(
                        #     bgcolor=ft.colors.BLACK38,
                        #     gradient=ft.LinearGradient(
                        #         begin=ft.alignment.top_center,
                        #         end=ft.alignment.bottom_center,
                        #         colors=[ft.colors.TEAL, ft.colors('balck12')],
                        #     ),
                        #     border_radius=ft.border_radius.only(
                        #         top_left=32,
                        #         top_right=18,
                        #         bottom_left=18,
                        #         bottom_right=32,
                        #     ),
                        #     content=ft.Row(
                        #         spacing=0,
                        #         controls=[
                        #             ft.Container(
                        #                 tooltip="TEST APP",
                        #                 ink=True,
                        #                 ink_color=ft.colors('yellow800'),
                        #                 bgcolor="GREEN,0.5",
                        #                 margin=ft.margin.only(
                        #                     left=2,
                        #                     top=2,
                        #                     right=8,
                        #                     bottom=2
                        #                 ),
                        #                 border_radius=ft.border_radius.only(
                        #                     top_left=32,
                        #                     top_right=18,
                        #                     bottom_left=18,
                        #                     bottom_right=32,
                        #                 ),
                        #                 alignment=ft.alignment.center,
                        #                 # border_radius = ft.border_radius.all(30),
                        #                 border=ft.border.all(
                        #                     2, ft.colors('balck12')),
                        #                 width=60,
                        #                 content=ft.Icon(
                        #                     name=ft.icons.ADD_TO_HOME_SCREEN_OUTLINED,),
                        #                 on_click=lambda _: self.show_test_app_editor(),
                        #             ),
                        #             ft.Container(
                        #                 tooltip="SAVE PROYECT",
                        #                 ink=True,
                        #                 ink_color=ft.colors.RED,
                        #                 bgcolor=ft.colors.RED_900,
                        #                 margin=ft.margin.only(
                        #                     left=2,
                        #                     top=2,
                        #                     right=8,
                        #                     bottom=2
                        #                 ),
                        #                 border_radius=ft.border_radius.only(
                        #                     top_left=32,
                        #                     top_right=18,
                        #                     bottom_left=18,
                        #                     bottom_right=32,
                        #                 ),
                        #                 alignment=ft.alignment.center,
                        #                 # border_radius = ft.border_radius.all(30),
                        #                 border=ft.border.all(
                        #                     2, ft.colors('balck12')),
                        #                 width=60,
                        #                 content=ft.Icon(
                        #                     name=ft.icons.SAVE_AS_ROUNDED,),
                        #                 # on_click=lambda _: self.save_proyect_app(),
                        #                 on_click=lambda _: self.save_proyect_app_now(),
                        #             ),
                        #             ft.IconButton(
                        #                 ft.icons.CIRCLE,
                        #                 icon_color="Yellow",
                        #                 tooltip="Minimize",
                        #                 on_click=lambda _: self.action_windows(
                        #                     action="Minimize"
                        #                 ),
                        #             ),
                        #             ft.IconButton(
                        #                 ft.icons.CIRCLE,
                        #                 icon_color="Green",
                        #                 tooltip="Resize",
                        #                 content=ft.Text(
                        #                     value="X", color="White"),
                        #                 on_click=lambda _: self.action_windows(
                        #                     action="Resize"
                        #                 ),
                        #             ),
                        #             ft.IconButton(
                        #                 ft.icons.CIRCLE,
                        #                 icon_color="Red",
                        #                 tooltip="Close",
                        #                 on_click=lambda _: self.action_windows(
                        #                     action="Close"
                        #                 ),
                        #             ),
                        #         ],
                        #     ),
                        # ),
                    ],
                )
            # )
        # )
        # return Drop_MenuUpContainer

    def yes_click(self, data, alert):
        if data == "yes":
            self.page.window.close()
        elif data == "close":
            alert.open = False
            self.page.update()

    def show_test_app_editor(self):
        self.show_widget_test: object = GLOBAL_VAR(get_global_var="TEST_CONTAINER")

        if not self.show_widget_test.visible:
            self.show_widget_test.visible = True
        else:
            self.show_widget_test.visible = False

        self.show_widget_test.update()

    def action_windows(self, action):
        if action == "Close":
            confirm_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please confirm"),
                content=ft.Text("Do you really want to exit this app?"),
                actions=[
                    ft.ElevatedButton(
                        text="Yes",
                        on_click=lambda _: self.yes_click(
                            data="yes",
                            alert=confirm_dialog
                        ),
                        bgcolor=ft.colors.RED_900,
                    ),
                    ft.OutlinedButton(
                        text="No",
                        on_click=lambda _: self.yes_click(
                            data="close",
                            alert=confirm_dialog
                        ),
                    ),
                ],
                actions_alignment="end",
            )
            self.page.overlay.append(confirm_dialog)
            confirm_dialog.open = True

        elif action == "Minimize":
            self.page.window.minimized = True

        elif action == "Resize":
            self.page.window.maximizable = True

        self.page.update()

    def save_proyect_app_now(self):
        """
        Saves a proyect application now:

        MAKE VISIBLE SAVE THE PROJECT
        """
        self.show_widget_save: object = GLOBAL_VAR(get_global_var="SAVE_DATA_CONTAINER")

        if not self.show_widget_save.visible:
            self.show_widget_save.visible = True
        else:
            self.show_widget_save.visible = False

        self.show_widget_save.update()
