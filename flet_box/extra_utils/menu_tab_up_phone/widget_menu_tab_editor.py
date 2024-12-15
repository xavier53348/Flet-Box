import time
import flet as ft

# import json
# from ..settings_var.save_export import MakeJasonFile
# from .skeleton_class_screens import get_skeleton

from ..menu_tab_up_phone.basic_menu_tab_up import BasicMenuUp
from ..settings_var.settings_widget import GLOBAL_VAR
from ..screen_manager.write_file_proyect import write_file

from .saving_screens_in_file_view import saving_screens_in_file
from .saving_all_class_screens_in_file_view import saving_all_class_screens_in_file


class MenuUpContainer(ft.Stack):
    # class imported
    create_frame_app =saving_all_class_screens_in_file

    def __init__(self, main_page="Erase this test"):
        super().__init__()

        self.main_page = main_page
        # self.widget = MakeJasonFile()

    def build(self):
        Basic_MenuUp = BasicMenuUp()

        Drop_MenuUpContainer = ft.Container(
            ink=False,
            bgcolor=ft.colors.BLACK38,
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.only(30),
            height=50,
            border=ft.border.all(
                0.6,
                ft.colors.with_opacity(0.1, ft.colors.CYAN_800),
            ),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.colors.with_opacity(0.8, ft.colors.BLACK12),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.WindowDragArea(
                content=ft.Row(
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
                                ft.colors.with_opacity(0.4, ft.colors.CYAN_800),
                            ),
                            margin=2,
                            # bgcolor=ft.colors.with_opacity(0.4,ft.colors.CYAN_800),
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.center_right,
                                colors=[
                                    # ft.colors.CYAN,
                                    ft.colors.BLUE_500,
                                    ft.colors.PURPLE_200,
                                    ft.colors.YELLOW_800,
                                ],
                            ),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=18,
                                color=ft.colors.with_opacity(0.1, ft.colors.WHITE12),
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        margin=ft.padding.only(
                                            left=18, top=1, right=0, bottom=1
                                        ),
                                        padding=ft.padding.only(
                                            left=0, top=0, right=0, bottom=0
                                        ),
                                        # height  = 40 ,
                                        image_src="logo.jpg",
                                        border=ft.border.all(
                                            2,
                                            ft.colors.with_opacity(
                                                0.8, ft.colors.WHITE
                                            ),
                                        ),
                                        image_fit="COVER",  # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                        width=60,
                                        border_radius=ft.border_radius.all(12),
                                        shadow=ft.BoxShadow(
                                            spread_radius=1,
                                            blur_radius=8,
                                            color=ft.colors.BLACK,
                                            offset=ft.Offset(0, 0),
                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                        ),
                                    ),
                                    ft.Container(
                                        ink=False,
                                        padding=ft.padding.only(
                                            left=0, top=0, right=16, bottom=0
                                        ),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Column(
                                            run_spacing=0,
                                            spacing=0,
                                            controls=[
                                                ft.Container(
                                                    # bgcolor=ft.colors.BLACK12,
                                                    margin=ft.margin.only(left=0, top=0, right=0, bottom=0),
                                                    padding=ft.padding.only(left=8, top=0, right=8, bottom=0),
                                                    border_radius=ft.border_radius.all(8),
                                                    content=ft.Text(
                                                        weight=ft.FontWeight.BOLD,
                                                        value="FLET - BOX",
                                                        size=17,
                                                        color=ft.colors.WHITE,
                                                    ),
                                                ),
                                                ft.Container(
                                                    # bgcolor=ft.colors.BLACK38,
                                                    margin=ft.margin.only(left=0, top=0, right=0, bottom=0),
                                                    padding=ft.padding.only(left=8, top=2, right=8, bottom=0),
                                                    border_radius=ft.border_radius.all(8),
                                                    border=ft.border.all(1,ft.colors.with_opacity(0.5, ft.colors.WHITE12),),
                                                    gradient=ft.LinearGradient(
                                                        begin=ft.alignment.top_center,
                                                        end=ft.alignment.center_right,
                                                        colors=[
                                                            ft.colors.BLUE_500,
                                                            ft.colors.PURPLE_200,
                                                            ft.colors.YELLOW_800,
                                                        ],
                                                    ),
                                                    # blur=(15,15),
                                                    shadow=ft.BoxShadow(
                                                        spread_radius=1,
                                                        blur_radius=22,
                                                        color=ft.colors.with_opacity(0.8, ft.colors.BLACK26),
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
                        ft.Container(
                            width=60,
                        ),  # <=== NOTE COMA
                        Basic_MenuUp,
                        ft.Container(
                            expand=True,
                        ),  # <=== NOTE COMA
                        ft.Container(
                            bgcolor=ft.colors.BLACK38,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=[ft.colors.TEAL, ft.colors.BLACK12],
                            ),
                            border_radius=ft.border_radius.only(
                                top_left=32,
                                top_right=18,
                                bottom_left=18,
                                bottom_right=32,
                            ),
                            content=ft.Row(
                                spacing=0,
                                controls=[
                                    ft.Container(
                                        tooltip="TEST APP",
                                        ink=True,
                                        ink_color=ft.colors.YELLOW_800,
                                        bgcolor="GREEN,0.5",
                                        margin=ft.margin.only(
                                                            left=2,
                                                            top=2,
                                                            right=8,
                                                            bottom=2
                                        ),
                                        border_radius=ft.border_radius.only(
                                                            top_left=32,
                                                            top_right=18,
                                                            bottom_left=18,
                                                            bottom_right=32,
                                        ),
                                        alignment=ft.alignment.center,
                                        # border_radius = ft.border_radius.all(30),
                                        border=ft.border.all(2, ft.colors.BLACK12),
                                        width=60,
                                        on_click=lambda _: self.save_proyect_app(),
                                        content=ft.Icon(name=ft.icons.ADD_TO_HOME_SCREEN_OUTLINED,),
                                    ),
                                    ft.Container(
                                        tooltip="SAVE PROYECT",
                                        ink=True,
                                        ink_color=ft.colors.RED,
                                        bgcolor=ft.colors.RED_900,
                                        margin=ft.margin.only(
                                                            left=2,
                                                            top=2,
                                                            right=8,
                                                            bottom=2
                                        ),
                                        border_radius=ft.border_radius.only(
                                                            top_left=32,
                                                            top_right=18,
                                                            bottom_left=18,
                                                            bottom_right=32,
                                        ),
                                        alignment=ft.alignment.center,
                                        # border_radius = ft.border_radius.all(30),
                                        border=ft.border.all(2, ft.colors.BLACK12),
                                        width=60,
                                        on_click=lambda _: self.save_proyect_app(),
                                        content=ft.Icon(name=ft.icons.SAVE_AS_ROUNDED,),
                                    ),
                                    ft.IconButton(
                                        ft.icons.CIRCLE,
                                        icon_color="Yellow",
                                        tooltip="Minimize",
                                        on_click=lambda _: self.action_windows(
                                            action="Minimize"
                                        ),
                                    ),
                                    ft.IconButton(
                                        ft.icons.CIRCLE,
                                        icon_color="Green",
                                        tooltip="Resize",
                                        content=ft.Text(value="X", color="White"),
                                        on_click=lambda _: self.action_windows(
                                            action="Resize"
                                        ),
                                    ),
                                    ft.IconButton(
                                        ft.icons.CIRCLE,
                                        icon_color="Red",
                                        tooltip="Close",
                                        on_click=lambda _: self.action_windows(
                                            action="Close"
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        )
        return Drop_MenuUpContainer

    def yes_click(self, data, alert):
        if data == "yes":
            self.main_page.window.close()
        elif data == "close":
            alert.open = False
            self.main_page.update()

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
            self.main_page.overlay.append(confirm_dialog)
            confirm_dialog.open = True

        elif action == "Minimize":
            self.main_page.window.minimized = True

        elif action == "Resize":
            self.main_page.window.maximizable = True

        self.main_page.update()

    def save_proyect_app(self):

        # #: SET GLOBAL VAR // LIST_SELECTED_WIDGETS // TO RESET AFTER PRESS SELECTED IN PHONE CONTAINER
        # selected_widget_clicked = GLOBAL_VAR( get_global_var='LIST_SELECTED_WIDGETS')

        # #: RESET COLOR
        # if selected_widget_clicked.border:
        #      selected_widget_clicked.border = ft.border.all(0, ft.colors.TRANSPARENT)
        #      selected_widget_clicked.update()

        #: GET LIST WITH ALL SCREENS
        self.get_row_screens = GLOBAL_VAR(get_global_var="row_phone").controls
        self.names_screens: list = []

        #: WRITE APP IN REAL TIME
        self.app_events_manager = "test/proyect_name/proyect_name/controls/"

        #: LIST SCREENS
        for tmp_widgets in self.get_row_screens:
            # VERY IMPORTANT THIS METHOD WILL ALLOW US CREATE STRUCTURE OF ALL CLASS SCREENS
            #: ALL FRAME OF PHONE    ALL CODE     ALL EVENT         ID SCREEN
            # streaming_phone_data, style_code, main_event_code, id_name = self.create_frame_app(
            #                                                         main_node_phone=tmp_widgets,
            #                                                         main_node_phone_id=tmp_widgets.uid
            #                                                         )

            self.dumped_data = self.create_frame_app(
                                        main_node_phone=tmp_widgets,
                                        main_node_phone_id=tmp_widgets.uid
                                        )

            self.streaming_phone_data = self.dumped_data.dumped_data.get("main_widget_form_skeleton")
            self.style_code           = self.dumped_data.dumped_data.get("main_style_code")
            self.main_event_code      = self.dumped_data.dumped_data.get("main_event_code")
            self.id_name              = self.dumped_data.dumped_data.get("id_name")

            # ==============================================
            # WRITE FILE CLASS WIDGET , STYLE WIDGET, EVENT WIDGET
            #: IF NO EXITS [ CREATE ] IF EXIST [ OVERWRITE]
            # print(self.streaming_phone_data)
            write_file(
                path_name=self.app_events_manager,
                file_name=self.id_name,
                main_code=self.streaming_phone_data,
                style_code=self.style_code,
                event_code=self.main_event_code,
            )
            # ==============================================

            self.names_screens.append(self.id_name)

            #: RUN ONLY IN PRODUCTION
            # print(self.streaming_phone_data)
            # print(self.style_code)
            # print(self.main_event_code)
            # print(self.id_name)

        # ==============================================
        #: NEED MAKE SCREEN BUILDER MANAGER APP
        saving_screens_in_file(
                                screens_list_name=self.names_screens,
                                path_to_write=self.app_events_manager
                            )
        # ==============================================

        #: NEED ACTIVATE ALER OF SELECTED WIDGET
        self.show_info_complete()

    def show_info_complete(self):
        selected_widget = GLOBAL_VAR(get_global_var="ALERT_WIDGET")
        selected_widget.offset = (1.59, -7.5)
        selected_widget.visible = True
        selected_widget.update()
        time.sleep(1)
        selected_widget.visible = False
        selected_widget.update()
