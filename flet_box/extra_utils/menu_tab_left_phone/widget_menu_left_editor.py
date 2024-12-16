import flet as ft
# from ..settings_var.save_export import WrapWidgetNode

# from ..tree_view.tree_view import TreeView
from .refactory_flet_box import refactory_flet_box


class MenuLeftContainer(ft.Stack):
    width_height = 42

    def __init__(self,
                 page: object = None,
                 phone_container: object = None,
                 menu_right_container: object = None,
                 ):
        super().__init__()

        self.page = page
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)

        self.phone_container = phone_container
        self.menu_right_container = menu_right_container
        # self.icon_browser = GLOBAL_VAR(get_global_var="ICON_BROWSER_CONTAINER")
        # self.color_browser = GLOBAL_VAR(get_global_var="COLOR_BROWSER_CONTAINER")
        # self.gpt_browser   = GLOBAL_VAR(get_global_var='GPT_BROWSER_CONTAINER')
        # self.text_editor = GLOBAL_VAR(get_global_var="TEXT_EDITOR_CONTAINER")
        # self.data_view = WrapWidgetNode()
        self.page.session.set('on_dev', self.on_developing)

    def build(self):
        self.eye_icon = ft.IconButton(
            icon=ft.icons('remove_red_eye'),
            on_click=lambda _: self.show_pone_container(
                phone_container=self.phone_container,
            )
        )
        self.eye_icon_edit = ft.IconButton(
            # phone_container= self.phone_container,
            tooltip="CLOSE EDIT WIDGET",
            icon=ft.icons('edit_square'),
            bgcolor="RED,0.2",
            icon_color="RED,0.8",
            on_click=lambda _: self.show_edit_container(
                menu_right_container=self.menu_right_container
            )
        )

        Drop_MenuLeftContainer = ft.Container(
            border_radius=ft.border_radius.all(30),
            expand=True,
            ink=False,
            bgcolor=ft.colors('black38'),
            padding=ft.padding.only(left=0, top=8, right=0, bottom=8),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            width=45,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors('black12'), ft.colors(
                    'cyan'), ft.colors('black12')],
            ),
            border=ft.border.all(
                0.8,
                ft.Colors.with_opacity(0.05, ft.colors('cyan')),
            ),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=16,
                color=ft.Colors.with_opacity(0.8, ft.colors('black26')),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.eye_icon,
                    self.eye_icon_edit,

                    ft.Container(height=8),
                    ft.Container(
                        expand=True,
                        ink=False,
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8,
                            controls=[
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    tooltip="ICONS",
                                    content=ft.IconButton(
                                        icon=ft.icons('add_reaction_outlined'),
                                        on_click=lambda _: self.show_widgets(
                                            show_widget="icon_browser"
                                        ),
                                    ),
                                    border=ft.border.all(
                                        1, ft.colors('cyan800')),
                                    bgcolor=ft.colors("black45"),
                                    height=self.width_height,
                                    width=self.width_height,
                                    border_radius=ft.border_radius.all(42),
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    tooltip="COLORS",
                                    content=ft.IconButton(
                                        icon=ft.icons('color_lens_outlined'),
                                        on_click=lambda _: self.show_widgets(
                                            show_widget="color_browser"
                                        ),
                                    ),
                                    border=ft.border.all(
                                        1, ft.colors('cyan800')),
                                    bgcolor=ft.colors("black45"),
                                    height=self.width_height,
                                    width=self.width_height,
                                    border_radius=ft.border_radius.all(42),
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    tooltip="CODE",
                                    content=ft.IconButton(
                                        icon=ft.icons('code_rounded'),
                                        on_click=lambda _: self.show_widgets(
                                            show_widget="text_editor"
                                        ),
                                    ),
                                    border=ft.border.all(
                                        1, ft.colors('cyan800')),
                                    bgcolor=ft.colors("black45"),
                                    height=self.width_height,
                                    width=self.width_height,
                                    border_radius=ft.border_radius.all(42),
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    tooltip="TREE",
                                    content=ft.IconButton(
                                        icon=ft.icons('account_tree_rounded'),
                                        on_click=lambda _: self.show_widgets(
                                            show_widget="tree_view"
                                        ),
                                    ),
                                    border=ft.border.all(
                                        1, ft.colors('cyan800')),
                                    bgcolor=ft.colors("black45"),
                                    height=self.width_height,
                                    width=self.width_height,
                                    border_radius=ft.border_radius.all(42),
                                ),
                                # ft.Container(
                                #     alignment=ft.alignment.center,
                                #     tooltip="GIT-HUB",
                                #     content=ft.IconButton(
                                #         icon=ft.icons.DEVELOPER_MODE,
                                #         on_click=lambda _: self.on_developing(
                                #             "Git-Hub"
                                #         ),
                                #     ),
                                #     border=ft.border.all(1, ft.colors('cyan800')),
                                #     bgcolor=ft.colors("black45"),
                                #     height=self.width_height,
                                #     width=self.width_height,
                                #     border_radius=ft.border_radius.all(42),
                                # ),
                                # ft.Container(alignment=ft.alignment.center,tooltip='CHAT-GPT'
                                # ,content=ft.IconButton(icon=ft.icons.DATA_OBJECT_OUTLINED ,
                                # on_click=lambda _:self.show_widgets(show_widget='gpt_browser')),
                                #     border        = ft.border.all(1, ft.colors('cyan800') ),
                                #     bgcolor       = ft.colors("black45"),
                                #     height        = self.width_height,
                                #     width         = self.width_height,
                                #     border_radius = ft.border_radius.all(42)
                                #     ),
                            ],
                        ),
                    ),
                    # ft.Container(
                    #     alignment=ft.alignment.center,
                    #     tooltip="LOAD FILE",
                    #     content=ft.IconButton(
                    #         icon=ft.icons('save_as_outlined'),
                    #         on_click=lambda _: self.show_widgets(
                    #             show_widget="color_browser"
                    #         ),
                    #     ),
                    #     border=ft.border.all(1, ft.colors('cyan200')),
                    #     # bgcolor=ft.colors("black45"),
                    #     bgcolor="Blue,0.2",
                    #     height=self.width_height,
                    #     width=self.width_height,
                    #     border_radius=ft.border_radius.all(42),
                    # ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        tooltip="LOAD SCREEN",
                        content=ft.IconButton(
                            icon=ft.icons('screenshot_rounded'),
                            on_click=lambda _: self.show_widgets(
                                show_widget="load screen"
                            ),
                        ),
                        border=ft.border.all(1, ft.colors('cyan200')),
                        # bgcolor=ft.colors("black45"),
                        bgcolor="purple,0.2",
                        height=self.width_height,
                        width=self.width_height,
                        border_radius=ft.border_radius.all(42),
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        tooltip="SAVE PROJECT",
                        content=ft.IconButton(
                            icon=ft.icons('save_outlined'),
                            on_click=lambda _: self.show_widgets(
                                show_widget="save_project"
                            ),
                        ),
                        border=ft.border.all(1, ft.colors('cyan200')),
                        # bgcolor=ft.colors("black45"),
                        bgcolor="Green,0.2",
                        height=self.width_height,
                        width=self.width_height,
                        border_radius=ft.border_radius.all(42),
                    ),
                    # ft.IconButton(icon=ft.icons.SETTINGS),
                ],
            ),
        )
        return Drop_MenuLeftContainer

    def show_edit_container(self, menu_right_container: object = None):
        # self.eye_icon_edit.icon= ft.icons.CODE_OFF_ROUNDED
        menu_right_container.visible = False
        menu_right_container.update()

    def show_pone_container(self, phone_container: object = None):

        if phone_container.visible:
            self.eye_icon.icon = ft.icons('code_off_rounded')
            phone_container.visible = False

        else:
            self.eye_icon.icon = ft.icons('remove_red_eye')
            phone_container.visible = True

        phone_container.update()

        self.eye_icon.update()
        # self.page.update()

    def show_widgets(self, show_widget: str = str(),):
        print(self.page.session.get('user_name'))
        # return

        if show_widget == "save_project":
            # MAIN SCREEN PHONE
            self.screen_phone = self.page.session.get("SELECTED_SCREEN")

            # PHONE CONTENT CONTENT
            self.screen_widget = self.screen_phone.content.content

            # ATTRIBUTES COLUMN PHONE
            # self.column_atributes = self.screen_widget.content.content
            self.column_atributes = self.screen_widget.content.content.content.content.content

            # COLUMN CONTROLS OF PHONR
            # controls_widgets = self.screen_widget.content.content.controls
            controls_widgets = self.screen_widget.content.content.content.content.content.controls

            self.dict_attributes = {
                "container": self.screen_phone,
                "effect_container": self.screen_widget.content,
                "column_attributes":self.column_atributes
            }

            # SAVING DATA
            code_returned = refactory_flet_box(page=self.page)

            for widgets_recursion in controls_widgets:
                code_returned.get_widget_attributes(widget=widgets_recursion)

            # WRITE DATA IN FILES
            # code_returned.save_all_data(
            #             screen_name='main_screen',
            #             container_attributes=self.dict_attributes,
            #             one_file=True,
            #     )
            # WRITE DATA IN FILES
            code_returned.save_all_data(
                        screen_name='main_screen',
                        container_attributes=self.dict_attributes,
                        one_file=True,
                )
            # ATTRIBUTES CONTAINER PHONE
            # self.container_image = self.screen_phone.image
            # self.container_gradient = self.screen_phone.gradient

            # self.container_padding = self.screen_widget.content.padding
            # self.container_blur = self.screen_widget.content.blur
            # self.container_bgcolor = self.screen_widget.content.bgcolor

        if show_widget == "icon_browser":
            # NEED IMPLEMENT YET
            self.on_developing("icon_browser")
            return

            self.icon_browser.visible = True if not self.icon_browser.visible else False

            # self.gpt_browser.visible   = False
            self.color_browser.visible = False
            self.text_editor.visible = False

            # self.gpt_browser.update()
            self.color_browser.update()
            self.text_editor.update()

            self.icon_browser.update()

        if show_widget == "load screen":
            # NEED IMPLEMENT YET
            # self.page.go('/screen_manager')
            self.page.views[1].controls[0].visible=False
            self.page.views[1].controls[1].visible=True
            self.page.views[1].update()

        if show_widget == "gpt_browser":
            # NEED IMPLEMENT YET
            self.on_developing("gpt_browser")
            return

            self.gpt_browser.visible = True if not self.gpt_browser.visible else False

            self.icon_browser.visible = False
            self.color_browser.visible = False
            self.text_editor.visible = False

            self.icon_browser.update()
            self.color_browser.update()
            self.text_editor.update()

            # self.gpt_browser.update()

        if show_widget == "tree_view":
            # NEED IMPLEMENT YET
            self.on_developing("tree_view")
            return
            #: THIS METOD visible_view() WILL return
            #: INPUT DATA IN TREEVIEW
            #: tree_view_data = self.data_view.show_tree_nodews(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
            #: TreeView.update_data(data=tree_view_data)
            TreeView.visible_view()

        if show_widget == "text_editor":
            # NEED IMPLEMENT YET
            self.on_developing("text_editor")
            return

            self.text_editor.visible = True if not self.text_editor.visible else False

            self.icon_browser.visible = False
            # self.gpt_browser.visible   = False
            self.color_browser.visible = False

            self.icon_browser.update()
            # self.gpt_browser.update()
            self.color_browser.update()

            self.text_editor.update()

    def on_developing(self, name_seccion: str = str(), body_string: str = str()):
        # NEED IMPLEMENT YET
        if body_string == "":
            self.data = f"""Hello, User!\n\n{name_seccion.upper()}\n{body_string}"""
        else:
            # self.data = body_string
            self.data = f"""Hello, User!\n\n{name_seccion.upper()}\n\n{body_string}"""

        self.dialog_alert = ft.AlertDialog(
            title=ft.Text(value=self.data, size=15),
            on_dismiss=lambda e: print("Dialog dismissed!"),
        )
        # self.page.dialog = self.dialog_alert
        self.page.overlay.append(self.dialog_alert)
        self.page.overlay[0].open = True
        self.page.update()
        self.page.overlay.pop()

    def action_windows(self, action):
        if action == "Close":
            self.page.window_close()

        elif action == "Minimize":
            self.page.window_minimized = True

        elif action == "Resize":
            self.page.window_maximizable = True
        self.page.update()
