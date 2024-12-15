import flet as ft
import os

from list_module_done import work_with_app
from render_view_app import test_flet_app

# from ..render_view_app.saving_screens_in_file_view import saving_screens_in_file

from saving_screens_in_file_view import saving_screens_in_file

current_selected: list = ["main_screen.py", "main_screen_styles.py", "main_screen_events.py"]

PATH_PROJEC_FILE:      str= os.path.realpath('test/proyect_name/proyect_name/main.py')
PATH_PROJEC_TO_EXPORT: str= os.path.realpath('/home/mjay/Escritorio/testing_create_package/test/proyect_name/proyect_name/controls/views')


class drop_down_builder(ft.Column):

    # path_project_export = '/home/mjay/Escritorio/testing_create_package/test/proyect_name/proyect_name/controls/views'
    proyect_path = PATH_PROJEC_FILE
    path_project_export = PATH_PROJEC_TO_EXPORT

    run_comand = test_flet_app(
        # comands="flet",
        # path_project=proyect_path,

    )

    def __init__(self,
                 text_choise: list = [],
                 dict_selection: dict = {},

                 ):
        super().__init__()

        self.dict_data_listed = dict_selection
        self.drop_down_screen = ft.Dropdown(
                        label=f"Choose your {text_choise[0]} ?",
                        width=220,
                        border_radius=ft.border_radius.all(30),
                        options=[],
                        on_change=lambda _: self.update_text_drop_down(
                            text_value=self.drop_down_screen.value),
        )
        self.drop_down_styles = ft.Dropdown(
                        label=f"Choose your {text_choise[1]} ?",
                        width=220,
                        disabled_hint_content=True,
                        border_radius=ft.border_radius.all(30),
                        options=[],
        )
        self.drop_down_events = ft.Dropdown(
                        label=f"Choose your {text_choise[2]} ?",
                        width=220,
                        disabled_hint_content=True,
                        border_radius=ft.border_radius.all(30),
                        options=[],
        )

    def build(self):
        self.controls = [
            ft.Container(
                bgcolor='BLACK,0.2',
                height=60,
                blur=(20, 20),


                width=330,
                padding=ft.padding.all(4),
                border_radius=ft.border_radius.all(30),
                content=ft.Row(
                    expand=False,
                    controls=[
                        self.drop_down_screen,
                        ft.IconButton(
                            bgcolor='white,0.1',
                            icon='Edit',
                            on_click=lambda _:self.edit_document(
                                widget_file="screen"),
                        ),
                        ft.IconButton(
                            bgcolor='red,0.5',
                            icon='Delete',
                            on_click=lambda _:self.delete_document(
                                widget_file="screen"),
                        ),
                    ],
                ),
            ),
            ft.Container(
                bgcolor='BLACK,0.2',
                height=60,
                blur=(20, 20),
                width=330,
                padding=ft.padding.all(4),
                border_radius=ft.border_radius.all(30),

                content=ft.Row(
                    expand=False,
                    controls=[
                        self.drop_down_styles,
                        ft.IconButton(
                            bgcolor='white,0.1',
                            icon='Edit',
                            on_click=lambda _:self.edit_document(
                                widget_file="style"),
                        ),
                        ft.IconButton(
                            bgcolor='red,0.5',
                            icon='Delete',
                            on_click=lambda _:self.delete_document(
                                widget_file="style"),
                        ),
                    ],
                ),
            ),
            ft.Container(
                bgcolor='BLACK,0.2',
                height=60,
                blur=(20, 20),
                width=330,
                padding=ft.padding.all(4),
                border_radius=ft.border_radius.all(30),

                content=ft.Row(
                    expand=False,
                    controls=[
                        self.drop_down_events,
                        ft.IconButton(
                            bgcolor='white,0.1',
                            icon='Edit',
                            on_click=lambda _:self.edit_document(
                                widget_file="event"),
                        ),
                        ft.IconButton(
                            bgcolor='red,0.5',
                            icon='Delete',
                            on_click=lambda _:self.delete_document(
                                widget_file="event"),
                        ),
                    ],
                ),
            ),
        ]

    def update_text_drop_down(self, text_value):

        self.drop_down_styles.options.clear()
        self.drop_down_events.options.clear()

        self.screen_name = text_value
        self.styles_name = f"{text_value}_styles"
        self.events_name = f"{text_value}_events"

        current_selected.clear()
        current_selected.append(f"{self.screen_name}.py")
        current_selected.append(f"{self.styles_name}.py")
        current_selected.append(f"{self.events_name}.py")

        self.drop_down_styles.label = f"  {self.styles_name}"
        self.drop_down_events.label = f"  {self.events_name}"

        self.drop_down_styles.update()
        self.drop_down_events.update()

    def delete_document(self, widget_file):
        print(f'delete: {widget_file}')

    def edit_document(self, widget_file):
        if widget_file == "screen":
            self.path_edit = current_selected[0]
        if widget_file == "style":
            self.path_edit = current_selected[1]
        if widget_file == "event":
            self.path_edit = current_selected[2]

        self.tmp_task = self.run_comand.call_cmd(call_cmd=f'subl {os.path.join(self.path_project_export,self.path_edit)}')


class hot_reload_app(ft.Container):

    proyect_path = PATH_PROJEC_FILE
    path_project_export = PATH_PROJEC_TO_EXPORT
    run_comand = test_flet_app(
                            comands="flet",
                            path_project=proyect_path,
                )
    list_dir = work_with_app(path_dir=path_project_export)

    def __init__(self, data='Erase this test'):
        super().__init__()
        self.title = data
        self.padding = ft.padding.all(16)
        self.margin = ft.margin.all(8)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.border = ft.border.all(6, ft.colors.BLACK12)
        self.width=380

        self.gradient = ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.alignment.bottom_center,
                                        colors=[ft.colors.TRANSPARENT,
                                                ft.colors.BLACK45],
                        )

        self.shadow = ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors.BLACK,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):

        self.drop_down_builder_screen = drop_down_builder(
            text_choise=["Screen", "Styles", "Events"])

        self.play_button = ft.Container(
            height=120,
            border=ft.border.all(4, ft.colors.BLACK12),
            bgcolor='blue,0.6',
            width=195,

            border_radius=ft.border_radius.all(30),
            content=ft.Stack(
                controls=[
                    ft.Container(
                        ink=True,
                        ink_color='black12',
                        height=120,
                        width=195,
                        content=ft.Icon(
                                        name='play_arrow_rounded',
                                        size=80,
                                        color='black12'),
                    ),
                    ft.Container(
                        ink=True,
                        ink_color='black12',
                        content=ft.Icon(name='play_arrow_rounded', size=80),
                        height=120,
                        width=195,
                        on_click=lambda _:self.play_demo_app(),
                    )
                ])
        )
        self.edit_app = ft.Container(
            height=52,
            border=ft.border.all(4, ft.colors.BLACK12),
            bgcolor='Green,0.5',
            width=120,

            border_radius=ft.border_radius.all(30),
            content=ft.Stack(
                controls=[
                    ft.Container(
                        ink=True,
                        width=120,
                        height=52,
                        ink_color='Green,0.5',
                        content=ft.Icon(name='Update',
                                        size=35,
                                        color='black12'),
                    ),
                    ft.Container(
                        ink=True,
                        ink_color='Green,0.5',
                        content=ft.Icon(name='Update', size=35),
                        height=52,
                        width=120,
                        on_click=lambda _:self.list_all_data(),
                    )
                ])
        )

        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.play_button,
                                ft.Column(
                                    controls=[
                                        self.edit_app,
                                        ft.Container(
                                            bgcolor='purple,0.5',
                                            border=ft.border.all(
                                                    3, ft.colors.BLACK12),

                                            height=52,
                                            width=120,
                                            border_radius=ft.border_radius.all(
                                                30),
                                            content=ft.Icon(name='edit'),
                                            on_click=lambda _:self.edit_demo_app(),
                                        ),
                                    ]
                                ),
                            ],
                        ),
                        self.drop_down_builder_screen,
                        ft.Container(
                                # expand=True,
                                bgcolor='teal,0.2',
                                border=ft.border.all(3, ft.colors.BLACK12),
                                padding         = ft.padding.all(8),    #: padding.only(left=8, top=8, right=8, bottom=8),
                                margin          = ft.margin.all(8),     #: margin.only (left=8, top=8, right=8, bottom=8),
                                alignment       = ft.alignment.center,  #: top_left,top_center,top_right,center_left,center,center_right
                                height=52,
                                width=320,
                                border_radius=ft.border_radius.all(30),
                                content=ft.Row(
                                            alignment            = ft.MainAxisAlignment.CENTER,     # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                            vertical_alignment   = ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                            controls=[
                                            ft.Icon(name='edit'),
                                            ft.Text(value="Open app screen Manager ")

                                            ]),
                                on_click=lambda _:self.edit_demo_app(file_widget="screen_manager"),
                            ),
                    ]),
            ]

        )

    def play_demo_app(self,):
        # PLAY DEMO APP
        # self.play_button.content.controls[1].visible = False
        # self.play_button.update()
        self.screens_dict_apth = os.path.dirname(self.path_project_export)

        # print(current_selected,'<<<<<<<<<<<<<<<<<<<')
        if not current_selected[0] == "main_screen.py":
            saving_screens_in_file(
                screens_list_name=[current_selected[0].strip('.py')],
                path_to_write=self.screens_dict_apth,
                )

        # CALL SCREEN OPEN NEW PAGE
        self.pid_task = self.run_comand.call_cmd()


    def stop_demo_app(self):
        self.run_comand.kill_cmd(pid=self.pid_task)

    def edit_demo_app(self, file_widget: str = "main_screen"):

        if file_widget == "screen_manager":
            # print(os.path.join("test/proyect_name/proyect_name/controls"))
            self.tmp_task = self.run_comand.call_cmd(call_cmd=f'subl {os.path.join("test/proyect_name/proyect_name/controls","app_screen_manager.py")}')

        else:
            self.tmp_task = self.run_comand.call_cmd(call_cmd=f'subl {os.path.join(self.path_project_export,current_selected[0])}')
            self.tmp_task = self.run_comand.call_cmd(call_cmd=f'subl {os.path.join(self.path_project_export,current_selected[1])}')
            self.tmp_task = self.run_comand.call_cmd(call_cmd=f'subl {os.path.join(self.path_project_export,current_selected[2])}')

    def list_all_data(self):
        """
        self.data_screen = self.data_elements.get('screens')
        self.data_styles = self.data_elements.get('styles')
        self.data_events = self.data_elements.get('events')

        for screen,styles,events in zip(
                                        self.data_screen,
                                        self.data_styles,
                                        self.data_events,
                                    ):

            self.drop_down_builder_screen.drop_down_widget.options.append(ft.dropdown.Option(f"  {screen}"),)
            self.drop_down_builder_styles.drop_down_widget.options.append(ft.dropdown.Option(f"  {styles}"),)
            self.drop_down_builder_events.drop_down_widget.options.append(ft.dropdown.Option(f"  {events}"),)

        self.drop_down_builder_screen.drop_down_widget.update()
        self.drop_down_builder_styles.drop_down_widget.update()
        self.drop_down_builder_events.drop_down_widget.update()"""
        # print('=====ss===')

        self.data_elements = self.list_dir.list_data()
        self.data_screen = self.data_elements.get('screens')

        self.drop_down_builder_screen.drop_down_screen.options.clear()
        for screen in self.data_screen:
            self.drop_down_builder_screen.dict_data_listed = self.data_elements
            self.drop_down_builder_screen.drop_down_screen.options.append(ft.dropdown.Option(f"{screen}"),)

        saving_screens_in_file(
                            screens_list_name=self.data_elements.get('screens'),
                            path_to_write=os.path.dirname(self.path_project_export),
                            )

        self.drop_down_builder_screen.drop_down_screen.update()

if __name__ == "__main__":

    def main(page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        page.window.bgcolor = ft.colors.RED_100
        page.window.left = 3
        page.window.top = 3
        page.window.height = 480
        page.window.width = 400
        page.padding = 0
        page.spacing = 0
        page.add(hot_reload_app())

    ft.app(target=main)
